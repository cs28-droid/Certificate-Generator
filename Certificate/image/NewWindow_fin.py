from PIL import Image, ImageDraw, ImageFont
from tkinter import *
from tkinter import filedialog
import PIL
import os
import pandas as pd

root = Tk()
root.geometry("500x500")
root.title("Certificate Form")
heading = Label(text="Certificate Form", bg="grey", fg="black", width="500", height="3")
heading.pack()

df = pd.read_csv('Book1.csv')
font = ImageFont.truetype('arial.ttf', 60)


def first_win():
    title = Label(text="Certificate Title * (Eg: School of Hard Knocks)")
    title2 = Label(text="Certificate Action * (Eg: THIS DIPLOMA IS PRESENTED TO)")
    name = Label(text="Name *")
    reason = Label(text="Certificate Reason * (Eg: For graduating with honors)")
    date = Label(text="Date *")

    title.place(x=15, y=70)
    title2.place(x=15, y=140)
    name.place(x=15, y=210)
    reason.place(x=15, y=280)
    date.place(x=15, y=350)

    title_text1 = StringVar()
    title2_text1 = StringVar()
    name_text1 = StringVar()
    reason_text1 = StringVar()
    Date1 = StringVar()

    title_entry1 = Entry(textvar=title_text1, width="40")
    title2_entry1 = Entry(textvar=title2_text, width="40")
    name_entry1 = Entry(textvar=name_text, width="40")
    reason_entry1 = Entry(textvar=reason_text, width="40")
    Date1 = Entry(textvar=Date, width="40")

    title_entry.place(x=15, y=100)
    title2_entry.place(x=15, y=170)
    name_entry.place(x=15, y=240)
    reason_entry.place(x=15, y=310)
    Date.place(x=15, y=380)


def save_certificate():
    first_win()
    title_info = title_text.get()
    title2_info = title2_text.get()
    name_info = name_text.get()
    reason_info = reason_text.get()
    date_info = Date.get()

    draw = PIL.ImageDraw.Draw(photo)

    font_type1 = ImageFont.truetype('Algerian.ttf', 28)
    font_type2 = ImageFont.truetype('Arial.ttf', 20)
    font_type3 = ImageFont.truetype('ChevinBold.ttf', 40)
    font_type4 = ImageFont.truetype('Arial.ttf', 22)
    font_type5 = ImageFont.truetype('Arial.ttf', 18)

    draw.text((100, 100), title_info.upper(), font=font_type1)
    draw.text((190, 145), title2_info.upper(), font=font_type2)
    draw.text((160, 225), name_info.upper(), font=font_type3)
    draw.text((90, 305), reason_info.upper(), font=font_type4)
    draw.text((230, 355), date_info.upper(), font=font_type5)

    label1 = Label(text=title_info.upper(), font="Times 18", fg="green", anchor=S, justify=CENTER).place(x=694, y=175)
    label2 = Label(text=title2_info.upper(), font=50, fg="green").place(x=780, y=220)
    label3 = Label(text=name_info.upper(), font=100, fg="green").place(x=820, y=300)
    label4 = Label(text=reason_info, font="Times 18", fg="green").place(x=780, y=380)
    label5 = Label(text=date_info, font=30, fg="green").place(x=865, y=450)


def download():
    PIL.Image._show(photo)
    file = filedialog.asksaveasfile(mode='w', defaultextension=".png",filetypes=(("PNG file", "*.png"), ("All Files", "*.*")))

    if file:
        abs_path = os.path.abspath(file.name)
        photo.save(abs_path)


def multiple():
    font2 = ImageFont.truetype('arial.ttf', 60)
    font1 = ImageFont.truetype('Algerian.ttf', 60)
    for index, j in df.iterrows():
        img = PIL.Image.open('blank.jpg')
        draw = PIL.ImageDraw.Draw(img)
        draw.text(xy=(735, 600), text='{}'.format(j['name']), fill=(0, 0, 0), font=font1)
        draw.text(xy=(725, 835), text='Graduating with honors', fill=(0, 0, 0), font=font2)
        draw.text(xy=(320, 1050), text='11th October, 2020', fill=(0, 0, 0), font=font2)
        img.save('pictures/{}.jpg'.format(j['name']))

        save = Label(text="Certificates are generated and saved in pictures folder.")
        save.place(x=750, y=900)


def clear():
    title_entry.delete(0, END)


def clear1():
    title2_entry.delete(0, END)


def clear2():
    name_entry.delete(0, END)


def clear3():
    reason_entry.delete(0, END)


def clear4():
    Date.delete(0, END)


photo = PIL.Image.open('certifactenew.png')
photo1 = PhotoImage(file='certifactenew.png')
template = Label(root, image=photo1)
template.place(x=600, y=100)

title_text = StringVar()
title2_text = StringVar()
name_text = StringVar()
reason_text = StringVar()
Date = StringVar()

title_entry = Entry(textvar=title_text, width="40")
title2_entry = Entry(textvar=title2_text, width="40")
name_entry = Entry(textvar=name_text, width="40")
reason_entry = Entry(textvar=reason_text, width="40")
Date = Entry(textvar=Date, width="40")


enter = Button(text="Generate Certificate", width="40", height="2", command=save_certificate, bg="grey")
enter.place(x=15, y=450)

clearall = Button(text="clear text", width="10", height="1", command=clear, bg="grey")
clearall.place(x=275, y=95)
clearall1 = Button(text="clear text", width="10", height="1", command=clear1, bg="grey")
clearall1.place(x=275, y=165)
clearall2 = Button(text="clear text", width="10", height="1", command=clear2, bg="grey")
clearall2.place(x=275, y=235)
clearall3 = Button(text="clear text", width="10", height="1", command=clear3, bg="grey")
clearall3.place(x=275, y=305)
clearall4 = Button(text="clear text", width="10", height="1", command=clear4, bg="grey")
clearall4.place(x=275, y=375)

SC = Button(root, text="Single Certificate", width="20", height="2", command=first_win).place(x=775, y=800)
MC = Button(root, text="Multiple Certificates", width="20", height="2", command=multiple).place(x=950, y=800)

button = Button(root, text="Download Certificate", width="40", height="2", command=download, bg="grey").place(x=775,y=600)


text_box = Text()

root.mainloop()
