import os
import cairosvg

for file in os.listdir('.'):
    name = file.split('.svg')[0]
    cairosvg.svg2png(url=name+'.svg',write_to=name+'.png',output_width=128,output_height=128) 
