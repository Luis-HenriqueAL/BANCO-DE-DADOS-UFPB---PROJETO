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

  # Resetar tela
  @staticmethod
  def limpar(self):
    for widget in self.window.winfo_children():
      widget.destroy()

  # Cria as divisões da tela
  def create_widgtes(self):

    self.LeftFrame = Frame(self.window, width=250, height=480, bg="#DDDDE7", relief="raised")
    self.LeftFrame.pack(side=LEFT)

    self.RightFrame = Frame(self.window, width=545, height=480, bg="#F5F5F5", relief="raised", )
    self.RightFrame.pack(side=RIGHT)
  
  # Cria a logo da tela inicial
  def create_logo_inicial(self):
    self.LogoLabel = Label(self.LeftFrame, image=self.logo, bg="#DDDDE7")
    self.LogoLabel.place(x=25, y=125)

  # Cria a logo da tela de usuário
  def create_logo_user(self):
    self.LogoLabel = Label(self.LeftFrame, image=self.logo_user, bg="#DDDDE7")
    self.LogoLabel.place(x=25, y=125)

  # Cria a logo da tela de administrador
  def create_logo_adm(self):
    self.LogoLabel = Label(self.LeftFrame, image=self.logo_adm, bg="#DDDDE7")
    self.LogoLabel.place(x=25, y=125)
    
  # Inicia a aplicação
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

  # Início do loop do cliente
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

    LoginButton = ttk.Button(self.RightFrame, text="Login", width=20, command = self.action_login_client)
    LoginButton.place(x=180, y=140)

    AdviceLabel = tk.Label(self.RightFrame, text="Clique abaixo para registrar-se!", bg="#F5F5F5")
    AdviceLabel.place(x=130, y=200)

    RegisterButton = ttk.Button(self.RightFrame, text="Registrar", width=30, command=self.register_client)
    RegisterButton.place(x=160, y=250)

    # VoltarButton = ttk.Button(self.RightFrame, text="Voltar", command=self.inicio)
    # VoltarButton.place(x=220, y=400)

  # Tentativa do login do cliente
  def action_login_client(self):
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

      ErrorLabel = tk.Label(self.RightFrame, text="Erro ao fazer login, tente novamente!", bg="#F5F5F5")
      ErrorLabel.place(x=120, y=100)
      AgainButton = ttk.Button(self.RightFrame, text="Tente novamente", command=self.client)
      AgainButton.place(x=120, y=150)
 
 # Exibição das opções do cliente
  def options_client(self):
    Application.limpar(self)
    self.create_widgtes()
    self.create_logo_user()

    TextLabel = tk.Label(self.RightFrame, text="Selecione a opção desejada", bg="#F5F5F5")
    TextLabel.place(x=120, y=100)

    BuyButton = ttk.Button(self.RightFrame, text="Seção de compras", command=self.sales_client)
    BuyButton.place(x=120, y=150)

    UpdateButton = ttk.Button(self.RightFrame, text="Atualize seu usuário", command=self.update_client)
    UpdateButton.place(x=120, y=200)

    VoltarButton = ttk.Button(self.RightFrame, text="Voltar", command=self.client)
    VoltarButton.place(x=120, y=400)

  # Opção de atualizar as informações do cliente
  def update_client(self):
    Application.limpar(self)
    self.create_widgtes()
    self.create_logo_user()

    UpdateUserLabel = tk.Label(self.RightFrame, text="Usuário:", bg="#f5f5f5")
    UpdateUserLabel.place(x=70, y=50)
    UpdateUserEntry = ttk.Entry(self.RightFrame, width=20)
    UpdateUserEntry.place(x=180, y=50)

    UpdateContactLabel = tk.Label(self.RightFrame, text="Contato:", bg="#f5f5f5")
    UpdateContactLabel.place(x=70, y=90)
    UpdateContactEntry = ttk.Entry(self.RightFrame, width=20)
    UpdateContactEntry.place(x=180, y=90)

    UpdateTeamLabel = tk.Label(self.RightFrame, text="Time:", bg="#f5f5f5")
    UpdateTeamLabel.place(x=70, y=130)
    UpdateTeamEntry = ttk.Entry(self.RightFrame, width=20)
    UpdateTeamEntry.place(x=180, y= 130)

    UpdateAnimeLabel = tk.Label(self.RightFrame, text="Anime:", bg="#f5f5f5")
    UpdateAnimeLabel.place(x=70, y=170)
    UpdateAnimeEntry = ttk.Entry(self.RightFrame, width=20)
    UpdateAnimeEntry.place(x=180, y=170)

    UpdateAddressLabel = tk.Label(self.RightFrame, text="Endereço:", bg="#f4f4f4")
    UpdateAddressLabel.place(x=70, y=210)
    UpdateAdressEntry= ttk.Entry(self.RightFrame, width=20)
    UpdateAdressEntry.place(x=180, y=210)

    UpdateUserIdLabel = tk.Label(self.RightFrame, text="ID:", bg="#f5f5f5")
    UpdateUserIdLabel.place(x=70, y = 250)
    UpdateUserIdEntry = ttk.Entry(self.RightFrame, width=20)
    UpdateUserIdEntry.place(x=180, y=250)

    UpdatetButton = ttk.Button(self.RightFrame, text="Atualizar dados", command=self.action_update_client)
    UpdatetButton.place(x=220, y=350)


    VoltarButton = ttk.Button(self.RightFrame, text="Voltar", command=self.options_client)
    VoltarButton.place(x=220, y=400)

  # Inserção e atualização dos dados do cliente
  def action_update_client(self):
    try:
      # Código de validação de login no BD
      Application.limpar(self)
      self.create_widgtes()
      self.create_logo_user()     

      ContinueLabel = tk.Label(self.RightFrame, text="Registro atualizado com sucesso!\nClique para continuar", bg="#F5F5F5")
      ContinueLabel.place(x=120, y=100)

      ContinueButton = ttk.Button(self.RightFrame, text="Continuar", width=30, command=self.options_client)
      ContinueButton.place(x=165, y=170)
    
    except:
      Application.limpar(self)
      self.create_widgtes()
      self.create_logo_user()

      ErrorLabel = tk.Label(self.RightFrame, text="Erro ao atualizar dados, tente novamente!", bg="#F5F5F5")
      ErrorLabel.place(x=120, y=100)
      AgainButton = ttk.Button(self.RightFrame, text="Tente novamente", command=self.update_client)
      AgainButton.place(x=120, y=150)

  # Registrar clientes
  def register_client(self):
    Application.limpar(self)
    self.create_widgtes()
    self.create_logo_user()

    SaveUserLabel = tk.Label(self.RightFrame, text="Usuário:", bg="#f5f5f5")
    SaveUserLabel.place(x=70, y=50)
    SaveUserEntry = ttk.Entry(self.RightFrame, width=20)
    SaveUserEntry.place(x=180, y=50)

    SaveContactLabel = tk.Label(self.RightFrame, text="Contato:", bg="#f5f5f5")
    SaveContactLabel.place(x=70, y=90)
    SaveContactEntry = ttk.Entry(self.RightFrame, width=20)
    SaveContactEntry.place(x=180, y=90)

    SaveTeamLabel = tk.Label(self.RightFrame, text="Time:", bg="#f5f5f5")
    SaveTeamLabel.place(x=70, y=130)
    SaveTeamEntry = ttk.Entry(self.RightFrame, width=20)
    SaveTeamEntry.place(x=180, y= 130)

    SaveAnimeLabel = tk.Label(self.RightFrame, text="Anime:", bg="#f5f5f5")
    SaveAnimeLabel.place(x=70, y=170)
    SaveAnimeEntry = ttk.Entry(self.RightFrame, width=20)
    SaveAnimeEntry.place(x=180, y=170)

    SaveAddressLabel = tk.Label(self.RightFrame, text="Endereço:", bg="#f5f5f5")
    SaveAddressLabel.place(x=70, y=210)
    SaveAdressEntry= ttk.Entry(self.RightFrame, width=20)
    SaveAdressEntry.place(x=180, y=210)

    SaveUserIdLabel = tk.Label(self.RightFrame, text="ID:", bg="#f5f5f5")
    SaveUserIdLabel.place(x=70, y = 250)
    SaveUserIdEntry = ttk.Entry(self.RightFrame, width=20)
    SaveUserIdEntry.place(x=180, y=250)

    SavetButton = ttk.Button(self.RightFrame, text="Salvar dados", command=self.action_register_client)
    SavetButton.place(x=220, y=350)

    VoltarButton = ttk.Button(self.RightFrame, text="Voltar", command=self.client)
    VoltarButton.place(x=220, y=400)

  # Inserção e registro dos dados dos clientes
  def action_register_client(self):
    try:
      # Código de validação de login no BD
      Application.limpar(self)
      self.create_widgtes()
      self.create_logo_user()     

      ContinueLabel = tk.Label(self.RightFrame, text="Registro salvo com sucesso!\nClique para continuar", bg="#F5F5F5")
      ContinueLabel.place(x=120, y=100)

      ContinueButton = ttk.Button(self.RightFrame, text="Continuar", width=30, command=self.client)
      ContinueButton.place(x=165, y=170)
    
    except:
      Application.limpar(self)
      self.create_widgtes()
      self.create_logo_user()

      ErrorLabel = tk.Label(self.RightFrame, text="Erro ao salvar dados, tente novamente!", bg="#F5F5F5")
      ErrorLabel.place(x=120, y=100)
      AgainButton = ttk.Button(self.RightFrame, text="Tente novamente", command=self.register_client)
      AgainButton.place(x=120, y=150)

  # Módulo de vendas do cliente
  def sales_client(self):
    Application.limpar(self)
    self.create_widgtes()
    self.create_logo_user
  
  # Início do loop do administrador
  def admin(self):
    Application.limpar(self)
    self.create_widgtes()
    self.create_logo_adm()

    UserLabel = tk.Label(self.RightFrame, text="Usuário:", bg="#F5F5F5")
    UserLabel.place(x=70, y=50)

    UserEntry = ttk.Entry(self.RightFrame, width=20)
    UserEntry.place(x=180, y=50)

    PassLabel = tk.Label(self.RightFrame, text="Senha:", bg="#F5F5F5")
    PassLabel.place(x=70, y=100)

    PassEntry = ttk.Entry(self.RightFrame, width=20)
    PassEntry.place(x=180, y=100)

    LoginButton = ttk.Button(self.RightFrame, text="Login", width=20, command = self.action_login_adm)
    LoginButton.place(x=180, y=140)

    AdviceLabel = tk.Label(self.RightFrame, text="Clique abaixo para registrar-se!", bg="#F5F5F5")
    AdviceLabel.place(x=130, y=200)

    RegisterButton = ttk.Button(self.RightFrame, text="Registrar", width=30, command=self.register_adm)
    RegisterButton.place(x=160, y=250)

    VoltarButton = ttk.Button(self.RightFrame, text="Voltar", command=self.inicio)
    VoltarButton.place(x=220, y=400)
    
  def register_adm(self):
    ...


if __name__ == "__main__":
    app = Application()