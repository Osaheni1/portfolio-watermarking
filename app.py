from tkinter import *
from PIL import Image, ImageDraw, ImageFont, ImageTk
from os import listdir

#------------read the following before proceeding---------------#
#make sure image size is not more than 1000 x 1000 in size or else some part of you image won't display in canvas
#logo size should not be more than 50 x 50 in size
#logo to should be saved in logo folder
#images be watermareked should be saved in img folder
#---------------------------------------------------------------------#

#------------ logo and text watermarking function ---------
def loadImages():
    path = "img/"
    imagesList = listdir(path)
    loadedImages = []
    for image in imagesList:
         img = Image.open(path + image)
         loadedImages.append(img)

    #loading up image from LoadedImage list using the spinbox output
    img = loadedImages[int(spinbox.get())]
    width, height = img.size

    #watermarking text Text input from Entry
    draw = ImageDraw.Draw(img)
    text = f"{entry.get()}"

    font = ImageFont.truetype('arial.ttf', 36)
    textwidth, textheight = draw.textsize(text, font)

    #get the width and height for the logo
    logo = Image.open("logo/logo.png")
    lwidth, lheight = logo.size

    # calculate the x,y coordinates of the text
    margin = 10
    x = width - textwidth - margin
    y = height - textheight - margin - 20

    #logo positioning on the base image
    lx = width - textwidth - margin -10- lwidth
    ly = height - lheight - 10

    # draw watermark in the bottom right corner
    draw.text((x, y), text, ('red'), font=font)
    logo = Image.open("logo/logo.png")

    img.paste(logo, (lx, ly))

    # Save watermarked image
    img.save(f'watermark/{int(spinbox.get())}.png')

    entry.delete(0, END)
    entry.insert(0, string="Saving...")
    #delay canvas for 2sec then run sas() function
    canvas.after(2000, sas)

#display watermarked image function
def sas():
    global watermarked_image
    path = "watermark/"
    imagesList = listdir(path)
    loadedmaker = []
    for image in imagesList:

        loadedmaker.append(image)
    watermarked_image = PhotoImage(file=f'{path}{loadedmaker[int(spinbox.get())]}')
    canvas.itemconfig(imag, image=watermarked_image)
    entry.delete(0, END)

#select next image function
def spinbox_used():
    next_image = tom_img[int(spinbox.get())]
    canvas.itemconfig(imag, image=next_image)





#------------Creating a new window and configurations---------------
window = Tk()
window.title("Widget Examples")

#creating canvas on the window
path = "img/"
imagesList = listdir(path)
tom_img = []
for img in imagesList:
    ne = PhotoImage(file=f"{path}{img}")
    tom_img.append(ne)

canvas = Canvas(width=1000, height=700, highlightthickness=0)
imag = canvas.create_image(500, 350, image=tom_img[0])
canvas.grid(column=1, row=2)

#spinbox for selection of image
spinbox = Spinbox(from_=0, to=len(tom_img)-1, width=5, command=spinbox_used)
spinbox.grid(column=0, row=0)

#calls leadImage() when pressed
button = Button(text="Add Watermark", command=loadImages)
button.grid(column=1, row=1)

#Enter the watermark text
entry = Entry(width=30)
entry.insert(END, string="input your waternmake text")
entry.grid(column=1, row=0)

window.mainloop()

