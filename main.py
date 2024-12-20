# Домашнее задание по теме "Структура проекта. Маршруты и модели Pydantic." module_17_1

from fastapi import FastAPI
from routers import task
from routers import user

app = FastAPI()

@app.get("/")
async def welcome():
    return {"message" : "Welcome to TaskManager"}

app.include_router(task.router)
app.include_router(user.router)


# загрузка    uvicorn main:app --reload

