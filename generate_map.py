import pandas as pd
import plotly.express as px
import text2emotion as te
import requests
from bs4 import BeautifulSoup

# --------------------------
# Step 1: Fetch live headlines
# --------------------------

def get_headlines():
    headlines = []
    try:
        # Example: scrape BBC News front page
        url = "https://www.bbc.com/news"
        res = requests.get(url)
        soup = BeautifulSoup(res.text, "html.parser")
        for h in soup.find_all("h3"):
            text = h.get_text().strip()
            if text:
                headlines.append(text)
    except:
        print("Failed to fetch live headlines, using local CSV fallback.")
    return headlines

headlines = get_headlines()
if not headlines:
    # fallback to CSV
    df = pd.read_csv("data/sample_data.csv")
    headlines = df['headline'].tolist()
    countries = df['country'].tolist()
else:
    # assign countries randomly (just for demo)
    import random
    countries = random.choices(
        ["United States","India","Brazil","Germany","Japan","United Kingdom"],
        k=len(headlines)
    )

# --------------------------
# Step 2: Build DataFrame
# --------------------------
df = pd.DataFrame({
    "headline": headlines,
    "country": countries
})

# --------------------------
# Step 3: Analyze emotions
# --------------------------
df['emotion'] = df['headline'].apply(
    lambda x: max(te.get_emotion(str(x)), key=te.get_emotion(str(x)).get)
)

# Aggregate dominant emotion by country
emotion_by_country = df.groupby('country')['emotion'].agg(
    lambda x: x.value_counts().index[0]
).reset_index()

# --------------------------
# Step 4: Generate map
# --------------------------
fig = px.choropleth(
    emotion_by_country,
    locations="country",
    locationmode="country names",
    color="emotion",
    title="🌍 Emotional Map of the Internet (Live Headlines)",
    color_discrete_sequence=px.colors.qualitative.Bold
)
fig.update_layout(template="plotly_dark", height=600)

# --------------------------
# Step 5: Save as standalone HTML
# --------------------------
fig.write_html("map.html")
print("✅ map.html generated! Open it in your browser to see the live map.")
