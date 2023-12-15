import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
 
st.write(
    """
    # Bike Sharing Dataset Analysis
    Dashboard by Itsna Hikhmatul Maula
    itsnahm7@gmail.com
    """
)

df_hour = pd.read_csv("df_hour_clean.csv")
df_day = pd.read_csv("df_day_clean.csv")


st.subheader("Trend of Bike Sharing each day")
st.line_chart(df_day, x="dteday", y="cnt")


st.subheader("Bike rental record based on season")
rental_by_season = df_day.groupby('season', as_index =False)['cnt'].sum()
st.bar_chart(rental_by_season, x="season", y="cnt")
st.caption("Based on exploration above, the highest bike rental occured in fall season which is more than 1 million times. The lowest bike rental happened in springer with online 400+ thousand.")


st.subheader("Bike rental record based on hour")
rental_record_per_hour = df_hour.groupby('hr', as_index =False)['cnt'].sum()
st.bar_chart(rental_record_per_hour, x="hr", y='cnt')


rental_record_per_hour_per_season = df_hour.groupby(['season','hr'])['cnt'].sum()
fall = rental_record_per_hour_per_season['fall'].sort_values(ascending=False)
springer = rental_record_per_hour_per_season['springer'].sort_values(ascending=False)
winter = rental_record_per_hour_per_season['winter'].sort_values(ascending=False)
summer = rental_record_per_hour_per_season['summer'].sort_values(ascending=False)


st.title('Bike rental based on hour every season')
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.subheader("Fall")
    st.dataframe(fall)

with col2:
    st.subheader("Springer")
    st.dataframe(springer)

with col3:
    st.subheader("Winter")
    st.dataframe(winter)

with col4: 
    st.subheader("Summer")
    st.dataframe(summer)

st.caption("Based on information above, we know top 3 of hour when highest bike rental happened in all of 4 season. 17, 18 and 8 is the best hour when bike rental mostly happened. The lowest bike rental happen in 4 season occured in around 3 to 5. Why the highest and the lowest bike rental occured in those time in fall season?")

df_fall = df_hour[df_hour['season'] == 'fall']

df_17188 = df_fall[df_fall['hr'] == 17]._append([df_fall[df_fall['hr'] == 18], df_fall[df_fall['hr'] == 8]])

st.title("Bike Sharing Analysis during Fall Season")
st.subheader("Bike Sharing record based on month")
month = df_17188.groupby('mnth', as_index =False)['cnt'].sum()
st.bar_chart(month, x="mnth", y="cnt")

st.subheader("Bike Sharing record based on year")
year = df_17188.groupby('yr', as_index =False)['cnt'].sum()
st.bar_chart(year, x="yr", y="cnt")

st.subheader("Bike Sharing record based on weathersit")
weathersit = df_17188.groupby('weathersit', as_index =False)['cnt'].sum()
st.bar_chart(weathersit, x="weathersit", y="cnt")

st.subheader("Bike Sharing record based on days")
weekday = df_17188.groupby('weekday', as_index =False)['cnt'].sum()
st.bar_chart(weekday, x="weekday", y="cnt")


list_of_numeric = ['temp', 'atemp', 'hum', 'windspeed']
