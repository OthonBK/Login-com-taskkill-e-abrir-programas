import customtkinter
import os
import tkinter as tk
import subprocess
import sys
from tkinter import messagebox
import psutil
import time
from pathlib import Path

file_path = "login.txt"
logged_in_user = ""  # defina a variável global e vazia

def fechar_root():
    os._exit(0)

if not os.path.exists(file_path):
    open(file_path, "w").close()

def check_login_exists(username: str, password: str) -> bool:
    with open(file_path, "r") as f:
        return any(line.strip() == f"{username},{password}" for line in f)

def check_username_exists(username):
    with open(file_path, "r") as f:
        for line in f:
            stored_username, _ = line.strip().split(",")
            if username == stored_username:
                return True
        return False

def login():
    global logged_in_user  # use a variável global
    username = entry1.get()
    password = entry2.get()
    if check_login_exists(username, password):
        print("Login bem sucedido")
        logged_in_user = username  # defina o valor da variável
        root.destroy()  # fecha a janela de login
    else:
        show_error()

def show_error():
    error_window = tk.Toplevel(root)
    error_window.configure(bg="#DCDCDC") # Define cor de fundo da janela
    error_label = tk.Label(error_window, text="Erro: Login incorreto", bg="#DCDCDC")
    error_label.pack()
    ok_button = tk.Button(error_window, text="OK", command=error_window.destroy, bg="#90EE90", fg="black") # Define cores do botão
    ok_button.pack()

def register():
    username = entry1.get()
    password = entry2.get()
    if check_username_exists(username):
        print("Usuário já existe")
    else:
        with open(file_path, "a") as f:
            f.write(f"{username},{password}\n")
        print("Novo usuário adicionado ao arquivo")

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("400x400")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(
    master=frame, text="BK Login System", font=("Roboto", 24))
label.pack(pady=12, padx=10)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
entry1.pack(pady=12, padx=10)

entry2 = customtkinter.CTkEntry(
    master=frame, placeholder_text="Password", show="*")
entry2.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Login", command=login)
button.pack(pady=12, padx=10)

button_register = customtkinter.CTkButton(
    master=frame, text="Registrar", command=register)
button_register.pack(pady=12, padx=10)

checkbox = customtkinter.CTkCheckBox(master=frame, text="Remenber Me")
checkbox.pack(pady=12, padx=10)

root.protocol("WM_DELETE_WINDOW", fechar_root)

root.mainloop()

# Agora que o usuário fez login, execute o programa de bloqueio (se autorizado)
# verifique se o usuário tem permissão para executar o programa
if logged_in_user in ["admin", "root"]:

    import os
    import tkinter as tk
    import psutil
    import time
    from tkinter import messagebox

    # Defina a lista de processos do aplicativo que você deseja bloquear
APP_NAMES = ['notepad.exe', 'firefox.exe', 'steam.exe', 'Discord.exe']

# Variável de controle do loop
running = False

#Define a função para verificar se o usuário tem permissão para executar o programa de bloqueio

def check_permission(user):
 return user in ["admin", "root"]
#Define a função para verificar se o usuário está logado

def is_logged_in():
 return bool(logged_in_user)

# Verifique se algum dos aplicativos está em execução

def check_if_running():
    for p in psutil.process_iter(['name']):
        if any(app_name in p.info['name'] for app_name in APP_NAMES):
            return True
    return False

# Função para iniciar o loop

def start_program():
    global running
    running = True
    while running:
        if check_if_running():
            for p in psutil.process_iter(['pid', 'name']):
                if any(app_name in p.info['name'] for app_name in APP_NAMES):
                    os.system(f"TASKKILL /F /PID {p.info['pid']}")
        root.update()  # atualiza a janela do Tkinter
        time.sleep(0.1)

# Função para parar o loop

def stop_program():
    global running
    running = False

# Define a aparência do botão quando pressionado

def on_press(button):
    button.config(relief="sunken")

# Define a aparência do botão quando liberado

def on_release(button):
    button.config(relief="raised")

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")

# Crie a janela
root = customtkinter.CTk()
root.geometry("350x300")

# Crie o título "Botões de Executar e Parar em Taskkill"
title = customtkinter.CTkLabel(root, text="TaskKill")
title.grid(row=0, column=0, columnspan=2)

# Crie o botão "Executar"
start_button = customtkinter.CTkButton(root, text="Executar", command=start_program)
start_button.grid(row=1, column=0, padx=5, pady=10)
start_button.bind("<ButtonPress-1>", lambda event: on_press(start_button))
start_button.bind("<ButtonRelease-1>", lambda event: on_release(start_button))

# Crie o botão "Parar"
stop_button = customtkinter.CTkButton(root, text="Parar", command=stop_program)
stop_button.grid(row=1, column=1, padx=40, pady=10)
stop_button.bind("<ButtonPress-1>", lambda event: on_press(stop_button))
stop_button.bind("<ButtonRelease-1>", lambda event: on_release(stop_button))

# Função para abrir o Firefox e o Discord
def open_firefox_and_discord():
    firefox_path = Path("C:/Program Files/Mozilla Firefox/firefox.exe")
    os.system(f'"{firefox_path}"')
    time.sleep(1)  # Espera 1 segundo
    discord_path = Path(
        f'C:/Users/{os.getlogin()}/AppData/Local/Discord/Update.exe').resolve()
    os.system(f'"{discord_path}" --processStart Discord.exe')


# Crie o título "Botões de Executar e Parar em Taskkill"
title = customtkinter.CTkLabel(root, text="Inicial Machine")
title.grid(row=2, column=0, columnspan=2)

# Cria o botão
button = customtkinter.CTkButton(master=root, text="Abrir Firefox e Discord", command=open_firefox_and_discord)
button.grid(row=3, column=0, padx=10, pady=10)

# Inicie o loop da interface gráfica
root.mainloop()
