import streamlit as st
import requests

# --- TELEGRAM AYARLARI ---
TOKEN = '8593680837:AAFFEgqzVObAl24xUJWpOzBT9kAaFPv0zqs'
MY_ID = 'SƏNİN_ID_NOMRƏN' # Bura @userinfobot-dan aldığın ID-ni yazmağı unutma

def mesaj_gonder(ad, elaqe, mesaj):
    metn = f"🔔 YENİ SİFARİŞ!\n\n👤 Ad: {ad}\n📞 Əlaqə: {elaqe}\n📝 Mesaj: {mesaj}"
    url = f"https://api.telegram.org{TOKEN}/sendMessage"
    payload = {'chat_id': MY_ID, 'text': metn}
    # Bu üsul (params) boşluqları və simvolları avtomatik düzəldir
    requests.get(url, params=payload)

# --- SAYTIN DİZAYNI ---
st.set_page_config(page_title="Feryad Digital", page_icon="💻")

st.title("🚀 Feryad Digital Xidmətlər")
st.write("Biznesinizi rəqəmsal dünyaya daşıyın!")

st.divider()
st.subheader("📩 Sifariş və ya sualınız var?")

with st.form("elaqe_formu", clear_on_submit=True):
    ad = st.text_input("Adınız:")
    elaqe = st.text_input("Email və ya Telefonunuz:")
    mesaj = st.text_area("Necə kömək edə bilərik?")
    submit = st.form_submit_button("Göndər")
    
    if submit:
        if ad and elaqe and mesaj:
            try:
                mesaj_gonder(ad, elaqe, mesaj)
                st.success(f"Təşəkkürlər, {ad}! Mesajınız bizə çatdı.")
                st.balloons()
            except Exception as e:
                st.error("Xəta baş verdi. Zəhmət olmasa bir az sonra yenidən yoxlayın.")
        else:
            st.warning("Zəhmət olmasa bütün xanaları doldurun!")
