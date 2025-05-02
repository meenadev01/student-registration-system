from http.client import HTTPException
from fastapi.params import Depends
from fastapi import FastAPI, HTTPException,status
from fastapi import FastAPI
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware
import mysql.connector



from loggin import security

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins =["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

security = HTTPBasic()
VALID_USERNAME = "Divya"
VALID_PASSWORD = "3216"

def basic_auth(credentials: HTTPBasicCredentials = Depends(security)):
    if credentials.username !=VALID_USERNAME or credentials.password !=VALID_PASSWORD:
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
            detail ="Invalid username and password",
            headers={"www-Authentic" :"Basic"},
        )
    return  credentials.username
class Login(BaseModel):
    username:str
    password: str

@app.post("/loginpage")
def read_root(obj:Login):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="loginpage",
        port=3310
    )
    myquery = mydb.cursor()
    myquery.execute("SELECT * FROM  login where username = %s AND password = %s", (obj.username, obj.password))

    rand = myquery.fetchall()
    mydb.commit()
    return rand
