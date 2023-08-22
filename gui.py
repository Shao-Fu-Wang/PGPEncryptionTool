import tkinter as tk
from tkinter import filedialog
from tkinter.ttk import Separator
import os
from pgp import *
import gui_interface

default_path=os.path.dirname(os.path.realpath(__file__))
encrypt_file_path=""
encrypt_key_path=""
decrypt_pgp_path=""
decrypt_key_path=""
file_extension=""

myPGP = pgp_util()
window = tk.Tk()
window.title("PGP tool")




