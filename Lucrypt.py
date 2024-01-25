"""
This program should take an input from the user and encrypt it using the steganography algorithm selected
Possible Encryption levels on lossless compression file types:
- LSB
"""
from PIL import Image
import argparse


def text_to_binary(text):
    # Convert input text into binary
    binary_text = ''.join(format(ord(char), '016b') for char in text)
    # Terminator sequence used later in decryption
    binary_text = binary_text + "0000000000000000"
    return binary_text


def encryptLSB(text, image, output_path=None):
    if output_path is None:
        output_path = image
    image = Image.open(image)
    binary_text = text_to_binary(text)
    width, height = image.size
    if len(binary_text) > width * height:
        raise ValueError('Text too long to be encrypted in this image, provide a larger image')
    # The index of the data bit currently being processed
    index = 0
    data_done = False
    for y in range(height):
        for x in range(width):
            if not data_done:
                pixel = list(image.getpixel((x, y)))
                current_data_bit = int(binary_text[index], base=2)
                # Distributing the data in all three RGB values allows less noticeable changes in the final image
                # at this stage a pixel looks like this pixel = [250,120,36]
                # we need to access the LSB of each of those channels and replace it with our data
                for channel in range(3):
                    # Set the LSB to the value of the current binary data
                    pixel[channel] = (pixel[channel] & ~1) | current_data_bit
                # Update the pixel
                image.putpixel((x, y), tuple(pixel))
                # Pass to the next data bit
                index += 1
                # if done with the text, set flag to true and exit
                if index == len(binary_text):
                    data_done = True
    # Save the image
    image.save(output_path)


def decryptLSB(image):
    image = Image.open(image)
    width, height = image.size
    bytestring = ""
    msg = ""
    for y in range(height):
        for x in range(width):
            pixel = list(image.getpixel((x, y)))
            bit = pixel[0] & 0b00000001
            bytestring += str(bit)
            if len(bytestring) == 16:
                if bytestring == "0000000000000000":
                    print(msg)
                    return 0
                msg += chr(int(bytestring, base=2))
                bytestring = ""


def main():
    parser = argparse.ArgumentParser(
        description='Lucrypter is a small program that allow to encrypt and decrypt text using LSB steganography')
    parser.add_argument('-e', '--encrypt', nargs='+', help='Asks for text to encrypt and an image to hide it in, '
                                                           'optional argument if you want the encrypted image in a '
                                                           'different path')
    parser.add_argument('-d', '--decrypt', nargs=1, help='Decrypt the image extracting the text')

    args = parser.parse_args()

    if args.encrypt:
        input_text = input("Enter the text to encrypt: ")
        input_image = args.encrypt[0]
        output_image = args.encrypt[-1] if len(args.encrypt) >= 2 else None
        encryptLSB(input_text, input_image, output_image)
    elif args.decrypt:
        input_image = args.decrypt[0]
        decryptLSB(input_image)
    else:
        print("Specify either the --encrypt/--decrypt flag")


if __name__ == '__main__':
    main()
