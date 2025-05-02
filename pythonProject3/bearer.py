from fastapi import FastAPI,HTTPException,Depends,Header,status
import uuid

app =FastAPI()
VALID_TOKEN="cfcc3bd0-85e8-4950-9658-32992c5a4ded"

@app.post("/generate_token")
def generate_bearer_token():
    token=str(uuid.uuid4())
    return {"token":token}


@app.post("/bearer")
def bearer_auth(authorization:str=Header(None)):
    if authorization==f"Bearer {VALID_TOKEN}":
        return {"message":"Token is valid"}
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid Token")