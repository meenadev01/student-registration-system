from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
import mysql.connector
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],

    allow_headers=["*"],
)
# --- Pydantic model for incoming data ---
class StudentRegisterRequest(BaseModel):
    name: str
    age: int
    email: EmailStr
    marks: int
    percentage: float
    department: str
    grade: str

# --- Function to connect to MySQL ---
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",           # <-- change if needed
        password="",           # <-- change if needed
        database="students",   # <-- your database name
        port=3306              # <-- port as an integer, NOT string
    )

# --- Route for student registration ---
@app.post("/students/register")
def register_student(student: StudentRegisterRequest):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        # Check if email already exists
        check_query = "SELECT * FROM register WHERE email = %s"
        cursor.execute(check_query, (student.email,))
        existing_student = cursor.fetchone()

        if existing_student:
            raise HTTPException(status_code=400, detail="Student with this email already exists.")

        # Insert new student
        insert_query = """
        INSERT INTO register (name, age, email, marks, percentage, department, grade)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(insert_query, (
            student.name,
            student.age,
            student.email,
            student.marks,
            student.percentage,
            student.department,
            student.grade
        ))
        conn.commit()

        return {"message": "Student registered successfully!"}

    except mysql.connector.Error as e:
        print("Database error:", e)
        raise HTTPException(status_code=500, detail="Database error")

    except Exception as e:
        print("Unexpected error:", e)
        raise HTTPException(status_code=500, detail="Server error")

    finally:
        try:
            cursor.close()
            conn.close()
        except:
            pass
