import mysql.connector
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # React app's origin
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='data',
            port=3310
        )
        return connection
    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detail=f"Database connection error: {err}")


@app.post("/insert")
def insert_data():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        # Use parameterized queries for safety
        data_to_insert = [("shefa", "33"), ("seetha", "45")]
        cursor.executemany("INSERT INTO auth (username,password) VALUES (%s, %s)", data_to_insert)

        conn.commit()
    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detail=f"Database operation error: {err}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

    return {'message': 'Data inserted successfully'}
