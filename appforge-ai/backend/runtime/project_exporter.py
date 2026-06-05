import shutil
import os


class ProjectExporter:

    def export_zip(self, project_folder):

        if not os.path.exists(project_folder):
            return None

        zip_file = shutil.make_archive(
            project_folder,
            "zip",
            project_folder
        )

        return zip_file