#  Emotional Map of the Internet

A quick, visual data science project that analyzes emotions in global headlines and visualizes them on a world map.

##  Features
- Emotion detection using `text2emotion`
- Interactive world map with `plotly`
- Flask app for local visualization
- Ready-to-run and easy to demo

## 🧰 Tech Stack
- Python, Flask, Pandas, Plotly, Text2Emotion

##  How It Works
1. Reads headlines from `data/sample_data.csv`
2. Runs emotion analysis on each
3. Aggregates dominant emotions by country
4. Displays interactive world map

##  Run Locally
```bash
git clone https://github.com/YOUR-USERNAME/emotional-map-of-the-internet.git
cd emotional-map-of-the-internet
pip install -r requirements.txt
python app.py
