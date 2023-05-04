import streamlit as st
import snowflake.connector
import pandas as pd
import time,datetime
import json
from streamlit_lottie import st_lottie

#loading json animation
with open('123755-designers.json', 'r') as f:
    lottie_json = json.load(f)
col1, col2 = st.columns([1, 3])
with col1:
    st_lottie(lottie_json, speed=1, width=100, height=100, key='lottie')
with col2:
    st.title("Quotes For U")

d=st.date_input("Select date")
formatted_date = d.strftime('%Y-%m-%d')

# Set up Snowflake connection details
conn = snowflake.connector.connect(
    account="ps41249.central-india.azure",
    user="NITHYA",
    password="Nithy@snowflake123",
    database="QUOTES",
    schema="TEST",
    warehouse="COMPUTE_WH"
)
# Create a cursor
cur = conn.cursor()
#print(d)
#print(type(d))

# Query the Snowflake database and retrieve data
query='SELECT quote,author FROM QUOTATIONS where index=%s'
rows = cur.execute(query,(formatted_date,)).fetchone()
txt = rows[0]+"\n"+"\t"*(5)+rows[1]
st.text(txt)

# Convert results to a pandas dataframe
#df = pd.DataFrame(rows, columns=[col[0] for col in cur.description])

# Display data in Streamlit app
#st.title('Snowflake Streamlit App')
#st.write(df)
