import tkinter as tk

def submit():
    with open("info.txt", "a") as f:
        f.write(f"Name: {name_entry.get()}\n")
        f.write(f"Address: {address_entry.get()}\n")
        f.write(f"Birthdate: {birthdate_entry.get()}\n")
        f.write(f"Phone: {phone_entry.get()}\n")
        f.write(f"Age: {age_entry.get()}\n\n")
    print("Saved to info.txt")

root = tk.Tk()

name_entry = tk.Entry(root)
name_entry.pack()
address_entry = tk.Entry(root)
address_entry.pack()
birthdate_entry = tk.Entry(root)
birthdate_entry.pack()
phone_entry = tk.Entry(root)
phone_entry.pack()
age_entry = tk.Entry(root)
age_entry.pack()

tk.Button(root, text="Submit", command=submit).pack()

root.mainloop()
