from app import app
from models import db, User, Question

with app.app_context():
    db.create_all()
    if not User.query.filter_by(username='test').first():
        u = User(username='test', nickname='Tester')
        u.set_password('test123')
        db.session.add(u)
    if Question.query.count() == 0:
        questions = [
            Question(
                text='Apa singkatan dari NLP?',
                choice_a='Natural Language Processing',
                choice_b='Neural Learning Program',
                choice_c='Network Logic Processor',
                choice_d='Natural Learning Prediction',
                correct='a'
            ),
            Question(
                text='Visi Komputer digunakan untuk apa?',
                choice_a='Mengenali gambar dan video',
                choice_b='Memahami teks',
                choice_c='Mendengar suara',
                choice_d='Menjalankan robot',
                correct='a'
            ),
            Question(
                text='Library Python populer untuk Machine Learning adalah?',
                choice_a='NumPy',
                choice_b='TensorFlow',
                choice_c='Matplotlib',
                choice_d='Pandas',
                correct='b'
            ),
            Question(
                text='Model NLP biasanya digunakan untuk?',
                choice_a='Prediksi harga saham',
                choice_b='Analisis sentimen teks',
                choice_c='Pengenalan wajah',
                choice_d='Kontrol robotik',
                correct='b'
            ),
            Question(
                text='Framework web yang digunakan dalam proyek ini adalah?',
                choice_a='Django',
                choice_b='FastAPI',
                choice_c='Flask',
                choice_d='Streamlit',
                correct='c'
            )
        ]
        db.session.add_all(questions)


    db.session.commit()
    print('Database berhasil dibuat dan diisi!')
