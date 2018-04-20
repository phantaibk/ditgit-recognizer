# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 16:59:34 2018

@author: Phan Tài
"""

from tabula import read_pdf
df = read_pdf("input/data1.pdf", output_format = "json")
df