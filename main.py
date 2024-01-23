"""
This program should take an input from the user and encrypt it using the steganography algorithm selected
Possible Encryption levels:
- LSB
"""
from PIL import Image


def text_to_binary(text):
    # Convert input text into binary
    binary_text = ''.join(format(ord(char), '08b') for char in text)
    binary_text =binary_text + "00000000"
    return binary_text


def encryptLSB(text, image, output_path):
    image = Image.open(image)
    binary_text = text_to_binary(text)
    print(binary_text)
    width, height = image.size
    print(len(binary_text))
    if len(binary_text) > width * height:
        raise ValueError('Text too long to be encrypted in this image, provide a larger image')
    # The index of the char currently being processed
    index = 0
    data_done = False
    current_bit = binary_text[index]
    for y in range(height):
        for x in range(width):
            if not data_done:
                pixel = list(image.getpixel((x, y)))

                print("Pixel selezionato: ",pixel, " coordinate x: ", x, " coordinate y: ", y)
                # Distributing the data in all three RGB values allows less noticeable changes in the final image
                # at this stage a pixel looks like this pixel = [250,120,36]
                # we need to access the LSB of each of those channels and replace it with our data
                for channel in range(3):
                    new_lsb = 0b0 if current_bit==0 else 0b1
                    # Set the LSB to zero to avoid conflicts and then to the value of the current binary data
                    pixel[channel] = (pixel[channel] & ~1) | new_lsb
                    print(pixel)
                # Update the pixel
                image.putpixel((x, y), tuple(pixel))
                print("pixel modificato:  ",pixel)

                # Pass to the next bit
                index += 1

                if index == len(binary_text):
                    data_done = True

    image.save(output_path)


def decryptLSB(image):
    image = Image.open(image)
    width, height = image.size
    text = ""
    bytestring = ""
    for y in range(width):
        for x in range(height):
            pixel = list(image.getpixel((x, y)))
            bit = pixel[0] & 0b00000001
            bytestring += str(bit)
            if len(bytestring) == 8:
                text += chr(int(bytestring))
                print(bytestring)
                print(text)


encryptLSB("stringa", "test.jpg", "encrypted.jpg")
decryptLSB("encrypted.jpg")
