from pydantic import BaseModel


class Todos_list_pyd(BaseModel):
    id: int
    done: bool
    text: str

    # class Config:
    #     orm_mode = True
