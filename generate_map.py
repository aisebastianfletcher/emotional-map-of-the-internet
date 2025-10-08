import folium
import pandas as pd

# Load your emotional data
data = pd.read_csv('data/sample_emotions.csv')

# Create a base map centered roughly on the world
m = folium.Map(location=[20, 0], zoom_start=2)

# Add markers for each country or coordinate
for _, row in data.iterrows():
    folium.CircleMarker(
        location=[row['latitude'], row['longitude']],
        radius=8,
        color='blue',
        fill=True,
        fill_color='blue',
        popup=f"{row['country']}: {row['emotion']} ({row['intensity']})"
    ).add_to(m)

# Save to HTML
m.save('map.html')

print("✅ Emotional map generated as map.html!")
