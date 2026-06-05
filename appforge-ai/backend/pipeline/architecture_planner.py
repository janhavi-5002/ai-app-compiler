from schemas.architecture_schema import ArchitectureSchema


class ArchitecturePlanner:

    def generate(self, intent):

        entities = ["User"]
        pages = []
        apis = []
        tables = ["users"]

        if "contacts" in intent.features:
            entities.append("Contact")
            pages.append("Contacts")
            apis.append("/contacts")
            tables.append("contacts")

        if "dashboard" in intent.features:
            pages.append("Dashboard")

        if "login" in intent.features:
            apis.append("/login")

        return ArchitectureSchema(
            entities=entities,
            pages=pages,
            apis=apis,
            tables=tables
        )