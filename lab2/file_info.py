import os
import datetime


class FileInfo:
    def __init__(self, file_path):
        self.file_path = file_path
        self.filename = os.path.basename(file_path)
        self.extension = os.path.splitext(self.filename)[1]

    def get_info(self):
        return {
            "Name": self.filename,
            "Extension": self.extension,
            "Created": datetime.datetime.fromtimestamp(os.path.getctime(self.file_path)).strftime(
                "%Y-%m-%d %H:%M:%S.%f"),
            "Updated": datetime.datetime.fromtimestamp(os.path.getmtime(self.file_path)).strftime(
                "%Y-%m-%d %H:%M:%S.%f"),
        }