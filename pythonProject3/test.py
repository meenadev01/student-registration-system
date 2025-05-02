from fastapi import FastAPI
from starlette.requests import Request
import time

app = FastAPI()

log_dict = {"key": "value"}

@app.middleware("http")
async def log_requests(request: Request,call_next):
    global log_dict
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    print(f"Request: {request.method} {request.url} | processed in {process_time:.4f}s")
    log_dict["log"] = f"Request: {request.method} {request.url} | processed in {process_time:.4f}s"
    return response

@app.get("/")
def home():
    return {"message": log_dict}
