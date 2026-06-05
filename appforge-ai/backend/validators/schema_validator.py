class SchemaValidator:

    def validate(self, schemas):

        errors = []

        if len(schemas["ui"].pages) == 0:
            errors.append("No UI pages generated")

        if len(schemas["api"].endpoints) == 0:
            errors.append("No API endpoints generated")

        if len(schemas["db"].tables) == 0:
            errors.append("No database tables generated")

        return errors