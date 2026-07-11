import pandas as pd
import numpy as np
import scipy.sparse as sp
import joblib
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import normalize
from utils import menu_group, flavor_group, get_menu_group, get_flavor_group

# =====================================================
# LOAD DATA & MODEL
# =====================================================
model         = joblib.load("model_rekomendasi.pkl")
df            = model["df"]
tfidf         = model["tfidf"]
tfidf_matrix  = model["tfidf_matrix"]
ohe_matrix    = model["ohe_matrix"]
item_profile  = model["item_profile"]
price_columns = model["price_columns"]
dine_columns  = model["dine_columns"]

df["maps_url"] = df.apply(
    lambda row: (
        f"https://www.google.com/maps/search/"
        f"{row['nama_tempat'].replace(' ', '+')}/"
        f"@{row['latitude']},{row['longitude']},17z"
    )
    if pd.notna(row["latitude"]) and pd.notna(row["longitude"])
    else None,
    axis=1
)
# =====================================================
# MAIN FUNCTION
# =====================================================
def get_rekomendasi(menu, flavor, price, dine, rating, top_n=10):

    menu_clean   = menu.replace("_", " ").lower()
    flavor_clean = flavor.replace("_", " ").lower()

    # =====================================================
    # 1. USER VECTOR
    # =====================================================
    tfidf_vec = tfidf.transform([f"{menu_clean} {flavor_clean}"])

    price_vec = np.zeros(len(price_columns))
    key = f"price_{price.strip()}"
    if key in price_columns:
        price_vec[price_columns.index(key)] = 1.0

    if dine == "takeaway":
        dine_vec = np.array([1.0, 0.0])
    elif dine == "dine_in":
        dine_vec = np.array([0.0, 1.0])
    else:
        dine_vec = np.array([0.5, 0.5])

    ohe_user = np.concatenate([price_vec, dine_vec])
    user_raw = sp.hstack([
        tfidf_vec,
        sp.csr_matrix(ohe_user.reshape(1, -1))
    ])
    user_vec = normalize(user_raw, norm='l2')

    # =====================================================
    # 2. SIMILARITY
    # =====================================================
    result_df = df.copy()
    result_df["similarity"] = cosine_similarity(item_profile, user_vec).flatten()
    result_df = result_df[result_df["similarity"] > 0].copy()

    # =====================================================
    # 3. HELPER FUNCTIONS
    # =====================================================
    def exact_match(series, kw):
        return series.str.lower().str.strip() == kw.lower().strip()

    def cooccurrence(df_temp, menu_kw, flavor_kw):
        return (
            exact_match(df_temp["menu_category"], menu_kw)
            &
            exact_match(df_temp["flavor_category"], flavor_kw)
        )

    def filter_pdr(d, use_price=True, use_dine=True, use_rating=True):
        if use_price:
            d = d[d["range_price"] == price.strip()]
        if use_dine and dine != "both":
            d = d[(d["dine_option"] == dine) | (d["dine_option"] == "both")]
        if use_rating:
            d = d[d["rating"] >= rating]
        return d

    # =====================================================
    # 4. GROUPING
    # =====================================================
    result    = pd.DataFrame()
    used_places = set()

    def add_grup(temp, label, sort_by_rating=False):
        nonlocal result, used_places

        temp = (
            temp[~temp["nama_tempat"].isin(used_places)]
            .drop_duplicates("nama_tempat")
            .copy()
        )

        if temp.empty:
            return

        sort_cols = (
            ["rating", "similarity"]
            if sort_by_rating
            else ["similarity", "rating"]
        )

        temp = (
            temp
            .sort_values(sort_cols, ascending=False)
            .head(top_n - len(result))
        )

        temp["recommendation_type"] = label
        used_places.update(temp["nama_tempat"].tolist())
        result = pd.concat([result, temp], ignore_index=True)

    # =====================================================
    # 5. GROUP LOGIC
    # =====================================================

    # -----------------------------------------------------
    # GRUP 1 — PALING COCOK
    # menu + flavor sama, semua filter aktif
    # -----------------------------------------------------
    add_grup(
        filter_pdr(
            result_df[cooccurrence(result_df, menu, flavor)]
        ),
        "Paling Cocok",
        sort_by_rating=True
    )

    # -----------------------------------------------------
    # GRUP 2 — HARGA & DINE BEDA
    # menu + flavor sama, longgarkan price & dine
    # -----------------------------------------------------
    if len(result) < top_n:
        add_grup(
            filter_pdr(
                result_df[cooccurrence(result_df, menu, flavor)],
                use_price=False,
                use_dine=False,
                use_rating=True
            ),
            "Harga / Dine Beda"
        )

    # -----------------------------------------------------
    # GRUP 3 — VARIASI RASA
    # menu sama, flavor beda, hanya filter rating
    # -----------------------------------------------------
    if len(result) < top_n:
        add_grup(
            filter_pdr(
                result_df[
                    exact_match(result_df["menu_category"], menu)
                    & ~cooccurrence(result_df, menu, flavor)
                ],
                use_price=False,
                use_dine=False,
                use_rating=True
            ),
            "Variasi Rasa"
        )

    # -----------------------------------------------------
    # GRUP 4 — MENU & FLAVOR SERUPA
    # -----------------------------------------------------
    if len(result) < top_n:
        m_grp = get_menu_group(menu)
        f_grp = get_flavor_group(flavor)

        if m_grp and f_grp:
            serumpun_menu   = menu_group[m_grp]
            serumpun_flavor = flavor_group[f_grp]

            menu_mask = (
                result_df["menu_category"].isin(serumpun_menu)
                & ~exact_match(result_df["menu_category"], menu)
            )

            flavor_mask = result_df["flavor_category"].apply(
                lambda x: any(
                    f.strip() in serumpun_flavor
                    for f in str(x).split(",")
                )
            )

            add_grup(
                filter_pdr(
                    result_df[
                        menu_mask
                        & flavor_mask
                        & ~result_df["nama_tempat"].isin(used_places)
                    ],
                    use_price=False,
                    use_dine=False,
                    use_rating=True
                ),
                "Menu & Rasa Serupa"
            )

    # -----------------------------------------------------
    # GRUP 5 — ALTERNATIF
    # semua item, last resort
    # -----------------------------------------------------
    if len(result) < top_n:
        add_grup(
            filter_pdr(
                result_df[~result_df["nama_tempat"].isin(used_places)],
                use_price=False,
                use_dine=False,
                use_rating=True
            ),
            "Alternatif Lainnya"
        )
    # =====================================================
    # 7. SAFETY NET
    # kalau rating filter terlalu ketat, lepas semua
    if result.empty:
        result = (
            result_df
            .sort_values(["similarity", "rating"], ascending=False)
            .head(top_n)
            .copy()
        )
        result["recommendation_type"] = "Alternatif Lainnya"

    # =====================================================
    # 7. OUTPUT
    # =====================================================
    result = result.head(top_n).reset_index(drop=True)
    result["rank"] = result.index + 1

    result["recommended_item"] = (
        result["menu_category"].str.replace("_", " ")
        + " "
        + result["flavor_category"]
            .str.split(",")
            .str[0]
            .str.strip()
            .str.replace("_", " ")
    )

    return result[[
        "rank",
        "nama_tempat",
        "recommended_item",
        "rating",
        "range_price",
        "dine_option",
        "similarity",
        "recommendation_type",
        "maps_url"
    ]]