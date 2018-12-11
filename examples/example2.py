import tkinter as tk
from tk_html_widgets import HTMLLabel

HTML = """
<p style="text-align: center;">
    <b>
        <a  href="https://www.python.org" style="color:#%02x%02x%02x; font-size:30px">
            www.python.org
        </a>
        <img src="py.png" width=50 height=50>
    </b>
</p>"""

root = tk.Tk()
html_label = HTMLLabel(root, html=HTML % (0, 0, 0), width=50)
html_label.pack(fill="both", expand=True)
html_label.fit_height()

rgb = [0, 0, 0]
i = 0
while True:
    for v in range(256):
        if i == 0:
            rgb[i] = v
        elif i == 1 or i == 2:
            rgb[i] = v
            rgb[i-1] = 255 - v
        elif i == 3:
            rgb[i-1] = 255 - v

        html_label.set_html(HTML % tuple(rgb))
        root.update()
    i += 1
    if i == 4:
        i = 0