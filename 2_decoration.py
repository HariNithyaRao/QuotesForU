import streamlit as st
import json
from streamlit_lottie import st_lottie
from streamlit_card import card
from streamlit_extras.colored_header import colored_header


#loading json animation
with open('D:/Ammulu/QuotesForU/123755-designers.json', 'r') as f:
    lottie_json = json.load(f)
col1, col2 = st.columns([1, 3])
with col1:
    st_lottie(lottie_json, speed=1, width=100, height=100, key='lottie')
with col2:
    st.markdown("<link href='https://fonts.googleapis.com/css2?family=Great+Vibes&display=swap' rel='stylesheet'>",unsafe_allow_html=True)
    st.markdown("<h2><span style='text-align: center; color: violet; font-family:Great Vibes, cursive;'>Quotes</span> <span style='color: orange;font-family:Great Vibes, cursive;'>For</span> <span style='color: blue;font-family:Great Vibes, cursive;'>U</span></h2>", unsafe_allow_html=True)
colored_header(
    label="",
    description="",
    color_name="violet-70",
)



