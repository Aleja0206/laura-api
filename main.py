from fastapi import FastAPI, HTTPException
from routes.persons import router as persons_router
from routes.planets import router as planet_router

app = FastAPI()
app.include_router(planet_router)
app.include_router(persons_router)

# search the middle item in array persons_lists
def search_middle_item(array):
    middle_item = array[len(array) // 2]
    return middle_item



@app.get("/")
def ping():
    return {"message": "Hello World"}