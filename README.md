# 🚦 Smart Traffic Intelligence System (Maitama)

An intelligent traffic analytics and route optimization system built with **Python, Streamlit, Machine Learning, GIS Mapping, and Graph Algorithms**.  

This project helps analyze road traffic patterns, predict travel speed, visualize traffic routes on maps, and find the fastest route between key locations in **Maitama, Abuja, Nigeria**.

🔗 **Live Demo:** https://olonisakin-k-pf.streamlit.app/

---

## 📌 Project Overview

Urban traffic congestion remains one of the biggest transportation challenges in modern cities. This project was developed to demonstrate how **Data Science, Artificial Intelligence, and GIS technologies** can be used to improve traffic management.

The system provides:

- 📊 Traffic dataset analysis  
- 🤖 Speed prediction using Machine Learning  
- 🗺️ Interactive GIS route visualization  
- 🔄 Route optimization using shortest path algorithms  
- 📈 Dashboard for intelligent decision making  

---

## 🚀 Features

### 📊 Data Analysis Dashboard
- Dataset preview  
- Scatter plot (Road Length vs Average Speed)  
- Correlation matrix for traffic variables  

### 🤖 Machine Learning Prediction
Uses **Random Forest Regressor** to predict:

- Average vehicle speed  
- Based on route distance and travel time  

### 🗺️ GIS Traffic Mapping
Interactive route map built with **PyDeck** showing traffic connections between locations.

### 🔄 Route Optimization
Uses **NetworkX Graph Algorithm** to calculate:

- Fastest route  
- Total travel time  
- Best navigation path  

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit**
- **Pandas**
- **NumPy**
- **Scikit-learn**
- **PyDeck**
- **NetworkX**

---

## 📂 Project Structure

```bash
Traffic-Intelligence-System-/
│── dad6.py
│── requirements.txt
│── assets/
│   ├── dashboard.png
│   ├── dashboard 1.png
│   ├── dashboard 2.png
│   ├── map.png
│   ├── map 1.png
│   ├── optimization.png
│   └── predict.png

⚙️ Installation
1️⃣ Clone the Repository
git clone https://github.com/yourusername/Traffic-Intelligence-System-.git
cd Traffic-Intelligence-System-

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Run the Application
streamlit run dad6.py
# 📸 Application Screenshots

## 🖥️ Dashboard Overview

![Dashboard](assets/dashboard.png)

---

## 📊 Full Dashboard Sections

![Dashboard 1](assets/dashboard 1.png)

![Dashboard 2](assets/dashboard 2.png)

---

## 🗺️ GIS Route Map

![Map](assets/map.png)

![Map 1](assets/map 1.png)

---

## 🎯 Speed Prediction

![Prediction](assets/predict.png)

---

## 🔄 Route Optimization

![Optimization](assets/optimization.png)

