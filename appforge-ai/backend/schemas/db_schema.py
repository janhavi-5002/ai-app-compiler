from pydantic import BaseModel
from typing import List


class DBSchema(BaseModel):
    tables: List[str]