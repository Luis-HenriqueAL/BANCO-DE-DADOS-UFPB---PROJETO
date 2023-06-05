import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import font

class Application():

  def __init__(self):
    # Criando a janela principal
    self.window = Tk()
    self.window.title("LN System - Acess Panel")
    self.window.geometry("800x480")
    self.window.configure(background="white")
    self.window.resizable(width=False, height=False)
    self.window.attributes("-alpha", 0.95)

    # Definir o tamanho da fonte proporcional às dimensões da janela
    window_width = self.window.winfo_width()
    font_size = max(16, int(window_width / 40))  # Ajuste o valor 40 para controlar a proporção
    self.default_font = font.Font(family="Helvetica", size=font_size)
    self.window.option_add("*Font", self.default_font)

    # Carregando imagens
    self.logo = PhotoImage(file="icons/logo_nb.png")
    self.logo_user = PhotoImage(file="icons/user.png")
    self.logo_adm = PhotoImage(file="icons/adm.png")

    self.inicio()

    self.window.mainloop()

  @staticmethod
  def limpar(self):
    for widget in self.window.winfo_children():
      widget.destroy()

  def create_widgtes(self):

    self.LeftFrame = Frame(self.window, width=250, height=480, bg="#DDDDE7", relief="raised")
    self.LeftFrame.pack(side=LEFT)

    self.RightFrame = Frame(self.window, width=545, height=480, bg="#F5F5F5", relief="raised", )
    self.RightFrame.pack(side=RIGHT)
  
  def create_logo_inicial(self):
    self.LogoLabel = Label(self.LeftFrame, image=self.logo, bg="#DDDDE7")
    self.LogoLabel.place(x=25, y=125)

  def create_logo_user(self):
    self.LogoLabel = Label(self.LeftFrame, image=self.logo_user, bg="#DDDDE7")
    self.LogoLabel.place(x=25, y=125)

  def create_logo_adm(self):
    self.LogoLabel = Label(self.LeftFrame, image=self.logo_adm, bg="#DDDDE7")
    self.LogoLabel.place(x=25, y=125)
    
  def inicio(self):
    Application.limpar(self)

    self.create_widgtes()

    self.create_logo_inicial()

    # Textos
    text_font = font.Font(family="Helvetica", size=self.default_font.cget("size") + 4,weight="bold")
    SysLabel = tk.Label(self.RightFrame, text="Seja bem-vindo!", font=text_font, bg="#F5F5F5")
    SysLabel.place(x=140, y=30)

    DescLabel = tk.Label(self.RightFrame, text="Selecione o seu tipo de usuário", font=text_font, bg="#F5F5F5")
    DescLabel.place(x=70, y=80)

    ButtonClient = ttk.Button(self.RightFrame, text="Cliente", width=35, command=self.client)
    ButtonClient.place(x=150, y=170)

    ButtonAdmin = ttk.Button(self.RightFrame, text="Administrador", width=35, command=self.admin)
    ButtonAdmin.place(x=150, y=230)

  def client(self):
    Application.limpar(self)
    self.create_widgtes()
    self.create_logo_user()
  
    UserLabel = tk.Label(self.RightFrame, text="Usuário:", bg="#F5F5F5")
    UserLabel.place(x=70, y=50)

    UserEntry = ttk.Entry(self.RightFrame, width=20)
    UserEntry.place(x=180, y=50)

    PassLabel = tk.Label(self.RightFrame, text="Senha:", bg="#F5F5F5")
    PassLabel.place(x=70, y=100)

    PassEntry = ttk.Entry(self.RightFrame, width=20)
    PassEntry.place(x=180, y=100)

    LoginButton = ttk.Button(self.RightFrame, text="Login", width=20, command = self.login_client)
    LoginButton.place(x=180, y=140)

    AdviceLabel = tk.Label(self.RightFrame, text="Clique abaixo para registrar-se!", bg="#F5F5F5")
    AdviceLabel.place(x=130, y=200)

    RegisterButton = ttk.Button(self.RightFrame, text="Registrar", width=30)
    RegisterButton.place(x=160, y=250)

    VoltarButton = ttk.Button(self.RightFrame, text="Voltar", command=self.inicio)
    VoltarButton.place(x=220, y=400)


  def login_client(self):
    Application.limpar(self)
    self.create_widgtes()
    self.create_logo_user()

    try:
      # Código de validação de login no BD
      Application.limpar(self)
      self.create_widgtes()
      self.create_logo_user()     

      ContinueLabel = tk.Label(self.RightFrame, text="Login realizado com sucesso!\nClique para continuar", bg="#F5F5F5")
      ContinueLabel.place(x=120, y=100)

      ContinueButton = ttk.Button(self.RightFrame, text="Continuar", width=30, command=self.options_client)
      ContinueButton.place(x=165, y=170)
    
    except:
      Application.limpar(self)
      self.create_widgtes()
      self.create_logo_user()

      ErrorLabel = tk.Label(self.RightFrame, text="Erro ao fazer login, tente Novamente!", bg="#F5F5F5")
      ErrorLabel.place(x=120, y=100)
      AgainButton = ttk.Button(self.RightFrame, text="Tente novamente", command=self.client)
      AgainButton.place(x=120, y=150)

  def options_client(self):
    Application.limpar(self)
    self.create_widgtes()
    self.create_logo_user()

    TextLabel = tk.Label(self.RightFrame, text="Selecione a opção desejada", bg="#F5F5F5")
    TextLabel.place(x=120, y=100)

    BuyButton = ttk.Button(self.RightFrame, text="Seção de compras")
    # , command=self.sales_client)
    BuyButton.place(x=120, y=150)

    UpdateLabel = ttk.Button(self.RightFrame, text="Atualize seu usuário", bg="#F5F5F5")
    UpdateLabel.place(x=120, y=200)
    # , command-self.update_client)

  def update_client(self):
    Application.limpar(self)
    self.create_widgtes()
    self.create_logo_user()

    

  

  def admin(self):
    Application.limpar(self)
    self.create_widgtes()
    self.create_logo_adm()






    voltar_button = ttk.Button(self.RightFrame, text="Voltar", command=self.inicio)
    voltar_button.place(x=220, y=400)
    

if __name__ == "__main__":
    app = Application()