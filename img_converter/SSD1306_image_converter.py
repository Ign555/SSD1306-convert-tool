################################################################
#
#
# SSD1306 image array creator
# Created by Ign555
# Version : v0.9
# File Creation : 18/04/2025
#
#
################################################################

from PIL import Image

class SSD1306Img:
    
    def __init__(self, path, w, h, screen_height=64):
        
        self.screen_height = screen_height
        
        self.img = Image.open(path).convert('1') #Convert image to black & white
        img_width, img_height = self.img.size #Get image size
        
        #Check if the desired image size is valid
        if w > 128 or h > screen_height: 
            exit(0)
        
        #Resize image
        self.h = h 
        self.w = w
        self.img = self.img.resize((w, h))  #Resize to the desired img format
     
    def __convert_image_to_array(self):
        
        self.image_data = []
        pixels = self.img.load() #Read image content

        for page in range (0, self.h, 8):
            for column in range(self.w):
                byte = 0
                for bit in range(8):
                    y = page + bit
                    if pixels[column, page] != 0:
                        byte |= (1 << bit)
                    self.image_data.append(byte)

    def __create_array(self, array_name):
        
        n_pixel = self.w * int(self.h/8)
        c_array = f"uint8_t {array_name}[{n_pixel}] = " + "{\n\n"
        
        for i in range(n_pixel):
            c_array += f"0x{self.image_data[i]:02X}"
            if i < n_pixel - 1:
                c_array += ", "
            if (i + 1) % self.w == 0:
                c_array  += "\n"
                
        c_array += "\n};"
            
        return c_array
        
    def __export_array(self, export_path, array_name):
        
        f = open(export_image, "w")
        f.write(self.__create_array(array_name))
    
    def export_image(self, export_path="", array_name="image_data"):
        
        self.__convert_image_to_array(self)
        self.__export_array(self, export_path, array_name)
        
    def print_array(self, array_name="image_data"):
        
        self.__convert_image_to_array()
        print(self.__create_array(array_name))

"""           
# Example
img = SSD1306Img("image.png", 32, 32, 32)
img.print_array()
"""

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