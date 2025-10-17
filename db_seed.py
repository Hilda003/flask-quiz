from app import app, db
from models import Question

with app.app_context():
    db.drop_all()
    db.create_all()

    questions = [
        Question(
            text="Apa kepanjangan dari AI?",
            choice_a="Artificial Intelligence",
            choice_b="Automatic Integration",
            choice_c="Applied Informatics",
            choice_d="Analytic Interface",
            correct="a"
        ),
        Question(
            text="Model deep learning yang populer untuk NLP?",
            choice_a="CNN",
            choice_b="RNN",
            choice_c="GAN",
            choice_d="SVM",
            correct="b"
        ),
        Question(
            text="Bahasa pemrograman utama untuk TensorFlow?",
            choice_a="Python",
            choice_b="C++",
            choice_c="Java",
            choice_d="Rust",
            correct="a"
        ),
        Question(
            text="Komponen utama jaringan saraf tiruan?",
            choice_a="Neuron",
            choice_b="Bit",
            choice_c="Core",
            choice_d="Thread",
            correct="a"
        ),
        Question(
            text="Library Python populer untuk computer vision?",
            choice_a="Pandas",
            choice_b="OpenCV",
            choice_c="NumPy",
            choice_d="Matplotlib",
            correct="b"
        )
    ]

    db.session.bulk_save_objects(questions)
    db.session.commit()
    print("5 questions berhasil di-seed ke database!")
