import os
from wand.image import Image
import subprocess

def Resize():
    maxSize = 4096
    
    path = os.path.dirname(os.path.abspath(__file__))
    folders = os.listdir(path)[:-1]
    for folder in folders:
        folderFiles = os.listdir(path+"\\"+folder)
        files = [folder + "\\" + file for file in folderFiles]
        # print(files)
        files = [file for file in files if ".bin" not in file]
        files = [file for file in files if "Biomes" not in file]
        files = [file for file in files if "Height" not in file]
        files = [file[:-4] for file in files]
        
        # with open(file = "OversizeList.txt", mode='w') as txt:
        for file in files:
            with Image(filename = file+".dds") as img:
                if img.width > maxSize:
                    print(file)
                    # DDS_Type = img.compression
                    # print("Over maxSize, exporting to png")
                    # img.resize(maxSize, int(maxSize/2))
                    # img.save(filename=file+".tif")
                    # # 15 -> DXT1
                    # # 18 -> DXT5
                    # # 19 -> DXT5_nm
                    # subprocess.run(f"nvtt_export {file}.tif -o {file}2.dds -f 15",shell=False)
                        
    
    
    
Resize()