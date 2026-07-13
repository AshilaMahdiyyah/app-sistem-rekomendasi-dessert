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
.hero-content { position: relative; z-index: 2; max-width: 640px; }
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
    font-weight: 800;
    font-size: 2.7rem;
    letter-spacing: 0.01em;
    line-height: 1.08;
    color: #FFF3E6 !important;
    margin: 0 0 2px;
    text-shadow: 0 2px 4px rgba(0,0,0,0.35), 0 4px 24px rgba(0,0,0,0.25);
}
.hero-banner h1 span {
    color: #F0C879 !important;
    text-shadow: 0 2px 4px rgba(0,0,0,0.3), 0 0 20px rgba(240,200,121,0.35);
}
.hero-banner p {
    font-family: 'Inter', sans-serif;
    font-weight: 500;
    font-size: 0.95rem;
    letter-spacing: 0.01em;
    color: rgba(255,255,255,0.9);
    margin: 0;
    line-height: 1.6;
    max-width: none;
    white-space: nowrap;
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
    font-size: 1.42rem;
    color: var(--text);
    margin-bottom: 2px;
    display: flex;
    flex-wrap: nowrap;
    align-items: center;
    gap: 8px;
    white-space: nowrap;
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
/* Center tulisan Reset */
div[data-testid="stButton"] button[kind="secondary"] p{
    margin: 0 !important;
    width: 100% !important;
    text-align: center !important;
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
    margin: 0 0 16px;
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

/* ====================================================
   RESULT CARD — 3 kolom eksplisit, ukuran ringkas/compact:
   1) Ranking (~8-10%)  2) Info restoran/menu (~65-70%)  3) Aksi (~20-25%)
   ==================================================== */
.result-card {
    position: relative;
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 12px 16px;
    margin-bottom: 12px;

    display: grid;
    grid-template-columns: minmax(46px, 10%) 1fr minmax(110px, 20%);
    gap: 4px 14px;
    align-items: center;
    width: 100%;

    box-sizing: border-box;

    box-shadow: 0 1px 6px rgba(142,24,51,.05);
    transition: transform .25s ease, box-shadow .25s ease, border-color .25s ease;
    animation: fadeInUp .45s ease both;
}
.result-card:hover {
    box-shadow: 0 8px 18px rgba(142,24,51,0.16);
    transform: translateY(-2px);
    border-color: var(--accent);
}

.star-rating {
    position: relative;
    display: inline-block;
    font-size: 0.92rem;
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

/* ==== Kolom 1: Ranking ==== */
.card-rank {
    display: flex;
    align-items: center;
    justify-content: center;
    min-width: 0;
}

.card-thumb {
    flex-shrink: 0;
    width: 46px;
    height: 46px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-family: 'Quicksand', sans-serif;
    font-weight: 700;
    font-size: 1.1rem;
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

/* ==== Kolom 2: restoran, menu, & informasi (fokus utama kartu) ==== */
.card-body {
    display: flex;
    flex-direction: column;
    gap: 4px;
    min-width: 0;
}
.card-body .place-name {
    font-family: 'Quicksand', sans-serif;
    font-weight: 700;
    font-size: 1.02rem;
    color: var(--text);
    white-space: normal;
    overflow-wrap: break-word;
    word-break: break-word;
    line-height: 1.25;
}

/* baris atas: nama tempat lalu badge tipe rekomendasi langsung di
   sampingnya (bukan didorong ke ujung kanan) */
.card-top-row {
    display: flex;
    align-items: center;
    justify-content: flex-start;
    gap: 6px;
    flex-wrap: nowrap;
}
.card-top-row .place-name {
    /* flex-grow: 0 so the box only takes up as much width as the
       text itself needs — otherwise it stretches to fill the row
       and the badge ends up far to the right instead of hugging
       the name. flex-shrink stays on so long names still truncate
       instead of overflowing the card. */
    flex: 0 1 auto;
    min-width: 0;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}
.card-top-row .badge-info {
    flex-shrink: 0;
}
.card-top-row .badge-info summary .rec-type-badge {
    font-size: 0.72rem;
    padding: 3px 10px;
}

.card-menu {
    display: flex;
    flex-direction: column;
    gap: 2px;
    min-width: 0;
}
.menu-label {
    font-family: 'Inter', sans-serif;
    font-size: 0.68rem;
    font-weight: 700;
    color: var(--subtitle);
    text-transform: uppercase;
    letter-spacing: 0.06em;
}
.menu-name-hero {
    font-family: 'Quicksand', sans-serif;
    font-weight: 700;
    font-size: 1.08rem;
    line-height: 1.2;
    letter-spacing: 0;
    color: var(--text);
    overflow-wrap: break-word;
    word-break: break-word;
}

.meta-pills {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    gap: 6px;
}

/* ==== 3. BADGE COLORS BY RECOMMENDATION TYPE ==== */
.rec-type-badge {
    border-radius: 40px;
    font-family: 'Inter', sans-serif;
    font-size: 0.78rem;
    padding: 4px 11px;
    font-weight: 600;
    white-space: nowrap;
}

.metric-pill {
    background: var(--badge-yellow);
    border: 1px solid var(--secondary);
    border-radius: 40px;
    padding: 4px 11px;
    font-family: 'Inter', sans-serif;
    font-size: 0.86rem;
    color: var(--badge-yellow-text);
    font-weight: 600;
    display: inline-flex;
    align-items: center;
    line-height: 1.2;
    white-space: nowrap;
    flex-shrink: 0;
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
    padding: 4px 11px;
    font-family: 'Inter', sans-serif;
    font-size: 0.86rem;
    font-weight: 600;
    display: inline-flex;
    align-items: center;
    gap: 5px;
    line-height: 1.2;
    white-space: nowrap;
    flex-shrink: 0;
    transition: transform .2s ease;
}
.dine-tag:hover { transform: translateY(-2px); }

/* ==== Kolom 3: aksi (tombol lokasi) ==== */
.card-action {
    display: flex;
    align-items: center;
    justify-content: center;
    min-width: 0;
}

.maps-link,
.maps-link:hover,
.maps-link:visited,
.maps-link:active {
    text-decoration: none !important;
    background: var(--primary) !important;
    border: none;
    color: #FFFFFF !important;
    border-radius: 40px;
    padding: 9px 16px;
    font-family: 'Inter', sans-serif;
    font-size: 0.88rem;
    font-weight: 700;
    white-space: nowrap;
    box-shadow: 0 3px 10px rgba(142,24,51,0.28);
    transition: box-shadow .25s ease, transform .25s ease, background .25s ease;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    box-sizing: border-box;
    width: 100%;
    max-width: 100%;
}
.maps-link {
    -webkit-tap-highlight-color: transparent;
    touch-action: manipulation;
    outline: none;
}
.maps-link:hover {
    background: var(--primary-hover) !important;
    box-shadow: 0 6px 14px rgba(110,18,39,0.36) !important;
    transform: translateY(-2px);
}
.maps-link:active {
    background: var(--primary-hover) !important;
    box-shadow: 0 3px 10px rgba(110,18,39,0.32) !important;
    transform: translateY(1px) scale(0.97) !important;
    transition: transform .12s ease, box-shadow .12s ease, background .12s ease !important;
}
.maps-link:focus-visible {
    outline: 2px solid var(--primary-hover);
    outline-offset: 2px;
    border-radius: 40px;
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

.search-hint {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
    background: var(--secondary);
    border: 1px solid var(--border);
    color: var(--primary);
    font-family: 'Inter', sans-serif;
    font-weight: 600;
    font-size: 0.88rem;
    border-radius: 40px;
    padding: 11px 16px;
    margin-top: 12px;
    text-align: center;
    animation: fadeInUp .4s ease both, bounceHint 1.4s ease-in-out infinite;
}
@keyframes bounceHint {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(3px); }
}

hr { border: none; border-top: 1px solid var(--border); margin: 10px 0 26px; }

/* ==== INFO POPOVER PER BADGE ==== */
.badge-info {
    position: relative;
    display: inline-block;
}
.badge-info summary {
    list-style: none;
    cursor: pointer;
    user-select: none;
}
.badge-info summary::-webkit-details-marker { display: none; }

.badge-info summary .rec-type-badge {
    display: inline-flex;
    align-items: center;
    gap: 5px;
}
.badge-info summary .info-icon {
    width: 11px;
    height: 11px;
    flex-shrink: 0;
    opacity: 0.9;
    vertical-align: middle;
}

.badge-info-content {
    position: absolute;
    top: calc(100% + 8px);
    left: 0;
    z-index: 30;
    width: 220px;
    max-width: 70vw;
    background: #FFFFFF;
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 10px 12px;
    box-shadow: 0 10px 28px rgba(142,24,51,0.18);
    font-family: 'Inter', sans-serif;
    font-size: 0.78rem;
    line-height: 1.4;
    color: var(--text);
    animation: fadeInUp .15s ease both;
}
.badge-info-content::before {
    content: "";
    position: absolute;
    top: -6px;
    left: 16px;
    width: 12px;
    height: 12px;
    background: #FFFFFF;
    border-left: 1px solid var(--border);
    border-top: 1px solid var(--border);
    transform: rotate(45deg);
}

@media (max-width: 640px) {
    .badge-info-content {
        width: 200px;
        max-width: calc(100vw - 48px);
        font-size: 0.74rem;
        left: 50%;
        right: auto;
        transform: translateX(-50%);
    }
    .badge-info-content::before {
        left: 50%;
        transform: translateX(-50%) rotate(45deg);
    }
}

@media (max-width: 640px) {
    .block-container { padding-left: 0.8rem !important; padding-right: 0.8rem !important; }

    .hero-banner { padding: 20px 22px; border-radius: 18px; gap: 12px; }
    .hero-banner h1 {
        font-size: 1.55rem;
        line-height: 1.2;
        letter-spacing: 0;
        overflow-wrap: break-word;
    }
    .hero-banner p { font-size: 0.85rem; white-space: normal; }
    .hero-eyebrow { font-size: 0.62rem; padding: 5px 11px; }
    .hero-visual { display: none; }

    .section-label { font-size: 1.12rem; margin-bottom: 2px; }

    /* Trim the large default column gap that Streamlit adds, which
       left an oversized blank gap once the two columns stack
       vertically on narrow screens */
    div[data-testid="stHorizontalBlock"]:has(.section-label) {
        row-gap: 6px !important;
    }
    div[data-testid="stHorizontalBlock"]:has(.section-label) > div[data-testid="stColumn"] {
        margin-bottom: 0 !important;
    }

    .results-header { font-size: 1.35rem; margin-bottom: 14px; }

    .result-card {
        grid-template-columns: auto 1fr;
        grid-template-areas:
            "rank body"
            "action action";
        padding: 16px 16px;
        gap: 10px 12px;
        margin-bottom: 16px;
    }
    .card-rank {
        grid-area: rank;
        align-items: flex-start;
        justify-content: flex-start;
    }
    .card-body {
        grid-area: body;
        gap: 6px;
    }
    .card-action {
        grid-area: action;
    }
    .card-thumb { width: 38px; height: 38px; font-size: 0.9rem; }
    .card-body .place-name { font-size: 0.98rem; }

    /* On mobile there isn't enough width to keep the place name on
       a single truncated line next to the badge — let it wrap onto
       multiple lines instead of being cut off, and keep the badge
       aligned to the top of the (now possibly multi-line) name
       instead of sitting far away or being center-squished. */
    .card-top-row {
        align-items: flex-start;
        flex-wrap: nowrap;
    }
    .card-top-row .place-name {
        white-space: normal;
        overflow: visible;
        text-overflow: unset;
        overflow-wrap: break-word;
        word-break: break-word;
    }
    .card-top-row .badge-info {
        margin-top: 2px;
    }

    /* The popover used to be centered under the badge itself, but
       when the badge sits near the card's right edge (short cards,
       long names) that pushed the 200px-wide box past the screen
       edge and it got clipped. Anchoring it to the card's own
       padding box (.result-card is position:relative) instead of
       the badge keeps it fully within the card — and therefore
       fully within the screen — no matter where the badge lands. */
    .badge-info {
        position: static;
    }
    .badge-info-content {
        left: 16px;
        right: 16px;
        width: auto;
        max-width: none;
        transform: none;
    }
    .badge-info-content::before {
        display: none;
    }

    .menu-label { font-size: 0.62rem; }
    .menu-name-hero { font-size: 0.92rem; }

    .meta-pills { gap: 5px; }
    .metric-pill,
    .dine-tag,
    .rec-type-badge {
        font-size: 0.7rem;
        padding: 3px 9px;
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

# ==== PENJELASAN TIAP TIPE REKOMENDASI (UNTUK POPOVER BADGE) ====
TYPE_INFO_MAP = {
    "paling cocok": "Pas banget! Menu, rasa, harga, dan opsi penyajiannya sesuai semua sama pilihanmu.",
    "harga / dine beda": "Menu & rasanya sama kok, cuma harga atau opsi penyajiannya agak beda.",
    "variasi rasa": "Menunya sama, tapi coba rasa lain — siapa tau kamu suka juga.",
    "menu & rasa serupa": "Gak ada yang persis, jadi ini yang paling mirip sama seleramu.",
    "alternatif lainnya": "Rekomendasi cadangan, tapi tetap yang paling mirip ke seleramu.",
}

def info_for_type(rec_type):
    key = str(rec_type).strip().lower()
    return TYPE_INFO_MAP.get(key, "Rekomendasi ini dipilih berdasarkan tingkat kemiripan dengan preferensimu.")


# =====================================================
# HERO BANNER
# =====================================================
st.markdown("""
<div class="hero-banner">
    <div class="hero-content">
        <span class="hero-eyebrow">🍨 Sistem Rekomendasi Dessert</span>
        <h1>Dessert Finder <span>Blok M</span></h1>
        <p>Temukan rekomendasi dessert di Blok M yang sesuai dengan seleramu!</p>
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
    st.markdown('<div class="section-label">🔍 Preferensi Rekomendasi</div>', unsafe_allow_html=True)

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
                "both"    : f"{DINE_ICONS['both']} Both"
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
        st.button("Reset", use_container_width=True, on_click=reset_filters, key="reset_btn")

    if cari:
        st.session_state.is_searching = True
        # On mobile the result column is stacked below the filter
        # column (not side-by-side), so give a nudge to scroll down
        # once the search has been triggered. Hidden on desktop via
        # the .mobile-only-text class.
        st.markdown(
            '<p class="mobile-only-text search-hint">👇 Lihat hasil rekomendasi di bawah</p>',
            unsafe_allow_html=True
        )


with col_result:
    if not cari:
        st.markdown("""
        <div class="placeholder-state">
            <div class="emoji">🍰</div>
            <p class="desktop-only-text">Pilih preferensi di sebelah kiri,<br>lalu klik <strong>Cari Rekomendasi</strong><br>untuk melihat hasil rekomendasi di sini.</p>
            <p class="mobile-only-text">Pilih preferensi di atas,<br>lalu klik <strong>Cari Rekomendasi</strong><br>untuk melihat hasil rekomendasi di sini.</p>
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
                    rec_info = info_for_type(rec_type)

                    maps_url = row.get("maps_url", None)
                    maps_btn = f'<a href="{maps_url}" target="_blank" class="maps-link">📍 Lihat Lokasi</a>' if maps_url else ''

                    stars_html = render_stars(row['rating'])

                    # stagger fade-in delay per card based on rank
                    delay = min(rank * 0.06, 0.4)

                    card_html = (
                        f'<div class="result-card" style="background:{theme["bg"]}; border-color:{theme["border"]}; border-left:4px solid {theme["accent"]}; animation-delay:{delay}s;">'

                        # ==== Kolom 1 — Ranking ====
                        f'<div class="card-rank">'
                        f'<div class="card-thumb {rank_cls}">#{rank}</div>'
                        f'</div>'

                        # ==== Kolom 2 — Restoran, menu, & informasi ====
                        f'<div class="card-body">'

                        # baris atas: nama tempat + badge tipe rekomendasi di sampingnya
                        f'<div class="card-top-row">'
                        f'<span class="place-name">{row["nama_tempat"]}</span>'
                        f'<details class="badge-info" name="rec-badge-group">'
                        f'<summary><span class="rec-type-badge" style="background:{theme["badge_bg"]}; color:{theme["badge_text"]};">{rec_type}'
                        f'<svg class="info-icon" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg">'
                        f'<circle cx="8" cy="8" r="6.75" stroke="currentColor" stroke-width="1.3"/>'
                        f'<rect x="7.25" y="6.75" width="1.5" height="4.5" rx="0.75" fill="currentColor"/>'
                        f'<circle cx="8" cy="4.85" r="0.95" fill="currentColor"/>'
                        f'</svg>'
                        f'</span></summary>'
                        f'<div class="badge-info-content">{rec_info}</div>'
                        f'</details>'
                        f'</div>'

                        # menu tetap di baris tersendiri di bawah nama tempat
                        # (label "Menu" lalu nama menu di bawahnya), ukuran ringkas
                        f'<div class="card-menu">'
                        f'<span class="menu-label">Menu</span>'
                        f'<span class="menu-name-hero">{prettify(row["recommended_item"])}</span>'
                        f'</div>'

                        # baris metrik: rating, harga, dine option saja
                        f'<div class="meta-pills">'
                        f'<div class="metric-pill">{stars_html} <span class="val">{row["rating"]}</span></div>'
                        f'<div class="metric-pill">💰 <span class="val">{row["range_price"]}</span></div>'
                        f'<div class="dine-tag">{dine_label}</div>'
                        f'</div>'
                        f'</div>'

                        # ==== Kolom 3 — Aksi ====
                        f'<div class="card-action">'
                        f'{maps_btn}'
                        f'</div>'

                        f'</div>'
                    )
                    st.markdown(card_html, unsafe_allow_html=True)
