# 📊 File Encryption Project

Encode files into a large set of images to achieve a dramatic increase in storage size—approximately 530 times the original! This project showcases a creative approach to data obfuscation by converting text into binary format and storing it within images.

From the concept of turning text into images, we explore how this method can vastly increase storage size, making it a fascinating example of data handling.

## Overview

This project converts text from `info.txt` into binary format and encodes it as a series of images in the `Secret/` folder. The encoded images can then be decoded back into the original text. This approach offers a unique way to increase storage size and can be a fun demonstration of data manipulation.

### Notable Features
- **Text Encoding**: Convert text to binary and encode it into a series of images.
- **Text Decoding**: Decode images back into the original text.
- **Size Comparison**: View the size increase ratio, which can be as high as 530 times the original data size!

## Installation

1. **Clone the Repository**:
   Clone the repository from GitHub and navigate into the project directory.
   ```bash
   git clone https://github.com/system1970/Storing-Files-using-Files.git
   cd Storing-Files-using-Files
   ```

2. **Install Dependencies**:
   Ensure you have Python 3 installed, then install the required packages using `pip`.
   ```bash    
   pip install -r requirements.txt
   ```

## Usage

1. **Prepare the Input File**:
   Add the text you want to encode to `info.txt`.

2. **Run the Encoding Script**:
   Execute the script to encode the text into binary images. The encoded images will be saved in the `Secret/` folder.
   ``` bash
   python src/file_encryption.py
   ```

3. **Decode the Images**:
   Use the decoding method in the script to convert the images back into text.

## Example

Here’s how you can use this project:

1. Place your text into `info.txt`.
2. Run the encoding script.
3. Check the `Secret/` folder for the output images.
4. Use the decoding method to retrieve the original text.

## Contributing

Feel free to fork the repository and submit a pull request with any improvements or fixes. Contributions are welcome!

