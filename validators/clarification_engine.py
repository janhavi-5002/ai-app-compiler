class ClarificationEngine:

    def generate_questions(
        self,
        issues
    ):

        questions = []

        for issue in issues:

            if issue == "Authentication not specified":

                questions.append(
                    "Should login/signup be included?"
                )

            elif issue == "Roles not specified":

                questions.append(
                    "Do you need Admin/User roles?"
                )

            elif issue == "Prompt too vague":

                questions.append(
                    "Can you provide more details?"
                )

        return questions