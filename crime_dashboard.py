import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(page_title='Dashboard by Aryaan')

# File location
file_path =r'D:\demo-dashboard\crime_data1.xlsx'

@st.cache_data
def load_data(file_path):
    data = pd.read_excel(file_path)
    return data

data = load_data(r'D:\demo-dashboard\crime_data1.xlsx')


st.title("Crime Statistics Dashboard")

st.sidebar.header("Filters")
selected_year = st.sidebar.selectbox("Select Year", sorted(data["Year"].unique()))
selected_state = st.sidebar.selectbox("Select State/UTs", sorted(data["States/UTs"].unique()))

filtered_data = data[(data["Year"] == selected_year) & (data["States/UTs"] == selected_state)]

st.write(f"### Crime Data for {selected_state} in {selected_year}")
st.dataframe(filtered_data)

fig1 = px.bar(filtered_data, x="District", y="Murder", title="Murder Cases by District")
st.plotly_chart(fig1)

fig2 = px.bar(filtered_data, x="District", y="Rape other than Custodial", title="Rape Cases (Other than Custodial) by District")
st.plotly_chart(fig2)

fig3 = px.pie(filtered_data, values="Kidnapping & Abduction_Total", names="District", title="Kidnapping & Abduction by District")
st.plotly_chart(fig3)

fig4 = px.line(filtered_data, x="District", y="Auto Theft", title="Auto Theft Cases by District")
st.plotly_chart(fig4)

fig5 = px.bar(filtered_data, x="District", y="Assault on Women with intent to outrage her Modesty", 
              title="Assault on Women (Intent to Outrage Modesty) by District")
st.plotly_chart(fig5)

fig6 = px.bar(filtered_data, x="District", y="Riots", title="Riots by District")
st.plotly_chart(fig6)
