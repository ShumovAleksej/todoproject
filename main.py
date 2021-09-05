from typing import List
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from fastapi.responses import FileResponse
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tables import Base
import tables, uvicorn, json, pydantic_models

app = FastAPI()
database_url = 'sqlite:///sqlite3.db'

origins = [
    "*",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/get_todos", response_model=List[pydantic_models.Todos_list_pyd])
def get_todos():
    Session = sessionmaker(bind=engine)
    session = Session()
    list_todos = session.query(tables.ToDoTable).all()
    session.close()
    ret_list = []
    for todo in list_todos:
        ret_list.append({'id': todo.id, 'text': todo.text, 'done': todo.done})
    return ret_list

@app.get("/add_todo")
def add_todo(text_add: str, done_add: bool = False):
    Session = sessionmaker(bind=engine)
    session = Session()
    new_row = tables.ToDoTable(done = done_add, text = text_add)
    session.add(new_row)
    session.commit() #сохранение изменений*
    session.close()
    return {'Okey'}

@app.get("/change_todo")
def change_todo(id_todo: int, text_todo: str, done_todo: bool = False):
    Session = sessionmaker(bind=engine)
    session = Session()
    changed_record = session.query(tables.ToDoTable).get(id_todo)
    changed_record.text = text_todo
    changed_record.done = done_todo
    session.commit() #сохранение изменений*
    session.close()
    return {'Okey'}

@app.get("/delete_todo")
def delete_todo(id_todo: int):
    Session = sessionmaker(bind=engine)
    session = Session()
    session.query(tables.ToDoTable).filter(tables.ToDoTable.id == id_todo).delete()
    session.commit() #сохранение изменений*
    session.close()
    return {'Okey'}

@app.get("/get_image")
def get_image():
    # Session = sessionmaker(bind=engine)
    # session = Session()
    # session.close()
    return FileResponse("rick.jpg", media_type="image/jpg")

engine = create_engine(
    database_url,
    connect_args={'check_same_thread': False},
)
# Base.metadata.create_all(engine)
# new_row = tables.ToDoTable(done = False, text ='sgrgrrge')
uvicorn.run(app, host='192.168.0.16')