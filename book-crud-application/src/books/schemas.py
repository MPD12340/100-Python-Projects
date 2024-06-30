from pydantic import BaseModel
from typing import List, Union, Any, Dict

class BookModel(BaseModel):
    id: str
    title: str
    pageCount: int | None = None
    price: str
    publication: str


class ResponseModel(BaseModel):
    success: bool
    data: Union[Dict[str, Any], List[Any], None] = None
    error: Union[str, None] = None    