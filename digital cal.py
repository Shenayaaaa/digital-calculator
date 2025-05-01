import tkinter as tk

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(str(screen.get()))
            screen.set(result)
        except Exception:
            screen.set("Error")
    elif text == "C":
        screen.set("")
    else:
        screen.set(screen.get() + text)

# Create main window
root = tk.Tk()
root.title("Colorful Digital Calculator")
root.geometry("400x550")
root.config(bg="#1f1f1f")  # Dark background

# Entry screen
screen = tk.StringVar()
entry = tk.Entry(root, textvar=screen, font="Arial 24 bold", bd=10, relief=tk.FLAT,
                 justify=tk.RIGHT, bg="#2c2c2c", fg="#ffffff", insertbackground="white")
entry.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)

# Button colors
button_bg = "#3a3a3a"
operator_bg = "#ff9800"
equal_bg = "#4caf50"
clear_bg = "#f44336"
button_fg = "#ffffff"

# Buttons layout
button_texts = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"]
]

for row in button_texts:
    frame = tk.Frame(root, bg="#1f1f1f")
    frame.pack(expand=True, fill="both")
    for btn_text in row:
        color = button_bg
        if btn_text in {"+", "-", "*", "/"}:
            color = operator_bg
        elif btn_text == "=":
            color = equal_bg
        elif btn_text == "C":
            color = clear_bg

        btn = tk.Button(
            frame, text=btn_text, font="Arial 20", fg=button_fg,
            bg=color, activebackground="#5e5e5e", relief=tk.FLAT
        )
        btn.pack(side="left", expand=True, fill="both", padx=1, pady=1)
        btn.bind("<Button-1>", click)

root.mainloop()
