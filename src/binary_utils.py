# src/binary_utils.py

def string_to_binary(input_string):
    """
    Converts a string to its binary representation.
    """
    return ''.join(format(ord(char), '08b') for char in input_string)

def binary_to_string(binary_string):
    """
    Converts a binary string back to its character string representation.
    """
    if len(binary_string) % 8 != 0:
        raise ValueError("The length of the binary string must be a multiple of 8.")
    
    byte_chunks = [binary_string[i:i+8] for i in range(0, len(binary_string), 8)]
    return ''.join(chr(int(byte, 2)) for byte in byte_chunks)

def file_to_binary_string(file_path):
    """
    Reads a file and converts its contents into a binary string.
    """
    with open(file_path, 'rb') as file:
        file_content = file.read()
    return ''.join(format(byte, '08b') for byte in file_content)

def binary_string_to_file(binary_string, output_file_path):
    """
    Converts a binary string into its corresponding file data and writes it to the specified path.
    """
    byte_chunks = [binary_string[i:i+8] for i in range(0, len(binary_string), 8)]
    byte_data = bytearray([int(byte, 2) for byte in byte_chunks])
    with open(output_file_path, 'wb') as output_file:
        output_file.write(byte_data)
