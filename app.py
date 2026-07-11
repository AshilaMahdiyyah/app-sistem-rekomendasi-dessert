import streamlit as st
import pandas as pd
from recommender import get_rekomendasi, df

# =====================================================
# PAGE CONFIG
# =====================================================
st.set_page_config(
    page_title="Dessert Finder · Blok M",
    page_icon="🍰",
    layout="wide"
)

# =====================================================
# CUSTOM CSS
# =====================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@500;600;700&family=Inter:wght@400;500;600;700&display=swap');

:root {
    --primary:       #9E182B;
    --primary-hover: #7A1220;
    --hero:          #F2AFBC;
    --bg:            #F2E0D2;
    --card:          #FFFFFF;
    --border:        #F2AFBC;
    --text:          #5C1622;
    --subtitle:      #B06B78;
    --badge-green:      #FDEFF2;
    --badge-green-text: #9E182B;
    --badge-blue:       #FBE4E9;
    --badge-blue-text:  #9E182B;
    --badge-yellow:      #F9CBD6;
    --badge-yellow-text: #7A1220;
}

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
    background-color: var(--bg);
    color: var(--text);
}
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding-top: 1.2rem !important; max-width: 1600px !important; margin: 0 auto !important; }

/* ============== HERO BANNER (Dakingo-style) ============== */
.hero-banner {
    position: relative;
    background: linear-gradient(120deg, #C4425A 0%, #9E182B 55%, #6E0F1D 100%);
    border-radius: 22px;
    padding: 40px 36px;
    margin-bottom: 26px;
    overflow: hidden;
    box-shadow: 0 10px 30px rgba(158,24,43,0.25);
}
.hero-banner::before {
    content: "";
    position: absolute;
    right: -60px;
    top: -60px;
    width: 240px;
    height: 240px;
    background: rgba(255,255,255,0.10);
    border-radius: 50%;
}
.hero-banner::after {
    content: "";
    position: absolute;
    right: 40px;
    bottom: -70px;
    width: 160px;
    height: 160px;
    background: rgba(255,255,255,0.08);
    border-radius: 50%;
}
.hero-content { position: relative; z-index: 2; max-width: 640px; }
.hero-eyebrow {
    display: inline-block;
    background: rgba(255,255,255,0.18);
    color: #FFF;
    font-family: 'Inter', sans-serif;
    font-weight: 600;
    font-size: 0.74rem;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    padding: 5px 14px;
    border-radius: 40px;
    margin-bottom: 14px;
}
.hero-banner h1 {
    font-family: 'Quicksand', sans-serif;
    font-weight: 700;
    font-size: 3rem;
    letter-spacing: 0.005em;
    line-height: 1.15;
    color: #FFFFFF;
    margin: 0 0 10px;
    text-shadow: 0 2px 14px rgba(0,0,0,0.18);
}
.hero-banner h1 span {
    color: #F9CBD6;
}
.hero-banner p {
    font-family: 'Inter', sans-serif;
    font-weight: 500;
    font-size: 0.95rem;
    letter-spacing: 0.01em;
    color: rgba(255,255,255,0.88);
    margin: 0;
    line-height: 1.5;
}
/* ============== FILTER LABEL ============== */
.section-label {
    font-family: 'Quicksand', sans-serif;
    font-weight: 700;
    font-size: 1.85rem;
    color: var(--text);
    margin-bottom: 18px;
    display: flex;
    align-items: center;
    gap: 8px;
}

div[data-testid="stVerticalBlock"] > div[data-testid="stElementContainer"] {
    margin-bottom: 0 !important;
}
div[data-testid="stSelectbox"], div[data-testid="stRadio"] {
    margin-bottom: 2px !important;
}
label[data-testid="stWidgetLabel"] {
    font-family: 'Inter', sans-serif !important;
    font-size: 0.74rem !important;
    font-weight: 600 !important;
    color: var(--subtitle) !important;
    margin-bottom: 2px !important;
}
div[data-baseweb="select"] > div {
    background: #FFFFFF !important;
    border: 1.5px solid var(--border) !important;
    border-radius: 10px !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 0.88rem !important;
    min-height: 38px !important;
    transition: border-color 0.2s, box-shadow 0.2s;
}
div[data-baseweb="select"] {
    min-height: 38px !important;
}
div[data-baseweb="select"] > div:focus-within {
    border-color: var(--primary) !important;
    box-shadow: 0 0 0 3px rgba(158,24,43,0.16) !important;
}

div[data-testid="stRadio"] > label {
    font-family: 'Inter', sans-serif !important;
    font-size: 0.74rem !important;
    font-weight: 600 !important;
    color: var(--subtitle) !important;
}
div[data-testid="stRadio"] > div {
    display: flex !important;
    flex-direction: row !important;
    gap: 6px !important;
    flex-wrap: wrap;
    margin-top: 4px !important;
}
div[data-testid="stRadio"] > div > label {
    background: #FFFFFF !important;
    border: 1.5px solid var(--border) !important;
    border-radius: 40px !important;
    padding: 5px 14px !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 0.82rem !important;
    font-weight: 500 !important;
    color: var(--text) !important;
    cursor: pointer !important;
    transition: all 0.15s ease !important;
}
div[data-testid="stRadio"] > div > label:hover {
    border-color: var(--primary) !important;
}
div[data-testid="stRadio"] > div > label:has(input:checked) {
    background: var(--primary) !important;
    border-color: var(--primary) !important;
    color: #FFF !important;
}
div[data-testid="stRadio"] input[type="radio"] { display: none !important; }

div[data-testid="stButton"] button {
    width: 100%;
    background: var(--primary) !important;
    color: #FFF !important;
    border: none !important;
    border-radius: 40px !important;
    font-family: 'Inter', sans-serif;
    font-weight: 700;
    letter-spacing: 0.01em;
    font-size: 0.95rem !important;
    padding: 11px 0 !important;
    cursor: pointer;
    box-shadow: 0 4px 14px rgba(158,24,43,0.3) !important;
    transition: box-shadow 0.15s ease, transform 0.15s ease, background 0.15s ease !important;
}
div[data-testid="stButton"] button:hover {
    background: var(--primary-hover) !important;
    box-shadow: 0 6px 18px rgba(122,18,32,0.4) !important;
    transform: translateY(-1px) !important;
}
div[data-testid="stButton"] button:focus-visible {
    outline: 2px solid var(--primary-hover) !important;
    outline-offset: 2px !important;
}

/* ============== RESULTS ============== */
.results-header {
    font-family: 'Quicksand', sans-serif;
    font-weight: 700;
    font-size: 1.9rem;
    color: var(--text);
    margin: 0 0 18px;
    display: flex;
    align-items: center;
    justify-content: space-between;
}
.results-header .count-pill {
    background: var(--badge-green);
    color: var(--badge-green-text);
    border-radius: 40px;
    padding: 5px 16px;
    font-family: 'Inter', sans-serif;
    font-weight: 600;
    font-size: 0.9rem;
}

.result-card {
    position: relative;
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 16px 18px;
    margin-bottom: 14px;

    display: flex;
    width: 100%;

    gap: 14px;
    align-items: center;

    box-sizing: border-box;

    box-shadow: 0 1px 8px rgba(158,24,43,.05);
    transition: .15s;
}
.result-card:hover {
    box-shadow: 0 8px 20px rgba(158,24,43,0.14);
    transform: translateY(-2px);
    border-color: var(--hero);
}

.star-rating {
    position: relative;
    display: inline-block;
    font-size: 0.95rem;
    line-height: 1;
    letter-spacing: 1px;
}
.star-rating .stars-bg { color: #E9D9D6; }
.star-rating .stars-fg {
    position: absolute;
    top: 0;
    left: 0;
    overflow: hidden;
    white-space: nowrap;
    color: #E0A32A;
}

.card-thumb {
    flex-shrink: 0;
    width: 50px;
    height: 50px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-family: 'Quicksand', sans-serif;
    font-weight: 700;
    font-size: 1.15rem;
    color: var(--badge-yellow-text);
    background: var(--badge-yellow);
    border: 1px solid #F2AFBC;
}
.card-thumb.rank-1 { background: #9E182B; border-color: #9E182B; color: #FFFFFF; }
.card-thumb.rank-2 { background: #FBE4E9; border-color: #F2AFBC; color: var(--primary); }
.card-thumb.rank-3 { background: #F2E0D2; border-color: #E8CBB0; color: #8A5A2E; }

.card-body { flex: 1; min-width: 0; }
.card-top-row {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 10px;
    margin-bottom: 4px;
}
.place-name {
    font-family: 'Quicksand', sans-serif;
    font-weight: 700;
    font-size: 1.45rem;
    color: var(--text);
}
.menu-name {
    font-family: 'Inter', sans-serif;
    font-size: 1rem;
    color: var(--subtitle);
    margin-bottom: 10px;
    font-weight:500;
}
.metrics-row {
    display: flex;
    gap: 6px;
    flex-wrap: nowrap;
    align-items: center;
}
.metrics-row > * {
    box-sizing: border-box;
    display: inline-flex;
    align-items: center;
    line-height: 1.2;
    white-space: nowrap;
    flex-shrink: 0;
}
.metric-pill {
    background: var(--badge-yellow);
    border: 1px solid #F2AFBC;
    border-radius: 40px;
    padding: 5px 14px;
    font-family: 'Inter', sans-serif;
    font-size: 0.9rem;
    color: var(--badge-yellow-text);
    font-weight: 600;
    gap: 4px;
}
.metric-pill .val {
    font-weight: 700;
}
.dine-tag {
    background: var(--badge-green);
    border: 1px solid #F2AFBC;
    color: var(--badge-green-text);
    border-radius: 40px;
    padding: 5px 14px;
    font-family: 'Inter', sans-serif;
    font-size: 0.9rem;
    font-weight: 600;
}
.rec-type-badge {
    border-radius: 40px;
    padding: 3px 12px;
    font-family: 'Inter', sans-serif;
    font-size: 0.88rem;
    padding: 5px 14px;
    font-weight: 600;
    background: var(--badge-blue);
    color: var(--badge-blue-text);
    white-space: nowrap;
}
.maps-link,
.maps-link:hover,
.maps-link:visited,
.maps-link:active {
    text-decoration: none !important;
    background: var(--card);
    border: 1px solid var(--primary);
    color: var(--primary) !important;
    border-radius: 40px;
    padding: 5px 14px;
    font-family: 'Inter', sans-serif;
    font-size: 0.9rem;
    font-weight: 600;
    white-space: nowrap;
}

.placeholder-state{
    display:flex;
    flex-direction:column;
    justify-content:center;
    align-items:center;

    height:500px;   /* sesuaikan jika perlu */

    text-align:center;

    background:transparent;
    border:none;
    box-shadow:none;
}

.empty-state{
    display:flex;
    flex-direction:column;
    justify-content:center;
    align-items:center;

    min-height:300px;

    text-align:center;

    background:transparent;
    border:none;
    box-shadow:none;
}
.empty-state .emoji, .placeholder-state .emoji { font-size: 2.6rem; }
.empty-state p, .placeholder-state p {
    font-family: 'Inter', sans-serif;
    font-size: 0.92rem;
    margin-top: 10px;
    line-height: 1.5;
}

hr { border: none; border-top: 1px solid var(--border); margin: 8px 0 24px; }
</style>
""", unsafe_allow_html=True)


# =====================================================
# HELPERS
# =====================================================
def prettify(text):
    if pd.isna(text):
        return "-"
    return str(text).replace("_", " ").title()

CATEGORY_ICONS = {
    "cake": "🎂", "kue": "🎂", "ice cream": "🍨", "es krim": "🍨",
    "pastry": "🥐", "cookies": "🍪", "kukis": "🍪", "pudding": "🍮",
    "puding": "🍮", "waffle": "🧇", "donut": "🍩", "pie": "🥧",
    "chocolate": "🍫", "cokelat": "🍫", "bread": "🍞", "roti": "🍞",
    "candy": "🍬", "dessert": "🍰",
}

def render_stars(rating):
    try:
        pct = max(0, min(100, (float(rating) / 5) * 100))
    except (TypeError, ValueError):
        pct = 0
    return (f'<span class="star-rating">'
            f'<span class="stars-bg">★★★★★</span>'
            f'<span class="stars-fg" style="width:{pct}%">★★★★★</span>'
            f'</span>')

def icon_for(category):
    if not category:
        return "🍰"
    key = str(category).lower()
    for k, v in CATEGORY_ICONS.items():
        if k in key:
            return v
    return "🍰"

# Warna berbeda untuk tiap recommendation_type — dibuat kontras
# agar tiap badge mudah dibedakan sekilas, tetap senada dengan palette
# Rose Quartz / Blush / Red Wine / Oat Milk

# 1) Paling Cocok -> Red Wine tegas (paling menonjol, ini rekomendasi utama)
THEME_REDWINE = {
    "bg": "#FBEEF0",
    "border": "#E3B4BB",
    "badge_bg": "#9E182B",
    "badge_text": "#FFFFFF",
    "accent": "#9E182B"
}

# 2) Harga / Dine Beda -> Oat Milk / Gold amber
THEME_OATMILK = {
    "bg": "#FBF5EE",
    "border": "#E8CBB0",
    "badge_bg": "#EFCBA0",
    "badge_text": "#7A4A12",
    "accent": "#D9A96B"
}

# 3) Variasi Rasa -> Plum / Mauve keunguan
THEME_MAUVE = {
    "bg": "#F8F1F5",
    "border": "#D9B8CC",
    "badge_bg": "#8E4E76",
    "badge_text": "#FFFFFF",
    "accent": "#8E4E76"
}

# 4) Menu & Rasa Serupa -> Blush pink cerah
THEME_BLUSH = {
    "bg": "#FDF1F3",
    "border": "#F2AFBC",
    "badge_bg": "#F2AFBC",
    "badge_text": "#5C1622",
    "accent": "#D9758C"
}

# 5) Alternatif Lainnya -> netral abu kecoklatan, sengaja beda arah
#    biar kontras jelas dari 4 warna lain yang bernuansa pink/merah
THEME_NEUTRAL = {
    "bg": "#F5F1EF",
    "border": "#D7CCC5",
    "badge_bg": "#8D7468",
    "badge_text": "#FFFFFF",
    "accent": "#8D7468"
}

TYPE_THEME_MAP = {
    "paling cocok": THEME_REDWINE,
    "harga / dine beda": THEME_OATMILK,
    "variasi rasa": THEME_MAUVE,
    "menu & rasa serupa": THEME_BLUSH,
    "alternatif lainnya": THEME_NEUTRAL,
}

def theme_for_type(rec_type):
    key = str(rec_type).strip().lower()
    return TYPE_THEME_MAP.get(key, THEME_NEUTRAL)


# =====================================================
# HERO BANNER
# =====================================================
st.markdown("""
<div class="hero-banner">
    <div class="hero-content">
        <h1>Dessert Finder <span>Blok M</span></h1>
        <p>Temukan rekomendasi dessert yang sesuai dengan seleramu.</p>
    </div>
</div>
""", unsafe_allow_html=True)


# =====================================================
# TWO-COLUMN LAYOUT: Filter (kiri) | Hasil (kanan)
# =====================================================
col_filter, col_result = st.columns([0.85, 2.3], gap="large")

# ─────────────────────────────────────────
# KOLOM KIRI — Filter
# ─────────────────────────────────────────
with col_filter:
    st.markdown('<div class="section-label">🔍 Filter Pencarian</div>', unsafe_allow_html=True)

    menu_options = sorted(df["menu_category"].dropna().unique().tolist())
    menu_display = [prettify(m) for m in menu_options]
    menu_map     = dict(zip(menu_display, menu_options))

    menu_selected_display = st.selectbox("Menu", menu_display)
    menu = menu_map[menu_selected_display]

    filtered_df = df[df["menu_category"] == menu]

    flavor_options = sorted(filtered_df["flavor_category"].dropna().unique().tolist()) if not filtered_df.empty else []
    flavor_display = [prettify(f) for f in flavor_options]
    flavor_map     = dict(zip(flavor_display, flavor_options))

    flavor_selected_display = st.selectbox("Flavor", flavor_display)
    flavor = flavor_map[flavor_selected_display] if flavor_display else None

    price = st.selectbox(
        "Rentang Harga",
        sorted(df["range_price"].dropna().unique().tolist())
    )

    dine = st.selectbox(
        "Dine Option",
        ["takeaway", "dine_in", "both"],
        format_func=lambda x: {
            "takeaway": "Takeaway",
            "dine_in" : "Dine In",
            "both"    : "Dine In & Takeaway"
        }.get(x, x)
    )

    st.markdown("<div style=\"height:6px\"></div>", unsafe_allow_html=True)

    rating_map   = {"3.5+": 3.5, "4.0+": 4.0, "4.5+": 4.5}
    rating_label = st.radio(
        "Minimum Rating",
        options=list(rating_map.keys()),
        index=1,
        horizontal=True,
        key="rating_radio"
    )
    rating = float(rating_map[rating_label])

    st.markdown("<div style=\"height:6px\"></div>", unsafe_allow_html=True)

    top_map   = {"Top 5": 5, "Top 10": 10}
    top_label = st.radio(
        "Jumlah Rekomendasi",
        options=list(top_map.keys()),
        index=1,
        horizontal=True,
        key="topn_radio"
    )
    top_n = top_map[top_label]

    st.markdown("<div style=\"height:14px\"></div>", unsafe_allow_html=True)

    cari = st.button("🍰 Cari Rekomendasi", use_container_width=True)


# ─────────────────────────────────────────
# KOLOM KANAN — Hasil Rekomendasi
# ─────────────────────────────────────────
with col_result:
    if not cari:
        st.markdown("""
        <div class="placeholder-state">
            <div class="emoji">🍰</div>
            <p>Pilih filter di sebelah kiri,<br>lalu klik <strong>Cari Rekomendasi</strong><br>untuk melihat hasilnya di sini.</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        if filtered_df.empty:
            st.markdown("""
            <div class="empty-state">
                <div class="emoji">😔</div>
                <p>Tidak ada data untuk menu ini.<br>Coba ubah filter dan cari lagi.</p>
            </div>
            """, unsafe_allow_html=True)
        else:
            with st.spinner("Sedang mencari dessert terbaik untukmu..."):
                result = get_rekomendasi(
                    menu=menu,
                    flavor=flavor,
                    price=price,
                    dine=dine,
                    rating=rating,
                    top_n=top_n
                )

            if "message" in result.columns:
                st.markdown("""
                <div class="empty-state">
                    <div class="emoji">😔</div>
                    <p>Tidak ditemukan rekomendasi yang sesuai.<br>
                    Coba ubah filter dan cari lagi.</p>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div class="results-header">
                    <span>Hasil Rekomendasi</span>
                </div>
                """, unsafe_allow_html=True)

                for _, row in result.iterrows():
                    rank      = int(row["rank"])
                    rank_cls  = f"rank-{rank}" if rank <= 3 else ""

                    dine_label = {
                        "takeaway": "Takeaway",
                        "dine_in" : "Dine In",
                        "both"    : "Dine In & Takeaway"
                    }.get(row["dine_option"], row["dine_option"])

                    rec_type = row['recommendation_type']
                    theme = theme_for_type(rec_type)

                    maps_url = row.get("maps_url", None)
                    maps_btn = f'<a href="{maps_url}" target="_blank" class="maps-link">📍 Lihat Lokasi</a>' if maps_url else ''

                    stars_html = render_stars(row['rating'])

                    card_html = (
                        f'<div class="result-card" style="background:{theme["bg"]}; border-color:{theme["border"]}; border-left:5px solid {theme["accent"]};">'
                        f'<div class="card-thumb {rank_cls}">#{rank}</div>'
                        f'<div class="card-body">'
                        f'<div class="place-name">{row["nama_tempat"]}</div>'
                        f'<div class="menu-name">{prettify(row["recommended_item"])}</div>'
                        f'<div class="metrics-row">'
                        f'<div class="rec-type-badge" style="background:{theme["badge_bg"]}; color:{theme["badge_text"]};">{rec_type}</div>'
                        f'<div class="metric-pill">{stars_html} <span class="val">{row["rating"]}</span></div>'
                        f'<div class="metric-pill">💰 <span class="val">{row["range_price"]}</span></div>'
                        f'<div class="dine-tag">{dine_label}</div>'
                        f'{maps_btn}'
                        f'</div>'
                        f'</div>'
                        f'</div>'
                    )
                    st.markdown(card_html, unsafe_allow_html=True)