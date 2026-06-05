import os
import py_compile


class ExecutionValidator:

    def validate(self, project_path):

        results = {}

        if not os.path.exists(project_path):
            return {
                "status": "FAIL",
                "reason": "Generated project folder not found"
            }

        for file in os.listdir(project_path):

            if not file.endswith(".py"):
                continue

            file_path = os.path.join(
                project_path,
                file
            )

            try:

                py_compile.compile(
                    file_path,
                    doraise=True
                )

                results[file] = "PASS"

            except Exception as e:

                results[file] = (
                    f"FAIL: {str(e)}"
                )

        return results