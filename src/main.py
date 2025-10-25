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
import argparse

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
        #self.font_converter.convert_and_export("tilemap.bmp", 8, 8)
        #self.img_converter.convert_and_export("tilemap.bmp")
        super().__init__()    
        
        self.main_gui = mg.MainGUI(self)
        
        
        
    
"""
*
* Launch settings
*
"""

if __name__ == "__main__":
    
    # Initialize Application
    app = SSD1306ConvertionTool()
    app.mainloop()

    # Initialize parser
    parser = argparse.ArgumentParser()
    
    parser.add_argument("-w", "--Writer", help = "Select font-writter converter input")
    parser.add_argument("-i", "--Image", help = "Select image converter input")
    parser.add_argument("-o", "--Output", help = "Output file")
    parser.add_argument("-n", "--Name", help = "Array name")
    parser.add_argument("-W", "--Width", help = "Font / Image width")
    parser.add_argument("-H", "--Height", help = "Font / Image Height")
    parser.add_argument("-I", "--Invert", help = "B/W Invert", action="store_true")
    
    #Get Argument
    args = parser.parse_args()
    
    output = ""
    name = ""
    invert = False
    
    if args.Output:
        output = args.Output
    else:
        output = "data.c"
    
    if args.Name:
        name = args.Name
    else:
        name = "data"
     
    if args.Invert:
        invert = True
     
    if args.Writer:
        
        print("Converting the font map...")
        
        if args.Width and args.Height:
            app.font_converter.convert_and_export(args.Writer, int(args.Width), int(args.Height), invert=invert, array_name=name, export_path=output)
        else:
            print("Size must be given")
        
        
    if args.Image:
        
        print("Converting the image...")
        
        if args.Width and args.Height:
            app.img_converter.convert_and_export(args.Image, int(args.Width), int(args.Height), invert=invert, array_name=name, export_path=output)
        else:
            app.img_converter.convert_and_export(args.Image, array_name=name, export_path=output)
        
        