from fastapi import FastAPI, HTTPException
import uvicorn

app = FastAPI()

@app.get("/plus", response_model=float)
def plus(x, y: float):
    return float(x)+float(y)


@app.get("/minus", response_model=float)
def minus(x, y: float):
    return float(x)-float(y)


@app.get("/multiply", response_model=float)
def multiply(x, y: float):
    return float(x)*float(y)


@app.get("/divide", response_model=float)
def divide(x,y:float):
    try:
        result=float(x)/float(y)
        return result
    except Exception as e:
        raise HTTPException()

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8001, reload=True)
