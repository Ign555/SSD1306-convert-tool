# -*- coding: utf-8 -*-

"""
*
*
* SSD1306-Convert-Tool
* Created by Ign555
* Version : v1.0
* File Creation : 22/05/2025
*
*
""" 

"""
*
* Module import
*
"""

##############################-Casuals modules-##############################

import sys

##############################-GUI modules-##############################

import tkinter as tk

##############################-App class modules-##############################

import SSD1306FontConverter as sfc
import SSD1306ImgCoverter as sic

##############################-App GUI class modules-##############################

import MainGUI as mg

"""
*
* Main
*
"""

class SSD1306ConvertionTool(tk.Tk):
        
    def __init__(self):
        
        ##############################-Init converters tool-##############################
        
        self.font_converter = sfc.SSD1306FontConverter()
        self.img_converter = sic.SSD1306ImgCoverter()
        
        ##############################-Init GUI-##############################
        self.font_converter.convert_and_export("tilemap.bmp", 16, 16)
        super().__init__()    
        
        self.main_gui = mg.MainGUI(self)
        
        
        
    
"""
*
* Launch settings
*
"""

if __name__ == "__main__":
    
    app = SSD1306ConvertionTool()
    app.mainloop()

