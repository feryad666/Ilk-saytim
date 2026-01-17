import streamlit as st
import requests

# --- TELEGRAM AYARLARI ---
# Bura toxunma, hər şey yerindədir
TOKEN = "8593680837:AAFFEgqzVObAl24xUJWpOzBT9kAaFPv0zqs"

# DİQQƏT: Aşağıdakı dırnaq içindəki sözləri sil və @userinfobot-dan aldığın ID-ni yaz
MY_ID = "BURA_OZ_ID_NOMRENI_YAZ" 

def mesaj_gonder(ad, elaqe, mesaj):
    # Linkin quruluşunu kod avtomatik düzəldir
    base_url = f"https://api.telegram.org{TOKEN}/sendMessage"
    metn = f"🚀 YENİ SİFARİŞ!\n\n👤 Ad: {ad}\n📞 Əlaqə: {elaqe}\n📝 Mesaj: {mesaj}"
    
    params = {
        "chat_id": MY_ID,
        "text": metn
    }
    
    response = requests.get(base_url, params=params)
    return response.status_code

# --- SAYTIN DİZAYNI ---
st.title("🚀 Feryad Digital Mağaza")
st.write("Sifariş formunu doldurun, biz sizinlə əlaqə saxlayaq.")

with st.form("sifaris_formu", clear_on_submit=True):
    ad = st.text_input("Adınız:")
    elaqe = st.text_input("Telefon və ya Email:")
    mesaj = st.text_area("Nə sifariş etmək istəyirsiniz?")
    submit = st.form_submit_button("Sifarişi Göndər")
    
    if submit:
        if ad and elaqe and mesaj:
            if MY_ID == "BURA_OZ_ID_NOMRENI_YAZ":
                st.error("Zəhmət olmasa koddakı MY_ID hissəsinə öz Telegram ID-nizi yazın!")
            else:
                try:
                    status = mesaj_gonder(ad, elaqe, mesaj)
                    if status == 200:
                        st.success(f"Təbriklər {ad}! Sifarişiniz bizə çatdı.")
                        st.balloons()
                    else:
                        st.error(f"Telegram xətası: Status kodu {status}. Botu oyatdığınızdan əmin olun.")
                except Exception as e:
                    st.error(f"Sistem xətası: {e}")
        else:
            st.warning("Zəhmət olmasa bütün xanaları doldurun!")
