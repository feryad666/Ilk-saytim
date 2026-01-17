import streamlit as st
import requests

# --- TELEGRAM FUNKSİYASI ---
def mesaj_gonder(ad, elaqe, xidmet, miqdar, cemi):
    tam_link = "https://api.telegram.org"
    metn = (f"🛍️ YENİ SİFARİŞ!\n\n"
            f"👤 Müştəri: {ad}\n"
            f"📞 Əlaqə: {elaqe}\n"
            f"🛠️ Xidmət: {xidmet}\n"
            f"🔢 Say: {miqdar}\n"
            f"💰 Cəmi: {cemi} AZN")
    parametrler = {"chat_id": "1333597393", "text": metn}
    requests.get(tam_link, params=parametrler)

# --- SAYTIN AYARLARI ---
st.set_page_config(page_title="Feryad Business Portal", page_icon="📈", layout="wide")

# --- SOL MENYU (SIDEBAR) ---
st.sidebar.image("https://cdn-icons-png.flaticon.com", width=100)
st.sidebar.title("Naviqasiya")
sehife = st.sidebar.radio("Getmək istədiyiniz bölmə:", ["🏠 Ana Səhifə", "🛒 Mağaza", "📞 Əlaqə & FAQ"])

# --- QİYMƏTLƏR ---
xidmetler = {"Telegram Bot": 100, "Veb Sayt": 300, "Data Analiz": 150, "Süni İntellekt": 500}

# --- 1. ANA SƏHİFƏ ---
if sehife == "🏠 Ana Səhifə":
    st.markdown("<h1 style='text-align: center;'>🚀 Feryad Digital Portalına Xoş Gəldiniz</h1>", unsafe_allow_html=True)
    st.image("https://images.unsplash.com", use_container_width=True)
    
    st.write("## Biz Kimik?")
    st.write("2026-cı ilin texnologiyaları ilə biznesinizi rəqəmsallaşdıran peşəkar komandayıq.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.success("✅ 100+ Uğurlu Layihə")
    with col2:
        st.success("✅ 24/7 Texniki Dəstək")

# --- 2. MAĞAZA ---
elif sehife == "🛒 Mağaza":
    st.title("🛍️ Xidmət Vitrini")
    
    col_a, col_b = st.columns([2, 1])
    
    with col_a:
        st.write("### Mövcud Xidmətlər")
        for x, q in xidmetler.items():
            st.write(f"🔹 **{x}** - {q} AZN")
        
        st.image("https://images.unsplash.com")

    with col_b:
        st.write("### Sürətli Sifariş")
        with st.form("order_form"):
            ad = st.text_input("Adınız:")
            elaqe = st.text_input("Nömrəniz:")
            secim = st.selectbox("Xidmət:", list(xidmetler.keys()))
            miqdar = st.number_input("Miqdar:", 1, 10)
            
            yekun = xidmetler[secim] * miqdar
            st.write(f"**Yekun Ödəniş: {yekun} AZN**")
            
            if st.form_submit_button("Sifarişi Gönder"):
                mesaj_gonder(ad, elaqe, secim, miqdar, yekun)
                st.balloons()
                st.success("Sifariş alındı!")

# --- 3. ƏLAQƏ & FAQ ---
elif sehife == "📞 Əlaqə & FAQ":
    st.title("📞 Dəstək Mərkəzi")
    
    with st.expander("Sual: Sifariş neçə günə hazır olur?"):
        st.write("Cavab: Xidmətdən asılı olaraq 3-7 iş günü ərzində.")
    
    with st.expander("Sual: Ödəniş üsulları hansılardır?"):
        st.write("Cavab: Kartdan karta və ya nağd şəkildə ödəniş mümkündür.")

    st.write("### Bizimlə birbaşa əlaqə:")
    st.write("📧 Email: support@feryad.az")
    st.write("📱 Telegram: @feryad_admin")

st.sidebar.write("---")
st.sidebar.write("📌 Son Yenilənmə: Yanvar, 2026")
