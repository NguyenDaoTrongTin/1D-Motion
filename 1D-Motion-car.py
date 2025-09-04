import tkinter as tk
import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageTk, ImageFont, ImageDraw, ImageGrab


class interface:
    def __init__(self, root):
        self.root = root
        self.root.title("Motion of car")
        self.root.geometry("600x400")
        self.screen_height = root.winfo_screenheight()
        self.screen_width = root.winfo_screenwidth()
        self.canvas = tk.Canvas(root, height=self.screen_height, width=self.screen_width)
        self.canvas.pack()

    def motion(self):
        self.img = Image.fromarray(cv2.resize(cv2.imread("car_rgba.png", cv2.IMREAD_UNCHANGED), (100,100)))
        self.img_flip = Image.fromarray(cv2.flip(np.array(cv2.resize(cv2.imread("car_rgba.png", cv2.IMREAD_UNCHANGED), (100,100))), 1))
        self.img_tk = ImageTk.PhotoImage(self.img)
        self.img_id = self.canvas.create_image(self.screen_width/2, self.screen_height/2,image= self.img_tk)

        self.cordinate_x = self.canvas.create_line(30, 10, 10, 30, 50, 30, 30, 10, 30, 310, 430, 310, 410, 290, 410, 330, 430, 310)
        self.canvas.create_polygon(30, 10, 10, 30, 50, 30, fill= "black", outline= "black")
        self.canvas.create_polygon(430, 310, 410, 290, 410, 330, fill= "black", outline= "black")
        self.canvas.create_text(20, 320, fill= "black", font= ("Times New Roman", 15), text= "O")

        y0 = 305
        y1 = 315
        for i in range(80, 401, 50):
            self.canvas.create_line(i, y0, i, y1)
            self.canvas.create_text(i, 330, fill= "black", font= ("Times New Roman", 10), text= f"{i-30}")

        x0 = 25
        x1 = 35
        for y in range(260, 11, -50):
            self.canvas.create_line(x0, y, x1, y)
            self.canvas.create_text(15, y, fill= "black", font= ("Times New Roman", 10), text= f"{310-y}")

if __name__ == "__main__":
    root = tk.Tk()
    project = interface(root)
    project.motion()
    root.mainloop()