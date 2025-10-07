from flask import Flask, render_template
import pandas as pd
import plotly.express as px
import text2emotion as te

app = Flask(__name__)

@app.route('/')
def index():
    # Load sample data
    df = pd.read_csv("data/sample_data.csv")

    # Analyze emotions
    df['emotion'] = df['headline'].apply(
        lambda x: max(te.get_emotion(str(x)), key=te.get_emotion(str(x)).get)
    )

    # Aggregate emotions by country
    emotion_by_country = df.groupby('country')['emotion'].agg(
        lambda x: x.value_counts().index[0]
    ).reset_index()

    # Create choropleth map
    fig = px.choropleth(
        emotion_by_country,
        locations="country",
        locationmode="country names",
        color="emotion",
        title="🌍 Emotional Map of the Internet",
        color_discrete_sequence=px.colors.qualitative.Bold
    )
    fig.update_layout(template="plotly_dark", height=600)

    # Convert plot to HTML
    graph_html = fig.to_html(full_html=False)

    return render_template('index.html', plot=graph_html)

if __name__ == '__main__':
    app.run(debug=True)
