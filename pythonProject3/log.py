from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import mysql.connector

app = FastAPI()

# CORS middleware for frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic model
class User(BaseModel):
    username: str
    password: str

# DB connection
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",           # set your MySQL password
        database="loginew",     # make sure this DB exists
        port=3310
    )

# Login endpoint
@app.post("/common")
def login(user: User):
    try:
        con = get_db_connection()
        cursor = con.cursor()

        cursor.execute(
            "SELECT * FROM loginnn WHERE username = %s AND password = %s",
            (user.username, user.password)
        )
        result = cursor.fetchone()

        cursor.close()
        con.close()

        if result:
            return {"status": "Success", "message": "Login successful"}
        else:
            raise HTTPException(status_code=401, detail="Invalid username or password")

    except mysql.connector.Error as e:
        print("MySQL error:", e)
        raise HTTPException(status_code=500, detail="Database error")

    except Exception as e:
        print("Unhandled error:", e)
        raise HTTPException(status_code=500, detail="Internal server error")
