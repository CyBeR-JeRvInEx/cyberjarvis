import streamlit as st

# Postavke ekrana
st.set_page_config(page_title="CyBeR-JeRvInEx OS", page_icon="🎤", layout="centered")

# Hakerski dizajn sajta
st.markdown("""
    <style>
    .stApp { background-color: #060a12; color: #00ff66; }
    h1 { color: #00ff66; font-family: 'Courier New', monospace; text-shadow: 0 0 10px #00ff66; text-align: center; }
    .stTextInput>div>div>input { background-color: #0f1624 !important; color: #00ff66 !important; border: 2px solid #00ff66 !important; font-family: 'Courier New', monospace; }
    </style>
""", unsafe_allow_html=True)

st.title("[ CYBER-JARVIS MULTILINGUAL OS ]")
st.write("UNIVERSAL SYSTEM: TEXT INTERACTION")

# Biranje jezika
jezik = st.selectbox("Izaberi jezik / Select Language", ["Srpski (SR)", "English (US)"])

if jezik == "Srpski (SR)":
    status_tekst = "Jarvis: Sistem spreman. Ukucajte bilo koji pojam za univerzalnu pretragu."
    placeholder_tekst = "Ukucaj bilo šta ovde i pritisni Enter..."
else:
    status_tekst = "Jarvis: System ready. Type any term for universal search."
    placeholder_tekst = "Type anything here and press Enter..."

st.info(status_tekst)

# Glavno polje za kucanje
komanda = st.text_input("", placeholder=placeholder_tekst)

if komanda:
    komanda_clean = komanda.lower().strip()
    st.success(f"Jarvis: Pretražujem '{komanda}' za Vas...")
    
    # 🎯 FIXNI LINK SA STROGO DEFINISANOM KOSOM CRTOM PRE SEARCH!
    target_url = f"https://google.com{komanda_clean}"
        
    # JavaScript za automatsko otvaranje u novom prozoru
    js_kod = f"<script>window.open('{target_url}', '_blank');</script>"
    st.components.v1.html(js_kod, height=0)
    
    # Rezervni link u slučaju blokade pop-up prozora
    st.markdown(f"🔗 [Klikni ovde ako pretraživač blokira prozor]({target_url})")
