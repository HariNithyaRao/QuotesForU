import streamlit as st
import snowflake.connector
import pandas as pd
import time,datetime
import json
from streamlit_lottie import st_lottie
from streamlit_extras.add_vertical_space import add_vertical_space
from streamlit_extras.colored_header import colored_header


#loading json animation
with open('123755-designers.json', 'r') as f:
    lottie_json = json.load(f)
col1, col2 = st.columns([1, 3])
with col1:
    st_lottie(lottie_json, speed=1, width=100, height=100, key='lottie')
with col2:
    st.markdown("<link href='https://fonts.googleapis.com/css2?family=Rammetto One&display=swap' rel='stylesheet'>",unsafe_allow_html=True)
    st.markdown("<h2><span style='text-align: center; color: violet; font-family:Rammetto One;'>Quotes</span> <span style='color: orange;font-family:Rammetto One, cursive;'>For</span> <span style='color: blue;font-family:Rammetto One, cursive;'>U</span></h2>", unsafe_allow_html=True)colored_header(
    label="",
    description="",
    color_name="violet-70",
)
d=st.date_input("Select a date",min_value=datetime.date(2023,3,30),
               max_value=datetime.date(2024,6,6))
formatted_date = d.strftime('%Y-%m-%d')

# Set up Snowflake connection details
conn = snowflake.connector.connect(
    account=st.secrets.connections.snowpark.account,
    user=st.secrets.connections.snowpark.user,
    password=st.secrets.connections.snowpark.password,
    database=st.secrets.connections.snowpark.database,
    schema=st.secrets.connections.snowpark.schema,
    warehouse=st.secrets.connections.snowpark.warehouse
)
# Create a cursor
cur = conn.cursor()
#print(d)
#print(type(d))

# Query the Snowflake database and retrieve data
query='SELECT quote,author FROM QUOTATIONS where index=%s'
rows = cur.execute(query,(formatted_date,)).fetchone()
st.write(rows[0])
add_vertical_space(1)
st.write("_",rows[1])
