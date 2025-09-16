import tkinter as tk
from tkinter import ttk, messaagebox
import qrcode
from PIL import Image, ImageTk


def generate_qrcode():
  url = entry_url.get()
  if not url:
    messagebox.showerror









#create the main window
root = tk.Tk()
root.title("QR Code Generator")
root.geometry("400x500")
root.configure(bg="#f0f4f7")

#URL input
label_url =ttk.Label
