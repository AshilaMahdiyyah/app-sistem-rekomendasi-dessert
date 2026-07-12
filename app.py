import streamlit as st
import pandas as pd
import streamlit.components.v1 as components
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
    --primary:        #8E1833;
    --primary-hover:  #6E1227;
    --secondary:      #F6D9E1;
    --accent:         #E7B85C;
    --bg:             #FFF8F2;

    --card:           #FFFFFF;
    --border:         #F6D9E1;
    --text:           #4A1120;
    --subtitle:       #9C6B78;

    --badge-green:      #FBEFE1;
    --badge-green-text: #8E1833;
    --badge-blue:       #F6D9E1;
    --badge-blue-text:  #8E1833;
    --badge-yellow:      #FBEAD0;
    --badge-yellow-text: #7A5416;
}

html, body {
    font-family: 'Inter', sans-serif;
    background-color: var(--bg);
    color: var(--text);
    overflow-x: hidden;
}
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding-top: 1.2rem !important; max-width: 1600px !important; margin: 0 auto !important; overflow-x: hidden; }
* { -webkit-tap-highlight-color: transparent; }
iframe[height="0"] { display: none !important; }

.hero-banner {
    position: relative;
    background: linear-gradient(135deg, #B03A5B 0%, #8E1833 48%, #520D22 100%);
    border-radius: 24px;
    padding: 34px 40px;
    margin-bottom: 26px;
    overflow: hidden;
    box-shadow: 0 16px 36px rgba(142,24,51,0.32);
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 24px;
    flex-wrap: wrap;
}
.hero-banner::before {
    content: "";
    position: absolute;
    right: -70px;
    top: -90px;
    width: 260px;
    height: 260px;
    background: radial-gradient(circle, rgba(255,255,255,0.14) 0%, rgba(255,255,255,0) 70%);
    border-radius: 50%;
}
.hero-banner::after {
    content: "";
    position: absolute;
    left: -40px;
    bottom: -80px;
    width: 200px;
    height: 200px;
    background: radial-gradient(circle, rgba(231,184,92,0.18) 0%, rgba(231,184,92,0) 70%);
    border-radius: 50%;
}
.hero-content { position: relative; z-index: 2; max-width: 600px; }
.hero-eyebrow {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: rgba(255,255,255,0.14);
    border: 1px solid rgba(255,255,255,0.28);
    color: #FFF;
    font-family: 'Inter', sans-serif;
    font-weight: 700;
    font-size: 0.7rem;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    padding: 6px 14px;
    border-radius: 40px;
    margin-bottom: 8px;
}
.hero-banner h1 {
    font-family: 'Quicksand', sans-serif;
    font-weight: 700;
    font-size: 2.35rem;
    letter-spacing: 0.005em;
    line-height: 1.1;
    color: #FFFFFF;
    margin: 0 0 2px;
    text-shadow: 0 2px 16px rgba(0,0,0,0.2);
}
.hero-banner h1 span {
    color: var(--accent);
}
.hero-banner p {
    font-family: 'Inter', sans-serif;
    font-weight: 500;
    font-size: 0.95rem;
    letter-spacing: 0.01em;
    color: rgba(255,255,255,0.9);
    margin: 0;
    line-height: 1.6;
    max-width: 480px;
}
.hero-visual {
    position: relative;
    z-index: 2;
    flex-shrink: 0;
    width: 108px;
    height: 108px;
    border-radius: 50%;
    background: rgba(255,255,255,0.12);
    border: 1.5px solid rgba(255,255,255,0.3);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 3.1rem;
    box-shadow: 0 8px 22px rgba(0,0,0,0.18), inset 0 0 0 1px rgba(255,255,255,0.05);
}

.section-label {
    font-family: 'Quicksand', sans-serif;
    font-weight: 700;
    font-size: 1.7rem;
    color: var(--text);
    margin-bottom: 2px;
    display: flex;
    align-items: center;
    gap: 8px;
}

/* Keep the outer two-column row top-aligned so the filter card
   doesn't stretch to match the height of the results column */
div[data-testid="stHorizontalBlock"]:has(.section-label) {
    align-items: flex-start !important;
}
div[data-testid="stHorizontalBlock"]:has(.section-label) > div[data-testid="stColumn"] {
    align-self: flex-start !important;
}

/* ==== 1. SIDEBAR / FILTER WRAPPED IN WHITE CARD ==== */
div[data-testid="stVerticalBlock"]:has(> div[data-testid="stElementContainer"] .section-label) {
    gap: 0 !important;
    background: #FFFFFF;
    border: 1px solid var(--border);
    border-radius: 20px;
    padding: 24px 22px 28px;
    box-shadow: 0 6px 24px rgba(142,24,51,0.08);
}
div[data-testid="stVerticalBlock"] > div[data-testid="stElementContainer"] {
    margin-bottom: 10px !important;
}
div[data-testid="stVerticalBlock"] > div[data-testid="stElementContainer"]:has(.section-label) {
    margin-bottom: 22px !important;
}
div[data-testid="stHorizontalBlock"] {
    margin-bottom: 10px !important;
}
div[data-testid="stSelectbox"], div[data-testid="stRadio"] {
    margin-bottom: 0 !important;
}
label[data-testid="stWidgetLabel"] {
    font-family: 'Inter', sans-serif !important;
    font-size: 0.74rem !important;
    font-weight: 600 !important;
    color: var(--subtitle) !important;
    margin-bottom: 4px !important;
    text-transform: uppercase;
    letter-spacing: 0.03em;
}

/* Single clean border on the outer control only; inner layers are
   explicitly stripped so it never doubles up */
div[data-testid="stSelectbox"] div[data-baseweb="select"] {
    background: #FFFFFF !important;
    border: 1.5px solid var(--border) !important;
    border-radius: 12px !important;
    min-height: 42px !important;
    box-shadow: 0 2px 6px rgba(142,24,51,0.05) !important;
    transition: border-color 0.2s, box-shadow 0.2s, background 0.2s !important;
}
div[data-testid="stSelectbox"] div[data-baseweb="select"] > div,
div[data-testid="stSelectbox"] div[data-baseweb="select"] > div > div {
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 0.9rem !important;
    min-height: 42px !important;
}
/* keep the selected value on one line with ellipsis instead of being clipped */
div[data-baseweb="select"] > div {
    flex-wrap: nowrap !important;
}
div[data-baseweb="select"] > div > div:first-of-type {
    overflow: hidden !important;
    white-space: nowrap !important;
    text-overflow: ellipsis !important;
    min-width: 0 !important;
}
div[data-baseweb="select"] > div > div:first-of-type * {
    overflow: hidden !important;
    text-overflow: ellipsis !important;
}
div[data-testid="stSelectbox"] div[data-baseweb="select"]:hover {
    border-color: var(--accent) !important;
    background: #FFFDF9 !important;
}
div[data-testid="stSelectbox"] div[data-baseweb="select"]:focus-within {
    border-color: var(--primary) !important;
    box-shadow: 0 0 0 4px rgba(142,24,51,0.14) !important;
}
ul[data-testid="stSelectboxVirtualDropdown"] {
    border-radius: 12px !important;
    overflow: hidden !important;
    box-shadow: 0 10px 30px rgba(142,24,51,0.18) !important;
    border: 1px solid var(--border) !important;
}
li[role="option"] {
    font-family: 'Inter', sans-serif !important;
    font-size: 0.88rem !important;
}
li[role="option"]:hover {
    background: var(--secondary) !important;
}

div[data-testid="stRadio"] > label {
    font-family: 'Inter', sans-serif !important;
    font-size: 0.74rem !important;
    font-weight: 600 !important;
    color: var(--subtitle) !important;
    text-transform: uppercase;
    letter-spacing: 0.03em;
}
div[data-testid="stRadio"] > div {
    display: flex !important;
    flex-direction: row !important;
    gap: 6px !important;
    flex-wrap: wrap;
    margin-top: 6px !important;
}
div[data-testid="stRadio"] > div > label {
    background: #FFFFFF !important;
    border: 1.5px solid var(--border) !important;
    border-radius: 40px !important;
    padding: 6px 14px !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 0.82rem !important;
    font-weight: 500 !important;
    color: var(--text) !important;
    cursor: pointer !important;
    transition: all 0.15s ease !important;
}
div[data-testid="stRadio"] > div > label:hover {
    border-color: var(--primary) !important;
    transform: translateY(-2px) !important;
}
div[data-testid="stRadio"] > div > label:has(input:checked) {
    background: var(--accent) !important;
    border-color: var(--accent) !important;
    color: var(--primary) !important;
    font-weight: 700 !important;
}
div[data-testid="stRadio"] input[type="radio"] { display: none !important; }

/* ==== 2. BUTTON HOVER ANIMATION ==== */
div[data-testid="stButton"] button {
    width: 100%;
    background: var(--primary) !important;
    color: #FFF !important;
    border: none !important;
    border-radius: 40px !important;
    font-family: 'Inter', sans-serif;
    font-weight: 700;
    letter-spacing: 0.01em;
    font-size: 1.08rem !important;
    padding: 17px 0 !important;
    cursor: pointer;
    box-shadow: 0 10px 26px rgba(142,24,51,0.38) !important;
    transition: box-shadow .25s ease, transform .25s ease, background .25s ease !important;
}
div[data-testid="stButton"] button:hover {
    background: var(--primary-hover) !important;
    box-shadow: 0 14px 32px rgba(110,18,39,0.46) !important;
    transform: translateY(-3px) !important;
}
div[data-testid="stButton"] button:active {
    transform: translateY(1px) scale(0.98) !important;
    box-shadow: 0 4px 14px rgba(110,18,39,0.4) !important;
}
div[data-testid="stButton"] button:focus-visible {
    outline: 2px solid var(--primary-hover) !important;
    outline-offset: 2px !important;
}

/* Reset button: quieter, outline-only style so it doesn't compete
   visually with the main "Cari Rekomendasi" action */
div[data-testid="stButton"] button[kind="secondary"] {
    background: #FFFFFF !important;
    color: var(--primary) !important;
    border: 1.5px solid var(--border) !important;
    box-shadow: none !important;
    padding: 15px 0 !important;
}
div[data-testid="stButton"] button[kind="secondary"]:hover {
    background: var(--secondary) !important;
    border-color: var(--primary) !important;
    box-shadow: none !important;
}

.search-loading {
    display: flex;
    align-items: center;
    gap: 10px;
    background: var(--secondary);
    border: 1px solid var(--border);
    color: var(--primary);
    font-family: 'Inter', sans-serif;
    font-weight: 600;
    font-size: 0.95rem;
    border-radius: 14px;
    padding: 14px 18px;
    margin-bottom: 18px;
    animation: pulseFade 1.1s ease-in-out infinite;
}
@keyframes pulseFade {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.55; }
}
.spinner-dot {
    width: 9px; height: 9px;
    border-radius: 50%;
    background: var(--primary);
    display: inline-block;
    animation: bounceDot 0.9s infinite ease-in-out;
}
.spinner-dot:nth-child(2) { animation-delay: 0.15s; }
.spinner-dot:nth-child(3) { animation-delay: 0.3s; }
@keyframes bounceDot {
    0%, 80%, 100% { transform: scale(0.6); opacity: 0.5; }
    40% { transform: scale(1); opacity: 1; }
}

/* ==== 5. FADE-IN ANIMATION FOR RESULTS ==== */
@keyframes fadeInUp {
    from { opacity: 0; transform: translateY(14px); }
    to   { opacity: 1; transform: translateY(0); }
}

.results-header {
    font-family: 'Quicksand', sans-serif;
    font-weight: 700;
    font-size: 1.8rem;
    color: var(--text);
    margin: 0 0 20px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    animation: fadeInUp .4s ease both;
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

/* ==== 2. CARD HOVER ANIMATION ==== */
.result-card {
    position: relative;
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 18px 20px;
    margin-bottom: 18px;

    display: flex;
    width: 100%;

    gap: 16px;
    align-items: center;

    box-sizing: border-box;

    box-shadow: 0 1px 8px rgba(142,24,51,.05);
    transition: transform .25s ease, box-shadow .25s ease, border-color .25s ease;
    animation: fadeInUp .45s ease both;
}
.result-card:hover {
    box-shadow: 0 10px 24px rgba(142,24,51,0.16);
    transform: translateY(-3px);
    border-color: var(--accent);
}

.star-rating {
    position: relative;
    display: inline-block;
    font-size: 0.95rem;
    line-height: 1;
    letter-spacing: 1px;
}
.star-rating .stars-bg { color: #ECD8DC; }
.star-rating .stars-fg {
    position: absolute;
    top: 0;
    left: 0;
    overflow: hidden;
    white-space: nowrap;
    color: var(--accent);
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
    border: 1px solid var(--secondary);
    transition: transform .25s ease;
}
.result-card:hover .card-thumb {
    transform: scale(1.08);
}
.card-thumb.rank-1 { background: var(--primary); border-color: var(--primary); color: #FFFFFF; }
.card-thumb.rank-2 { background: var(--secondary); border-color: #EFC0CE; color: var(--primary); }
.card-thumb.rank-3 { background: #FBEAD0; border-color: #EFD3A0; color: #7A5416; }

.card-body { flex: 1; min-width: 0; width: 100%; }

.card-top-row {
    display: flex;
    align-items: center;
    flex-wrap: wrap;
    gap: 10px 12px;
    margin-bottom: 12px;
    width: 100%;
}
.place-name {
    font-family: 'Quicksand', sans-serif;
    font-weight: 700;
    font-size: 1.4rem;
    color: var(--text);
    white-space: normal;
    overflow-wrap: break-word;
    word-break: break-word;
    max-width: 100%;
}
.menu-name {
    font-family: 'Inter', sans-serif;
    font-size: 1.12rem;
    color: var(--subtitle);
    font-weight: 600;
    white-space: normal;
    overflow-wrap: break-word;
    word-break: break-word;
    max-width: 100%;
}

/* ==== 3. BADGE COLORS BY RECOMMENDATION TYPE ==== */
.rec-type-badge {
    border-radius: 40px;
    font-family: 'Inter', sans-serif;
    font-size: 0.85rem;
    padding: 5px 14px;
    font-weight: 600;
    white-space: nowrap;
}

.metrics-row {
    display: flex;
    gap: 8px;
    flex-wrap: wrap;
    row-gap: 8px;
    align-items: center;
    justify-content: space-between;
}
.metrics-left {
    display: flex;
    gap: 8px;
    flex-wrap: wrap;
    row-gap: 8px;
    align-items: center;
}
.metrics-row > div, .metrics-left > div {
    box-sizing: border-box;
    display: inline-flex;
    align-items: center;
    line-height: 1.2;
    white-space: nowrap;
    flex-shrink: 0;
}
.metric-pill {
    background: var(--badge-yellow);
    border: 1px solid var(--secondary);
    border-radius: 40px;
    padding: 5px 14px;
    font-family: 'Inter', sans-serif;
    font-size: 0.9rem;
    color: var(--badge-yellow-text);
    font-weight: 600;
    gap: 4px;
    transition: transform .2s ease;
}
.metric-pill:hover { transform: translateY(-2px); }
.metric-pill .val {
    font-weight: 700;
}

/* ==== 4. DINE OPTION ICON TAG ==== */
.dine-tag {
    background: var(--badge-green);
    border: 1px solid var(--secondary);
    color: var(--badge-green-text);
    border-radius: 40px;
    padding: 5px 14px;
    font-family: 'Inter', sans-serif;
    font-size: 0.9rem;
    font-weight: 600;
    display: inline-flex;
    align-items: center;
    gap: 5px;
    transition: transform .2s ease;
}
.dine-tag:hover { transform: translateY(-2px); }

.maps-link,
.maps-link:hover,
.maps-link:visited,
.maps-link:active {
    text-decoration: none !important;
    background: var(--primary) !important;
    border: none;
    color: #FFFFFF !important;
    border-radius: 40px;
    padding: 8px 18px;
    font-family: 'Inter', sans-serif;
    font-size: 0.9rem;
    font-weight: 700;
    white-space: nowrap;
    box-shadow: 0 4px 12px rgba(142,24,51,0.28);
    transition: box-shadow .25s ease, transform .25s ease, background .25s ease;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    box-sizing: border-box;
    max-width: 100%;
}
.maps-link:hover {
    background: var(--primary-hover) !important;
    box-shadow: 0 8px 18px rgba(110,18,39,0.36) !important;
    transform: translateY(-3px);
}

.placeholder-state{
    display:flex;
    flex-direction:column;
    justify-content:center;
    align-items:center;

    height:500px;

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
    animation: fadeInUp .4s ease both;
}
.empty-state .emoji, .placeholder-state .emoji { font-size: 2.6rem; }
.empty-state p, .placeholder-state p {
    font-family: 'Inter', sans-serif;
    font-size: 0.92rem;
    margin-top: 12px;
    line-height: 1.5;
}
/* swap wording between desktop ("sebelah kiri") and mobile ("di atas")
   layouts, since the columns stack vertically on small screens */
.desktop-only-text { display: block; }
.mobile-only-text { display: none; }

hr { border: none; border-top: 1px solid var(--border); margin: 10px 0 26px; }

@media (max-width: 640px) {
    .block-container { padding-left: 0.8rem !important; padding-right: 0.8rem !important; }

    .hero-banner { padding: 20px 22px; border-radius: 18px; gap: 12px; }
    .hero-banner h1 { font-size: 1.7rem; }
    .hero-banner p { font-size: 0.85rem; }
    .hero-eyebrow { font-size: 0.62rem; padding: 5px 11px; }
    .hero-visual { display: none; }

    .section-label { font-size: 1.3rem; margin-bottom: 2px; }

    .results-header { font-size: 1.35rem; }

    .result-card {
        flex-direction: column;
        align-items: flex-start;
        padding: 16px;
        gap: 12px;
    }
    .card-thumb { width: 40px; height: 40px; font-size: 0.95rem; }
    .card-top-row { gap: 6px 10px; }
    .place-name { font-size: 1.15rem; }
    .menu-name { font-size: 1rem; }

    .metrics-row { flex-direction: column; align-items: flex-start; gap: 10px; }
    .metrics-left { flex-wrap: wrap; gap: 6px; }
    .metric-pill,
    .dine-tag,
    .rec-type-badge {
        font-size: 0.78rem;
        padding: 4px 10px;
    }
    .maps-link { width: 100%; justify-content: center; text-align: center; }

    .placeholder-state { display: none; }

    .desktop-only-text { display: none; }
    .mobile-only-text { display: block; }
}

/* Hover/lift transforms are meant for mouse users only — on touch
   devices (phones/tablets) these get "stuck" on tap and cause the
   jittery/shaky feeling, so we cancel them there. */
@media (hover: none), (pointer: coarse) {
    .result-card,
    .result-card:hover,
    .result-card:hover .card-thumb,
    .metric-pill,
    .metric-pill:hover,
    .dine-tag,
    .dine-tag:hover,
    .maps-link,
    .maps-link:hover,
    div[data-testid="stButton"] button,
    div[data-testid="stButton"] button:hover,
    div[data-testid="stRadio"] > div > label,
    div[data-testid="stRadio"] > div > label:hover,
    div[data-testid="stSelectbox"] div[data-baseweb="select"],
    div[data-testid="stSelectbox"] div[data-baseweb="select"]:hover {
        transform: none !important;
    }
}

</style>
""", unsafe_allow_html=True)


# =====================================================
# PREVENT MOBILE KEYBOARD + FIX "TAP OUTSIDE TO CLOSE" ON DROPDOWNS
# =====================================================
# 1) st.selectbox's underlying input accepts typing (to search/filter
#    options), which triggers the mobile virtual keyboard on tap. This
#    marks those inputs as read-only so tapping only opens the option
#    list — no keyboard.
# 2) On mobile browsers, tapping outside an open dropdown often fails
#    to close it (touch events don't reliably trigger BaseWeb's
#    click-outside listener), forcing the user to pick an option just
#    to get rid of it. We add our own touch/click listener that blurs
#    the open select whenever the tap lands outside it or its popover
#    list, closing it without changing the selection.
components.html("""
<script>
function disableSelectKeyboard() {
    try {
        const doc = window.parent.document;
        const inputs = doc.querySelectorAll('div[data-baseweb="select"] input');
        inputs.forEach(function(el) {
            el.setAttribute('readonly', 'readonly');
            el.setAttribute('inputmode', 'none');
        });
    } catch (e) {}
}

function closeDropdownOnOutsideTap(e) {
    try {
        const doc = window.parent.document;
        const active = doc.activeElement;
        if (!active || active.tagName !== 'INPUT') return;
        const insideSelect = active.closest('div[data-baseweb="select"]');
        if (!insideSelect) return;

        const target = e.target;
        const tappedInsideSelect = target.closest && target.closest('div[data-baseweb="select"]');
        const tappedInsidePopover = target.closest && (
            target.closest('div[data-baseweb="popover"]') ||
            target.closest('ul[data-testid="stSelectboxVirtualDropdown"]') ||
            target.closest('li[role="option"]')
        );
        if (!tappedInsideSelect && !tappedInsidePopover) {
            active.blur();
        }
    } catch (err) {}
}

disableSelectKeyboard();
try {
    const observer = new MutationObserver(disableSelectKeyboard);
    observer.observe(window.parent.document.body, { childList: true, subtree: true });
} catch (e) {}

try {
    window.parent.document.addEventListener('touchstart', closeDropdownOnOutsideTap, true);
    window.parent.document.addEventListener('mousedown', closeDropdownOnOutsideTap, true);
} catch (e) {}
</script>
""", height=0)


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

# ==== 4. ICONS UNTUK DINE OPTION ====
DINE_ICONS = {
    "takeaway": "🥡",
    "dine_in":  "🍽️",
    "both":     "🍽️🥡",
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

# ==== 3. TEMA WARNA BADGE PER TIPE REKOMENDASI ====
THEME_GREEN = {   # paling cocok
    "bg": "#EAF6EC",
    "border": "#B7E0BE",
    "badge_bg": "#2E7D32",
    "badge_text": "#FFFFFF",
    "accent": "#2E7D32"
}
THEME_YELLOW = {  # harga / dine beda
    "bg": "#FFF8E5",
    "border": "#F5DA9A",
    "badge_bg": "#C98A0A",
    "badge_text": "#FFFFFF",
    "accent": "#E0A430"
}
THEME_BLUE = {    # variasi rasa
    "bg": "#E9F2FC",
    "border": "#A9CDEF",
    "badge_bg": "#1565C0",
    "badge_text": "#FFFFFF",
    "accent": "#1565C0"
}
THEME_PURPLE = {  # menu & rasa serupa
    "bg": "#F3ECF8",
    "border": "#D2B4E3",
    "badge_bg": "#6A1B9A",
    "badge_text": "#FFFFFF",
    "accent": "#6A1B9A"
}
THEME_BROWN = {   # alternatif lainnya
    "bg": "#F1EAE4",
    "border": "#D2B9A4",
    "badge_bg": "#6D4C33",
    "badge_text": "#FFFFFF",
    "accent": "#6D4C33"
}

TYPE_THEME_MAP = {
    "paling cocok": THEME_GREEN,
    "harga / dine beda": THEME_YELLOW,
    "variasi rasa": THEME_BLUE,
    "menu & rasa serupa": THEME_PURPLE,
    "alternatif lainnya": THEME_BROWN,
}

def theme_for_type(rec_type):
    key = str(rec_type).strip().lower()
    return TYPE_THEME_MAP.get(key, THEME_BROWN)


# =====================================================
# HERO BANNER
# =====================================================
st.markdown("""
<div class="hero-banner">
    <div class="hero-content">
        <span class="hero-eyebrow">🍨 Sistem Rekomendasi Dessert</span>
        <h1>Dessert Finder <span>Blok M</span></h1>
        <p>Temukan rekomendasi dessert yang sesuai dengan seleramu</p>
    </div>
    <div class="hero-visual">🍰</div>
</div>
""", unsafe_allow_html=True)


# =====================================================
# SESSION STATE
# =====================================================
if "is_searching" not in st.session_state:
    st.session_state.is_searching = False
if "has_result" not in st.session_state:
    st.session_state.has_result = False


# =====================================================
# TWO-COLUMN LAYOUT
# =====================================================
col_filter, col_result = st.columns([1, 2.15], gap="large")

with col_filter:
    st.markdown('<div class="section-label">🔍 Filter Pencarian</div>', unsafe_allow_html=True)

    menu_options = sorted(df["menu_category"].dropna().unique().tolist())
    menu_display = [prettify(m) for m in menu_options]
    menu_map     = dict(zip(menu_display, menu_options))

    f_col1, f_col2 = st.columns(2)
    with f_col1:
        menu_selected_display = st.selectbox("Menu", menu_display, key="menu_select")
        menu = menu_map[menu_selected_display]

    filtered_df = df[df["menu_category"] == menu]

    flavor_options = sorted(filtered_df["flavor_category"].dropna().unique().tolist()) if not filtered_df.empty else []
    flavor_display = [prettify(f) for f in flavor_options]
    flavor_map     = dict(zip(flavor_display, flavor_options))

    with f_col2:
        flavor_selected_display = st.selectbox("Flavor", flavor_display, key="flavor_select")
        flavor = flavor_map[flavor_selected_display] if flavor_display else None

    f_col3, f_col4 = st.columns(2)
    with f_col3:
        price = st.selectbox(
            "Rentang Harga",
            sorted(df["range_price"].dropna().unique().tolist()),
            key="price_select"
        )
    with f_col4:
        dine = st.selectbox(
            "Dine Option",
            ["takeaway", "dine_in", "both"],
            format_func=lambda x: {
                "takeaway": f"{DINE_ICONS['takeaway']} Takeaway",
                "dine_in" : f"{DINE_ICONS['dine_in']} Dine In",
                "both"    : f"{DINE_ICONS['both']} Keduanya"
            }.get(x, x),
            key="dine_select"
        )

    rating_map   = {"3.5+": 3.5, "4.0+": 4.0, "4.5+": 4.5}
    rating_label = st.radio(
        "Minimum Rating",
        options=list(rating_map.keys()),
        index=1,
        horizontal=True,
        key="rating_radio"
    )
    rating = float(rating_map[rating_label])

    top_map   = {"Top 5": 5, "Top 10": 10}
    top_label = st.radio(
        "Jumlah Rekomendasi",
        options=list(top_map.keys()),
        index=1,
        horizontal=True,
        key="topn_radio"
    )
    top_n = top_map[top_label]

    st.markdown("<div class=\"btn-spacer\" style=\"height:6px\"></div>", unsafe_allow_html=True)

    def reset_filters():
        for k in ["menu_select", "flavor_select", "price_select", "dine_select", "rating_radio", "topn_radio"]:
            if k in st.session_state:
                del st.session_state[k]
        st.session_state.is_searching = False

    btn_col1, btn_col2 = st.columns([1.4, 1])
    with btn_col1:
        cari = st.button("🍰  Cari Rekomendasi", use_container_width=True, type="primary")
    with btn_col2:
        st.button("🔄 Reset", use_container_width=True, on_click=reset_filters, key="reset_btn")

    if cari:
        st.session_state.is_searching = True


with col_result:
    if not cari:
        st.markdown("""
        <div class="placeholder-state">
            <div class="emoji">🍰</div>
            <p class="desktop-only-text">Pilih filter di sebelah kiri,<br>lalu klik <strong>Cari Rekomendasi</strong><br>untuk melihat hasilnya di sini.</p>
            <p class="mobile-only-text">Pilih filter di atas,<br>lalu klik <strong>Cari Rekomendasi</strong><br>untuk melihat hasilnya di sini.</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        loading_placeholder = st.empty()
        loading_placeholder.markdown("""
        <div class="search-loading">
            <span class="spinner-dot"></span><span class="spinner-dot"></span><span class="spinner-dot"></span>
            Sedang mencari rekomendasi dessert terbaik untukmu...
        </div>
        """, unsafe_allow_html=True)

        if filtered_df.empty:
            loading_placeholder.empty()
            st.markdown("""
            <div class="empty-state">
                <div class="emoji">😔</div>
                <p>Tidak ada data untuk menu ini.<br>Coba ubah filter dan cari lagi.</p>
            </div>
            """, unsafe_allow_html=True)
        else:
            result = get_rekomendasi(
                menu=menu,
                flavor=flavor,
                price=price,
                dine=dine,
                rating=rating,
                top_n=top_n
            )

            loading_placeholder.empty()

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
                        "takeaway": f"{DINE_ICONS['takeaway']} Takeaway",
                        "dine_in" : f"{DINE_ICONS['dine_in']} Dine In",
                        "both"    : f"{DINE_ICONS['both']} Dine In & Takeaway"
                    }.get(row["dine_option"], row["dine_option"])

                    rec_type = row['recommendation_type']
                    theme = theme_for_type(rec_type)

                    maps_url = row.get("maps_url", None)
                    maps_btn = f'<a href="{maps_url}" target="_blank" class="maps-link">📍 Lihat Lokasi</a>' if maps_url else ''

                    stars_html = render_stars(row['rating'])

                    # stagger fade-in delay per card based on rank
                    delay = min(rank * 0.06, 0.4)

                    card_html = (
                        f'<div class="result-card" style="background:{theme["bg"]}; border-color:{theme["border"]}; border-left:5px solid {theme["accent"]}; animation-delay:{delay}s;">'
                        f'<div class="card-thumb {rank_cls}">#{rank}</div>'
                        f'<div class="card-body">'
                        f'<div class="card-top-row">'
                        f'<span class="place-name">{row["nama_tempat"]}</span>'
                        f'<span class="menu-name">{prettify(row["recommended_item"])}</span>'
                        f'<span class="rec-type-badge" style="background:{theme["badge_bg"]}; color:{theme["badge_text"]};">{rec_type}</span>'
                        f'</div>'
                        f'<div class="metrics-row">'
                        f'<div class="metrics-left">'
                        f'<div class="metric-pill">{stars_html} <span class="val">{row["rating"]}</span></div>'
                        f'<div class="metric-pill">💰 <span class="val">{row["range_price"]}</span></div>'
                        f'<div class="dine-tag">{dine_label}</div>'
                        f'</div>'
                        f'{maps_btn}'
                        f'</div>'
                        f'</div>'
                        f'</div>'
                    )
                    st.markdown(card_html, unsafe_allow_html=True)
