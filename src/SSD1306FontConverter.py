# -*- coding: utf-8 -*-

"""
*
*
* SSD1306 font array creator
* Created by Ign555
* Version : v1.0
* File Creation : 18/04/2025
* ( does not work )
*
""" 

"""
*
* Module import
*
"""

##############################-Processing modules-##############################

from PIL import Image

"""
*
* Font converter macros
*
"""

SSD1306_COLUMN = 128
WHITE_PIXEL_VALUE = 255
PIXEL_IN_PAGE = 8
BIT_IN_BYTE = 8

"""
*
* SSD1306FontConverter class
*
"""

class SSD1306FontConverter:
    
    font_data = []
    
    def __init__(self, path, character_w, character_h, n_character=128):
        
        self.n_character = n_character
        
        self.img = Image.open(path).convert('1')
        self.bitmap_w, self.bitmap_h = self.img.size
        
        if self.bitmap_w % character_w != 0 or  self.bitmap_h % character_h != 0: exit(0)   
        
        self.character_h = character_h
        self.character_w = character_w
    
    def __character_id_to_coordinate(self, char_id):
        
        x = ( char_id * self.character_w ) % self.bitmap_w
        y = ( char_id * self.character_w ) / self.bitmap_w
        
        return x, y, x + self.character_w, y + self.character_h
        
        
    def __character_bitmap_to_hex(self, char_id):
        
        character = self.img.crop(self.__character_id_to_coordinate(char_id))
        pixels = character.load() #Read image content
        
        #Flatten image height pixels into byte
        for page in range (0, self.character_h):
            for column in range(0, self.character_w, BIT_IN_BYTE):
                byte = 0
                for bit in range(BIT_IN_BYTE):
                    if pixels[column + bit, page] == WHITE_PIXEL_VALUE:
                        byte |= (1 << bit)
                self.font_data.append(byte)
                
    def __convert_font_bitmap_to_array(self):
        
        for i in range(self.n_character):
            self.__character_bitmap_to_hex(i)
        print(len(self.font_data))
        
    def __create_array(self, array_name):
        
        n_element = int(self.n_character * ( (self.character_w-PIXEL_IN_PAGE) / PIXEL_IN_PAGE + 1) * self.character_h)
        c_array = f"const SSD1306_FONT {array_name}[{n_element}] = " + "{\n\n"
        print(n_element)
        for i in range(n_element):
            c_array += f"0x{self.font_data[i]:02X}"
            if i < n_element - 1:
                c_array += ", "
            if (i + 1) % self.character_w  == 0:
                c_array  += "\n"
                
        c_array += "\n};"
        
        return c_array

    #def export_font(self):
        
        #print()
        
    def print_array(self):    
        
        self.__convert_font_bitmap_to_array()
        print(self.__create_array("test"))
        
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