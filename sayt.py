import streamlit as st
import requests

# --- TELEGRAM AYARLARI ---
TOKEN = '8593680837:AAFFEgqzVObAl24xUJWpOzBT9kAaFPv0zqs'
# Bura MÜTLƏQ öz rəqəmlərdən ibarət ID-ni yaz (məsələn: '12345678')
MY_ID = 'Bura_ID_Rəqəmlərini_Yaz' 

def mesaj_gonder(ad, elaqe, mesaj):
    metn = f"Sifariş gəldi!\nAd: {ad}\nƏlaqə: {elaqe}\nMesaj: {mesaj}"
    # Linkin strukturu tam dəqiq belə olmalıdır:
    url = f"https://api.telegram.org{TOKEN}/sendMessage"
    payload = {'chat_id': MY_ID, 'text': metn}
    requests.get(url, params=payload)

# --- SAYTIN GÖRÜNÜŞÜ ---
st.title("🚀 Feryad Digital Mağaza")

with st.form("my_form", clear_on_submit=True):
    ad = st.text_input("Adınız:")
    elaqe = st.text_input("Əlaqə nömrəniz:")
    mesaj = st.text_area("Sifarişiniz nədir?")
    submit = st.form_submit_button("Sifarişi Tamamla")
    
    if submit:
        if ad and elaqe and mesaj:
            try:
                mesaj_gonder(ad, elaqe, mesaj)
                st.success("Təbriklər! Sifarişiniz qəbul edildi. Telegram-a bildiriş göndərildi.")
                st.balloons()
            except Exception as e:
                st.error(f"Xəta: {e}")
        else:
            st.warning("Zəhmət olmasa bütün xanaları doldurun!")
