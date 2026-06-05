class MutationEngine:

    def apply_change(
        self,
        architecture,
        change_request
    ):

        changes = []

        request = change_request.lower()

        if "payment" in request:

            if "subscriptions" not in architecture.tables:
                architecture.tables.append(
                    "subscriptions"
                )

                changes.append(
                    "Added subscriptions table"
                )

            if "/payments" not in architecture.apis:
                architecture.apis.append(
                    "/payments"
                )

                changes.append(
                    "Added payments API"
                )

            if "Billing" not in architecture.pages:
                architecture.pages.append(
                    "Billing"
                )

                changes.append(
                    "Added Billing page"
                )

        return architecture, changes