# Lucrypter
Lucrypter allows to encrypt text messages within Lossless image formats, it currently supports LSB encryption and PNG

## Usage
| Example              | Outcome                                                                             |
|--------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `python lucrypt.py -e IMAGE_PATH.png`              | Asks for input text and hides it inside IMAGE_PATH.png, original image will be modified                                                                              |
| `python lucrypt.py -e IMAGE_PATH.png OUT_PATH.png` | Asks for input text and hides it in a copy of IMAGE.png, if OUT_PATH.png <br> doesn't exist it will be created, otherwise the existing file OUT_PATH.png will be modified |
| `python lucrypt.py -d IMAGE_PATH.png`              | Prints the text hidden in IMAGE_PATH.png 
