import fastapi
import uvicorn

print("Hello World")

api = fastapi.FastAPI()
# Use Alt-Enter for context help

@api.get("/")
def index():
    return {"msg": "Hello from FastAPI",
            "Another Message": "Hello World"}

uvicorn.run(api)