# SSD1306 convertion tool guide
## Information 
These python scripts should help you to convert an image to an array compatible with my [CH32V00x-X-SSD1306 library](https://github.com/Ign555/CH32V00x-X-SSD1306).  

Please, if you use it, do not remove my credits.

## Install
No instalation procedure requiered. You only have to unzip the downloaded file and launch the script that you want to use.   

## Use 

To use, execute ```main.py```

You will have different option to add in the command :  

```-w``` or ```-i``` ```[YOUR INPUT FILE'S NAME]``` These to option are made to choose between the covertion to an image data or the convertion to a font.  
```-o``` ```[YOUR OUTPUT FILE'S NAME]``` This option gives the output file's name. ( optional )  
```-n``` ```[YOUR OUTPUT ARRAY'S NAME]``` This option gives the name of the array in the output file. ( optional )   
```-W ``` and  ```-H ``` These options gives the dimension of the final image or the size of a character in a font. It is only optional for the image convertion  

### Documentation  

No documentation available  

## Changelog

02/09/2025 : Add Image converter and font converter. There use are merge into a main file  

15/05/2025 : POO + Image file creator for SSD1306 and same for font  

17/04/2025 : Project beginning  

## To do list

* GUI

### License

This library is provided under BSD 3-Clause License. 
For more information, please look in LICENSE.md 

Please, if you have any suggest/question contact me on contact@ingeno.fr
