# Project 9: AI in Transportation

- **Topic:** AI in Transportation
- **Student Name:** Y. Prudhvi Naidu
- **Course:** Python Fundamentals Lab

---

## 📌 Project Overview
This beginner-friendly Python project demonstrates how artificial intelligence and computational logic optimize modern transportation systems. By representing routes with fundamental Python data structures, calculating transit times, and evaluating the fastest route, the program outputs a standalone, fully styled, and interactive web dashboard (`index.html`).

---

## 🚀 How to Run the Project

1. **Open your terminal** and switch to the project folder:
   ```bash
   cd "/Users/yegireddyprudhvinaidu/Desktop/project python"
   ```

2. **Execute the Python script**:
   ```bash
   python3 create_webpage.py
   ```

3. **View the generated webpage**:
   - On macOS:
     ```bash
     open index.html
     ```
   - On Windows / Linux: Double-click `index.html` or open it with your favorite browser.

> **Offline Guarantee:** This project requires **no external Python libraries** (`pip`) and **no active internet connection** (no CDN dependencies or web fonts). Everything is self-contained.

---

## 🧠 Python Concepts Applied

1. **List of Dictionaries**: Each route is modeled as a dictionary containing its name, distance in km, and average speed in km/h.
2. **Modular Functions**: A clean `travel_time(distance, speed)` function implements the arithmetic formula `(distance / speed) * 60` to return travel time in minutes.
3. **Loop Iteration**: A `for` loop evaluates each route, assigns computed transit times, and formats output.
4. **Optimal Search with `min()` & `key`**: Built-in `min(routes, key=lambda r: r['time'])` efficiently identifies the fastest route.
5. **Dynamic HTML Generation with f-Strings**: Interpolates computed metrics directly into HTML, table rows, and responsive CSS bar chart elements.
6. **File Handling with `open()`**: Context manager `with open("index.html", "w", encoding="utf-8")` guarantees safe file writing.

---

## 📊 Sample Route Benchmark Results

| Route Name | Distance | Average Speed | Estimated Time | Status |
| :--- | :---: | :---: | :---: | :---: |
| Central Station to Airport | 30.0 km | 50.0 km/h | 36.0 min | Standard |
| University to Airport | 18.0 km | 45.0 km/h | 24.0 min | Standard |
| Riverside to Airport | 12.0 km | 32.0 km/h | 22.5 min | Standard |
| Hillview to Airport | 20.0 km | 32.0 km/h | 37.5 min | Standard |
| **Green Park to Airport** | **10.0 km** | **40.0 km/h** | **15.0 min** | **⚡ Fastest Route** |

*The initial fastest route identified is **Green Park to Airport** at **15.0 minutes**.*

---

## 🌐 Webpage Highlights

- **Fastest Route Summary Card:** Dynamically spotlights the top recommendation with key statistics.
- **Evaluated Route Table:** Color-coded table with badges highlighting optimal travel choices.
- **Pure CSS Responsive Bar Chart:** Proportional horizontal bar chart displaying travel times without external charting libraries.
- **Interactive Route Simulator:** A client-side form allows users to enter custom route names, distances, and speeds; client-side JavaScript instantly validates input (`> 0`) and recalculates the fastest route, table rows, and chart in real time.
- **Educational AI Context:** Detailed sections explaining real-time traffic prediction, intelligent dynamic routing, collision avoidance, and autonomous vehicles (LiDAR, sensor fusion, V2X platooning).

---

## 📝 Student Reflection
Using Python dictionaries allowed me to cleanly organize structured transit properties like distances and speeds into intuitive key-value pairs. Writing a dedicated `travel_time()` function and executing a loop made applying the arithmetic formula and iterating over all routes effortless and maintainable. Finally, leveraging `min()` with a custom `key` lambda elegantly extracted the optimal route without manual sorting, while Python's file handling via `open()` seamlessly transformed pure data into a complete, styled HTML dashboard.
