from file_info import FileInfo
import re

class ProgramFile(FileInfo):
    def __init__(self, file_path):
        super().__init__(file_path)

    def get_program_file_info(self):
        with open(self.file_path, "r", encoding="utf-8") as file:
            content = file.read()
        lines = content.split("\n")
        class_count = content.count("class ")
        # Check the file extension
        if self.extension == ".java":
            # Java
            method_count = len(re.findall(
                r"(public|protected|private|static|\s) +[\w\<\>\[\]]+\s+(\w+) *\([^\)]*\) *(\{?|[^;])",
                content))
        elif self.extension == ".py":
            # Python
            method_count = content.count("def ")
        else:
            method_count = 0
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