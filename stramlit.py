import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns
import plotly.express as px

st.title('Penguin explorer - Updated Version for Testing purpose')

st.write('**Little** *app* for exploring `penguin` [dataset](https://allisonhorst.github.io/palmerpenguins)')

st.image('https://de.wikipedia.org/wiki/Datei:Penguin_in_Antarctica_jumping_out_of_the_water.jpg')

st.header('Data')

df=pd.read_csv('penguins_extra.csv')

st.write('Display a sample of data', df.sample(20) )

# file = st.file_uploader('upload a file')
# file = pd.read_csv(file)
#st.write(file.head())

species = st.selectbox('Choose which species to display', df.species.unique())

df_species = df.loc[df.species==species]

st.write(f'Displaying a subset for {species} penguins', df_species.sample(20))

st.subheader('Plotting')
fig, ax = plt.subplots()

ax = sns.scatterplot(data=df, x = 'bill_length_mm', y='bill_depth_mm', hue='species', size='sex')

# ax = sns.scatterplot(data=df_species, x = 'bill_length_mm', y='bill_depth_mm', hue='species', size='sex')

st.pyplot(fig)

st.subheader('creating interface interactive plot')
fig = px.scatter(df, x='bill_length_mm',y = 'flipper_length_mm', color='species', animation_frame='species',hover_name='name', range_x=[30,70], range_y=[150,250])
st.plotly_chart(fig)


st.bar_chart(df.groupby('species')['island'].count())

# make a map
st.map(df)