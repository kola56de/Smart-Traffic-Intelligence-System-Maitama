import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk
import networkx as nx
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error

st.set_page_config(layout="wide")
st.title("🚦 Smart Traffic Intelligence System (Maitama)")

# ----------------------------
# SAMPLE MAITAMA DATASET
# ----------------------------
data = {
    "start": [
        "Banex Junction", "Banex Junction", "Banex Junction",
        "Hospital Junction", "Hospital Junction",
        "Wuse Market Junction", "Wuse Market Junction"
    ],
    "end": [
        "Hospital Junction", "University Junction", "Wuse Market Junction",
        "University Junction", "Wuse Market Junction",
        "Head of Service", "University Junction"
    ],
    "length_km": [2.5, 3.9, 1.7, 1.3, 2.5, 3.6, 1.0],
    "time_sec": [471, 364, 101, 132, 227, 185, 149],
    "avg_speed": [19, 29, 62, 35, 39, 37, 25],
    "start_lat": [9.084, 9.084, 9.084, 9.08, 9.08, 9.07, 9.07],
    "start_lon": [7.489, 7.489, 7.489, 7.5, 7.5, 7.495, 7.495],
    "end_lat": [9.08, 9.072, 9.085, 9.072, 9.085, 9.06, 9.06],
    "end_lon": [7.5, 7.51, 7.48, 7.51, 7.48, 7.47, 7.47],
}

df = pd.DataFrame(data)

# ----------------------------
# DATA PREVIEW
# ----------------------------
st.subheader("📊 Dataset Preview")
st.dataframe(df)

# ----------------------------
# DATA ANALYSIS
# ----------------------------
st.subheader("📈 Data Analysis")

st.write("### Scatter Plot (Length vs Speed)")
st.scatter_chart(df[["length_km", "avg_speed"]].set_index("length_km"))

st.write("### Correlation Heatmap")
st.write(df.corr(numeric_only=True))

# ----------------------------
# MACHINE LEARNING MODEL
# ----------------------------
X = df[["length_km", "time_sec"]]
y = df["avg_speed"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestRegressor(n_estimators=200)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)

st.subheader("🤖 Model Performance")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("📈 R² Score", f"{r2:.2f}")

with col2:
    st.metric("📉 MAE", f"{mae:.2f}")

with col3:
    st.metric("🤖 Model", "Random Forest")

# ----------------------------
# PREDICTION SECTION
# ----------------------------
st.subheader("🎯 Predict Speed")

length = st.number_input("Route Length (km)", value=2.0)
time = st.number_input("Travel Time (sec)", value=200)

if st.button("Predict Speed"):
    pred = model.predict([[length, time]])
    st.success(f"Predicted Speed: {pred[0]:.2f} km/h")

# ----------------------------
# GIS MAP
# ----------------------------
st.subheader("🗺️ Route Map")

layer = pdk.Layer(
    "LineLayer",
    data=df,
    get_source_position='[start_lon, start_lat]',
    get_target_position='[end_lon, end_lat]',
    get_width=5,
)

view_state = pdk.ViewState(
    latitude=9.08,
    longitude=7.49,
    zoom=12
)

st.pydeck_chart(pdk.Deck(layers=[layer], initial_view_state=view_state))

# ----------------------------
# ROUTE OPTIMIZATION
# ----------------------------
st.subheader("🔄 Route Optimization")

locations = sorted(list(set(df['start']).union(set(df['end']))))

start_node = st.selectbox("Start Location", locations)
end_node = st.selectbox("Destination", locations)

G = nx.Graph()

for _, row in df.iterrows():
    G.add_edge(
        row['start'],
        row['end'],
        weight=row['time_sec']
    )

if st.button("Find Best Route"):
    try:
        path = nx.shortest_path(G, source=start_node, target=end_node, weight='weight')
        cost = nx.shortest_path_length(G, source=start_node, target=end_node, weight='weight')

        st.success(f"Best Route: {' → '.join(path)}")
        st.info(f"Total Travel Time: {cost} sec")

    except:
        st.error("No route found")

# ----------------------------
# MAP FOR OPTIMIZED ROUTE
# ----------------------------
location_coords = {}

for _, row in df.iterrows():
    location_coords[row['start']] = (row['start_lat'], row['start_lon'])
    location_coords[row['end']] = (row['end_lat'], row['end_lon'])

if 'path' in locals():
    route_data = []

    for i in range(len(path) - 1):
        start = location_coords[path[i]]
        end = location_coords[path[i+1]]

        route_data.append({
            "start_lon": start[1],
            "start_lat": start[0],
            "end_lon": end[1],
            "end_lat": end[0],
        })

    route_df = pd.DataFrame(route_data)

    route_layer = pdk.Layer(
        "LineLayer",
        data=route_df,
        get_source_position='[start_lon, start_lat]',
        get_target_position='[end_lon, end_lat]',
        get_color=[255, 0, 0],
        get_width=8,
    )

    st.pydeck_chart(pdk.Deck(
        layers=[route_layer],
        initial_view_state=view_state
    ))
