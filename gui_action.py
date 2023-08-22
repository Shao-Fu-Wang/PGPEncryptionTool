import tkinter as tk
from gui import *
import gui_interface
from tkinter import filedialog

def print_to_text_log(text):
    gui_interface.text_log.insert(tk.END, text + '\n')

def on_button_name_set_click():
    myKey = myPGP.make_key(gui_interface.entry_name.get())
    print_to_text_log("Make key success!")
    myPGP.export_key(myKey, gui_interface.entry_name.get())
    print_to_text_log("Export key success!")

########## Encrypt file ##########
def on_button_encrypt_choice_click():
    encrypt_file_path=filedialog.askopenfilename(initialdir=None)
    gui_interface.entry_encrypt.delete("0", tk.END)
    gui_interface.entry_encrypt.insert("0", encrypt_file_path)
    print("Select encrypt file from : ", encrypt_file_path)
    print_to_text_log("Select encrypt file from : " + encrypt_file_path)

def on_button_encrypt_key_choice_click():
    encrypt_key_path=filedialog.askopenfilename(initialdir=None)
    gui_interface.entry_encrypt_key.delete("0", tk.END)
    gui_interface.entry_encrypt_key.insert("0", encrypt_key_path)
    print_to_text_log("Select public key from : " + encrypt_key_path)

def on_button_encrypt_click():
    encrypt_file_path=gui_interface.entry_encrypt.get()
    encrypt_key_path=gui_interface.entry_encrypt_key.get()
    print_to_text_log("Opened encrypt file from : " + gui_interface.entry_encrypt.get())
    myPGP.encryptFile(target_path = encrypt_file_path, public_key_path = encrypt_key_path)
    print_to_text_log("Encrypt success!")

########## Decrypt file ##########
def on_button_decrypt_pgp_choice_click():
    decrypt_pgp_path=filedialog.askopenfilename(initialdir=None)
    gui_interface.entry_decrypt_pgp.delete("0", tk.END)
    gui_interface.entry_decrypt_pgp.insert("0", decrypt_pgp_path)
    print_to_text_log("Select decrypt file from : " + decrypt_pgp_path)

def on_button_decrypt_key_choice_click():
    decrypt_key_path=filedialog.askopenfilename(initialdir=None)
    gui_interface.entry_decrypt_key.delete("0", tk.END)
    gui_interface.entry_decrypt_key.insert("0", decrypt_key_path)
    print_to_text_log("Select private key from : " + decrypt_key_path)

def on_button_decrypt_click():
    decrypt_pgp_path=gui_interface.entry_decrypt_pgp.get()
    decrypt_key_path=gui_interface.entry_decrypt_key.get()
    print_to_text_log("Opened PGP file from : " + decrypt_pgp_path)
    print_to_text_log("Opened  private key from : " + decrypt_key_path)
    myPGP.decryptFile(target_path = decrypt_pgp_path, private_key_path = decrypt_key_path)
    print_to_text_log("Decrypt success!")
