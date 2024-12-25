from sqlalchemy.orm import sessionmaker
from sqlalchemy import text
from models import Student, Course, Instructor, Enrollment, Review

def add_sample_data(session):
    # Додавання студентів
    student1 = Student(first_name="John", last_name="Doe", email="john.doe@example.com")
    student2 = Student(first_name="Jane", last_name="Smith", email="jane.smith@example.com")

    # Додавання курсів
    course1 = Course(name="Python Programming", description="Learn Python from scratch", price=199.99)
    course2 = Course(name="Data Science", description="Introduction to Data Science", price=299.99)

    # Додавання інструктора
    instructor = Instructor(first_name="Alice", last_name="Brown", email="alice.brown@example.com", bio="Experienced Python instructor")

    # Додавання реєстрацій
    enrollment1 = Enrollment(student=student1, course=course1)
    enrollment2 = Enrollment(student=student2, course=course2)

    # Додавання відгуків
    review1 = Review(student=student1, course=course1, rating=5, comment="Great course!")
    review2 = Review(student=student2, course=course2, rating=4, comment="Very informative.")

    # Збереження в базу
    session.add_all([student1, student2, course1, course2, instructor, enrollment1, enrollment2, review1, review2])
    session.commit()

def display_data(session):
    # Вивід студентів
    print("\n== Студенти ==")
    print(f"| {'ID':<5} | {'Ім`я':<20} | {'Прізвище':<20} | {'Email':<30} | {'Дата реєстрації':<20} |")
    print("-" * 95)
    students = session.query(Student).all()
    for student in students:
        print(f"| {student.id:<5} | {student.first_name:<20} | {student.last_name:<20} | {student.email:<30} | {student.enrollment_date:%Y-%m-%d} |")

    # Вивід курсів
    print("\n== Курси ==")
    print(f"| {'ID':<5} | {'Назва':<30} | {'Опис':<50} | {'Вартість':<10} |")
    print("-" * 100)
    courses = session.query(Course).all()
    for course in courses:
        print(f"| {course.id:<5} | {course.name:<30} | {course.description:<50} | {course.price:<8.2f} |")

    # Вивід інструкторів
    print("\n== Інструктори ==")
    print(f"| {'ID':<5} | {'Ім`я':<20} | {'Прізвище':<20} | {'Email':<30} | {'Біографія':<40} |")
    print("-" * 115)
    instructors = session.query(Instructor).all()
    for instructor in instructors:
        print(f"| {instructor.id:<5} | {instructor.first_name:<20} | {instructor.last_name:<20} | {instructor.email:<30} | {instructor.bio:<40} |")

    # Вивід реєстрацій
    print("\n== Реєстрації ==")
    print(f"| {'ID':<5} | {'Студент ID':<15} | {'Курс ID':<10} | {'Дата реєстрації':<20} |")
    print("-" * 60)
    enrollments = session.query(Enrollment).all()
    for enrollment in enrollments:
        print(f"| {enrollment.id:<5} | {enrollment.student_id:<15} | {enrollment.course_id:<10} | {enrollment.enrollment_date:%Y-%m-%d} |")

    # Вивід відгуків
    print("\n== Відгуки ==")
    print(f"| {'ID':<5} | {'Студент ID':<15} | {'Курс ID':<10} | {'Рейтинг':<10} | {'Коментар':<30} | {'Дата відгуку':<20} |")
    print("-" * 105)
    reviews = session.query(Review).all()
    for review in reviews:
        print(f"| {review.id:<5} | {review.student_id:<15} | {review.course_id:<10} | {review.rating:<10} | {review.comment:<30} | {review.review_date:%Y-%m-%d} |")
