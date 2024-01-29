<a>
    <img src="https://i.imgur.com/MYoL8dH.png" alt="Lucrypter logo" title="Lucrypter" align="right" height="200" />
</a>



# Lucrypter
Lucrypter is a steganography encrypter and decrypter that allows to encrypt text messages within lossless image formats, it currently supports LSB encryption and PNG

## Usage
### Installation
To run Lucrypter you only need the [PIL Image module](https://pillow.readthedocs.io/en/stable/reference/Image.html), you can install it directly running in the terminal 
```
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade Pillow
```
or using the `requirements.txt`
```
pip install -r requirements.txt
```
### Running
Open your terminal and navigate to the script folder using `cd`
```
C:\Users\Luca>cd Documents\GitHub\Lucrypter

C:\Users\Luca\Documents\GitHub\Lucrypter> 
```

To use Lucrypter run the python script in the terminal with the following options:
| Example                                                        | Outcome                                                                                                                                                                                    |
|----------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `python Lucrypt.py -e <IMAGE_PATH.png>`                        | Asks for input text and hides it inside IMAGE_PATH.png, **original image will be modified**                                                                                                |
| `python Lucrypt.py -e <IMAGE_PATH.png> <OUT_PATH.png>`         | Asks for input text and hides it in a copy of IMAGE.png called OUT_PATH, <br> if OUT_PATH.png  doesn't exist it will be created, otherwise the existing file OUT_PATH.png will be modified |
| `python Lucrypt.py -d <IMAGE_PATH.png>`                        | Prints the text hidden in IMAGE_PATH.png                                                                                                                                                   |

# How does it work?
Every digital image is made of `pixels`, each pixel contains information about the **color** and sometimes
the **transparency** it will display. Colored images are usually saved with the `RGB` pixel format, where
the color is expressed as the amount of the `Red`,`Green`and `Blue` the pixel contains:<br><br>
![image](https://github.com/Green-H/Lucrypter/assets/93196082/da38d64d-b38d-4bff-9c6e-9f5b9cf8b460) <br> [image credits](https://www.researchgate.net/publication/346669123_LSB_Steganography_Using_Pixel_Locator_Sequence_with_AES)<br><br>
As the information for each color is stored as an `8-bit` binary number we can modify the rightmost bit resulting in a basically undetectable change to the naked eye. This rightmost bit is the `Least Significat Bit` also called `LSB` and
because binary numbers work with the powers of two (starting from right to left) and $2^0=1$ we can change the LSB with minimal impact on the pixel color:<br><br>
![image](https://github.com/Green-H/Lucrypter/assets/93196082/8ab4a650-7a0c-44c4-960b-a69b718844b1)<br><br>
This allows us to flip the last bit of the RGB pixel in each channel according to the bit of the character in the text we need to hide preserving the image overall appearance: <br><br>
![image](https://github.com/Green-H/Lucrypter/assets/93196082/bdd21c5f-54d1-4a12-859c-37e31cd83a92)<br><br>





