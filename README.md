# Emotional Map of the Internet

[![Python](https://img.shields.io/badge/Python-3.11-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

This project visualizes emotions from headlines around the world on an interactive map. It analyzes text data, determines dominant emotions per country, and displays them on a global map.

---

## Table of Contents

- [Features](#features)  
- [How It Works](#how-it-works)  
- [Getting Started](#getting-started)  
- [Live Demo](#live-demo)  
- [Project Structure](#project-structure)  
- [Notes](#notes)

---

## Features

- Detect emotions in text using `text2emotion`  
- Aggregate dominant emotions by country  
- Interactive world map with `plotly`  
- Optional Flask app for local visualization  
- Easy to run and extend with your own data

---

## How It Works

1. Reads headlines from `data/sample_emotions.csv`  
2. Analyzes emotions for each headline  
3. Aggregates dominant emotions by country  
4. Displays results on an interactive map you can explore in your browser  

---

## Getting Started

Clone the repository and install dependencies:

```bash
git clone https://github.com/aisebastianfletcher/emotional-map-of-the-internet.git
cd emotional-map-of-the-internet
pip install -r requirements.txt


## Generate the map

"python generate_map.py"

## Open the map in your browser

"start index.html"

## Live Demo

View the live interactive map here:
https://aisebastianfletcher.github.io/emotional-map-of-the-internet/

## PROJECT STRUCTURE 

emotional-map-of-the-internet/
├── data/                # Your CSV files
├── generate_map.py      # Script to generate the map
├── index.html           # Interactive map for GitHub Pages
├── README.md            # Project description
├── preview.png          # Screenshot of the map
├── requirements.txt     # Python dependencies
└── .gitignore           # Files to ignore


## BONUS: Extending the Project.....

You can add more sources for headlines, such as Reddit, Twitter, or news APIs. Here’s an example of how to fetch Reddit posts using the praw library:

import praw
import pandas as pd

# Initialize Reddit API
reddit = praw.Reddit(
    client_id='YOUR_CLIENT_ID',
    client_secret='YOUR_CLIENT_SECRET',
    user_agent='emotional-map-bot'
)

# Select subreddit and fetch posts
subreddit = reddit.subreddit('worldnews')
posts = subreddit.hot(limit=100)

# Collect post titles
headlines = [post.title for post in posts]

# Save to CSV
df = pd.DataFrame(headlines, columns=['headline'])
df.to_csv('data/reddit_headlines.csv', index=False)

