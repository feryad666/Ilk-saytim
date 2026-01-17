import streamlit as st
import requests

# --- TELEGRAM AYARLARI ---
# Bura öz bot tokenini yaz
TOKEN = '8593680837:AAFFEgqzVObAl24xUJWpOzBT9kAaFPv0zqs'
# Bura öz Telegram ID-ni yazmalısan (Aşağıda necə tapacağını deyəcəm)
MY_ID = 'SƏNİN_ID_NOMRƏN' 

def mesaj_gonder(ad, elaqe, mesaj):
    metn = f"🔔 YENİ SİFARİŞ!\n\n👤 Ad: {ad}\n📞 Əlaqə: {elaqe}\n📝 Mesaj: {mesaj}"
    url = f"https://api.telegram.org{TOKEN}/sendMessage?chat_id={MY_ID}&text={metn}"
    requests.get(url)

# --- SAYTIN DİZAYNI ---
st.set_page_config(page_title="Feryad Digital", page_icon="💻")

st.title("🚀 Feryad Digital Xidmətlər")
st.write("Biznesinizi rəqəmsal dünyaya daşıyın!")

# Sifariş Forması
st.divider()
st.subheader("📩 Sifariş və ya sualınız var?")

with st.form("elaqe_formu"):
    ad = st.text_input("Adınız:")
    elaqe = st.text_input("Email və ya Telefonunuz:")
    mesaj = st.text_area("Necə kömək edə bilərik?")
    submit = st.form_submit_button("Göndər")
    
    if submit:
        if ad and elaqe and mesaj:
            mesaj_gonder(ad, elaqe, mesaj)
            st.success(f"Təşəkkürlər, {ad}! Mesajınız bizə çatdı.")
        else:
            st.error("Zəhmət olmasa bütün xanaları doldurun!")
