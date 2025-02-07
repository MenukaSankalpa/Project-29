from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root=Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False,False)

#search box
search_image=PhotoImage(file=r"Weatherapp\search.png")
myimage=Label(image=search_image)
myimage.place(x=20,y=20)

textfield=tk.Entry(root,justify="center",width="17",font=("poppins",25,"bold"),bg="#404040",border=0,fg="white")
textfield.place(x=50, y=40)
textfield.focus()

search_icon=PhotoImage(file=r"Weatherapp\search_icon.png")
myimage_icon=Label(image=search_icon,borderwidth=0,cursor="hand2",bg="#404040")
myimage_icon.place(x=400,y=34)

#logo
Logo_image=PhotoImage(file=r"Weatherapp\logo.png")
logo=Label(image=Logo_image)
logo.place(x=150,y=100)

#bottombox

Frame_image=PhotoImage(file=r"Weatherapp\box.png")
frame_myimage=Label(image=Frame_image)
frame_myimage.pack(padx=5,pady=5,side=BOTTOM)

#label
label1=Label(root,text="Wind",font=("Helvetica",15,"bold"),fg="white",bg="#1ab5ef")
label1.place(x=120,y=400)

label2=Label(root,text="Humidity",font=("Helvetica",15,"bold"),fg="white",bg="#1ab5ef")
label2.place(x=250,y=400)

label3=Label(root,text="Description",font=("Helvetica",15,"bold"),fg="white",bg="#1ab5ef")
label3.place(x=430,y=400)

label4=Label(root,text="Pressure",font=("Helvetica",15,"bold"),fg="white",bg="#1ab5ef")
label4.place(x=650,y=400)

root.mainloop()