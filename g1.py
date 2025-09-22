from color_capture import colorList, getColor, getHex, export_colors_to_file
import tkinter as tk
from tkinter import filedialog, messagebox, Listbox, Entry, Button, END

class ColorCaptureApp:
    def __init__(self, root):
        self.root = root
        root.title("Color Capture Tool")
        self.listbox = Listbox(root)
        self.listbox.pack()
        
        self.export_btn = Button(root, text="Export", command=self.export)
        self.export_btn.pack()

        self.clear_btn = Button(root, text="Clear", command=self.clear)
        self.clear_btn.pack()

        self.exit_btn = Button(root, text="Exit", command=root.quit)
        self.exit_btn.pack()

    def export(self):
        fp = filedialog.asksaveasfilename(defaultextension=".txt")
        if fp:
            export_colors_to_file(fp)
            messagebox.showinfo("Success", f"Colors exported to {fp}")

    def clear(self):
        colorList.clear()
        self.listbox.delete(0, END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ColorCaptureApp(root)
    root.mainloop()
#asdfghjui