#
# import mysql.connector
# from fastapi import FastAPI, HTTPException,status
# from fastapi.params import Depends
# from fastapi.security import HTTPBasic, HTTPBasicCredentials
# from pydantic import BaseModel
# from select import select
# from starlette.middleware.cors import CORSMiddleware
#
#
#
# app = FastAPI()
#
# app.add_middleware(
#
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"]
# )
# security = HTTPBasic()
#
# VALID_USERNAME = "meena"
# VALID_PASSWORD = "328"
#
# def basic_auth(credentials: HTTPBasicCredentials =Depends(security)):
#     if credentials.username  != VALID_USERNAME or credentials.password  != VALID_PASSWORD:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Invalid username or password",
#             headers={"www-Authentic" : "Basic"},
#         )
#     return credentials.username
# class login(BaseModel):
#     username:str
#     password:str
# @app.post("/common")
# def read_rot(obj:login):
#     mydb =mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="",
#         database="loginew",
#         port=3310
#     )
#     mypost = mydb.cursor()
#     # mypost.execute("select * from loginnn WHERE username='"+obj.username+"' AND password = '"+obj.password+"'")
#     mypost.execute("SELECT * FROM loginnn WHERE username=%s AND password=%s", (obj.username, obj.password))
#
#     w =mypost.fetchall()
#     mydb.commit()
#     return w



