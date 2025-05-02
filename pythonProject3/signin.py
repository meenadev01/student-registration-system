from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
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

# --- Pydantic model for request ---
class SignInRequest(BaseModel):
    username: str
    password: str


# --- Function to connect to MySQL database ---
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",  # <-- change this
        password="",  # <-- change this
        database="students",
        port="3306"
    )


# --- Route for sign-in ---
@app.post("/sign")
def sign_in(request: SignInRequest):
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        # Check username and password
        query = "SELECT * FROM signin WHERE username = %s AND password = %s"
        cursor.execute(query, (request.username, request.password))

        user = cursor.fetchone()

        if user:
            return {
                "message": "Sign In successful",
                "user": {
                    "username": user.get("username"),
                    "password": user.get("password", "")
                }
            }
        else:
            raise HTTPException(status_code=401, detail="Invalid username or password")

    except mysql.connector.Error as e:
        print("Database error:", e)
        raise HTTPException(status_code=500, detail="Database connection error")

    except Exception as e:
        print("Unexpected error:", e)
        raise HTTPException(status_code=500, detail="Server error")

    finally:
        try:
            cursor.close()
            conn.close()
        except:
            pass
