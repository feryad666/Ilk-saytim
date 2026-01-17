import streamlit as st
import requests

def mesaj_gonder(ad, elaqe, mesaj):
    # Linki tam hazır şəkildə bura qoyuram, heç bir simvolu dəyişmə
    tam_link = "https://api.telegram.org"
    
    metn = f"🚀 YENİ SİFARİŞ!\n\n👤 Ad: {ad}\n📞 Əlaqə: {elaqe}\n📝 Mesaj: {mesaj}"
    
    parametrler = {
        "chat_id": "1333597393",
        "text": metn
    }
    
    response = requests.get(tam_link, params=parametrler)
    return response.status_code

# --- SAYTIN GÖRÜNÜŞÜ ---
st.set_page_config(page_title="Feryad Digital", page_icon="🚀")
st.title("🚀 Feryad Digital Mağaza")

with st.form("sifaris_formu", clear_on_submit=True):
    ad = st.text_input("Adınız:")
    elaqe = st.text_input("Telefon və ya Email:")
    mesaj = st.text_area("Nə sifariş etmək istəyirsiniz?")
    submit = st.form_submit_button("Sifarişi Göndər")
    
    if submit:
        if ad and elaqe and mesaj:
            try:
                status = mesaj_gonder(ad, elaqe, mesaj)
                if status == 200:
                    st.success(f"Təbriklər {ad}! Sifarişiniz Telegram-a göndərildi.")
                    st.balloons()
                else:
                    st.error(f"Xəta kodu: {status}. Zəhmət olmasa Telegram-da botu tapıb START basın.")
            except Exception as e:
                st.error(f"Sistem xətası: {e}")
        else:
            st.warning("Zəhmət olmasa bütün xanaları doldurun!")
