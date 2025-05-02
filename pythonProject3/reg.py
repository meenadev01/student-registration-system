import mysql.connector
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
from typing import List

app = FastAPI()

# Configure CORS to handle all origins for local testing
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for testing (Adjust for production)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Database connection function
def get_db_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="loginew",
        port=3310,
        use_pure=True
    )

    return connection



# Basic Authentication setup
security = HTTPBasic()
VALID_USERNAME = "Ram"
VALID_PASSWORD = "1234"


def basic_auth(credentials: HTTPBasicCredentials = Depends(security)):
    if credentials.username != VALID_USERNAME or credentials.password != VALID_PASSWORD:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=" username or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username


# Pydantic models for input validation
class Item(BaseModel):
    username: str
    password: str


# User login verification from the 'userinform' table
@app.post("/reg")
def reg(obj: Item):
    conn = get_db_connection()
    cursor = conn.cursor()


    cursor.execute("SELECT * FROM loginnn WHERE username = %s AND password = %s", (obj.username, obj.password))
    user = cursor.fetchone()

    conn.close()

    if user:
        return {"status": "Success", "message": "Login successful"}

    else:
        raise HTTPException(status_code=400, detail=" username or password")


# Basic authentication secured route
@app.post("/num")
def get_secure_data(username: str = Depends(basic_auth)):
    return {"message": "Access granted", "username": username}





#
# Insert user into 'userinform' table
@app.post("/insert")
def insert_data(user: Item):
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        query = "INSERT INTO userinform (username, password) VALUES (%s, %s)"
        values = (user.username, user.password)
        cursor.execute(query, values)
        conn.commit()
        return {"message": "Data inserted successfully", "data": user}
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=f"Failed to insert data: {str(e)}")
    finally:
        cursor.close()
        conn.close()


# Forgot password functionality
class ForgotPasswordRequest(BaseModel):
    username: str
    new_password: str


@app.post("/forgot_password")
def forgot_password(request: ForgotPasswordRequest):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT username FROM userinform WHERE username = %s", (request.username,))
    user = cursor.fetchone()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    cursor.execute("UPDATE userinform SET password = %s WHERE username = %s", (request.new_password, request.username))
    conn.commit()
    conn.close()

    return {"status": "Success", "message": "Password updated successfully"}
#
#
# # Fetch all users from 'userinform' table
@app.get("/usersinform")
def get_users():
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM userinform")
        users = cursor.fetchall()
        return [{"username": user[0], "password": user[1]} for user in users]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching users: {str(e)}")
    finally:
        cursor.close()
        conn.close()


class Student(BaseModel):
    Name: str
    email: str
    phone: str
    dob: str
    gender: str
    Department: str
    Semester: int
    CGPA: float
#
#
# # Register a student
@app.post("/stform")
def register_student(student: Student):
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        # Check if email or phone already exists
        cursor.execute("SELECT * FROM students WHERE email = %s OR phone = %s", (student.email, student.phone))
        existing_student = cursor.fetchone()

        if existing_student:
            raise HTTPException(status_code=400, detail="Email or phone already registered")

        # Insert new student
        query = """
        INSERT INTO students (Name, email, phone, dob, gender, Department, Semester, CGPA)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (
        student.Name, student.email, student.phone, student.dob, student.gender, student.Department, student.Semester,
        student.CGPA)
        cursor.execute(query, values)
        conn.commit()
        return {"message": "Student registered successfully"}

    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=f"Failed to register student: {str(e)}")

    finally:
        cursor.close()
        conn.close()
#
#
# # Search students
class SearchQuery(BaseModel):
    Search: str


@app.post("/search")
def search_students(query: SearchQuery):
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        search_term = f"%{query.Search}%"
        sql_query = """
        SELECT * FROM students
        WHERE Name LIKE %s OR email LIKE %s OR phone LIKE %s OR Department LIKE %s OR Semester  LIKE %s OR CGPA  LIKE %s
        """
        cursor.execute(sql_query, (search_term, search_term, search_term, search_term, search_term, search_term))
        results = cursor.fetchall()
        print(results)
        return [{"sid": stu[0], "Name": stu[0], "email": stu[1], "phone": stu[2], "dob": stu[3], "gender": stu[4],
                 "Department": stu[5], "Semester": stu[6], "CGPA": stu[7]} for stu in results]

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        cursor.close()
        conn.close()


# # Filter students by department
class DepartmentItem(BaseModel):
    Department: str


@app.post("/dep")
def filter_students_by_department(obj: DepartmentItem):
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        query = "SELECT * FROM students WHERE Department= %s"
        cursor.execute(query, (obj.Department,))
        results = cursor.fetchall()

        return [{"sid": stu[0], "Name": stu[1], "email": stu[2], "phone": stu[3], "dob": stu[4], "gender": stu[5],
                 "Department": stu[6], "Semester": stu[7], "CGPA": stu[8]} for stu in results]\
            if results \
            else {"status": "Failure", "message": "No students found in this department"}

    finally:
        cursor.close()
        conn.close()

#
# # Filter students by semester
class SemesterItem(BaseModel):
    Semester: int


@app.post("/sem")
def filter_students_by_semester(obj: SemesterItem):
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        query = "SELECT * FROM students WHERE Semester = %s"
        cursor.execute(query, (obj.Semester,))
        results = cursor.fetchall()

        return [{"sid": stu[0], "Name": stu[0], "email": stu[1], "phone": stu[2], "dob": stu[3], "gender": stu[4],
                 "Department": stu[5], "Semester": stu[6], "CGPA": stu[7]} for stu in results]\
            if results else {"status": "Failure", "message": "No students found in this semester"}

    finally:
        cursor.close()
        conn.close()
#
#
# Filter students by CGPA
class CGPAItem(BaseModel):
    CGPA:float


@app.post("/cgpa")
def filter_students_by_cgpa(obj: CGPAItem):
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        query = "SELECT * FROM students WHERE CGPA BETWEEN %s AND %s"
        cursor.execute(query, (obj.CGPA - 0.01, obj.CGPA + 0.01))

        results = cursor.fetchall()
        print(f"Executed Query: {query} with CGPA=({obj.CGPA - 0.01}, {obj.CGPA + 0.01})")
        print(f"Query Results: {results}")

        if not results:
            return {"status": "Failure", "message": "No students found with this CGPA"}


        return [{"sid": stu[0], "Name": stu[0], "email": stu[1], "phone": stu[2], "dob": stu[3], "gender": stu[4],
                 "Department": stu[5], "Semester": stu[6], "CGPA": stu[7]} for stu in results] \
            if results else {"status": "Failure", "message": "No students found with this CGPA"}

    finally:
        cursor.close()
        conn.close()



class DeleteRequest(BaseModel):
    user_ids: List[str]

@app.delete("/delete")
def delete_users(request: DeleteRequest):
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        if not request.user_ids:
            raise HTTPException(status_code=400, detail="No user IDs provided for deletion.")

        # Convert list of IDs into a comma-separated string for SQL
        format_strings = ','.join(['%s'] * len(request.user_ids))
        query = (f"DELETE FROM student WHERE email"
                 f" IN ({format_strings})")
        cursor.execute(query, tuple(request.user_ids))
        conn.commit()

        return {"message": "Users deleted successfully", "deleted_count": cursor.rowcount}

    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        cursor.close()
        conn.close()













