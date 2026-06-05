from pydantic import BaseModel
from typing import List


class APISchema(BaseModel):
    endpoints: List[str]