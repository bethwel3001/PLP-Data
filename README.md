# 🦠 COVID-19 Global Data Tracker

This project is a data analysis and visualization tool that tracks global COVID-19 trends over time. It processes real-world data on cases, deaths, and vaccinations and presents both a Jupyter Notebook report and an interactive dashboard using Dash.

---

## 🎯 Project Objectives

- Import and clean COVID-19 data from a reliable source.
- Analyze trends in cases, deaths, and vaccinations over time.
- Compare statistics across selected countries.
- Visualize data with informative charts and an optional map.
- Communicate findings through code, visuals, and narrative.

---

## 🛠️ Tools and Libraries Used

- **Python 3**
- **Pandas** – Data manipulation and cleaning
- **Matplotlib & Seaborn** – Static visualizations
- **Plotly** – Interactive visualizations (in Dash)
- **Dash** – Web-based interactive dashboard
- **Jupyter Notebook** – Narrative + code report

---

## 🚀 How to Run/View the Project

### 1. Jupyter Notebook Report
Open the `.ipynb` file:
```bash
jupyter notebook covid_tracker_notebook.ipynb
```
This will launch a web interface where you can view the report and execute the code cells.

### 2. Python script
Run the .py file to see the analysis via plots in terminal:
```bash
python covid_tracker.py
```
### 3. Interactive Dashboard
Install requirements if needed:
```bash
pip install dash pandas plotly
```
Run the Dash app:
```bash
python covid_dash_app.py
```
Open a web browser and navigate to `http://127.0.0.1:8050`

---
## 📊 Insights & Reflections
. The USA had significantly higher case and death counts compared to Kenya and India, consistent with global population trends.

. Vaccination rollouts started at different times across countries, with notable surges in mid-2021.

. The interactive dashboard allows real-time filtering and exploration of country-specific trends.

. Cleaning real-world data required handling missing values and date formatting.

. This project demonstrates how data science and visualization can uncover important public health trends and support storytelling with data.