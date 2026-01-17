import streamlit as st
import requests

# --- TELEGRAM FUNKSİYASI ---
def mesaj_gonder(ad, elaqe, mesaj):
    tam_link = "https://api.telegram.org"
    metn = f"🚀 YENİ SİFARİŞ!\n\n👤 Ad: {ad}\n📞 Əlaqə: {elaqe}\n📝 Mesaj: {mesaj}"
    parametrler = {"chat_id": "1333597393", "text": metn}
    requests.get(tam_link, params=parametrler)

# --- SAYTIN DİZAYNI (VİSUAL) ---
st.set_page_config(page_title="Feryad Digital", page_icon="👨‍💻", layout="wide")

# 1. Başlıq və Loqo (Header)
st.markdown("<h1 style='text-align: center; color: #007BFF;'>🚀 Feryad Digital Agentliyi</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 20px;'>Biznesiniz üçün sürətli və müasir proqram təminatı!</p>", unsafe_allow_html=True)
st.divider()

# 2. Xidmətlərimiz (Sütunlar şəklində)
st.write("### ✨ Xidmətlərimiz")
col1, col2, col3 = st.columns(3)

with col1:
    st.info("### 🤖 Telegram Botlar")
    st.write("Avtomatik satış və sifariş qəbul edən botlar yığılır.")
    st.write("**Qiymət: 100 AZN-dən**")

with col2:
    st.success("### 🌐 Veb Saytlar")
    st.write("Sizin üçün müasir idarəetmə paneli olan saytlar hazırlayırıq.")
    st.write("**Qiymət: 300 AZN-dən**")

with col3:
    st.warning("### 📈 Data Analiz")
    st.write("Məlumatların toplanması və Excel hesabatların hazırlanması.")
    st.write("**Qiymət: 150 AZN-dən**")

st.divider()

# 3. Sifariş Forması (Daha yığcam)
st.write("### 📩 Bizimlə Əlaqə")
c1, c2 = st.columns([1, 1])

with c1:
    st.write("Suallarınız var? Formu doldurun, biz sizə Telegram vasitəsilə cavab verək.")
    st.image("https://cdn.pixabay.com")

with c2:
    with st.form("sifaris_formu", clear_on_submit=True):
        ad = st.text_input("Tam Adınız:")
        elaqe = st.text_input("Telefon və ya Email:")
        mesaj = st.text_area("Hansı xidmətlə maraqlanırsınız?")
        submit = st.form_submit_button("Sifarişi Göndər")
        
        if submit:
            if ad and elaqe and mesaj:
                try:
                    mesaj_gonder(ad, elaqe, mesaj)
                    st.balloons()
                    st.success(f"Təşəkkürlər {ad}! Sifarişiniz qəbul olundu.")
                except:
                    st.error("Xəta baş verdi.")
            else:
                st.warning("Xanaları doldurun.")

# 4. Footer (Alt hissə)
st.write("---")
st.write("© 2026 Feryad Digital - Bütün hüquqlar qorunur.")
