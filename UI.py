import tkinter as tk
from PIL import Image, ImageTk
from tkinter import*
from database import *
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter import ttk
import datetime

conn, cursor = initialize_connection()
 
def center_window(width, height):
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry(f'{width}x{height}+{x}+{y}')
 
class WelcomeWindow(tk.Frame):
    def __init__(self, master):
        super().__init__()
        self.master = master
        self.master.title("Bem Vindo")
        self.master.geometry('300x370')
        self.configure(bg="#1c2e4a")
        self.master.configure(bg="#1c2e4a")
        self.master.iconbitmap('icone.ico')

        self.image = tk.PhotoImage(file="imageminicio.png")

        image_label = tk.Label(self, image=self.image, bd=0)
        image_label.pack(pady=10)

        login_button = tk.Button(self, text="Login", width=20, command=self.open_login_window, borderwidth = 3, background="#eef4ff", foreground="black", font=("Georgia", 10))
        login_button.pack(padx=10, pady=(20, 10))
         
        register_button = tk.Button(self, text="Registrar", width=20, command=self.open_register_window, borderwidth = 3, background="#eef4ff", foreground="black", font=("Georgia", 10))
        register_button.pack(pady=10, padx=60)

        self.pack()
         
    def open_login_window(self):
        for widget in self.winfo_children(): 
            widget.destroy()
        self.destroy()
        LoginWindow(self.master)
         
    def open_register_window(self):
        for widget in self.winfo_children(): 
            widget.destroy()
        self.destroy()
        RegisterWindow(self.master)
 
class LoginWindow(tk.Frame):
    def __init__(self, master):
        super().__init__()
        self.master = master
        self.master.title("Login")
        self.master.resizable(False, False)
        self.master.geometry('300x370')
        self.configure(bg="#1c2e4a")
        self.master.configure(bg="#1c2e4a")
        self.master.iconbitmap('icone.ico')
         
        tk.Label(self, text="Email:       ", background="#1e2e4a", foreground="#eef4ff", font=("Georgia", 12)).grid(row=0, column=0)
        self.username_entry = tk.Entry(self, borderwidth = 3, background="#eef4ff")
        self.username_entry.grid(row=0, column=1, padx=10, pady=20)
         
        tk.Label(self, text="Senha:       ", background="#1e2e4a", foreground="#eef4ff", font=("Georgia", 12)).grid(row=1, column=0)
        self.password_entry = tk.Entry(self, show="*", borderwidth = 3, background="#eef4ff")
        self.password_entry.grid(row=1, column=1, padx=10, pady=0)

        submit_button = tk.Button(self, text="Voltar", width=8, command=self.back, borderwidth = 3, background="#eef4ff", foreground="black", font=("Georgia", 9))
        submit_button.grid(row=2, column=0, padx=10, pady=27, sticky="e")
         
        carros_button = tk.Button(self, text="Avançar", width=8, command=self.submit, borderwidth = 3, background="#eef4ff", foreground="black", font=("Georgia", 9))
        carros_button.grid(row=2, column=1, padx=10, pady=27, sticky="e")

        self.username_entry.config(width=27)
        self.password_entry.config(width=27)

        self.image = tk.PhotoImage(file="loginimagem.png")

        image_label = tk.Label(self, image=self.image, bd=0)
        image_label.grid(row=3, columnspan=2, pady=10, padx= 30)
    
        self.pack()
             
    def submit(self):
        email = self.username_entry.get()
        password = self.password_entry.get()

        if email and password:
            data = {"email": email, "password": password}
            if login(cursor, data):
                print("Login approved (console)")
                for widget in self.winfo_children():
                    widget.destroy()
                self.destroy()
                CarrosWindow(self.master)
            else: 
                messagebox.showwarning("Aviso", "Senha ou login incorretos.")
        else:
                messagebox.showwarning("Aviso", "Por favor, preencha todos os campos.")
  
    def back(self):
        for widget in self.winfo_children(): 
            widget.destroy()
        self.destroy()
        WelcomeWindow(self.master)

class RegisterWindow(tk.Frame):
    def __init__(self, master):
        super().__init__()
        self.master = master
        self.master.title("Registro")
        self.master.resizable(False, False)
        self.master.geometry('300x370')
        self.configure(bg="#1c2e4a")
        self.master.configure(bg="#1c2e4a")
        self.master.iconbitmap('icone.ico')
         
        tk.Label(self, text="Primeiro nome:", background="#1e2e4a", foreground="#eef4ff", font=("Georgia", 10)).grid(row=0, column=0, padx= 6, sticky="w")
        self.first_name_entry = tk.Entry(self, width=26, borderwidth = 2, background="#eef4ff")
        self.first_name_entry.grid(row=0, column=1, padx=10, pady=10, sticky="e")
         
        tk.Label(self, text="Ultimo nome:", background="#1e2e4a", foreground="#eef4ff", font=("Georgia", 10)).grid(row=1, column=0, padx= 6, sticky="w")
        self.last_name_entry = tk.Entry(self, width=26, borderwidth = 2, background="#eef4ff")
        self.last_name_entry.grid(row=1, column=1, padx=10, pady=10, sticky="e")
         
        tk.Label(self, text="Senha:", background="#1e2e4a", foreground="#eef4ff", font=("Georgia", 10)).grid(row=3, column=0, padx= 6, sticky="w")
        self.password_entry = tk.Entry(self, show="*", width=26, borderwidth = 2, background="#eef4ff")
        self.password_entry.grid(row=3, column=1, padx=10, pady=10, sticky="e")
         
        tk.Label(self, text="Email:", background="#1e2e4a", foreground="#eef4ff", font=("Georgia", 10)).grid(row=2, column=0, padx= 6, sticky="w")
        self.email_entry = tk.Entry(self, width=26, borderwidth = 2, background="#eef4ff")
        self.email_entry.grid(row=2, column=1, padx=10, pady=10, sticky="e")
         
        tk.Label(self, text="Genero:", background="#1e2e4a", foreground="#eef4ff", font=("Georgia", 10)).grid(row=4, column=0, padx= 6, sticky="w")
        self.gender_combobox = ttk.Combobox(self, values=["M", "F"], width = 2, background="#eef4ff")
        #self.gender_entry = tk.Entry(self, width=10)
        self.gender_combobox.grid(row=4, column=1, padx=10, pady=10, sticky="e")
         
        tk.Label(self, text="Idade:", background="#1e2e4a", foreground="#eef4ff", font=("Georgia", 10)).grid(row=5, column=0, padx= 6, sticky="w")
        self.age_entry = tk.Entry(self, width=10, borderwidth = 2, background="#eef4ff")
        self.age_entry.grid(row=5, column=1, padx=10, pady=10, sticky="e")
         
        tk.Label(self, text="Endereço:", background="#1e2e4a", foreground="#eef4ff", font=("Georgia", 10)).grid(row=6, column=0, padx= 6, sticky="w")
        self.address_entry = tk.Text(self, width=20, height=3, borderwidth = 2, background="#eef4ff")
        self.address_entry.grid(row=6, column=1, padx=10, pady=10, sticky="e")
         
        submit_button = tk.Button(self, text="Registrar", width=10, command=self.submit, borderwidth = 3, background="#eef4ff", foreground="black", font=("Georgia", 9))
        submit_button.grid(row=7, column=1, padx=10, pady=4, sticky="e")
 
        submit_button = tk.Button(self, text="Voltar", width=10, command=self.back, borderwidth = 3, background="#eef4ff", foreground="black", font=("Georgia", 9))
        submit_button.grid(row=7, column=0, sticky="w", padx=10, pady= 4)

        self.pack()
         
    def submit(self):
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        password = self.password_entry.get()
        email = self.email_entry.get()
        gender = self.gender_combobox.get()
        age = self.age_entry.get()

        if first_name and last_name and password and email and gender and age:

            if len(password) < 6:
                messagebox.showwarning("Aviso", "A senha deve ter no mínimo 6 caracteres.")
            elif "@" not in email:
                messagebox.showwarning("Aviso", "O email deve conter '@'.")
            elif gender not in ["M", "F"]:
                messagebox.showwarning("Aviso", "O gênero deve ser 'M' ou 'F'.")
            elif not age.isdigit() or int(age) > 130:
                messagebox.showwarning("Aviso", "A idade deve ser um número válido menor ou igual a 130.")
            else:

                data = {
                    "firstName": self.first_name_entry.get(),
                    "lastName": self.last_name_entry.get(),
                    "password": self.password_entry.get(),
                    "email": self.email_entry.get(),
                    "gender": self.gender_combobox.get(),
                    "age": self.age_entry.get(),
                    "address": self.address_entry.get(1.0, tk.END).strip()
                }
                register(cursor, conn, data)
                self.open_aprovacao_window()
        else:
            messagebox.showwarning("Aviso", "Por favor, preencha todos os campos.")

    def back(self):
        for widget in self.winfo_children(): 
            widget.destroy()
        self.destroy()
        WelcomeWindow(self.master)

    def open_aprovacao_window(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.destroy()
        messagebox.showinfo("Sucesso", "Registro concluido")
        WelcomeWindow(self.master)         
 
class MainWindow(tk.Frame):
    def __init__(self, master):
        super().__init__()
        self.master = master
        center_window(600, 400)
        self.master.geometry('300x370')
        self.pack()
        self.configure(bg="#1c2e4a")
        self.master.configure(bg="#1c2e4a")
        self.master.iconbitmap('icone.ico')

class CarrosWindow(tk.Frame):
    def __init__(self, master):
        super().__init__()
        self.master = master
        self.master.title("Registro Carros")
        self.master.resizable(False, False)
        self.master.geometry('303x370')
        self.configure(bg="#1c2e4a")
        self.master.configure(bg="#1c2e4a")
        self.master.iconbitmap('icone.ico')

        tk.Label(self, text="Marca:", background="#1e2e4a", foreground="#eef4ff", font=("Georgia", 12)).grid(row=0, column=0, padx= 20, sticky="w")
        self.marca_entry = tk.Entry(self, width=26, borderwidth = 2, background="#eef4ff")
        self.marca_entry.grid(row=0, column=1, padx=10, pady=10, sticky="e")

        tk.Label(self, text="Modelo:", background="#1e2e4a", foreground="#eef4ff", font=("Georgia", 12)).grid(row=1, column=0, padx= 20, sticky="w")
        self.modelo_entry = tk.Entry(self, width=26, borderwidth = 2, background="#eef4ff")
        self.modelo_entry.grid(row=1, column=1, padx=10, pady=10, sticky="e")

        tk.Label(self, text="Ano:", background="#1e2e4a", foreground="#eef4ff", font=("Georgia", 12)).grid(row=2, column=0, padx= 20, sticky="w")
        self.ano_entry = tk.Entry(self, width=26, borderwidth = 2, background="#eef4ff")
        #self.ano_entry.place(x=110, y=80)
        self.ano_entry.grid(row=2, column=1, padx=10, pady=10, sticky="e")

        tk.Label(self, text="Placa:", background="#1e2e4a", foreground="#eef4ff", font=("Georgia", 12)).grid(row=3, padx= 20, column=0, sticky="w")
        self.placa_entry = tk.Entry(self, width=26, borderwidth = 2, background="#eef4ff")
        self.placa_entry.grid(row=3, column=1, padx=10, pady=10, sticky="e")

        tk.Label(self, text="Km:", background="#1e2e4a", foreground="#eef4ff", font=("Georgia", 12)).grid(row=4, padx= 20, column=0, sticky="w")
        self.km_entry = tk.Entry(self, width=26, borderwidth = 2, background="#eef4ff")
        self.km_entry.grid(row=4, column=1, padx=10, pady=10, sticky="e")

        tk.Label(self, text="Preco:", background="#1e2e4a", foreground="#eef4ff", font=("Georgia", 12)).grid(row=5, padx= 20, column=0, sticky="w")
        self.preco_entry = tk.Entry(self, width=26, borderwidth = 2, background="#eef4ff")
        self.preco_entry.grid(row=5, column=1, padx=10, pady=10, sticky="e")

        tk.Label(self, text="Cor:", background="#1e2e4a", foreground="#eef4ff", font=("Georgia", 12)).grid(row=6, column=0, padx= 20, sticky="w")
        self.cor_entry = tk.Entry(self, width=26, borderwidth = 2, background="#eef4ff")
        self.cor_entry.grid(row=6, column=1, padx=10, pady=10, sticky="e")

        submit_button = tk.Button(self, text="Registrar", width=13, command=self.registro, borderwidth = 3, background="#eef4ff", foreground="black", font=("Georgia", 8))
        submit_button.grid(row=7, column=0, padx=10, pady=10, sticky="e")

        view_button = tk.Button(self, text="Ver Carros", width=8, command=self.ver_carros, borderwidth = 3, background="#eef4ff", foreground="black", font=("Georgia", 8))
        view_button.grid(row=7, column=1, padx=10, pady=10, sticky="w")

        submit_button = tk.Button(self, text="Excluir Carros", width=11, command=self.open_deletarcarros, borderwidth = 3, background="#eef4ff", foreground="black", font=("Georgia", 8))
        submit_button.grid(row=7, column=1, padx=10, pady=10, sticky="e")

        submit_button = tk.Button(self, text="Atualizar Carros", width=13, command=self.open_atualizarcarros, borderwidth = 3, background="#eef4ff", foreground="black", font=("Georgia", 8))
        submit_button.grid(row=8, column=0, sticky="e", padx=10, pady = 2)

        submit_button = tk.Button(self, text="Voltar", width=8, command=self.back_tela, borderwidth = 3, background="#eef4ff", foreground="black", font=("Georgia", 8))
        submit_button.grid(row=8, column=1, sticky="w", padx=10, pady= 2)

        self.pack() 

    def registro(self):
        data = {}
        data["marca"] = self.marca_entry.get()
        data["modelo"] = self.modelo_entry.get()
        data["ano"] = self.ano_entry.get()
        data["placa"] = self.placa_entry.get()
        data["km"] = self.km_entry.get()
        data["preco"] = self.preco_entry.get()
        data["cor"] = self.cor_entry.get()

        if not all(data.values()):
            messagebox.showwarning("Aviso", "Por favor, preencha todos os campos.")
            return

        if not data["ano"].isdigit():
            messagebox.showwarning("Aviso", "Por favor, insira um ano válido.")
            return
        
        ano = int(data["ano"])
        if ano < 0 or ano > datetime.datetime.now().year:
            messagebox.showwarning("Aviso", "Por favor, insira um ano válido.")
            return

        km_str = data["km"].replace(".", "")
        if not km_str.isdigit():
            messagebox.showwarning("Aviso", "Por favor, insira um valor válido para km.")
            return
        
        km = float(data["km"])
        if km < 0:
            messagebox.showwarning("Aviso", "Por favor, insira um valor válido para o km.")
            return

        preco_str = data["preco"].replace(".", "")
        if not preco_str.isdigit():
            messagebox.showwarning("Aviso", "Por favor, insira um valor válido para o preço.")
            return
        
        preco = float(data["preco"])
        if preco < 0:
            messagebox.showwarning("Aviso", "Por favor, insira um valor válido para o preço.")
            return

        register2(cursor, conn, data)
        self.open_atualizacao_window()

    def open_atualizacao_window(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.destroy()
        messagebox.showinfo("Sucesso", "Registro concluido")
        CarrosWindow(self.master)

    def ver_carros(self):

        for widget in self.winfo_children():
            widget.destroy()

        self.configure(bg="#1c2e4a")
        self.master.configure(bg="#1c2e4a")
        self.master.geometry('950x295+300+200')

        main_frame = tk.Frame(self, bg="#1c2e4a")
        main_frame.pack(fill="both", expand=True)

        canvas = tk.Canvas(main_frame, bg="#1c2e4a", width=650)
        canvas.pack(side="left", fill="both", expand=True)

        scrollbar = ttk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
        scrollbar.pack(side="right", fill="y")

        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        frame = tk.Frame(canvas, bg="#1c2e4a")
        canvas.create_window((0, 0), window=frame, anchor="nw")

        cursor.execute("SELECT * FROM carros")
        carros = cursor.fetchall()
        
        for i, carro in enumerate(carros):
            tk.Label(frame, text=f" Carro {i + 1}:  ", background="#1c2e4a", foreground="#eef4ff", font=("Georgia", 10)).grid(row=i, column=0, sticky="w")
            tk.Label(frame, text=f" Marca: {carro[1]}  ", background="#1c2e4a", foreground="#eef4ff", font=("Georgia", 10)).grid(row=i, column=1, sticky="w")
            tk.Label(frame, text=f" Modelo: {carro[2]}  ", background="#1c2e4a", foreground="#eef4ff", font=("Georgia", 10)).grid(row=i, column=2, sticky="w")
            tk.Label(frame, text=f" Ano: {carro[3]}  ", background="#1c2e4a", foreground="#eef4ff", font=("Georgia", 10)).grid(row=i, column=3, sticky="w")
            tk.Label(frame, text=f" Placa: {carro[4]}  ", background="#1c2e4a", foreground="#eef4ff", font=("Georgia", 10)).grid(row=i, column=4, sticky="w")
            tk.Label(frame, text=f" Km: {carro[5]}  ", background="#1c2e4a", foreground="#eef4ff", font=("Georgia", 10)).grid(row=i, column=5, sticky="w")
            tk.Label(frame, text=f" Preco: {carro[6]}  ", background="#1c2e4a", foreground="#eef4ff", font=("Georgia", 10)).grid(row=i, column=6, sticky="w")
            tk.Label(frame, text=f" Cor: {carro[7]}  ", background="#1c2e4a", foreground="#eef4ff", font=("Georgia", 10)).grid(row=i, column=7, sticky="w")

        frame.update_idletasks()
        canvas.configure(scrollregion=canvas.bbox("all"))

        submit_button = tk.Button(self, text="Voltar", width=680, command=self.back_carros, background="#eef4ff", font=("Georgia", 10))
        submit_button.pack()

        self.pack()

    def open_deletarcarros(self):
        for widget in self.winfo_children(): 
            widget.destroy()
        self.destroy()
        DeletarCarros(self.master)

    def open_atualizarcarros(self):
        for widget in self.winfo_children(): 
            widget.destroy()
        self.destroy()
        AtualizarCarros(self.master)

    def back_carros(self):
        for widget in self.winfo_children(): 
            widget.destroy()
        self.destroy()
        CarrosWindow(self.master)

    def back_tela(self):
        for widget in self.winfo_children(): 
            widget.destroy()
        self.destroy()
        LoginWindow(self.master)

class AtualizacaoWindow(tk.Frame):
    def __init__(self, master):
        super().__init__()
        self.master.title("Sucesso")
        self.master.geometry('300x370')
        self.configure(bg="#1c2e4a")
        self.master.configure(bg="#1c2e4a")
        self.master.iconbitmap('icone.ico')
        data = {}

        tk.Label(self, text="ATUALIZAÇÂO REALIZADA", bg="white").grid(row=0, column=0, sticky="w")  
        self.pack()

class DeletarCarros(tk.Frame):
    def __init__(self, master):
        super().__init__()
        self.master = master
        self.master.title("Deletar Carros")
        self.master.resizable(False, False)
        center_window(240, 150)
        self.master.geometry('300x370')
        self.configure(bg="#1c2e4a")
        self.master.configure(bg="#1c2e4a")
        self.master.iconbitmap('icone.ico')

        tk.Label(self, text="Placa:", background="#1e2e4a", foreground="#eef4ff", font=("Georgia", 12)).grid(row=1, column=0, padx= 8, sticky="w")
        self.placa_entry = tk.Entry(self, width=26, borderwidth = 3, background="#eef4ff")
        self.placa_entry.grid(row=1, column=1, padx=10, pady=10, sticky="e")

        submit_button = tk.Button(self, text="Excluir", width=8, command=self.excluir_carro, borderwidth = 3, background="#eef4ff", foreground="black", font=("Georgia", 9))
        submit_button.grid(row=2, column=1, padx=10, pady=27, sticky="e")

        submit_button = tk.Button(self, text="Voltar", width=8, command=self.back_deletar, borderwidth = 3, background="#eef4ff", foreground="black", font=("Georgia", 9))
        submit_button.grid(row=2, column=0, padx=10, pady=27, sticky="e")

        self.image = tk.PhotoImage(file="imagematualizaremover.png")

        image_label = tk.Label(self, image=self.image, bd=0)
        image_label.grid(row=3, columnspan=2, pady=30, padx= 40)

        self.pack()

    def excluir_carro(self):
        data = {}
        data["placa"] = self.placa_entry.get()

        if all(data.values()):
            if self.placa_exists(data["placa"]):
                excluir_carro_por_placa(cursor, conn, data)
                self.open_exclusao_window()
            else:
                messagebox.showwarning("Aviso", "Placa não encontrada no banco de dados.")
        else:
            messagebox.showwarning("Aviso", "Por favor, preencha todos os campos.")

    def open_exclusao_window(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.destroy()
        messagebox.showinfo("Sucesso", "Exclusão concluida")
        DeletarCarros(self.master)         

    def back_deletar(self):
        for widget in self.winfo_children(): 
            widget.destroy()
        self.destroy()
        CarrosWindow(self.master)

    def placa_exists(self, placa):

        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="registrocarros"
        )

        cursor = conn.cursor()

        query = "SELECT COUNT(*) FROM carros WHERE placa = %s"
        cursor.execute(query, (placa,))
        count = cursor.fetchone()[0]
        cursor.close()
        conn.close()

        if count > 0:
            return True
        else:
            return False

class AtualizarCarros(tk.Frame):
    def __init__(self, master):
        super().__init__()
        self.master = master
        self.master.title("Atualizar")
        self.master.resizable(False, False)
        center_window(240, 150)

        self.configure(bg="#1c2e4a")
        self.master.configure(bg="#1c2e4a")
        self.master.geometry('300x370')
        self.master.iconbitmap('icone.ico')
    
        tk.Label(self, text=" Placa:", background="#1e2e4a", foreground="#eef4ff", font=("Georgia", 12)).grid(row=0, column=0, sticky="w")
        
        self.placa_entry = tk.Entry(self, width=26, borderwidth = 3, background="#eef4ff")
        self.placa_entry.grid(row=0, column=1, padx=10, pady=10, sticky="e")

        tk.Label(self, text=" Preco:", background="#1e2e4a", foreground="#eef4ff", font=("Georgia", 12)).grid(row=1, column=0, sticky="w")
        self.preco_entry = tk.Entry(self, width=26, borderwidth = 3, background="#eef4ff")
        self.preco_entry.grid(row=1, column=1, padx=10, pady=10, sticky="e")

        submit_button = tk.Button(self, text="Atualizar", width=8, command=self.atualizar_carro, borderwidth = 3, background="#eef4ff", foreground="black", font=("Georgia", 9))
        submit_button.grid(row=2, column=1, padx=10, pady=27, sticky="e")

        submit_button = tk.Button(self, text="Voltar", width=8, command=self.back_deletar, borderwidth = 3, background="#eef4ff", foreground="black", font=("Georgia", 9))
        submit_button.grid(row=2, column=0, padx=10, pady=27, sticky="e")

        self.image = tk.PhotoImage(file="imagematualizaremover.png")

        image_label = tk.Label(self, image=self.image, bd=0)
        image_label.grid(row=3, columnspan=2, pady=10, padx= 30)

        self.pack()

    def atualizar_carro(self):
        data = {}
        data["placa"] = self.placa_entry.get()
        data["preco"] = self.preco_entry.get()
           
        if all(data.values()):
            if self.placa_exists(data["placa"]):
                atualizar_carro_preco(cursor, conn, data)
                self.open_atualizar_window()
            else:
                messagebox.showwarning("Aviso", "Placa não encontrada no banco de dados.")
        else:
            messagebox.showwarning("Aviso", "Por favor, preencha todos os campos.")
      
    def open_atualizar_window(self):

        for widget in self.winfo_children():
            widget.destroy()
        self.destroy()
        messagebox.showinfo("Sucesso", "Atualização concluida")
        AtualizarCarros(self.master)

    def back_deletar(self):
        for widget in self.winfo_children(): 
            widget.destroy()
        self.destroy()
        CarrosWindow(self.master)

    def placa_exists(self, placa):

        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="registrocarros"
        )
        cursor = conn.cursor()

        query = "SELECT COUNT(*) FROM carros WHERE placa = %s"
        cursor.execute(query, (placa,))
        count = cursor.fetchone()[0]
        cursor.close()
        conn.close()

        if count > 0:
            return True
        else:
            return False

root = tk.Tk()
root.eval('tk::PlaceWindow . center')
WelcomeWindow(root)
root.mainloop()