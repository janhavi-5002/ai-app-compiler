from pydantic import BaseModel
from typing import List


class ArchitectureSchema(BaseModel):
    entities: List[str]
    pages: List[str]
    apis: List[str]
    tables: List[str]