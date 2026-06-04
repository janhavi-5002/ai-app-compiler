class ReliabilityScore:

    def calculate(
        self,
        validation_errors,
        consistency_issues
    ):

        score = 100

        score -= len(validation_errors) * 10
        score -= len(consistency_issues) * 15

        if score < 0:
            score = 0

        return score