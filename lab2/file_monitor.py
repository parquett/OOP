import os
import datetime
from file_info import FileInfo
from image_file import ImageFile
from text_file import TextFile
from program_file import ProgramFile


class FileMonitor:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.snapshot_time = None
        self.files = {}

    def commit(self):
        self.snapshot_time = datetime.datetime.now()
        self.files = {}

    def info(self, filename):
        file_path = os.path.join(self.folder_path, filename)
        if os.path.exists(file_path):
            extension = os.path.splitext(filename)[1]
            if extension in {".jpg", ".png"}:
                file_object = ImageFile(file_path)
            elif extension == ".txt":
                file_object = TextFile(file_path)
            elif extension in {".py", ".java"}:
                file_object = ProgramFile(file_path)
            else:
                file_object = FileInfo(file_path)
            file_info = file_object.get_info()
            for key, value in file_info.items():
                print(f"{key}: {value}")
        else:
            print(f"File '{filename}' not found in the folder.")


    def status(self):
        if self.snapshot_time is None:
            print("No snapshot has been taken. Use 'commit' to create a snapshot.")
            return

        status_output = []
        current_files = set(os.listdir(self.folder_path))
        tracked_files = set(self.files.keys())

        for filename in current_files:
            last_updated = datetime.datetime.fromtimestamp(os.path.getmtime(os.path.join(self.folder_path, filename)))
            if filename not in self.files:
                self.files[filename] = last_updated
                if last_updated > self.snapshot_time:
                    status_output.append(f"{filename} - Created")
                else:
                    status_output.append(f"{filename} - No changes")
            elif last_updated > self.snapshot_time:
                status_output.append(f"{filename} - Changed")
            else:
                status_output.append(f"{filename} - No changes")

        for filename in tracked_files - current_files:
            status_output.append(f"{filename} - Deleted")

        print(f"Created Snapshot at: {self.snapshot_time}")
        for entry in status_output:
            print(entry)
