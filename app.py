import streamlit as st
import pandas as pd

st.set_page_config(page_title='Vancouver Neighbourhood Safety', layout='wide')

df = pd.read_csv('data/processed_vancouver_crime_data_2025.csv')
total_incidents = len(df)
neighbourhoods = list(df['NEIGHBOURHOOD'].unique())
crime_types = list(df['TYPE'].unique())
timeline= list(df['TIME_OF_DAY'].unique())

#st.title('🍁 Vancouver Neighbourhood Safety')
st.markdown(
    "<h1 style='text-align:center; font-size:45px;'>🍁 Vancouver Neighbourhood Safety</h1>", unsafe_allow_html=True
    )

left_col, right_col = st.columns([0.9, 2.5])

with left_col:
    text = """This dashboard provides insights into 2025 crime incidents recorded by the Vancouver Police Department across Vancouver neighbourhoods. Explore the data to understand safety trends and make informed decisions about where to live, work, or visit in the city."""
    st.markdown(text)
    
    st.metric(label="Total Incidents", value=f"{total_incidents:,}")
    st.divider()
    
    st.subheader("Filters")
    selected_neighbourhood = st.selectbox("Neighbourhood", options=["All"] + neighbourhoods)
    selected_crime_type = st.selectbox("Crime Type", options=["All"] + crime_types)
    selected_time = st.selectbox("Time of Day", options=["All"] + timeline)
    