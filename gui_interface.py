import tkinter as tk
from gui import *
import gui_action as action

# window.geometry("550x450")

########## Generate Key ##########
label_name = tk.Label(text="(Optional)Name:")
label_name.grid(column=0, row=0)
entry_name = tk.Entry()
entry_name.grid(column=1, row=0)
button_generate_key = tk.Button(text="Generate Key", command=action.on_button_name_set_click)
button_generate_key.grid(column=2, row=0)

########## Encrypt file ##########
label_encrypt = tk.Label(text="Target File Path:")
label_encrypt.grid(column=0, row=1)

entry_encrypt = tk.Entry()
entry_encrypt.grid(column=1, row=1)

button_encrypt_choice = tk.Button(text="Select File", command=action.on_button_encrypt_choice_click)
button_encrypt_choice.grid(column=2, row=1)

button_encrypt = tk.Button(text="Encrypt File", command=action.on_button_encrypt_click)
button_encrypt.grid(column=6, row=1)

label_decrypt_key = tk.Label(text="Public Key Path:")
label_decrypt_key.grid(column=3, row=1)

entry_encrypt_key = tk.Entry()
entry_encrypt_key.grid(column=4, row=1)

button_decrypt_pgp = tk.Button(text="Select File", command=action.on_button_encrypt_key_choice_click)
button_decrypt_pgp.grid(column=5, row=1)


# sep = Separator(window, orient="horizontal")
# sep.place(relx=0, rely=0.47, relwidth=1, relheight=1)

########## Decrypt file ##########
label_decrypt_pgp = tk.Label(text="Locked File Path:")
label_decrypt_pgp.grid(column=0, row=2)

entry_decrypt_pgp = tk.Entry()
entry_decrypt_pgp.grid(column=1, row=2)

button_decrypt_pgp = tk.Button(text="Select File", command=action.on_button_decrypt_pgp_choice_click)
button_decrypt_pgp.grid(column=2, row=2)


label_decrypt_key = tk.Label(text="Private Key Path:")
label_decrypt_key.grid(column=3, row=2)

entry_decrypt_key = tk.Entry()
entry_decrypt_key.grid(column=4, row=2)

button_decrypt_pgp = tk.Button(text="Select File", command=action.on_button_decrypt_key_choice_click)
button_decrypt_pgp.grid(column=5, row=2)


button_decrypt = tk.Button(text="Decrypt File", command=action.on_button_decrypt_click)
button_decrypt.grid(column=6, row=2)

########## Log ##########
log_name = tk.Label(text="log output:")
log_name.grid(column=0, row=3)
text_log = tk.Text(window, height = 20, width = 80)
text_log.insert(tk.END,
"""# README

***************DON'T SHARE PRIVATE KEY***************
*********************私鑰嚴禁外流********************

## 產生密鑰
1. 輸入 Key 的名稱(選填)    input name of the key(optional)
2. 點擊產生                 click generate
3. 產生兩把 Key 到資料夾內  key generated in this .exe's directory

## 加密
4. 選取要被加密的檔案(如:foo.txt, bar.zip)  select file to be encrypted
5. 選擇剛剛產生的 Public Key                select the generated public_key.asc
6. 點擊加密                                 click on button

## 解密
7. 選擇加密後的檔案(如:foo.txt)             select file to be decrypted
8. 選擇 Private Key                         select private key
9. 點擊解密                                 click on button
""")
text_log.grid(column=1, row=3, columnspan=8)

window.mainloop()