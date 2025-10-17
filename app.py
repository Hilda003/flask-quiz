from flask import Flask, render_template, redirect, url_for, request, flash, jsonify, session
from config import Config
from models import db, User, Question, Attempt
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
import requests
import random

from datetime import datetime, timedelta

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

login = LoginManager(app)
login.login_view = 'login'

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        nickname = request.form['nickname']
        password = request.form['password']
        confirm = request.form['confirm']

        if password != confirm:
            flash('Password tidak sama!')
            return redirect(url_for('register'))

        if User.query.filter_by(username=username).first():
            flash('Username sudah dipakai!')
            return redirect(url_for('register'))

        if User.query.filter_by(nickname=nickname).first():
            flash('Nickname sudah dipakai!')
            return redirect(url_for('register'))

        user = User(username=username, nickname=nickname)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        flash('Registrasi berhasil, silakan login!')
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()

        if user is None or not user.check_password(password):
            flash('Login gagal, coba lagi!')
            return redirect(url_for('login'))

        login_user(user)
        return redirect(url_for('quiz'))
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/quiz', methods=['GET', 'POST'])
@login_required
def quiz():

    questions = Question.query.all()

    if 'question_index' not in session:
        session['question_index'] = 0
        session['score'] = 0

    question_index = session['question_index']

    if question_index >= len(questions):
        final_score = session['score']
        current_user.score = final_score
        db.session.commit()

        session.pop('question_index', None)
        session.pop('score', None)

        return render_template('result.html', score=final_score)

    q = questions[question_index]

    if request.method == 'POST':
        answer = request.form.get('answer')

        if answer and q.correct.lower() == answer.lower():
            session['score'] += 1

        session['question_index'] += 1
        return redirect(url_for('quiz'))

    return render_template('quiz.html', question=q)

@app.route('/leaderboard')
def leaderboard():
    users = User.query.order_by(User.score.desc()).limit(20).all()
    return render_template('leaderboard.html', users=users)

@app.route('/', methods=['GET', 'POST'])
def home():
    weather_data = None
    if request.method == 'POST':
        city = request.form['city']
        api_key = "08ecbbf6e94d25abb1c3c5a66325a414"
        url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric&lang=id"

        try:
            response = requests.get(url)
            data = response.json()

            if data["cod"] == "200":
                forecast_list = []
                today = datetime.now()

                for i in range(3):
                    day = today + timedelta(days=i)
                    date_str = day.strftime("%A, %d %B %Y")
                    day_str = day.strftime("%Y-%m-%d")

                    temps = [f["main"]["temp"] for f in data["list"] if day_str in f["dt_txt"]]

                    if temps:
                        forecast_list.append({
                            "date": date_str,
                            "day_temp": round(sum(temps[:len(temps)//2]) / len(temps[:len(temps)//2]), 1),
                            "night_temp": round(sum(temps[len(temps)//2:]) / len(temps[len(temps)//2:]), 1)
                        })


                weather_data = {
                    "city": data["city"]["name"],
                    "forecast": forecast_list
                }

        except Exception as e:
            flash("Kota tidak ditemukan atau koneksi gagal.")
            print(e)

    return render_template('home.html', weather=weather_data)

if __name__ == '__main__':
    app.run(debug=True)
