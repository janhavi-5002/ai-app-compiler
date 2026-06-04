import os


class RuntimeGenerator:

    def generate(self, architecture):

        output_dir = "generated_app"

        os.makedirs(output_dir, exist_ok=True)

        with open(
            f"{output_dir}/models.py",
            "w"
        ) as f:

            f.write("# Auto Generated Models\n\n")

            for table in architecture.tables:

                class_name = table.capitalize()

                f.write(
                    f"class {class_name}:\n"
                )

                f.write(
                    "    pass\n\n"
                )

        with open(
            f"{output_dir}/routes.py",
            "w"
        ) as f:

            f.write(
                "# Auto Generated Routes\n\n"
            )

            for api in architecture.apis:

                route_name = api.replace(
                    "/",
                    ""
                )

                if not route_name:
                    continue

                f.write(
                    f"def {route_name}():\n"
                )

                f.write(
                    "    pass\n\n"
                )

        with open(
            f"{output_dir}/main.py",
            "w"
        ) as f:

            f.write(
                "# Auto Generated Application\n"
            )

        return output_dir