from flask import Flask
import pymysql
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")


@app.route("/")
def home():
    connection = None

    try:
        connection = pymysql.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME,
            cursorclass=pymysql.cursors.DictCursor,
            connect_timeout=5
        )

        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT id, name, email, course FROM students"
            )
            students = cursor.fetchall()

        html = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Student Management System</title>
        </head>
        <body>
            <h1>Student Management System</h1>
            <table border="1" cellpadding="10">
                <tr>
                    <th>ID</th>
                    <th>Name</th>
                    <th>Email</th>
                    <th>Course</th>
                </tr>
        """

        for student in students:
            html += f"""
                <tr>
                    <td>{student['id']}</td>
                    <td>{student['name']}</td>
                    <td>{student['email']}</td>
                    <td>{student['course']}</td>
                </tr>
            """

        html += """
            </table>
        </body>
        </html>
        """
