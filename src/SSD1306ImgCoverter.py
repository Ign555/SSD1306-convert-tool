# -*- coding: utf-8 -*-

"""
*
*
* SSD1306 image array creator
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
* Image converter macros
*
"""

PIXEL_IN_BYTE = 8
WHITE_PIXEL_VALUE = 255
N_METADATA = 3

"""
*
* SSD1306ImgCoverter class
*
"""

class SSD1306ImgCoverter:
    
    def __init__(self):
        pass
        
    ##############################-Convertion methodes ( public )-##############################   
    
    def convert_and_export(self, img_path, w=-1, h=-1, array_name="image_data", export_path="array.c"):    
        
        if array_name == "": array_name = "image_data"
        if export_path == "": export_path = "array.c"
        
        c_array_str = self.__convert(img_path, w, h, array_name)
        
        with open(export_path, "w") as f:
            f.write(c_array_str)

    def convert_and_print(self, img_path, w=-1, h=-1, array_name="image_data"): 
        if array_name == "": array_name = "image_data"
        c_array_str = self.__convert(img_path, w, h, array_name)
        print(c_array_str)
    
       
    ##############################-Convertion private methodes-##############################
    
    def __convert(self, img_path, w, h, array_name="image_data"):
        
        img = self.__convert_BW(img_path, w, h)
        img_data = self.__convert_image_to_array(img)
        c_array_str = self.__create_c_array(img_data, array_name)
        return c_array_str
    
    def __convert_BW(self, img_path, w, h):
        
        img = Image.open(img_path)
        
        if w != -1 and h != -1:
            img = img.resize((w, h)) #Resize image 
            
        img = img.convert('1') #Convert image to black & white
        
        return img
    
    
    def __convert_image_to_array(self, img):
        
        image_data = []
        pixels = img.load() #Read image content
        w, h = img.size
        
        #Insert image "metadata" into the array
        image_data.append(w)
        image_data.append(h)
        image_data.append(int(math.ceil(w/PIXEL_IN_BYTE)))
        
        #Flatten image width pixels into byte
        for y in range (0, h): #For all pixel in height 
            
            for pixelgroup in range(0, w, PIXEL_IN_BYTE): #For each group of 8 pixel in a row
                
                byte = 0
                
                for bit in range(PIXEL_IN_BYTE):  #For each pixel of this group    
                    x = pixelgroup + bit
                    if pixels[x, y] == WHITE_PIXEL_VALUE: #If the image data at this position is white
                        byte |= (1 << bit)
                        
                image_data.append(byte) #Place the maked byte into an array
                
        return image_data

    def __create_c_array(self, image_data, array_name="img"):
        
        h = image_data[1]
        element_in_line = image_data[2]
        n_element = h * element_in_line #Calculate the number of element in the exported array
        
        c_array = '#include "SSD1306_img.h"\n\n'
        c_array += f"const SSD1306_IMG {array_name}[{n_element + N_METADATA}] = " + "{\n\n" #Create the array header
        c_array += f"0x{image_data[0]:02X}, 0x{image_data[1]:02X}, 0x{image_data[2]:02X},\n" #Append image information line
        
        for i in range(0, n_element):
            
            c_array += f"0x{image_data[i + N_METADATA]:02X}" #Append the array with the byte in a C_array format
            
            if i < n_element - 1: #If we are not on the last line
                c_array += ", "
                
            if (i + 1) % element_in_line == 0: #If we are on the last pixel of the image, back to line
                c_array  += "\n"
                
        c_array += "\n};" #Closing the array
            
        return c_array
        
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
#thx LXY