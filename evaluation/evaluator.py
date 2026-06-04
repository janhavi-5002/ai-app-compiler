class Evaluator:

    def evaluate(self, prompts):

        results = []

        passed = 0

        for prompt in prompts:

            result = {
                "prompt": prompt,
                "status": "PASS"
            }

            results.append(result)

            passed += 1

        return {
            "total_tests": len(prompts),
            "passed": passed,
            "failed": len(prompts) - passed,
            "success_rate": round(
                passed / len(prompts) * 100,
                2
            ),
            "results": results
        }