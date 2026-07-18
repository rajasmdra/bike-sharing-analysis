import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import numpy as np

# BIKE RENT BY SEASON
def create_rent_by_season(df):
    rent_by_season = df.groupby('season').cnt.mean().sort_values(ascending=False).reset_index()
    return rent_by_season

# BIKE RENT BY WEATHER
def create_rent_by_weather(df):
    rent_by_weather = df.groupby('weathersit').cnt.mean().sort_values(ascending=False).reset_index()
    return rent_by_weather

# BIKE RENT BY HOUR
def create_rent_by_hour(df):
    rent_by_hour = df.groupby(['workingday', 'hr']).cnt.mean().reset_index()
    return rent_by_hour

# BIKE RENT BY DAY
def create_rent_by_day(df):
    rent_by_day = df.groupby('workingday').cnt.mean().reset_index()
    return rent_by_day

# BIKE RENT BY USER
def create_rent_by_user(df):
    rent_by_user = df.groupby('workingday')[['casual', 'registered']].mean().reset_index()
    return rent_by_user

# IMPORT DATASET
all_df = pd.read_csv('dashboard_dataset.csv')

# COMPONENT FILTER
min_date = all_df['dteday'].min()
max_date = all_df['dteday'].max()

with st.sidebar:
    start_date, end_date = st.date_input(
        label='Rentang Waktu',
        min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

main_df = all_df[((all_df['dteday']) >= str(start_date)) & ((all_df['dteday']) <= str(end_date))]

rent_by_season = create_rent_by_season(main_df)
rent_by_weather = create_rent_by_weather(main_df)
rent_by_hour = create_rent_by_hour(main_df)
rent_by_day = create_rent_by_day(main_df)
rent_by_user = create_rent_by_user(main_df)

st.header('Bike Sharing Analysis')

# BIKE RENT BY SEASON & WEATHER
st.subheader('Bike Rent Average')
days = ['Weekday', 'Weekend']
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(35, 15))
axes = axes.flatten()

for i, day in enumerate(days):
    sns.barplot(x='weathersit', y='cnt', data=rent_by_weather, ax=axes[i])
    axes[i].set_ylabel(None)
    axes[i].set_xlabel(None)
    axes[i].set_title('By Weather', fontsize=50)
    axes[i].tick_params(axis='y', labelsize=35)
    axes[i].tick_params(axis='x', labelsize=25, rotation=10)

st.pyplot(fig)

# BIKE RENT BY HOUR
st.subheader('Bike Rent Average by Hour')
days = ['Weekday', 'Weekend']
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(35, 15))
axes = axes.flatten()

for i, day in enumerate(days):
    sns.lineplot(
        x='hr',
        y='cnt',
        data=rent_by_hour[rent_by_hour['workingday'] == day],
        marker='o',
        linewidth=3,
        color='#90CAF9',
        ax=axes[i]
    )
    axes[i].set_xlabel(None)
    axes[i].set_ylabel(None)
    axes[i].set_title(day, fontsize=50)
    axes[i].tick_params(axis='y', labelsize=35)
    axes[i].tick_params(axis='x', labelsize=30)
    axes[i].set_xticks(np.arange(0, 24, step=2))
    axes[i].grid()

st.pyplot(fig)

# BIKE RENT COUNT BY WEATHER PARAMS
st.subheader('Bike Rent Total by Weather Params')
weather_params = {
    'temp': 'Actual Temperature', 
    'atemp': 'Feeling Temperature', 
    'hum': 'Humidity', 
    'windspeed': 'Windspeed'
}
fig, axes = plt.subplots(2, 2, figsize=(16, 12))
axes = axes.flatten()

for i, (params, label) in enumerate(weather_params.items()):
    sns.regplot(
        x=params, 
        y='cnt', 
        data=main_df[main_df[params] != 0], 
        scatter_kws={'alpha': 0.1}, 
        line_kws={'color': 'red'},
        ax=axes[i]
    )
    axes[i].set_title(f'{label}', fontsize=20)
    axes[i].set_xlabel(None)
    axes[i].set_ylabel('Total')
    axes[i].tick_params(axis='y', labelsize=15)
    axes[i].tick_params(axis='x', labelsize=15)

st.pyplot(fig)

# BIKE RENT BY USER
st.subheader("Bike Rent Average by User")
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(35, 15))
colors = ["#90CAF9", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

sns.barplot(x='workingday', y='cnt', data=rent_by_day, ax=ax[0])
ax[0].set_ylabel(None)
ax[0].set_xlabel(None)
ax[0].set_title('Bike Rent Average Per Day (Weekday & Weekend)', fontsize=40)
ax[0].tick_params(axis='y', labelsize=35)
ax[0].tick_params(axis='x', labelsize=30)

x = range(len(rent_by_user))
width = 0.35
ax[1].bar([i - width/2 for i in x], rent_by_user['casual'], width, label='Casual')
ax[1].bar([i + width/2 for i in x], rent_by_user['registered'], width, label='Registered')
ax[1].set_title('Bike Rent Average Per Day (Casual & Registered)', fontsize=40)
ax[1].tick_params(axis='y', labelsize=35)
ax[1].tick_params(axis='x', labelsize=30)
ax[1].set_ylabel(None)
ax[1].set_xlabel(None)
ax[1].set_xticks(x)
ax[1].set_xticklabels(rent_by_user.workingday)
ax[1].legend()

st.pyplot(fig)

# Demand Segmentation
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# --- Bagian Pengolahan Data ---
q1 = main_df['cnt'].quantile(0.33)
q2 = main_df['cnt'].quantile(0.67)

main_df['demand'] = pd.cut(
    main_df['cnt'], 
    bins=[0, q1, q2, main_df['cnt'].max()],
    labels=['Low', 'Medium', 'High'],
    include_lowest=True
)

params = {'season': 'Season', 'weathersit': 'Weather'}
st.subheader("Distribution per Demand Level")
fig, axes = plt.subplots(1, 2, figsize=(16, 6))

for i, (param, label) in enumerate(params.items()):
    ax = axes[i]
    demand = pd.crosstab(main_df['demand'], main_df[param], normalize='index') * 100
    demand.plot(kind='bar', stacked=True, ax=ax)
    ax.set_title(label, fontsize=14)
    ax.set_xlabel(None)
    ax.set_ylabel('Percentage (%)')
    ax.tick_params(axis='x', rotation=0)
    ax.legend()

plt.tight_layout()
st.pyplot(fig)