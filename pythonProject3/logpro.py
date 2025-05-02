
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr
import mysql.connector

app = FastAPI()

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="students",
        port="3306"
    )


class LoginRequest(BaseModel):
    email: str
    password: str


@app.post("/login")
def login(request: LoginRequest):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    try:
        query = "SELECT * FROM users WHERE email = %s AND password = %s"
        cursor.execute(query, (request.email, request.password))

        user = cursor.fetchone()

        if user:
            return {
                "message": "Login successful",
                "user": {"email": user["email"], "password": user.get("password")}
            }
        else:
            raise HTTPException(status_code=401, detail="Invalid email or password")

    finally:
        cursor.close()
        conn.close()


# class SignInRequest(BaseModel):
#     username: str
#     password: str

# @app.post("/sign")
# def sign_in(request: SignInRequest):
#     try:
#         conn = get_db_connection()
#         cursor = conn.cursor(dictionary=True)
#
#         # Check username and password
#         query = "SELECT * FROM signin WHERE username = %s AND password = %s"
#         cursor.execute(query, (request.username, request.password))
#
#         user = cursor.fetchone()
#
#         if user:
#             return {
#                 "message": "Sign In successful",
#                 "user": {
#                     "username": user.get("username"),
#                     "password": user.get("password", "")
#                 }
#             }
#         else:
#             raise HTTPException(status_code=401, detail="Invalid username or password")
#
#     except mysql.connector.Error as e:
#         print("Database error:", e)
#         raise HTTPException(status_code=500, detail="Database connection error")
#
#     except Exception as e:
#         print("Unexpected error:", e)
#         raise HTTPException(status_code=500, detail="Server error")
#
#     finally:
#         try:
#             cursor.close()
#             conn.close()
#         except:
#             pass
#
#
#
# class StudentRegisterRequest(BaseModel):
#     name: str
#     age: int
#     email:EmailStr
#     marks: int
#     percentage: float
#     department: str
#     grade: str
#
# # --- Function to connect to MySQL ---
# def get_db_connection():
#     return mysql.connector.connect(
#         host="localhost",
#         user="root",           # <-- change if needed
#         password="",           # <-- change if needed
#         database="students",   # <-- your database name
#         port=3306              # <-- port as an integer, NOT string
#     )
#
# # --- Route for student registration ---
# @app.post("/students/register")
# def register_student(student: StudentRegisterRequest):
#     try:
#         conn = get_db_connection()
#         cursor = conn.cursor()
#
#         # Check if email already exists
#         check_query = "SELECT * FROM register WHERE email = %s"
#         cursor.execute(check_query, (student.email,))
#         existing_student = cursor.fetchone()
#
#         if existing_student:
#             raise HTTPException(status_code=400, detail="Student with this email already exists.")
#
#         # Insert new student
#         insert_query = """
#         INSERT INTO register (name, age, email, marks, percentage, department, grade)
#         VALUES (%s, %s, %s, %s, %s, %s, %s)
#         """
#         cursor.execute(insert_query, (
#             student.name,
#             student.age,
#             student.email,
#             student.marks,
#             student.percentage,
#             student.department,
#             student.grade
#         ))
#         conn.commit()
#
#         return {"message": "Student registered successfully!"}
#
#     except mysql.connector.Error as e:
#         print("Database error:", e)
#         raise HTTPException(status_code=500, detail="Database error")
#
#     except Exception as e:
#         print("Unexpected error:", e)
#         raise HTTPException(status_code=500, detail="Server error")
#
#     finally:
#         try:
#             cursor.close()
#             conn.close()
#         except:
#             pass
#
#         @app.get("/students")
#         def get_students(search: str = "", filter_dept: str = "", sort_field: str = "name"):
#             try:
#                 conn = get_db_connection()
#                 cursor = conn.cursor()
#
#                 # Construct base query
#                 query = "SELECT * FROM register WHERE name LIKE %s OR email LIKE %s"
#                 params = (f"%{search}%", f"%{search}%")
#
#                 # Apply department filter if provided
#                 if filter_dept:
#                     query += " AND department = %s"
#                     params = (*params, filter_dept)
#
#                 # Apply sorting if specified
#                 query += f" ORDER BY {sort_field}"
#
#                 cursor.execute(query, params)
#                 students = cursor.fetchall()
#
#                 return {"students": students}
#
#             except mysql.connector.Error as e:
#                 print("Database error:", e)
#                 raise HTTPException(status_code=500, detail="Database error")
#
#             except Exception as e:
#                 print("Unexpected error:", e)
#                 raise HTTPException(status_code=500, detail="Server error")
#
#             finally:
#                 try:
#                     cursor.close()
#                     conn.close()
#                 except:
#                     pass