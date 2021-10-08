import io
from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage
from Links import *
from PIL import Image, ImageTk
from urllib.request import urlopen

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("assets")


def relative_to_assets(path: str) -> Path:
    url = str(ASSETS_PATH / Path(path))
    url = url.replace('\\', '/')
    url = url.replace(':/', '://', 1)
    print(url)
    link = urlopen(url)
    rawimg = io.BytesIO(link.read())
    img = Image.open(rawimg)
    return img


window = Tk()

window.geometry("560x562")
window.configure(bg="#FF867F")
window.title("Phoebus Links")
window.iconphoto(True, ImageTk.PhotoImage(relative_to_assets('icon.png')))

canvas = Canvas(
    window,
    bg="#FF867F",
    height=312,
    width=560,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)

image_image_1 = ImageTk.PhotoImage(relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    279.99999999999994,
    156.0,
    image=image_image_1
)

image_image_2 = ImageTk.PhotoImage(relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    114.99999999999994,
    144.0,
    image=image_image_2
)

image_image_3 = ImageTk.PhotoImage(relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    285.99999999999994,
    244.0,
    image=image_image_3
)

image_image_4 = ImageTk.PhotoImage(relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    285.99999999999994,
    347.0,
    image=image_image_4
)

image_image_5 = ImageTk.PhotoImage(relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    205.99999999999994,
    473.0,
    image=image_image_5
)

image_image_6 = ImageTk.PhotoImage(relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    118.99999999999994,
    480.0,
    image=image_image_6
)

image_image_7 = ImageTk.PhotoImage(relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    288.99999999999994,
    480.0,
    image=image_image_7
)

button_image_1 = ImageTk.PhotoImage(relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: Comunicacao(),
    relief="flat"
)
button_1.place(
    x=37.99999999999994,
    y=134.0,
    width=154.0,
    height=44.0
)

button_image_2 = ImageTk.PhotoImage(relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: psPhoebus(),
    relief="flat"
)
button_2.place(
    x=36.99999999999994,
    y=234.0,
    width=178.0,
    height=44.0
)

button_image_3 = ImageTk.PhotoImage(relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: psPrisma(),
    relief="flat"
)
button_3.place(
    x=218.99999999999994,
    y=234.0,
    width=179.0,
    height=44.0
)

button_image_4 = ImageTk.PhotoImage(relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: awsPrisma(),
    relief="flat"
)
button_4.place(
    x=400.99999999999994,
    y=234.0,
    width=134.0,
    height=44.0
)

button_image_5 = ImageTk.PhotoImage(relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: bsC(),
    relief="flat"
)
button_5.place(
    x=36.99999999999994,
    y=337.0,
    width=178.0,
    height=44.0
)

button_image_6 = ImageTk.PhotoImage(relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: ocS(),
    relief="flat"
)
button_6.place(
    x=218.99999999999994,
    y=337.0,
    width=179.0,
    height=44.0
)

button_image_7 = ImageTk.PhotoImage(relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: cpA(),
    relief="flat"
)
button_7.place(
    x=400.99999999999994,
    y=337.0,
    width=134.0,
    height=44.0
)

button_image_8 = ImageTk.PhotoImage(relative_to_assets("button_8.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: gSkins(),
    relief="flat"
)
button_8.place(
    x=47.99999999999994,
    y=470.0,
    width=134.0,
    height=44.0
)

button_image_9 = ImageTk.PhotoImage(relative_to_assets("button_9.png"))
button_9 = Button(
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: kVersions(),
    relief="flat"
)
button_9.place(
    x=217.99999999999994,
    y=470.0,
    width=134.0,
    height=44.0
)

canvas.create_text(
    430.0,
    10.0,
    anchor="nw",
    text="Versão: 1.2 - 08/10/21",
    fill="#828282",
    font=("Poppins Medium", 12 * -1)
)

window.resizable(False, False)
window.mainloop()
