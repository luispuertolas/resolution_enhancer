import cv2
import numpy as np
from tkinter import filedialog
from tkinter import Tk
from PIL import Image

def load_image():
    root = Tk()
    root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    root.withdraw()
    return cv2.imread(root.filename)

def save_image(image):
    root = Tk()
    f = filedialog.asksaveasfile(mode='w', defaultextension=".png")
    if f is None: 
        return
    im_pil = Image.fromarray(image)
    im_pil.save(f.name)
    root.withdraw()

def upscale_image(image, scale):
    width = int(image.shape[1] * scale)
    height = int(image.shape[0] * scale)
    dim = (width, height)
    resized = cv2.resize(image, dim, interpolation=cv2.INTER_CUBIC)
    return resized

def main():
    # Load image
    image = load_image()

    # Upscale image
    upscale_factor = 16
    upscaled_image = upscale_image(image, upscale_factor)

    # Save image
    save_image(upscaled_image)

if __name__ == "__main__":
    main()
