import tkinter as tk
import cv2
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
        self.img = Image.fromarray(cv2.resize(cv2.imread("car.png"), (100,100)))
        self.img_tk = ImageTk.PhotoImage(self.img)
        self.img_id = self.canvas.create_image(self.screen_width/2, self.screen_height/2,image= self.img_tk)

if __name__ == "__main__":
    root = tk.Tk()
    project = interface(root)
    project.motion()
    root.mainloop()