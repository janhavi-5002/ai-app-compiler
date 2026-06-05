from schemas.intent_schema import IntentSchema


class IntentExtractor:

    def extract(self, prompt: str):

        prompt = prompt.lower()

        features = []

        feature_keywords = [
            "login",
            "contacts",
            "dashboard",
            "analytics",
            "payments",
            "billing",
            "reports"
        ]

        for feature in feature_keywords:
            if feature in prompt:
                features.append(feature)

        return IntentSchema(
            app_type="CRM",
            features=features,
            roles=["admin", "user"]
        )