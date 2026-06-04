class RequirementAnalyzer:

    def analyze(self, prompt):

        issues = []

        prompt = prompt.lower()

        if len(prompt.split()) < 4:
            issues.append(
                "Prompt too vague"
            )

        if "crm" in prompt:

            if "login" not in prompt:
                issues.append(
                    "Authentication not specified"
                )

            if "role" not in prompt:
                issues.append(
                    "Roles not specified"
                )

        return issues