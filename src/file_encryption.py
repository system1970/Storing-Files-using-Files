# src/file_encryption.py
import os
from .binary_utils import string_to_binary, binary_to_string
from .image_utils import create_binary_image, create_binary_image_folder, is_zero
from .file_utils import create_folder, get_file_size, get_folder_size

class FileEncryption:
    """
    A class to handle file encryption by encoding text into binary images and decoding it back to text.
    """

    def __init__(self, info_file="info.txt", output_folder="Secret", mode=1):
        """
        Initializes the FileEncryption object by reading the info file and encoding the contents.
        """
        self.info_file = info_file
        self.output_folder = output_folder
        self.text = self._read_info(info_file)
        self.encode(self.text, mode)

    def _read_info(self, info_file):
        """
        Reads the contents of the specified file.
        """
        with open(info_file, 'r') as file:
            return file.read()

    def encode(self, text="", mode=1):
        """
        Encodes the provided text into a binary format and saves it as images.
        """
        binary_string = string_to_binary(text)
        encoding_function = create_binary_image if mode == 0 else create_binary_image_folder
        encoding_function(binary_string, self.output_folder)
        print(f"Text encoded and saved in '{self.output_folder}'")
        self.display_sizes()
        return self

    def decode(self, folder_path=None):
        """
        Decodes the binary images back into the original text.
        """
        folder_path = folder_path or self.output_folder

        def get_files():
            return sorted([os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.endswith(".png")], key=lambda x: int(os.path.splitext(os.path.basename(x))[0]))

        binary_string = "".join([str(int(not is_zero(file))) for file in get_files()])
        decoded_text = binary_to_string(binary_string)
        print(f"Decoded text: {decoded_text}")
        return decoded_text

    def display_sizes(self):
        """
        Displays the size of the info.txt file and the total size of the Secret folder.
        Also calculates and prints the size increase ratio.
        """
        info_size_bytes = os.path.getsize(self.info_file)
        secret_size_bytes = self._get_secret_size_in_bytes()

        info_size = get_file_size(self.info_file)
        secret_size = get_folder_size(self.output_folder)
        ratio = secret_size_bytes / info_size_bytes if info_size_bytes > 0 else 0

        print(f"Info.txt [{info_size}] -> Secret folder [{secret_size}]")
        print(f"Information size increased by {round(ratio, 2)} times")

    def _get_secret_size_in_bytes(self):
        """
        Helper function to calculate the total size of the Secret folder in bytes.
        """
        total_size = 0
        for dirpath, dirnames, filenames in os.walk(self.output_folder):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                total_size += os.path.getsize(fp)
        return total_size
