# -*- coding: utf-8 -*-

"""
*
*
* SSD1306 font array creator
* Created by Ign555
* Version : v1.0
* File Creation : 18/04/2025
* 
*
""" 

"""
*
* Module import
*
"""

##############################-Casuals modules-##############################

import math

##############################-Processing modules-##############################

from PIL import Image

"""
*
* Font converter macros
*
"""

WHITE_PIXEL_VALUE = 255
PIXEL_IN_PAGE = 8
PIXEL_IN_BYTE = 8
N_METADATA = 3

"""
*
* SSD1306FontConverter class
*
"""

class SSD1306FontConverter:
    
    def __init__(self):
        pass
    
    ##############################-Convertion methodes ( public )-##############################  
    
    def convert_and_export(self, img_path, fw, fh, w=-1, h=-1, array_name="font_data", export_path="font.c"):    
        
        if array_name == "": array_name = "font_data"
        if export_path == "": export_path = "font.c"
        
        c_array_str = self.__convert(img_path, w, h, fw, fh, array_name)
        
        with open(export_path, "w") as f:
            f.write(c_array_str)

    def convert_and_print(self, img_path, fw, fh, w=-1, h=-1, array_name="font_data"): 
        if array_name == "": array_name = "font_data"
        c_array_str = self.__convert(img_path, w, h,  fw, fh, array_name)
        print(c_array_str)
    
       
    ##############################-Convertion private methodes-##############################
    
    def __convert(self, img_path, w, h, fw, fh, array_name):
        
        img = self.__convert_BW(img_path, w, h)
        font_data = self.__convert_font_table_to_array(img, fw, fh)
        c_array_str = self.__create_c_array(font_data, array_name)
        return c_array_str
    
    def __convert_BW(self, img_path, w, h):
        
        img = Image.open(img_path)
        
        if w != -1 and h != -1:
            img = img.resize((w, h)) #Resize image 
            
        img = img.convert('1') #Convert image to black & white
        
        return img   
    
    def __convert_font_table_to_array(self, img, fw, fh):
        
        font_data = []
        w, h = img.size
        
        if w % fw != 0 or h % fh != 0: exit(0)
        
        n_charater_row = int(w/fw)
        n_charater_column = int(h/fh)
        
        #Insert image "metadata" into the array
        font_data.append(fw)
        font_data.append(fh)
        font_data.append(int(math.ceil(fw/PIXEL_IN_BYTE))) #Number of byte for one character

        #For each line
        for y in range(n_charater_column):
            
            #For each column
            for x in range(n_charater_row):
                
                #Calculate x and y coordinate
                character_x = x * fw
                character_y = y * fh
                
                #Make array of character and put it into the "font_data" array
                character_rectangle = (character_x, character_y, character_x + fw, character_y + fh)
                character_img = img.crop(character_rectangle) #Crop the image to keep the char only
                character_pixels = character_img.load() #Convert the cropped image into an array
                font_data.append(self.__character_image_to_bytes_array(character_pixels, fw, fh))
            
        return font_data
    
    def __create_c_array(self, font_data, array_name="font"):
        
        h = font_data[1]
        element_in_line = font_data[2]
        n_element = 128 *  element_in_line * h #Calculate the number of element in the exported array
        
        #File header
        c_array = '#include "SSD1306_writer.h"\n\n'
        c_array += f"const SSD1306_FONT {array_name}[{n_element + N_METADATA}] = " + "{\n\n" #Create the array header
        c_array += f"0x{font_data[0]:02X}, 0x{font_data[1]:02X}, 0x{font_data[2]:02X},\n\n" #Append image information line
        
        for i in range(128):
            
            character = chr(i) if i > 64 else ''
            c_array += f"//ascii : {i} -> {character}\n"
            
            for character_row in range(h): #For each character's row
                c_array += f"0x{font_data[i + N_METADATA][character_row]:02X}" #Append the array with the byte in a C_array format
                
                if i < n_element - 1: #If we are not on the last line
                    c_array += ", "
                
                if (i + 1) % element_in_line == 0: #If we are on the last pixel of the image, back to line
                    c_array  += "\n"
            
            
            c_array  += "\n\n\n" #After each charater section, double jump
                
        c_array += "\n};" #Closing the array
            
        return c_array
    
    ##############################-Tools methodes ( private )-##############################
    
    def __character_image_to_bytes_array(self, char_pixels, fw, fh):
        
        char_data = []

        #Flatten image width pixels into byte
        for y in range (0, fh): #For all pixel in height 
            
            for pixelgroup in range(0, fw, PIXEL_IN_BYTE): #For each group of 8 pixel in a row
                
                byte = 0
                
                for bit in range(PIXEL_IN_BYTE):  #For each pixel of this group    
                    
                 
                    x = pixelgroup + bit
                    
                    if x >= fw : continue #Avoid index out of range 
                    
                    if char_pixels[x, y] == WHITE_PIXEL_VALUE: #If the image data at this position is white
                        byte |= (1 << bit)
                        
                char_data.append(byte) #Place the maked byte into an array
        
        return char_data
          
"""
                                                                                                    
                                                                                                    
                                                                       .                            
                                                .                          .                        
                .                                                                                   
                                  .                           .                                     
                                          .                                                      .  
                                                  .                     .                           
                            .                                .                                      
                 .                 .        .     .                                                 
                                                          .                             .           
                                                                                                    
                                                                                       .            
                                                                                              .     
                                  .                                                                 
                                                                               .                    
                                                                                                  . 
                                           .                                                        
                                                                                                    
                                     .                                             .                
                                           .                                                        
                   @@@@@@            =@@@@@@            @@@@@@*       .    @@@@@@                   
                   @@@@@@            =@@@@@@            @@@@@@*            @@@@@@                   
              .    @@@@@@            =@@@@@@            @@@@@@*            @@@@@@                   
                   @@@@@@            =@@@@@@            @@@@@@*            @@@@@@                   
                   @@@@@@            =@@@@@@            @@@@@@*    .       @@@@@@                   
                   @@@@@@            =@@@@@@            @@@@@@*            @@@@@@   .               
                   @@@@@@            =@@@@@@            @@@@@@*            @@@@@@                   
                   @@@@@@            =@@@@@@            @@@@@@*            @@@@@@                   
                   @@@@@@            =@@@@@@      .     @@@@@@*            @@@@@@    .              
                   @@@@@@            =@@@@@@            @@@@@@*            @@@@@@                   
                   @@@@@@        .   =@@@@@@            @@@@@@*            @@@@@@                   
                   @@@@@@            =@@@@@@            @@@@@@*            @@@@@@                   
                   @@@@@@            =@@@@@@            @@@@@@*            @@@@@@                   
  .                      @@@@@@@@@@@@*                        =@@@@@@@@@@@@                         
                         @@@@@@@@@@@@*                        =@@@@@@@@@@@@                 .       
                         @@@@@@@@@@@@*                        =@@@@@@@@@@@@                         
                         @@@@@@@@@@@@*                        =@@@@@@@@@@@@                         
      .............        .                                             .       .............      
      .............        .                                           .         .............      
      .............     . .                                      .               ..............     
      .............                  =@@@@@@    . @@@@@@      =@@@@@@            .............      
      .............                  =@@@@@@.     @@@@@@      =@@@@@@            .............      
      .............  .               =@@@@@@      @@@@@@      =@@@@@@            .............      
      .............                  =@@@@@@      @@@@@@      =@@@@@@            .............     .
       .                       .            @@@@@@      @@@@@@*                          .          
                                            @@@@@@      @@@@@@*                                     
                    .                       @@@@@@      @@@@@@*     .            .                  
                                                                                                    
                                                                                                    
                                           .           .         . .        .                       
                          .                                                                         
     .                                                                   .                          
                                                                         .      .                   
"""