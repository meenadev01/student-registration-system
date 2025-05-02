import mysql.connector
from pydantic import BaseModel
from fastapi import FastAPI,Depends,HTTPException,status
from fastapi.security import HTTPBasic,HTTPBasicCredentials
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
mycursor.execute("SELECT * FROM datas")
myresult = mycursor.fetchall()

security=HTTPBasic()
VALID_USERNAME="meena"

VALID_PASSWORD="309"

def basic_auth(credentials:HTTPBasicCredentials=Depends(security)):
    if credentials.username != VALID_USERNAME or credentials.password != VALID_PASSWORD:
        raise  HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="invalid username or password",
            headers={"WWW-authenticate":"Basic"},
        )
    return  credentials.username
@app.post("/check")
def  get_secure_data(username:str=Depends(basic_auth)):
    return {
        "message":"access granted",
        "username":username
    }
class Item(BaseModel):
    username:str
    password:int

@app.post("/sampledata")
def read_root2(obj:Item):
    for db_username,db_password in myresult:
        if obj.username==db_username and obj.password==db_password:
            return {"status":"Success","message":"Login successful"}
        return {"status":"Failure","message":"Invalid username or password"}
