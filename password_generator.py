from tkinter import *

window = Tk()

window.title("My Application")
window.geometry("720x480")
window.minsize(480, 360)
window.iconbitmap("scum.ico")
window.config(background="#4065A4")

frame = Frame(window, bg='#4065A4')

# creation d'image
width = 300
height = 300
image = PhotoImage(file="password_onbording.png").zoom(35).subsample(80)
canvas = Canvas(window, width=width, height=height, bg='#4065A4')
canvas.create_image(width/2, height/2, image=image)
canvas.pack(expand=YES)

# creer un titre
label_title = Label(frame, text="Mot de pass", font=("Helvetica", 20), bg="#4065A4", fg='white

# afficher la frame
frame.pack(expand=YES)

# afficher la fenetre
window.mainloop()
