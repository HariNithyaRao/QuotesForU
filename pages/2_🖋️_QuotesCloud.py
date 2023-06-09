import streamlit as st
import time,datetime
import json
import sqlite3
from streamlit_lottie import st_lottie
from streamlit_extras.add_vertical_space import add_vertical_space
from streamlit_extras.colored_header import colored_header

st.set_page_config(page_title="Quotes", page_icon=":lower_left_fountain_pen:", layout="wide")

con = sqlite3.connect("pages/Quotes.db")
cur=con.cursor()

#loading json animation
with open('123755-designers.json', 'r') as f:
    lottie_json = json.load(f)
col1, col2 = st.columns([1, 3])
with col1:
    st_lottie(lottie_json, speed=1, width=124, height=120, key='lottie')
with col2:
    st.markdown("<link href='https://fonts.googleapis.com/css2?family=Rammetto One&display=swap' rel='stylesheet'>",unsafe_allow_html=True)
    st.markdown("<h2><span style='text-align: center; color: violet;font-size: 70px; font-family:Rammetto One;'>Quotes</span> <span style='color: orange;font-size: 70px;font-family:Rammetto One, cursive;'>For</span> <span style='color: blue;font-size: 70px;font-family:Rammetto One, cursive;'>U</span></h2>", unsafe_allow_html=True)
colored_header(
    label="",
    description="",
    color_name="violet-70",
)
d=st.date_input("Select a date",min_value=datetime.date(2023,3,30),
               max_value=datetime.date.today())
formatted_date = d.strftime('%Y-%m-%d')



# Query the Snowflake database and retrieve data
rows = cur.execute("select quote,author from q where id = (?)",(formatted_date,)).fetchone()

txt1 = '<span style="color:midnightblue;font-size: 45px;font-family:Belgrano">{}</span>'.format(rows[0])
txt2='<span style="color: midnightblue;font-size: 40px;font-family:Belgrano;">{}</span>'.format(rows[1])

st.markdown(txt1, unsafe_allow_html=True)
add_vertical_space(1)
st.markdown(txt2,unsafe_allow_html=True)
