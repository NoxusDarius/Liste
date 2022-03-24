import tkinter as tk
from doppel import ausgabe as aus, Arraylist as array, LinkedList as link, befuellen_linked as beli, befuellen_array as bear, werte_erstellen as we
root = tk.Tk()
link = link()
array = array()
status = True


def clear():
    global status
    status = True
    link.display()
    link.clear_list()
    print("Hallo")


def print_Hallo():
    global status
    print(status)

    if(status is True and (len(e1.get()) != 0) and e1.get().isnumeric()):
        status = False

        print(e1.get())
        x = we(int(e1.get()))
        aus()
        beli(x, link)
        bear(x, array)
        lasc = link.sortASC()
        ldesc = link.sortDESC()
        aasc = array.sortASC()
        adesc = array.sortDESC()
        labelasc = tk.Label(
            root, text="Linked List aufsteigend", bg="#ffffff", fg="black")
        label2 = tk.Label(root, text='{:5.3f}s'.format(
            lasc), bg="#ffffff", fg="black")
        labeldesc = tk.Label(
            root, text="Linked List absteigend", bg="#ffffff", fg="black")
        label3 = tk.Label(root, text='{:5.3f}s'.format(
            ldesc), bg="#ffffff", fg="black")
        labelaasc = tk.Label(root, text="List aufsteigend",
                             bg="#ffffff", fg="black")
        label4 = tk.Label(root, text='{:5.3f}s'.format(
            aasc), bg="#ffffff", fg="black")
        labeladesc = tk.Label(root, text="List absteigend",
                              bg="#ffffff", fg="black")
        label5 = tk.Label(root, text='{:5.3f}s'.format(
            adesc), bg="#ffffff", fg="black")
        label2.grid(row=3, column=3, padx='5', pady='5', sticky='ew')
        label3.grid(row=4, column=3, padx='5', pady='5', sticky='ew')
        label4.grid(row=5, column=3, padx='5', pady='5', sticky='ew')
        label5.grid(row=6, column=3, padx='5', pady='5', sticky='ew')
        labelasc.grid(row=3, column=2, padx='5', pady='5', sticky='ew')
        labeldesc.grid(row=4, column=2, padx='5', pady='5', sticky='ew')
        labelaasc.grid(row=5, column=2, padx='5', pady='5', sticky='ew')
        labeladesc.grid(row=6, column=2, padx='5', pady='5', sticky='ew')

    else:
        print("Es ist nichts eingegeben")


root.minsize(width=1200, height=700)
root.maxsize(width=900, height=500)
label1 = tk.Label(root, text="Eingabe Zahlen", bg="#ffffff", fg="black")
label1.grid(row=0, column=2, padx='5', pady='5', sticky='ew')

root.resizable(width=True, height=True)
schalt1 = tk.Button(root, text="Sort", command=print_Hallo)
schalt2 = tk.Button(root, text="Clear List", command=clear)

e1 = tk.Entry(root)
e1.grid(row=0, column=3)
schalt1.grid(row=2, column=2)
schalt2.grid(row=2, column=3)


root.mainloop()

print("Hat Funktioniert")
