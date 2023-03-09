from typing import Union
from fastapi import FastAPI, File, UploadFile
from database import engine, Base, ToDo
from sqlalchemy.orm import Session
import sqlite3


Base.metadata.create_all(engine)
import shemas
app = FastAPI()
from starlette.responses import FileResponse 



@app.get("/")

async def root():
    return FileResponse('index.html')




@app.post("/upload")
def upload(file: UploadFile = File(...)):
    try:
        contents = file.file.read()
        with open(file.filename, 'wb') as f:
            f.write(contents)
    except Exception:
        return {"message": "Error"}
    finally:
        file.file.close()

    return {"message": f"Sucess"}



@app.post("/add")
def  add_todo(todo: shemas.ToDo):                                #shema jasona
    """
    API call for adding a TODO item
    """
    session = Session(bind=engine, expire_on_commit = False)
    todoDB = ToDo(task=todo.task)
    session.add(todoDB)
    session.commit()
    id = todoDB.id
    session.close()
    return f"Created new TODO item with id {id}"

@app.delete("/delete/{id}")
def delete_todo(id:int):
    return "Delete TODO"

@app.put("/update/{id}")
def update_todo():
    return "Update TODO"

@app.get("/get/{id}")
def get_todo():
    return {"item_id": item_id}

@app.get("/list")
def get_all_todos():
    return "ALL TODOs"
###    

### SQL PODATKOVNE BAZE
 
conn = sqlite3.connect('database_sgl_2.db')   

with conn:
    conn.execute("""CREATE TABLE IF NOT EXISTS data (
                id text,
                numberof integer,
                time char(16),
                location char(50),
                g_url char(50),
                typeof text
                );""")
conn.close()

