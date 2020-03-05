from tkinter import *

window = Tk()

window.title("Générateur de mot de passe")
window.geometry("720x480")
window.minsize(480, 360)
window.iconbitmap("password.ico")
window.config(background="#4065A4")

#creer la frame principale
frame = Frame(window, bg='#4065A4')

# creation d'image
width = 300
height = 300
image = PhotoImage(file="password_onbording.png").zoom(35).subsample(80)
canvas = Canvas(frame, width=width, height=height, bg='#4065A4', bd=0, highlightthickness=0)
canvas.create_image(width/2, height/2, image=image)
canvas.grid(row=0, column=0, sticky=W)

#creer une sous boite
right_frame = Frame(frame, bg='#4065A4')

#creer un titre
label_title = Label(right_frame, text="Mot de passe", font=("Helvetica", 20), bg="#4065A4", fg='white')
label_title.grid(row=0,column=1,sticky=W)

# creer un champs/entr
password_entry = Entry(right_frame, font=("Helvetica", 20), bg="#4065A4", fg='white')
password_entry.pack()

# on place la sous boite à droite de la frame principal
right_frame.grid(row=0, column=1, sticky=W)

# afficher la frame
frame.pack(expand=YES)

# afficher la fenetre
window.mainloop()
