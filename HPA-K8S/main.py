from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to this fantastic app!"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_name": "Item " + str(item_id)}