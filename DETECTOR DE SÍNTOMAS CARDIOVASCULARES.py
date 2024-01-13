from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("DETECTOR DE SÍNTOMAS CARDIOVASCULARES")
root.geometry("400x400")
root.configure(background="gray49")

Question1_radiobutton = StringVar(value="0")
Question1 = Label(root,text ="¿Experimentas dificultad para respirar durante tus actividades cotidianas?")
Question1.pack()
Question1_r1 = Radiobutton(root, text="Si", variable= Question1_radiobutton, value="Si")
Question1_r1.pack()
Question1_r2 = Radiobutton(root, text="No", variable= Question1_radiobutton, value="No")
Question1_r2.pack()

Question2_radiobutton = StringVar(value="0")
Question2 = Label(root,text ="¿Presentas hinchazón en los pies, tobillos, piernas, abdomen o/y los zapatos te aprietan?")
Question2.pack()
Question2_r1 = Radiobutton(root, text="Si", variable= Question2_radiobutton, value="Si")
Question2_r1.pack()
Question2_r2 = Radiobutton(root, text="No", variable= Question2_radiobutton, value="No")
Question2_r2.pack()

Question3_radiobutton = StringVar(value="0")
Question3 = Label(root,text ="¿Presentas algún síntoma de esta lista o similar: Confusión, Desorientación o pérdida de memoria?")
Question3.pack()
Question3_r1 = Radiobutton(root, text="Si", variable= Question3_radiobutton, value="Si")
Question3_r1.pack()
Question3_r2 = Radiobutton(root, text="No", variable= Question3_radiobutton, value="No")
Question3_r2.pack()

Question4_radiobutton = StringVar(value="0")
Question4 = Label(root,text ="¿Sientes que te falta el aire mientras reposas o estás acostado?")
Question4.pack()
Question4_r1 = Radiobutton(root, text="Si", variable= Question4_radiobutton, value="Si")
Question4_r1.pack()
Question4_r2 = Radiobutton(root, text="No", variable= Question4_radiobutton, value="No")
Question4_r2.pack()

Question5_radiobutton = StringVar(value="0")
Question5 = Label(root,text ="¿Experimentas un silbido o una tos persistente que produce mucosidad blanca o con sangre?")
Question5.pack()
Question5_r1 = Radiobutton(root, text="Si", variable= Question5_radiobutton, value="Si")
Question5_r1.pack()
Question5_r2 = Radiobutton(root, text="No", variable= Question5_radiobutton, value="No")
Question5_r2.pack()

def fever_score():
    score = 0
    if Question1_radiobutton.get() == "Si":
        score = score + 20
        print(score)
        
    if Question2_radiobutton.get() == "Si":
        score = score + 20
        print(score)
        
    if Question3_radiobutton.get() == "Si":
        score = score + 20
        print(score)
    
    if Question4_radiobutton.get() == "Si":
        score = score + 20
        print(score)
        
    if Question5_radiobutton.get() == "Si":
        score = score + 20
        print(score)
        
    if score <=20:
        messagebox.showinfo("Reporte", "Estás bien, más o menos, no es necesario ver a un doctor.")
        
    elif score > 20 and score <= 40:
        messagebox.showinfo("Reporte", "Tal vez debas ver al doctor, mejor vé.")
        
    else:
        messagebox.showinfo("Reporte", "Ok, es serio, vé a un doctor en cuanto puedas.")
        
btn = Button(root, text="Ver resultado", command=fever_score)
btn.pack()


root.mainloop()