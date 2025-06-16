
## 🌤️ **Weather Forecast Web Application**

### 🔷 Project Overview

The **Weather Forecast App** is a web-based application built using **Python (Flask)** along with **HTML** and **CSS** for the frontend. It helps users check the **current weather conditions** of any city they search, and also displays weather information for four predefined cities: **Hyderabad, Mumbai, Kolkata, and Bengaluru**.

The application fetches real-time weather data using the **WeatherAPI** service.

---

### 🧠 What the Project Does

* 🔍 Lets users **search** for any city to see its weather.
* 🌡️ Displays:

  * Current temperature
  * Min & Max temperatures
  * Average temperature
  * Humidity & Dew point
  * Chance of rain
  * Wind speed, direction, and degree
* 🏙️ Always shows live weather data for 4 major Indian cities.

---

### 📦 How It Works

1. **User Interface (HTML/CSS):**

   * A clean frontend with a search bar and weather cards for data display.
   * Icons and layout styled for responsiveness and clarity.

2. **Backend (Python Flask):**

   * Receives user input (city name) from the HTML form.
   * Sends request to WeatherAPI and fetches weather JSON data.
   * Parses weather details from the response.
   * Passes the data to the frontend using Jinja2 templating.

3. **API Integration:**

   * Uses `http://api.weatherapi.com` to get real-time weather data.
   * Requires an API key to fetch the weather info.

---

### ⚙️ How to Use This Project

#### 🔧 Prerequisites

* Python installed on your system.
* Internet connection (for fetching weather data).
* A text editor like VS Code.

#### 🛠️ Steps to Run Locally

1. **Install dependencies**:

   ```bash
   pip install flask requests
   ```

2. **Start the Flask server**:

   ```bash
   python app.py
   ```

3. **Open browser and visit**:

   ```
   http://127.0.0.1:5000
   ```

4. **Search any city** using the search bar and view its current weather conditions!

---

### 📁 Folder Structure

```
weather-forecast-app/
│
├── app.py                 # Main Flask application
│
├── static/
│   └── style.css          # CSS for styling the UI
│
├── templates/
│   └── index.html         # HTML with Jinja2 templating
│
└── README.md              # Project documentation (this file)
```

---

### 📌 Project Purpose

* To apply Flask knowledge in a real-world project.
* To understand how **APIs** are used to fetch data dynamically.
* To design a **responsive frontend** and connect it to a Python backend.
* To explore basic **data parsing** and web integration.

---
🙋‍♂️ Made By
Syed Vaseem Basha

Proudly built as part of learning web development with Flask.

