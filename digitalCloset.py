import tkinter as tk
from tkinter import messagebox
import sqlite3
import random

class DigitalClosetApp:
    def __init__(self, root):
        self.root = root
        self.root.title(" Digital closet App")
        # connect 2 the database
        self.conn =sqlite3.connect('closet.db')
        self.cur = self.conn.cursor()
        self.create_table()
            
        self.style_label = tk.label(root,text="select:")
        self.style_label.pack()
        self.style_var= tk.StringVar(root)
        self.style_var.set("Casual") # this will be the default style
        self.style_dropdown = tk.optionMenu(root, self.style_var, "Casual", "Formal", "Gothic","Biker", "Formal","earthy","tomboy")
        self.style_dropdown.pack()

        self.add_clothes_button = tk.Button(root, text="Add Clothes",command=self.add_clothes)
        self.add_clothes_button.pack()

        self.creat_outfit_button =tk.Button(root, text="Create Outfit", command=self.create_outfit)
        self.create_outfit_button.pack()

    def create_table(self):
        self.cur.execute(''' CREATE TABLE IF NOT EXISTS clothes
                         (id INTERGER PRIMARY KEY,
                         name TEXT,
                         style TEXT)
                         ''')
        self.conn.commit()

    def add_clothes(self):
        name = tk.simpledialog.askstring("Enter Clothes", "Enter name of clothing item :")
        style=self.style_var.get()
        if name:
            self.cur.execute("INSERT INTO clothes(name,style) VALUE(? ,?)",(name ,style))
            self.conn.commit()
            messagebox.showinfo("sucess", "Clothing item added successfully!")

    def get_clothes(self,style):
        self.cur.execute("SELLECT name FROM clothes WHERE style=?",(style,))
        return self.cur.fetchall()

    def create_outfit(self):
     style =self. style_var.get()
     clothes = self.get_clothes(style)
     if clothes:
        outfit = random.choice(clothes)
        messagebox.showinfo("Your Outfit for today",f"You show wear:{outfit[0]}")
     else:
        messagebox.showwarning("No Clothes Found","No clothes for the selected style .")

if __name__=="__main__":
    root=tk.Tk()
    app= DigitalClosetApp(root) 
    root.mainloop()       
             