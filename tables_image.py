import sqlalchemy as sa
import test_img2, uvicorn, base64
from fastapi import FastAPI
from sqlalchemy.ext.declarative import declarative_base
from fastapi.responses import FileResponse
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker

app = FastAPI()
Base = declarative_base()


class ToDoTable(Base):
    __tablename__ = 'IMGTest'
    id = sa.Column(sa.Integer, primary_key=True)
    img = sa.Column(sa.String)


engine = create_engine(
    'sqlite:///img.db',
    connect_args={'check_same_thread': False},
)
# Base.metadata.create_all(engine)

def use_name(name, chet):
    r = ''
    for i in name:
        if chet == 0:
            break
        if i in '\/:*?"<>|':
            continue
        r += i
        chet -= 1
    return r


@app.get("/get_image")
def get_image(name: str):
    Session = sessionmaker(bind=engine)
    session = Session()
    # new_row = ToDoTable(img = picture_data)
    # session.add(new_row)
    # session.commit()
    picture_data = test_img2.get_pic_str(name)
    list_todos = session.query(ToDoTable).all()
    test_img2.save_pic(list_todos[0].img, name)
    session.close()
    return FileResponse(name, media_type="image/jpg")


uvicorn.run(app, host='192.168.0.16', port=8080)