from schemas.ui_schema import UISchema
from schemas.api_schema import APISchema
from schemas.db_schema import DBSchema
from schemas.auth_schema import AuthSchema


class SchemaGenerator:

    def generate(self, architecture):

        ui_schema = UISchema(
            pages=architecture.pages
        )

        api_schema = APISchema(
            endpoints=architecture.apis
        )

        db_schema = DBSchema(
            tables=architecture.tables
        )

        auth_schema = AuthSchema(
            roles={
                "admin": ["create", "read", "update", "delete"],
                "user": ["read"]
            }
        )
        ui_schema = UISchema(
            pages=[]
        )

        return {
            "ui": ui_schema,
            "api": api_schema,
            "db": db_schema,
            "auth": auth_schema
        }
        