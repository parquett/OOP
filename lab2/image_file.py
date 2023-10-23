import struct
from file_info import FileInfo


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