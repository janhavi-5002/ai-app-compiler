class RepairEngine:

    def repair(self, schemas, errors):

        repair_log = []

        if "No UI pages generated" in errors:
            schemas["ui"].pages.append("Dashboard")
            repair_log.append(
                "Added Dashboard page"
            )

        if "No API endpoints generated" in errors:
            schemas["api"].endpoints.append("/health")
            repair_log.append(
                "Added health endpoint"
            )

        if "No database tables generated" in errors:
            schemas["db"].tables.append("users")
            repair_log.append(
                "Added users table"
            )

        return schemas, repair_log