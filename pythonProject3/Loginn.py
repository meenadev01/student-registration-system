from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime, timedelta


app = FastAPI()
import pymysql
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Database Connection
def get_db_connection():
    return pymysql.connect(
        host=os.getenv("MYSQL_HOST"),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        database=os.getenv("MYSQL_DATABASE"),
        cursorclass=pymysql.cursors.DictCursor
    )


# Pydantic Model for Account
class Account(BaseModel):
    name: str
    phone: str
    join_date: str
    expiry_date: str


# ✅ Route: Get all registered accounts
@app.get("/accounts/")
def get_all_accounts():
    conn = get_db_connection()
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM accounts")
        accounts = cursor.fetchall()
    conn.close()
    return accounts


# ✅ Route: Get accounts expiring within 3 days
@app.get("/accounts/expiring-soon")
def get_expiring_accounts():
    today = datetime.today().date()
    three_days_later = today + timedelta(days=3)

    conn = get_db_connection()
    with conn.cursor() as cursor:
        query = "SELECT * FROM accounts WHERE expiry_date BETWEEN %s AND %s"
        cursor.execute(query, (today, three_days_later))
        expiring_accounts = cursor.fetchall()
    conn.close()

    return expiring_accounts


# ✅ Route: Register a new account
@app.post("/accounts/register")
def register_account(account: Account):
    conn = get_db_connection()
    with conn.cursor() as cursor:
        query = "INSERT INTO accounts (name, phone, join_date, expiry_date) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (account.name, account.phone, account.join_date, account.expiry_date))
        conn.commit()
    conn.close()
    return {"message": "Account registered successfully"}


# ✅ Route: Delete an account
@app.delete("/accounts/{account_id}")
def delete_account(account_id: int):
    conn = get_db_connection()
    with conn.cursor() as cursor:
        query = "DELETE FROM accounts WHERE id = %s"
        cursor.execute(query, (account_id,))
        conn.commit()
    conn.close()

    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Account not found")

    return {"message": "Account deleted successfully"}
