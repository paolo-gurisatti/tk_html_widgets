import tkinter as tk
from tk_html_widgets import HTMLLabel

root = tk.Tk()
text = HTMLLabel(root)
text.pack(fill="both", expand=True)
text.set_html('<h1 style="color: red; text-align: center"> Hello World </H1>')
text.fit_height()
root.mainloop()