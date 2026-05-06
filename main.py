from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "RoleFit AI v2 is up and running"}
