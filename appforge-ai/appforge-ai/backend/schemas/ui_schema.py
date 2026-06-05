from pydantic import BaseModel
from typing import List


class UISchema(BaseModel):
    pages: List[str]