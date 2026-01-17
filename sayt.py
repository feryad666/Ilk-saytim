import streamlit as st

st.set_page_config(page_title="Feryad Digital", page_icon="💻", layout="wide")

# Saytın yuxarı hissəsi (Header)
st.title("🚀 Feryad Digital Xidmətlər")
st.subheader("Biznesinizi rəqəmsal dünyaya daşıyın!")

# Xidmətlər bölməsi (3 sütun)
col1, col2, col3 = st.columns(3)

with col1:
    st.image("https://cdn-icons-png.flaticon.com", width=100)
    st.write("### Python Botlar")
    st.write("Telegram və WhatsApp üçün avtomatlaşdırılmış botlar.")
    st.button("Qiymət: 100 AZN", key="bot")

with col2:
    st.image("https://cdn-icons-png.flaticon.com", width=100)
    st.write("### Veb Saytlar")
    st.write("Müasir və sürətli idarəetmə panelli saytlar.")
    st.button("Qiymət: 300 AZN", key="web")

with col3:
    st.image("https://cdn-icons-png.flaticon.com", width=100)
    st.write("### Data Analitika")
    st.write("Məlumatların toplanması və Excel hesabatlar.")
    st.button("Qiymət: 150 AZN", key="data")

# Sifariş Forması
st.divider()
st.subheader("📩 Sifariş və ya sualınız var?")
with st.form("elaqe_formu"):
    ad = st.text_input("Adınız:")
    email = st.text_input("Email və ya Telefonunuz:")
    mesaj = st.text_area("Necə kömək edə bilərik?")
    submit = st.form_submit_button("Göndər")
    
    if submit:
        st.success(f"Təşəkkürlər, {ad}! Ən qısa zamanda sizinlə əlaqə saxlayacağıq.")
        
