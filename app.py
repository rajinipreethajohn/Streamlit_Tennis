import streamlit as st 
import pandas as pd
import plotly.express as px

# Streamlit app header
st.title('Tennis 🎾 Grand Slam Winners 🏆 1950-2023')

# URL of the CSV file
url = 'https://raw.githubusercontent.com/rajinipreethajohn/Streamlit_Tennis/main/tennis.csv'

# Read the CSV file
df = pd.read_csv(url)

st.write("")
s = df.style.format({"Expense": lambda x : '{:.4f}'.format(x)})
st.dataframe(s)

st.title('Tournament and Winner Info')
fig = px.scatter(df, x='YEAR', y = 'WINNER_NATIONALITY', color="TOURNAMENT", hover_name="WINNER")
fig.update_layout(width=800)
st.write(fig)

# Define the Grand Slam tournaments
grand_slams = ['Wimbledon', 'U.S. Open', 'French Open', 'Australian Open']

# Filter data for the Grand Slam tournaments
df_grand_slams = df[df['TOURNAMENT'].isin(grand_slams)]

# Create a custom text column with rotated labels
df_grand_slams['YEAR'] = df_grand_slams['YEAR'].astype(int)  # Convert YEAR to integers
df_grand_slams['WINNER_TEXT'] = df_grand_slams['WINNER'] + '<br>' + df_grand_slams['YEAR'].astype(str)

# Streamlit app header
st.title('Slide by Years for Details')

# Year selection using a slider with step size 1
selected_year = int(st.slider('Select a Year', min_value=1950, max_value=2023, value=2023, step=1))

# Create an interactive line plot based on the selected year
filtered_df = df_grand_slams[df_grand_slams['YEAR'] <= selected_year]

fig = px.line(filtered_df, x='YEAR', y='WINNER', color='TOURNAMENT',
            title=f'Grand Slam Winners by Year Upto({selected_year})', labels={'WINNER': 'Winner'})

# Customize the plot layout
fig.update_traces(mode='lines+markers', marker=dict(size=7), textposition='top center', textfont=dict(size=10))
fig.update_xaxes(title='Year', tickangle=45)
fig.update_yaxes(title='Winner')

# Set custom text column as hover text
fig.update_traces(text=filtered_df['WINNER_TEXT'])

# Show the interactive plot
st.plotly_chart(fig)
