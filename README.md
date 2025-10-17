# 🧠 AI Quiz App with Weather Forecast (Flask Project)

A simple **Flask web application** that allows users to register, log in, take a quiz about AI-related topics, and check the weather forecast using the **OpenWeatherMap API**.

---

## 🚀 Features

* User registration and login system (Flask-Login)
* Randomized quiz with score tracking
* Leaderboard (Top 20 users)
* Weather forecast (3-day prediction)


---

## 🧩 Tech Stack

* **Backend:** Python 3, Flask, Flask-SQLAlchemy, Flask-Login
* **Database:** SQLite
* **Frontend:** HTML, CSS, Bootstrap
* **API:** OpenWeatherMap

---

## Preview
<img width="1680" height="1050" alt="image" src="https://github.com/user-attachments/assets/0cd0e700-4d34-42ce-a219-1ade4a0fc1ef" />
<img width="1680" height="1050" alt="image" src="https://github.com/user-attachments/assets/6051cd1e-4307-465f-b3aa-c00d36967f0c" />
<img width="1680" height="1050" alt="image" src="https://github.com/user-attachments/assets/f4340afa-9628-46d5-869b-7966d494af63" />
<img width="1680" height="1050" alt="image" src="https://github.com/user-attachments/assets/8e76963f-58be-48b1-b5e4-9d86641d6a2b" />
<img width="1680" height="1050" alt="image" src="https://github.com/user-attachments/assets/dba70b98-80f8-4acf-8638-fc95f3043f58" />






## ⚙️ Installation (Run Locally)

### 1️⃣ Clone the project

```bash
git clone https://github.com/yourusername/flask-quiz.git
cd flask-quiz
```

### 2️⃣ Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate      # Mac/Linux
venv\Scripts\activate         # Windows
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

If you don’t have a `requirements.txt`, create one:

```bash
pip freeze > requirements.txt
```

### 4️⃣ Initialize the database

```bash
python db_init.py
```

This will create the SQLite database (`app.db`) and populate initial quiz questions.

### 5️⃣ Run the Flask app

```bash
python app.py
```

Then open your browser and visit:
👉 [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🌦️ Weather API Configuration

The app uses the [OpenWeatherMap API](https://openweathermap.org/api).
You need to insert your API key in `app.py`:

```python
api_key = "YOUR_API_KEY"
```

You can get one for free by signing up at [https://openweathermap.org/appid](https://openweathermap.org/appid).

---

## 📂 Project Structure

```
flask-quiz/
│
├── app.py                # Main Flask application
├── models.py             # Database models
├── config.py             # Configuration (DB URI, secret key, etc)
├── db_init.py            # Script to initialize the DB
├── requirements.txt
│
├── templates/            # HTML templates
│   ├── base.html
│   ├── home.html
│   ├── login.html
│   ├── register.html
│   ├── quiz.html
│   └── leaderboard.html
│
└── static/
    ├── css/
    │   └── style.css

```

---

## ☁️ Deployment

The app can be deployed easily on:

* [PythonAnywhere](https://www.pythonanywhere.com/)
* [Render](https://render.com/)
* [Railway](https://railway.app/)

---

## 👨‍💻 Author

**Hildatul** — Developer passionate about building interactive web apps.


