import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

# --- BRANDING & APP CONFIG [cite: 28, 43] ---
st.set_page_config(page_title="On Tap by Bar Buddies", layout="wide")

# Custom CSS for the Nightlife/Dark Mode aesthetic [cite: 73]
st.markdown("""
    <style>
    .main { background-color: #0E1117; color: #FFFFFF; }
    .stButton>button { width: 100%; border-radius: 20px; background-color: #6200ee; color: white; }
    .price-card { padding: 15px; border-radius: 10px; border: 1px solid #333; margin-bottom: 10px; background-color: #1e1e1e; }
    </style>
    """, unsafe_allow_html=True)

# --- NAVIGATION [cite: 19] ---
page = st.sidebar.radio("Navigate", ["Live Map", "Top Shelf Shop", "Events", "Group Status", "Phone Mode"])

# --- PAGE 1: LIVE MAP [cite: 44] ---
if page == "Live Map":
    st.header("📍 Friend Map")
    st.write("Ensuring that if you are lost, you will eventually be regrouped[cite: 11].")
    
    # Map centered on Mass St, Lawrence, KS [cite: 73]
    m = folium.Map(location=[38.9717, -95.2353], zoom_start=16, tiles="CartoDB dark_matter")
    
    # Founder status based on Operations section [cite: 90, 91]
    friends = [
        {"name": "Walker Phillips", "loc": [38.9719, -95.2351], "status": "Managing Production"},
        {"name": "Brody Sherman", "loc": [38.9705, -95.2355], "status": "Marketing Lead"},
        {"name": "Joseph Recalde-Phillips", "loc": [38.9730, -95.2360], "status": "Sales Lead"}
    ]
    
    for f in friends:
        folium.Marker(f["loc"], popup=f"{f['name']}: {f['status']}", icon=folium.Icon(color='purple')).add_to(m)
    
    st_folium(m, width=700, height=450)
    if st.button("🚨 TRIGGER SOS [cite: 51]"):
        st.error("SOS Alert Sent! Safety regrouping initiated[cite: 6].")

# --- PAGE 2: TOP SHELF SHOP (Selling Page) [cite: 52] ---
elif page == "Top Shelf Shop":
    st.header("🛍️ Top Shelf Collection")
    st.write("Interactive trackers made of textured plastics and metals[cite: 27].")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<div class='price-card'><b>Tito's Edition</b><br>$22.99</div>", unsafe_allow_html=True) # [cite: 39]
        st.markdown("<div class='price-card'><b>Jack Edition</b><br>$22.99</div>", unsafe_allow_html=True) # [cite: 39]
    with col2:
        st.markdown("<div class='price-card'><b>Lavender & Camo</b><br>$19.99</div>", unsafe_allow_html=True) # [cite: 39]
        st.success("Student Base Price: $15.99 (Includes community bar crawls) [cite: 40]")

# --- PAGE 3: EVENTS [cite: 8, 73] ---
elif page == "Events":
    st.header("🍺 Lawrence Events")
    st.info("Exclusive community gatherings and bar crawls[cite: 40].")
    st.write("- **Mass St. Bar Crawl**: Tonight @ 10PM [cite: 73]")
    st.write("- **Big Rivalry Game Celebration**: Saturday @ After Game [cite: 7]")
    st.write("- **Greek Life Social**: Thursday @ 9PM [cite: 38]")

# --- PAGE 4: GROUP STATUS & PHONE MODE [cite: 18, 29] ---
elif page in ["Group Status", "Phone Mode"]:
    st.header("📱 Phone Mode & Safety Status")
    st.write("Protecting the student body while they are out drinking[cite: 18, 83].")
    
    st.checkbox("Enable Low Battery Friend Tracking")
    st.checkbox("Alert me if a friend leaves the Mass St. area [cite: 73]")
    
    # Operations Team Data [cite: 90, 91]
    status_data = {
        "Member": ["Walker Phillips", "Brody Sherman", "Joseph Recalde-Phillips"],
        "Role": ["Production & Supplier Coordination", "Marketing & Sales", "Partnerships"],
        "Safety Status": ["Regrouped", "Active", "Active"]
    }
    st.table(pd.DataFrame(status_data))