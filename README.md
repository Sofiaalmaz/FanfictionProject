
# Project Harry Potter Fanfiction Data Analysis

## Description

The project is aimed at collecting and analyzing data related to fanfiction based on the Harry Potter books. The main goal of the project is to explore trends and patterns in the creation and popularity of fanfictions, as well as analyze key features such as number of pages, likes, subscribers, and reviews.

Imagine you're a beginner fanfiction writer who wants to become popular right away, but you don’t know which genre to write in, which characters to use, or how long your fanfic should be. This project will help answer those questions.

The main project is in `analysis/fanfiction_project.ipynb`. The scraping code is in `parser/`. The website code is in `web/`.

## Data

Two data sources are used for analysis:

1. Fanfictions from 2004 to 2019 — data obtained from Kaggle.
2. Fanfictions from 2020 to 2024 — data collected via web scraping from the international website fanfiction.net.

## Pipeline Description

1. **Data Collection:**
    - Data from 2004 to 2019 was downloaded from Kaggle.
    - Data from 2020 to 2024 was collected via scraping fanfiction.net.

    - [Link to the collected data](https://drive.google.com/drive/folders/1oXK6g34vket1i1YB1r8SczxPUdDObDRM?usp=sharing)

2. **Data Preparation:**
    - Processing of the 2004–2019 dataset by removing unnecessary columns and formatting.
    - Similar processing for the 2020–2024 dataset, including filling in missing values and renaming columns.
    - Merging the two datasets into one.
    - Removing duplicate fanfictions.

3. **Data Analysis:**
    - Analysis of popular pairings.
    - Grouping data by year and calculating average values for favorites, followers, and reviews.
    - Identifying popularity trends of fanfictions and their attributes over the years.

4. **Data Visualization:**
    - Visualization is done using Matplotlib, Seaborn, and WordCloud for plotting graphs and charts.
    - Example: creating a plot of fanfiction popularity over time using the `sns.lineplot` function.

5. **Visual Demo via Streamlit:**
   Some of the project’s graphs are available through Streamlit:  
   http://medpaint.ru:8501/  
   If the link doesn't work, message me on Telegram @sofiaalmaz.

## Analysis Results

- Fanfiction popularity is steadily increasing.
- The best rating to use is T, and the best genre is Romance.
- The most effective character combination is Harry Potter and Severus Snape.
- The optimal fanfic length is between 200,000 and 300,000 words.
- Using popular keywords has a slight effect on fanfic popularity.

## Project Architecture

The project has the following structure:

```
├── .gitignore
├── README.md
├── analysis/
│   ├── __init__.py
│   ├── data.py
│   ├── fanfiction_project.ipynb
│   ├── features.py
│   └── visualization.py
├── data/
│   ├── fanfiction_data.csv
│   └── hpcleanvlarge1.csv
├── parser/
│   ├── __init__.py
│   ├── main.py
│   └── processing.py
├── poetry.lock
├── pyproject.toml
└── web/
    ├── __init__.py
    └── app.py
```

### Component Descriptions

- **analysis/** – Contains scripts for data analysis.
    - `data.py` – functions for preparing and merging data.
    - `features.py` – functions for extracting additional features from the data.
    - `visualization.py` – functions for data visualization.
    - `fanfiction_project.ipynb` – main Jupyter notebook for data analysis.
- **data/** – Contains raw data.
    - `fanfiction_data.csv` – data from 2020 to 2024.
    - `hpcleanvlarge1.csv` – data from 2004 to 2019.
- **parser/** – Contains scripts for data collection.
    - `main.py` – main script to start the scraping process.
    - `processing.py` – functions for processing the scraped data.
- **web/** – Contains scripts for the web interface.
    - `app.py` – main script to run the web application.

## Technologies Used

- Python
- Selenium for web scraping
- advanced pandas usage (grouping, etc.)
- regular expressions
- numpy / scipy for mathematical tasks
- networkx library
- complex visualizations
- predictive models like regression or decision trees
- Streamlit used for displaying some project graphs
- libraries such as LinearSegmentedColormap, tqdm, itertools, collections, wordcloud, sklearn.metrics, which were not covered in the course
- Matplotlib
- Seaborn
- Jupyter Notebook for convenient data analysis
- Poetry for managing dependencies
