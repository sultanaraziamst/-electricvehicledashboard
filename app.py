import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Streamlit app
st.title('Gloval Electric Vehicle data Visualization')
st.write("This dashboard provides a comprehensive overview of the electric vehicle (EV) industry, exploring its historical evolution, technological advancements, and current market trends. From early innovations to modern-day advancements, the dashboard offers insights into the driving forces behind the EV revolution.")

# Streamlit app
df = pd.read_csv("IEA Global EV Data 2024 new.csv")
chart_data = pd.DataFrame(np.random.randn(30, 3), columns=["Region", "Category", "year"])
st.bar_chart(chart_data)

# lline graph
fig2 = px.line(df, x='powertrain', y='unit', color='year',
                  hover_name='region', title='Type of vheicles by year and unit')
st.plotly_chart(fig2)

#bargraph
fig3 = px.bar(df, x='year', y='mode', color='year',
                  hover_name='region', title='GDP per capita vs Happiness Score for Top Countries')
st.plotly_chart(fig3)


# can be `box`, `violin`

fig6 = px.histogram(df, x='unit', y='region', color='region',
                        hover_data='region', title = 'vfjf')
st.plotly_chart(fig6)

         