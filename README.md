<a>
    <img src="https://i.imgur.com/MYoL8dH.png" alt="Lucrypter logo" title="Lucrypter" align="right" height="200" />
</a>



# Lucrypter
Lucrypter is a steganography encryptor and decrypter that allows to encrypt text messages within lossless image formats, it currently supports LSB encryption and PNG

## Usage
### Installation
To run Lucrypter you need the `PIL Image` module, you can install it  `requirements.txt` t
### Run
Open your terminal and navigate to the script folder using `cd`
```
C:\Users\Luca>cd Documents\GitHub\Lucrypter

C:\Users\Luca\Documents\GitHub\Lucrypter> 
```

To use Lucrypter run the python script in the terminal with the following options:
| Example                                                        | Outcome                                                                                                                                                                                    |
|----------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `python lucrypt.py -e <IMAGE_PATH.png>`                        | Asks for input text and hides it inside IMAGE_PATH.png, original image will be modified                                                                                                    |
| `python lucrypt.py -e <IMAGE_PATH.png> <OUT_PATH.png>`         | Asks for input text and hides it in a copy of IMAGE.png called OUT_PATH, <br> if OUT_PATH.png  doesn't exist it will be created, otherwise the existing file OUT_PATH.png will be modified |
| `python lucrypt.py -d <IMAGE_PATH.png>`                        | Prints the text hidden in IMAGE_PATH.png                                                                                                                                                   |
