from tkinter import *
def draw_point(canvas,center,radius,color):
    x, y = center
    canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill=color)

window = Tk()
window.title("Canvas")
window.geometry("500x500")
mycan = Canvas(window, width=300, height=300, bg="blue",bd="12",relief="groove")
mycan.pack(pady=20)
center = (150, 100)
radius = 5
color ="red"
draw_point(mycan, center, radius, color)
window.mainloop()