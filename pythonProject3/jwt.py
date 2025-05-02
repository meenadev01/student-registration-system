from fastapi import FastAPI,status,HTTPException
from jose import JWTError,jwt
from jose.constants import ALGORITHMS
#pip install python-jose
from pydantic import BaseModel
from datetime import datetime,timedelta

SECRET_KEY="123456"
ALGORITHM="HS256"
class Token(BaseModel):
    access_token:str
    token_type:str

app=FastAPI()
@app.get("/get_token")
async def get_token():
    expire=datetime.utcnow()+timedelta(minutes=15)
    data={
        'info':'secret information',
        'from':'GFG',
        'exp':expire
    }
    encode_jwt=jwt.encode(data,SECRET_KEY,algorithm=ALGORITHM)
    return {'token':encode_jwt}
class TokenRequest(BaseModel):
    token:str

@app.post("/verify_token")
async def verify_token(authorization: TokenRequest):
    try:
        payload=jwt.decode(authorization.token,SECRET_KEY,algorithms=ALGORITHM)
        return payload
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="could not validate credentials"
        )








