class ConsistencyValidator:

    def validate(
        self,
        architecture,
        schemas
    ):

        issues = []

        for page in architecture.pages:

            page_lower = page.lower()

            if page_lower == "contacts":

                if "contacts" not in schemas["db"].tables:
                    issues.append(
                        "Contacts page missing DB table"
                    )

                if "/contacts" not in schemas["api"].endpoints:
                    issues.append(
                        "Contacts page missing API"
                    )

        return issues