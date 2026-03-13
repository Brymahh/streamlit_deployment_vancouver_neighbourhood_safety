import streamlit as st
import pandas as pd

df = pd.read_csv('data/processed_vancouver_crime_data_2025.csv')
st.title('🍁 Vancouver Neighbourhood Safety')

total_incidents = len(df)
neighbourhoods = list(df['NEIGHBOURHOOD'].unique())
crime_types = list(df['TYPE'].unique())
timeline= list(df['TIME_OF_DAY'].unique())