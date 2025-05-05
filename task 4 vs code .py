import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os 
print("saving to:", os .getcwd())

# Load the dataset (update path if needed)
df = pd.read_csv('Downloads/AccidentsBig.csv', low_memory=False)

# Convert date/time columns
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df['Time'] = pd.to_datetime(df['Time'], format='%H:%M', errors='coerce')
df.dropna(subset=['Date', 'Time'], inplace=True)

# Extract hour and weekday
df['Hour'] = df['Time'].dt.hour
df['Weekday'] = df['Date'].dt.day_name()

# Set style
sns.set(style='whitegrid')

# 1. Accidents by Hour
plt.figure(figsize=(10, 5))
sns.countplot(data=df, x='Hour', palette='Blues_d')
plt.title('Number of Accidents by Hour of Day')
plt.xlabel('Hour')
plt.ylabel('Accident Count')
plt.tight_layout()
plt.savefig('accidents_by_hour.png')
plt.show()

# 2. Accidents by Day of Week
plt.figure(figsize=(10, 5))
order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
sns.countplot(data=df, x='Weekday', order=order, palette='Purples_d')
plt.title('Number of Accidents by Day of the Week')
plt.xlabel('Day')
plt.ylabel('Accident Count')
plt.tight_layout()
plt.savefig('accidents_by_day.png')
plt.show()

# 3. Accidents by Weather
plt.figure(figsize=(10, 5))
sns.countplot(data=df, y='Weather_Conditions', order=df['Weather_Conditions'].value_counts().head(10).index, palette='coolwarm')
plt.title('Top Weather Conditions During Accidents')
plt.xlabel('Accident Count')
plt.ylabel('Weather Condition')
plt.tight_layout()
plt.savefig('weather_conditions.png')
plt.show()

# 4. Accidents by Road Surface
plt.figure(figsize=(10, 5))
sns.countplot(data=df, y='Road_Surface_Conditions', order=df['Road_Surface_Conditions'].value_counts().head(10).index, palette='Greens_d')
plt.title('Road Surface Conditions During Accidents')
plt.xlabel('Accident Count')
plt.ylabel('Road Surface')
plt.tight_layout()
plt.savefig('road_surface.png')
plt.show()

# 5. Accidents by Light Conditions
plt.figure(figsize=(10, 5))
sns.countplot(data=df, y='Light_Conditions', order=df['Light_Conditions'].value_counts().head(10).index, palette='magma')
plt.title('Light Conditions During Accidents')
plt.xlabel('Accident Count')
plt.ylabel('Lighting')
plt.tight_layout()
plt.savefig('light_conditions.png')
plt.show()