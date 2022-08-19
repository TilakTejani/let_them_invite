from pdf2image import convert_from_path 
import pandas as pd
from PIL import Image, ImageFont, ImageDraw
import time

import util

#DECLARE CONSTANTS
POPPLER_PATH = "poppler-0.68.0\\bin"
DPI = 240
FONT = ImageFont.truetype('C:\\Windows\\Fonts\\COOPBL.ttf', 75)
COLOR_FOR_TEXT = (231, 175, 71)
DIR_LIST=["img_src","edited_images","saved_pdfs"]

def pdftopil(PDF_PATH):
    # converts pdf to images
    start_time = time.time()
    pil_images = convert_from_path(PDF_PATH, dpi=DPI, fmt="jpg", poppler_path=POPPLER_PATH)
    print ("Time taken : " + str(time.time() - start_time))
    return pil_images
    
def save_pil_images(pil_images):
    #This method helps in converting the images in PIL Image file format to the required image format
    for i, image in enumerate(pil_images):
        image.save("img_src\\page_" + str(i + 1) + ".jpg")
    

def edit_images(name, POS_FOR_PAGES):
    # editing images to write names
    for i, POS in enumerate(POS_FOR_PAGES):
        img = Image.open(f"img_src\\page_{i+1}.jpg")
        draw = ImageDraw.Draw(img)
        if(POS[0]!=-1 and POS[1]!=-1):
            draw.text(POS, name, COLOR_FOR_TEXT, font=FONT)
        img.save(f"edited_images\\page_{i+1}.jpg")
    

def convert_images_to_pdf(name, NO_OF_PAGES):
    # creating pdfs from saved images
    img_list = [Image.open(f"edited_images\\page_{i+1}.jpg") for i in range(NO_OF_PAGES)]
    im = [img.convert('RGB') for img in img_list]
    im[0].save(f"saved_pdfs\\{name}.pdf",save_all=True,append_images=im[1:])

def edit_pdfs(name_list, LOCS):
    # editing pdfs
    for index, rows in name_list.iterrows():
        edit_images(rows['Name'], LOCS)
        convert_images_to_pdf(rows['Name'], len(LOCS))

def create_pdfs(PDF_PATH, CSV_PATH, LOCS):
        for dir in DIR_LIST:
            util.create_dirs(dir)
        PIL_IMAGES = pdftopil(PDF_PATH)
        save_pil_images(PIL_IMAGES)
        df = pd.read_csv(CSV_PATH, index_col="Index")
        edit_pdfs(df, LOCS)
