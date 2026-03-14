import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

st.set_page_config(page_title='Vancouver Neighbourhood Safety', layout='wide')

df = pd.read_csv('data/processed_vancouver_crime_data_2025.csv')
total_incidents = len(df)
neighbourhoods = list(df['NEIGHBOURHOOD'].unique())
crime_types = list(df['TYPE'].unique())
timeline= list(df['TIME_OF_DAY'].unique())

#st.title('🍁 Vancouver Neighbourhood Safety')
st.markdown(
    "<h1 style='text-align:center; font-size:45px; margin-top:0px;'>🍁 Vancouver Neighbourhood Safety</h1>", unsafe_allow_html=True
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
    

filtered_df = df.copy()
if selected_neighbourhood != "All":
    filtered_df = filtered_df[filtered_df['NEIGHBOURHOOD'] == selected_neighbourhood]
if selected_crime_type != "All":
    filtered_df = filtered_df[filtered_df['TYPE'] == selected_crime_type]
if selected_time != "All":
    filtered_df = filtered_df[filtered_df['TIME_OF_DAY'] == selected_time]


with right_col:
    first_plot = st.container()
    second_plot = st.container()
    
    with first_plot:
        st.subheader("Proportion of Crime Types")
        crime_counts = (filtered_df['TYPE']
                        .value_counts(normalize=True)
                        .reset_index()
                        )
        crime_counts.columns = ['TYPE', 'Percentage']
        crime_counts['Percentage'] = (crime_counts['Percentage'] * 100).round(2)
        crime_counts = crime_counts.sort_values('Percentage', ascending=False)
        #print(sorted)
        
        st.bar_chart(crime_counts, x='TYPE', y='Percentage')
        # fig = px.bar(
        #     crime_counts,
        #     x='TYPE',
        #     y='Percentage',
        #     color='TYPE',
        #     orientation='v',
        # )
        
        # fig.update_layout(
        #     showlegend=False,
        #     xaxis_title=None
        # )
        
        # st.plotly_chart(fig, use_container_width=True)
        # fig, ax = plt.subplots(figsize=(8, 4))
        # ax.bar(crime_counts['TYPE'], crime_counts['Frequency'])
        # ax.set_xlabel("Crime Type")
        # ax.set_ylabel("Frequency")
        # plt.xticks(rotation=45, ha='right')
        # plt.tight_layout()
        # st.pyplot(fig)
        
        
    with second_plot:
        st.subheader("Incidents by Time of Day")
        
        time_counts = filtered_df['TIME_OF_DAY'].value_counts(normalize=True).reset_index()
        time_counts.columns = ['TIME_OF_DAY', 'Proportion']
        
        fig = px.bar(
            time_counts,
            x='Proportion',
            y=[''] * len(time_counts),   
            color='TIME_OF_DAY',
            orientation='h',
            barmode='stack'
        )
        
        fig.update_layout(
            height=150,
            showlegend=True,
            yaxis=dict(showticklabels=False),  
            legend=dict(title=None, orientation='h', yanchor='bottom', y=3, xanchor='center', x=0.5)
        )
        
        st.plotly_chart(fig, use_container_width=True)