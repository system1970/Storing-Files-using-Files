# main.py
from src.file_encryption import FileEncryption

def main():
    """
    Main function to run the FileEncryption class and demonstrate encoding and decoding.
    """
    encryption_object = FileEncryption()
    encryption_object.decode()

if __name__ == "__main__":
    main()
