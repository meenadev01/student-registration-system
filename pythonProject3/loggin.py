from fastapi import FastAPI,Depends,HTTPException,status
from fastapi.security import  HTTPBasic,HTTPBasicCredentials
import mysql.connector
from pydantic import BaseModel

app = FastAPI()

def get_db_connection():

        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="lucky",
            port="3310"
        )
        return connection

mydb = get_db_connection()
mycursor = mydb.cursor()
mycursor.execute("select * from datas")
myresult =mycursor.fetchall()

security = HTTPBasic()

VALID_USERNAME = "meena"
VALID_PASSWORD ="0309"

def basic_auth(credentials: HTTPBasicCredentials = Depends(security)):
    if credentials.username !=VALID_USERNAME or credentials.password != VALID_PASSWORD:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password",
            headers={"www.Authenticate" : "Basic"},
        )
    return credentials.username

@app.post("/check")
def get_secure_data(username: str = Depends(basic_auth)):
    return {
        "message":"Access granted",
        "username":username,
    }

class Item(BaseModel):
    username: str
    password: str


@app.post("/sampledata")
def read_root2(obj:Item):
        if obj.username==VALID_USERNAME and obj.password==VALID_PASSWORD :

            return {"status":"success","message":"Login successfully"}
        return {"status":"Failure","message":"Invalid username and password"}
