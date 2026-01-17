import streamlit as st
import requests

# --- TELEGRAM FUNKSIYASI ---
def mesaj_gonder(ad, elaqe, xidmet, miqdar, cemi):
    tam_link = "https://api.telegram.org"
    metn = (f"🛍️ YENİ SİFARİŞ!\n\n"
            f"👤 Müştəri: {ad}\n"
            f"📞 Əlaqə: {elaqe}\n"
            f"🛠️ Xidmət: {xidmet}\n"
            f"🔢 Say: {miqdar}\n"
            f"💰 Cəmi Məbləğ: {cemi} AZN")
    
    parametrler = {"chat_id": "1333597393", "text": metn}
    requests.get(tam_link, params=parametrler)

# --- SAYTIN AYARLARI ---
st.set_page_config(page_title="Feryad Shop", page_icon="🛒", layout="centered")

# --- QİYMƏT CƏDVƏLİ ---
xidmetler = {
    "Telegram Bot yığılması": 100,
    "Veb Sayt hazırlanması": 300,
    "Data Analiz xidməti": 150,
    "Loqo Dizaynı": 50
}

# --- DİZAYN ---
st.title("🛒 Feryad Digital Mağaza")
st.write("Xidmətlərimizi seçin və anında sifariş verin.")

st.divider()

# Sifariş Bölməsi
col1, col2 = st.columns(2)

with col1:
    st.image("https://cdn-icons-png.flaticon.com", width=200)
    st.info("Bütün xidmətlərimizə 2026-cı il zəmanəti verilir!")

with col2:
    with st.form("sifaris_formu", clear_on_submit=True):
        ad = st.text_input("Adınız və Soyadınız:")
        elaqe = st.text_input("Əlaqə nömrəniz:")
        
        # Seçim qutusu
        secilen_xidmet = st.selectbox("Xidmət seçin:", list(xidmetler.keys()))
        
        # Say seçimi
        say = st.number_input("Miqdar:", min_value=1, max_value=10, value=1)
        
        # Hesablama
        qiymet = xidmetler[secilen_xidmet]
        yekun = qiymet * say
        
        st.write(f"### Yekun: {yekun} AZN")
        
        submit = st.form_submit_button("Sifarişi Təsdiqlə")
        
        if submit:
            if ad and elaqe:
                try:
                    mesaj_gonder(ad, elaqe, secilen_xidmet, say, yekun)
                    st.balloons()
                    st.success("Sifarişiniz uğurla göndərildi! Sizinlə əlaqə saxlayacağıq.")
                except:
                    st.error("Sistemdə xəta baş verdi.")
            else:
                st.warning("Zəhmət olmasa məlumatları tam doldurun.")

# --- FOOTER ---
st.divider()
st.caption("© 2026 Feryad Digital Services. Powered by Python & Streamlit.")
