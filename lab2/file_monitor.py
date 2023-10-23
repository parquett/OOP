import os
import datetime
import struct

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

class ImageFile(FileInfo):
    def __init__(self, file_path):
        super().__init__(file_path)

    def get_image_size(self):
        with open(self.file_path, 'rb') as f:
            header = f.read(24)
            if header.startswith(b'\x89PNG\r\n\x1a\n'):
                width, height = struct.unpack('>LL', header[16:24])
            elif header[0:2] == b'\xff\xd8':
                f.seek(0)
                size = f.read(2)
                if size == b'\xff\xd8':
                    f.seek(0)
                while size and ord(size[0:1]) == 0xff and size[1:2] != b'\xdb':
                    size = size[2:4]
                    size = struct.unpack('>H', size)[0]
                    f.seek(size - 2, 1)
                    size = f.read(4)
                width, height = struct.unpack('>HH', size)
            else:
                width, height = None, None
            return f"{width}x{height}" if width and height else "N/A"

    def get_info(self):
        file_info = super().get_info()
        file_info["Image Size"] = self.get_image_size()
        return file_info

class TextFile(FileInfo):
    def __init__(self, file_path):
        super().__init__(file_path)

    def get_text_file_info(self):
        with open(self.file_path, "r", encoding="utf-8") as file:
            lines = file.readlines()
        return {
            "Line Count": len(lines),
            "Word Count": sum(len(line.split()) for line in lines),
            "Character Count": sum(len(line) for line in lines),
        }

    def get_info(self):
        file_info = super().get_info()
        text_file_info = self.get_text_file_info()
        file_info["Line Count"] = text_file_info["Line Count"]
        file_info["Word Count"] = text_file_info["Word Count"]
        file_info["Character Count"] = text_file_info["Character Count"]
        return file_info

class ProgramFile(FileInfo):
    def __init__(self, file_path):
        super().__init__(file_path)

    def get_program_file_info(self):
        with open(self.file_path, "r", encoding="utf-8") as file:
            content = file.read()
        lines = content.split("\n")
        class_count = content.count("class ")
        method_count = content.count("def ")
        return {
            "Line Count": len(lines),
            "Class Count": class_count,
            "Method Count": method_count,
        }

    def get_info(self):
        file_info = super().get_info()
        program_file_info = self.get_program_file_info()
        file_info["Line Count"] = program_file_info["Line Count"]
        file_info["Class Count"] = program_file_info["Class Count"]
        file_info["Method Count"] = program_file_info["Method Count"]
        return file_info
