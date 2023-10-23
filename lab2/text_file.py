from file_info import FileInfo


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