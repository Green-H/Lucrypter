"""
This program should take an input from the user and encrypt it using the steganography algorithm selected
Possible Encryption levels on lossless compression file types:
- LSB
"""
from PIL import Image


def text_to_binary(text):
    # Convert input text into binary
    binary_text = ''.join(format(ord(char), '08b') for char in text)
    # Terminator sequence used later in decryption
    binary_text = binary_text + "00000000"
    print("The string converted to binary is: " + binary_text)
    return binary_text


def encryptLSB(text, image, output_path):
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
                print("Pixel values before encryption: ", image.getpixel((x, y)))
                current_data_bit = int(binary_text[index], base=2)
                # Distributing the data in all three RGB values allows less noticeable changes in the final image
                # at this stage a pixel looks like this pixel = [250,120,36]
                # we need to access the LSB of each of those channels and replace it with our data
                for channel in range(3):
                    # Set the LSB to the value of the current binary data
                    pixel[channel] = (pixel[channel] & ~1) | current_data_bit
                # Update the pixel
                image.putpixel((x, y), tuple(pixel))
                print("Pixel values after encryption: ", image.getpixel((x, y)))
                print("--------------------------------------")
                # Pass to the next data bit
                index += 1
                # if done with the text, set flag to true and exit
                if index == len(binary_text):
                    data_done = True
    # Save the image
    image.save(output_path)
    print(">>>>>>>>>>>>>>>>>>>>>>>><")
    test = Image.open(output_path)
    print("The processed image first pixel is: ", image.getpixel((0, 0)))
    print("In the output image the first pixel is: ", test.getpixel((0, 0)))


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
            if len(bytestring) == 8:
                if bytestring == "00000000":
                    return msg
                msg += chr(int(bytestring, base=2))
                print(msg)
                bytestring = ""


encode = ("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque fermentum massa maximus turpis "
          "iaculis efficitur. Ut non ullamcorper leo. Cras tincidunt ligula vitae diam pellentesque feugiat. Nulla "
          "quis turpis ac magna pellentesque varius nec vitae neque. Vivamus et augue dapibus, dapibus ligula id, "
          "interdum elit. Duis imperdiet est scelerisque tempus interdum. Duis rutrum consequat metus eget "
          "sollicitudin. Nunc elementum venenatis facilisis.")
encryptLSB(encode, "PNG_transparency_demonstration_1.png", "pngtest.png")
print("===============================================================================")

decryptLSB("pngtest.png")
