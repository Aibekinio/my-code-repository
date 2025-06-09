import tkinter as tk

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(str(screen.get()))
            screen.set(result)
        except:
            screen.set("Error")
    elif text == "C":
        screen.set("")
    else:
        screen.set(screen.get() + text)


root = tk.Tk()
root.title("Калькулятор")
root.geometry("300x300")


screen = tk.StringVar()
entry = tk.Entry(root, textvar=screen, font=("Arial", 20), justify='right')
entry.pack(fill="x", padx=10, pady=10)


buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"]
]

for row in buttons:
    frame = tk.Frame(root)
    frame.pack(expand=True, fill="both")
    for text in row:
        btn = tk.Button(frame, text=text, font=("Arial", 18), relief="ridge", border=1)
        btn.pack(side="left", expand=True, fill="both")
        btn.bind("<Button-1>", click)

root.mainloop()
