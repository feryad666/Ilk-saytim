import streamlit as st
import requests

# --- TELEGRAM AYARLARI ---
# Tokenin düzdür, toxunma.
TOKEN = '8593680837:AAFFEgqzVObAl24xUJWpOzBT9kAaFPv0zqs'
# Bura @userinfobot-dan aldığın RƏQƏMLƏRİ yaz (Dırnaq işarəsini silmə)
MY_ID = 'Bura_ID_Rəqəmlərini_Yaz' 

def mesaj_gonder(ad, elaqe, mesaj):
    metn = f"Sifariş gəldi!\nAd: {ad}\nƏlaqə: {elaqe}\nMesaj: {mesaj}"
    # Ən sadə və zəmanətli link forması
    url = f"https://api.telegram.org{TOKEN}/sendMessage?chat_id={MY_ID}&text={metn}"
    requests.get(url)

# --- SAYT ---
st.title("Sınaq Saytı")

with st.form("form"):
    ad = st.text_input("Adınız:")
    elaqe = st.text_input("Telefon:")
    mesaj = st.text_area("Mesaj:")
    duyme = st.form_submit_button("Göndər")
    
    if duyme:
        try:
            mesaj_gonder(ad, elaqe, mesaj)
            st.success("Mesaj göndərildi! Telegram-ı yoxlayın.")
        except Exception as e:
            st.error(f"Xəta baş verdi: {e}")
