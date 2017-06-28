# -*- coding: utf-8 -*-

from PIL import Image
import tkinter as tk
from IPython.display import display

root = tk.Tk()
root.withdraw()

def merge_images(file1, file2, file3, file4):
    """Merge two images into one, displayed side by side
    :param file1: path to first image file
    :param file2: path to second image file
    :return: the merged Image object
    """
    image1 = Image.open(file1)
    image2 = Image.open(file2)
    image3 = Image.open(file3)
    image4 = Image.open(file4)

    (width1, height1) = image1.size
    (width2, height2) = image2.size
    (width3, height3) = image3.size
    (width4, height4) = image4.size

    result_width = width1 + width2 + width3 + width4
    result_height = max(height1, height2, height3, height4)

    result = Image.new('RGB', (result_width, result_height))
    result.paste(im=image1, box=(0, 0))
    result.paste(im=image2, box=(width1, 0))
    result.paste(im=image3, box=(width1 + width2, 0))
    result.paste(im=image4, box=(width1 + width2 + width3, 0))
    
    print("merge_images completed")
    display(result)
    return result

file1 = tk.filedialog.askopenfilename()
file2 = tk.filedialog.askopenfilename()
file3 = tk.filedialog.askopenfilename()
file4 = tk.filedialog.askopenfilename()


merge_images(file1, file2, file3, file4)