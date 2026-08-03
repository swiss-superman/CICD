from fastapi import FastAPI, Response
from fastapi.responses import RedirectResponse, JSONResponse
from starlette.status import HTTP_404_NOT_FOUND
from dotenv import load_dotenv
import random
from cs50 import SQL
import os

load_dotenv()

app = FastAPI(
    description = "API(FastAPI) endpoints with k8s deployment",
    version = "v1.0"
)

db = SQL(os.getenv("DB_URL"))

""" Utility Endpoints """
@app.get("/")
async def index():
    return RedirectResponse(url="/health")

@app.get("/health")
async def health():
    return {
        "status": "healthy",
        "code": 200,
        "time": db.execute("SELECT datetime() AS now")[0]['now'],
        "version": os.getenv("API_VERSION"),
        "project info": "/project/info",
        "something_random": "hello, all!"
    }

@app.get("/info")
async def randominfo():
    rows = db.execute("SELECT name FROM student")
    names = [r['name'] for r in rows]
    return {
        "rand_str": os.getenv("USER_NAME"),
        "rand_pstr": os.getenv("USER_PASSWORD"),
        "names": names
    }

@app.get("/random/{guess}")
async def search(guess: int):
    if guess == random.randint(1, 10):
        return {
            "message": "Great, the same pseudo-random number was generated"
        }
    else:
        return {
            "message": "Invalid random number guessed, try something between (1, 10)"
        }

@app.get("/contribute")
async def contribute():
    return {
        "message": "Contribute to the project @ https://github.com/swiss-superman/CICD.git"
    }

@app.get("/project/info")
async def projectinfo():
    return {
        "github": "https://github.com/swiss-superman/CICD.git",
        "dockerhub": "https://hub.docker.io/kaoksn/dummyapi",
        "pull": "docker pull docker.io/kaoksn/dummyapi:latest",
        "version": os.getenv("API_VERSION")
    }

""" Error Handlers """
@app.exception_handler(404)
async def not_found_handler(request: Response, exc):
    return JSONResponse(
        status_code=HTTP_404_NOT_FOUND,
        content={
            "message": "Not found",
            "path": str(request.url)
        }
    )

@app.exception_handler(500)
async def internal_server_error(request: Response, exc):
    return JSONResponse(
        status_code=500,
        content = {
            "message": "Internal Sever Error.",
            "path": str(request.url)
        }
    )
