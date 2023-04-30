import tkinter as tk

def perfecto():
  
    num = int(entry.get())
    divisors = []
    for i in range(1, num):
        if num % i == 0:
            divisors.append(i)
    if sum(divisors) == num:
        result_label.config(text=f"{num} es un número perfecto.")
    else:
        result_label.config(text=f"{num} no es un número perfecto.")

root = tk.Tk()
root.title("Números perfectos")

label = tk.Label(root, text="Ingrese un número:")
entry = tk.Entry(root)
check_button = tk.Button(root, text="Verificar", bg="#009186", command=perfecto)
result_label = tk.Label(root, text="")

label.pack()
entry.pack()
check_button.pack()
result_label.pack()

root.mainloop()
