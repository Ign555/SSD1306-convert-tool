# -*- coding: utf-8 -*-

"""
*
*
* SSD1306-Convert-Tool
* Created by Ign555
* Version : v1.0
* File Creation : 24/05/2025
*
*
""" 

"""
*
* Module import
*
"""

##############################-GUI modules-##############################

import tkinter as tk

"""
*
* MainGUI class
*
"""

class MainGUI(tk.Frame):
    
    def __init__(self, app):
        
        ##############################-Class init and property-##############################   
        
        super().__init__(app)
        
        self.app = app
        
        ##############################-Make GUI-##############################   
        
        