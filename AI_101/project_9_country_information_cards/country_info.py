import streamlit as st
import requests

st.set_page_config(page_title="Country Info", layout="centered")

st.title("🌍 Country Information Cards")

# Get list of countries
@st.cache_data
def get_all_countries():
    response = requests.get("https://restcountries.com/v3.1/all")
    if response.status_code == 200:
        return sorted([country['name']['common'] for country in response.json()])
    else:
        return []

country_list = get_all_countries()
selected_country = st.selectbox("Select a country", country_list)

# Fetch and display country info
@st.cache_data
def get_country_info(name):
    url = f"https://restcountries.com/v3.1/name/{name}?fullText=true"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()[0]
    else:
        return None

if selected_country:
    data = get_country_info(selected_country)
    if data:
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image(data["flags"]["png"], width=200)
        with col2:
            st.subheader(data["name"]["common"])
            st.markdown(f"**Capital:** {data.get('capital', ['N/A'])[0]}")
            st.markdown(f"**Region:** {data['region']}")
            st.markdown(f"**Population:** {data['population']:,}")
            st.markdown(f"**Area:** {data.get('area', 0):,} km²")
            st.markdown(f"**Languages:** {', '.join(data.get('languages', {}).values())}")
    else:
        st.error("Failed to fetch country data.")
