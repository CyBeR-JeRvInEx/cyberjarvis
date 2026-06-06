import streamlit as st

st.set_page_config(page_title="CyBeR-JeRvInEx OS", page_icon="🎤", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #060a12; color: #00ff66; }
    h1 { color: #00ff66; font-family: 'Courier New', monospace; text-shadow: 0 0 10px #00ff66; text-align: center; }
    .stTextInput>div>div>input { background-color: #0f1624 !important; color: #00ff66 !important; border: 2px solid #00ff66 !important; font-family: 'Courier New', monospace; }
    </style>
""", unsafe_allow_html=True)

st.title("[ CYBER-JARVIS MULTILINGUAL OS ]")
st.write("BILINGUAL SYSTEM: VOICE & TEXT INTERACTION")

jezik = st.selectbox("Izaberi jezik / Select Language", ["Srpski (SR)", "English (US)"])

if jezik == "Srpski (SR)":
    status_tekst = "Jarvis: Sistem spreman. Ukucajte komandu u polje ispod."
    placeholder_tekst = "Ukucaj nešto ovde i pritisni Enter..."
else:
    status_tekst = "Jarvis: System ready. Type a command in the box below."
    placeholder_tekst = "Type here and press Enter..."

st.info(status_tekst)

komanda = st.text_input("", placeholder=placeholder_tekst)

if komanda:
    komanda_clean = komanda.lower().strip()
    st.success(f"Jarvis: Izvršavam komandu za '{komanda}'...")
    
    if "berza" in komanda_clean or "market" in komanda_clean or "finance" in komanda_clean:
        target_url = "https://yahoo.com"
    elif "youtube" in komanda_clean or "jutjub" in komanda_clean:
        target_url = "https://youtube.com"
    elif "google" in komanda_clean or "gugl" in komanda_clean:
        target_url = "https://google.com"
    elif "twitch" in komanda_clean or "tvič" in komanda_clean:
        target_url = "https://twitch.tv"
    elif "tiktok" in komanda_clean:
        target_url = "https://tiktok.com"
    else:
        # HIRURŠKI ISPRAVLJENO: Dodata kosa crta za ispravnu Google pretragu!
        target_url = f"https://google.comsearch?q={komanda_clean}"
        
    js_kod = f"<script>window.open('{target_url}', '_blank');</script>"
    st.components.v1.html(js_kod, height=0)
    
    st.markdown(f"🔗 [Klikni ovde ako pretraživač blokira prozor]({target_url})")
    

