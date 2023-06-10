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
    self.logo_manager = PhotoImage(file="icons/manager.png")
    self.logo_seller = PhotoImage(file="icons/seller.png")

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
  
  def create_logo_manager(self):
    self.LogoLabel = Label(self.LeftFrame, image=self.logo_manager, bg="#DDDDE7")
    self.LogoLabel.place(x=25, y=125)

  def create_logo_seller(self):
    self.LogoLabel = Label(self.LeftFrame, image=self.logo_seller, bg="#DDDDE7")
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

    ButtonManager = ttk.Button(self.RightFrame, text="Gerente", width=35, command = self.manager)
    ButtonManager.place(x=150, y=290)

    ButtonSeller = ttk.Button(self.RightFrame, text="Vendedor", width=35, command = self.seller)
    ButtonSeller.place(x=150, y=350)

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

    VoltarButton = ttk.Button(self.RightFrame, text="Voltar", command=self.inicio)
    VoltarButton.place(x=220, y=400)

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

    UpdateUserLabel = tk.Label(self.RightFrame, text="Nome Completo:", bg="#f5f5f5")
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

    SaveUserLabel = tk.Label(self.RightFrame, text="Nome completo:", bg="#f5f5f5")
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
  # Fim do loop do cliente

  #---------------------------------------------------------------#
  
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

    VoltarButton = ttk.Button(self.RightFrame, text="Voltar", command=self.inicio)
    VoltarButton.place(x=220, y=400)
  
  # Tentativa de login do adm
  def action_login_adm(self):
    try:
      # Código de validação de login no BD
      Application.limpar(self)
      self.create_widgtes()
      self.create_logo_adm()     

      ContinueLabel = tk.Label(self.RightFrame, text="Login realizado com sucesso!\nClique para continuar", bg="#F5F5F5")
      ContinueLabel.place(x=120, y=100)

      ContinueButton = ttk.Button(self.RightFrame, text="Continuar", width=30, command=self.options_adm)
      ContinueButton.place(x=165, y=170)
    
    except:
      Application.limpar(self)
      self.create_widgtes()
      self.create_logo_adm()

      ErrorLabel = tk.Label(self.RightFrame, text="Erro ao fazer login, tente novamente!", bg="#F5F5F5")
      ErrorLabel.place(x=120, y=100)
      AgainButton = ttk.Button(self.RightFrame, text="Tente novamente", command=self.admin)
      AgainButton.place(x=120, y=150)

  # Exibição das opções do adm
  def options_adm(self):
    Application.limpar(self)
    self.create_widgtes()
    self.create_logo_adm()

    TextLabel = tk.Label(self.RightFrame, text="Selecione a opção desejada", bg="#F5F5F5")
    TextLabel.place(x=120, y=100)

    BuyButton = ttk.Button(self.RightFrame, text="Cadastrar novo gerente", command=self.register_manager)
    BuyButton.place(x=120, y=150)

    UpdateButton = ttk.Button(self.RightFrame, text="Gerenciar gerentes", command=self.list_manager)
    UpdateButton.place(x=120, y=200)

    VoltarButton = ttk.Button(self.RightFrame, text="Voltar", command=self.admin)
    VoltarButton.place(x=120, y=400)

  # Exibição das opções para registro de gerente
  def register_manager(self):
    Application.limpar(self)
    self.create_widgtes()
    self.create_logo_adm()

    SaveAdmLabel = tk.Label(self.RightFrame, text="Nome completo:", bg="#f5f5f5")
    SaveAdmLabel.place(x=70, y=50)
    SaveAdmEntry = ttk.Entry(self.RightFrame, width=20)
    SaveAdmEntry.place(x=180, y=50)

    SaveContactLabel = tk.Label(self.RightFrame, text="Contato:", bg="#f5f5f5")
    SaveContactLabel.place(x=70, y=90)
    SaveContactEntry = ttk.Entry(self.RightFrame, width=20)
    SaveContactEntry.place(x=180, y=90)

    SaveUserIdLabel = tk.Label(self.RightFrame, text="ID:", bg="#f5f5f5")
    SaveUserIdLabel.place(x=70, y = 130)
    SaveUserIdEntry = ttk.Entry(self.RightFrame, width=20)
    SaveUserIdEntry.place(x=180, y=130)

    SaveStockLabel = tk.Label(self.RightFrame, text="Estoque responsável:", bg="#f5f5f5")
    SaveStockLabel.place(x=70, y=170)
    SaveStockEntry = ttk.Entry(self.RightFrame, width=20)
    SaveStockEntry.place(x=180, y= 170)

    SavePassLabel = tk.Label(self.RightFrame, text="Senha:", bg="#f5f5f5")
    SavePassLabel.place(x=70, y=210)
    SavePassEntry = ttk.Entry(self.RightFrame, width=20)
    SavePassEntry.place(x=180, y= 210)   

    SavetButton = ttk.Button(self.RightFrame, text="Salvar dados", command=self.action_register_manager)
    SavetButton.place(x=220, y=350)

    VoltarButton = ttk.Button(self.RightFrame, text="Voltar", command=self.admin)
    VoltarButton.place(x=220, y=400)

  # Tentativa de registro de gerente
  def action_register_manager(self):
    try:
      # Código de validação de login no BD
      Application.limpar(self)
      self.create_widgtes()
      self.create_logo_adm()     

      ContinueLabel = tk.Label(self.RightFrame, text="Gerente salvo com sucesso!\nClique para continuar", bg="#F5F5F5")
      ContinueLabel.place(x=120, y=100)

      ContinueButton = ttk.Button(self.RightFrame, text="Continuar", width=30, command=self.options_adm)
      ContinueButton.place(x=165, y=170)
    
    except:
      Application.limpar(self)
      self.create_widgtes()
      self.create_logo_adm()

      ErrorLabel = tk.Label(self.RightFrame, text="Erro ao salvar dados, tente novamente!", bg="#F5F5F5")
      ErrorLabel.place(x=120, y=100)
      AgainButton = ttk.Button(self.RightFrame, text="Tente novamente", command=self.register_manager)
      AgainButton.place(x=120, y=150)

  # Exibição das opções para atualização de gerente
  def update_manager(self):
    Application.limpar(self)
    self.create_widgtes()
    self.create_logo_adm()

    UpdateAdmLabel = tk.Label(self.RightFrame, text="Nome completo:", bg="#f5f5f5")
    UpdateAdmLabel.place(x=70, y=50)
    UpdateAdmEntry = ttk.Entry(self.RightFrame, width=20)
    UpdateAdmEntry.place(x=180, y=50)

    UpdateContactLabel = tk.Label(self.RightFrame, text="Contato:", bg="#f5f5f5")
    UpdateContactLabel.place(x=70, y=90)
    UpdateContactEntry = ttk.Entry(self.RightFrame, width=20)
    UpdateContactEntry.place(x=180, y=90)

    UpdateUserIdLabel = tk.Label(self.RightFrame, text="ID:", bg="#f5f5f5")
    UpdateUserIdLabel.place(x=70, y = 130)
    UpdateUserIdEntry = ttk.Entry(self.RightFrame, width=20)
    UpdateUserIdEntry.place(x=180, y=130)

    UpdateStockLabel = tk.Label(self.RightFrame, text="Estoque responsável:", bg="#f5f5f5")
    UpdateStockLabel.place(x=70, y=170)
    UpdateStockEntry = ttk.Entry(self.RightFrame, width=20)
    UpdateStockEntry.place(x=180, y= 170)

    UpdatePassLabel = tk.Label(self.RightFrame, text="Senha:", bg="#f5f5f5")
    UpdatePassLabel.place(x=70, y=210)
    UpdatePassEntry = ttk.Entry(self.RightFrame, width=20)
    UpdatePassEntry.place(x=180, y= 210)   

    UpdateButton = ttk.Button(self.RightFrame, text="Atualizar dados", command=self.action_update_manager)
    UpdateButton.place(x=220, y=350)

    VoltarButton = ttk.Button(self.RightFrame, text="Voltar", command=self.client)
    VoltarButton.place(x=220, y=400)
    
  # Tentativa de atualização de gerente
  def action_update_manager(self):
    try:
      # Código de validação de login no BD
      Application.limpar(self)
      self.create_widgtes()
      self.create_logo_adm()     

      ContinueLabel = tk.Label(self.RightFrame, text="Gerente atualizado com sucesso!\nClique para continuar", bg="#F5F5F5")
      ContinueLabel.place(x=120, y=100)

      ContinueButton = ttk.Button(self.RightFrame, text="Continuar", width=30, command=self.options_adm)
      ContinueButton.place(x=165, y=170)
    
    except:
      Application.limpar(self)
      self.create_widgtes()
      self.create_logo_adm()

      ErrorLabel = tk.Label(self.RightFrame, text="Erro ao atualizar dados, tente novamente!", bg="#F5F5F5")
      ErrorLabel.place(x=120, y=100)
      AgainButton = ttk.Button(self.RightFrame, text="Tente novamente", command=self.update_manager)
      AgainButton.place(x=120, y=150)

  # Tentativa de remoção de gerente
  def action_remove_manager(self):
    try:
      # Código de validação de login no BD
      Application.limpar(self)
      self.create_widgtes()
      self.create_logo_adm()     

      ContinueLabel = tk.Label(self.RightFrame, text="Gerente removido com sucesso!\nClique para continuar", bg="#F5F5F5")
      ContinueLabel.place(x=120, y=100)

      ContinueButton = ttk.Button(self.RightFrame, text="Continuar", width=30, command=self.options_adm)
      ContinueButton.place(x=165, y=170)
    
    except:
      Application.limpar(self)
      self.create_widgtes()
      self.create_logo_adm()

      ErrorLabel = tk.Label(self.RightFrame, text="Erro ao remover dados, tente novamente!", bg="#F5F5F5")
      ErrorLabel.place(x=120, y=100)
      AgainButton = ttk.Button(self.RightFrame, text="Tente novamente", command=self.update_manager)
      AgainButton.place(x=120, y=150)

  # Listagem de gerentes
  def list_manager(self):
    # gerenciador = Gerenciador()
    # gerentes = gerenciador.listar_gerentes()
    
    Application.limpar(self)
    self.create_widgtes()
    self.create_logo_adm()

    text_label = tk.Label(self.window, text="Gerentes cadastrados:",  padx=10, pady=10)
    text_label.pack()

    # Criação da barra de rolagem
    scrollbar = ttk.Scrollbar(self.RightFrame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
    # Criação da lista de resultados
    lista_gerentes = tk.Listbox(self.window, yscrollcommand=scrollbar.set, justify='center')
    # lista_gerentes.pack(side=tk.LEFT, fill=tk.X, expand=True)
    lista_gerentes.pack(fill="x", expand=1)
    
    # for gerente in gerentes:
    #   lista_gerentes.insert(tk.END, gerente)

    def mostrar_gerente_selecionado():
      selected_item = lista_gerentes.get(tk.ACTIVE)
      
      Application.limpar(self)
      self.create_widgtes()
      self.create_logo_adm()
      
      item_label = tk.Label(self.RightFrame, text="Gerente selecionado:", font="Helvetica", padx=10, pady=10)
      item_label.pack()
          
      item_text = tk.Label(self.RightFrame, text=f"Id: {selected_item[0]}\nNome: {selected_item[1]}\Contato: {selected_item[2]}:\nEstoques vinculados: {selected_item[3]}", font="Helvetica", padx=10, pady=10)
      item_text.pack()

      alterar_button = tk.Button(self.RightFrame, text="Alterar", command=lambda: self.update_manager(selected_item))
      alterar_button.pack(pady=10)

      Remover_button = tk.Button(self.RightFrame, text="Remover", command=lambda: self.action_remove_manager(selected_item))
      Remover_button.pack(pady=10)
      
      voltar_button = tk.Button(self.RightFrame, text="Voltar", command=self.list_manager)
      voltar_button.pack(pady=10)
    
    lista_gerentes.bind("<Double-Button-1>", lambda event: mostrar_gerente_selecionado())

    scrollbar.config(command=lista_gerentes.yview)

    voltar_button = ttk.Button(self.window, text="Voltar", command=self.options_adm)
    voltar_button.place(x=500,y=400)
  # Fim do loop do administrador

  #---------------------------------------------------------------#

  # Início do loop de gerente
  def manager(self):
    Application.limpar(self)
    self.create_widgtes()
    self.create_logo_manager()

    UserLabel = tk.Label(self.RightFrame, text="Usuário:", bg="#F5F5F5")
    UserLabel.place(x=70, y=50)

    UserEntry = ttk.Entry(self.RightFrame, width=20)
    UserEntry.place(x=180, y=50)

    PassLabel = tk.Label(self.RightFrame, text="Senha:", bg="#F5F5F5")
    PassLabel.place(x=70, y=100)

    PassEntry = ttk.Entry(self.RightFrame, width=20)
    PassEntry.place(x=180, y=100)

    LoginButton = ttk.Button(self.RightFrame, text="Login", width=20, command = self.action_login_manager)
    LoginButton.place(x=180, y=140)

    VoltarButton = ttk.Button(self.RightFrame, text="Voltar", command=self.inicio)
    VoltarButton.place(x=220, y=400)

  # Tentativa de login do gerente
  def action_login_manager(self):
    Application.limpar(self)
    self.create_widgtes()
    self.create_logo_manager()

    try:
      # Código de validação de login no BD
      Application.limpar(self)
      self.create_widgtes()
      self.create_logo_manager()     

      ContinueLabel = tk.Label(self.RightFrame, text="Login realizado com sucesso!\nClique para continuar", bg="#F5F5F5")
      ContinueLabel.place(x=120, y=100)

      ContinueButton = ttk.Button(self.RightFrame, text="Continuar", width=30, command=self.options_manager)
      ContinueButton.place(x=165, y=170)
    
    except:
      Application.limpar(self)
      self.create_widgtes()
      self.create_logo_manager()

      ErrorLabel = tk.Label(self.RightFrame, text="Erro ao fazer login, tente novamente!", bg="#F5F5F5")
      ErrorLabel.place(x=120, y=100)
      AgainButton = ttk.Button(self.RightFrame, text="Tente novamente", command=self.manager)
      AgainButton.place(x=120, y=150)

  # Exibição das opções do gerente
  def options_manager(self):
    Application.limpar(self)
    self.create_widgtes()
    self.create_logo_manager()

    TextLabel = tk.Label(self.RightFrame, text="Selecione a opção desejada", bg="#F5F5F5")
    TextLabel.place(x=120, y=100)

    SellerButton = ttk.Button(self.RightFrame, text="Cadastrar novo vendedor", command=self.register_seller)
    SellerButton.place(x=120, y=150)

    UpdateSellerButton = ttk.Button(self.RightFrame, text="Gerenciar vendedores", command=self.list_seller)
    UpdateSellerButton.place(x=120, y=200)

    StockButton = ttk.Button(self.RightFrame, text="Cadastrar novo estoque", command=self.register_stock)
    StockButton.place(x=120, y=250)

    UpdateStockButton = ttk.Button(self.RightFrame, text="Gerenciar estoques", command=self.list_stock)
    UpdateStockButton.place(x=120, y=300)

    VoltarButton = ttk.Button(self.RightFrame, text="Voltar", command=self.manager)
    VoltarButton.place(x=120, y=400)

  # Exibição das opções para registro de vendedores
  def register_seller(self):
    Application.limpar(self)
    self.create_widgtes()
    self.create_logo_manager()
    
    SaveAdmLabel = tk.Label(self.RightFrame, text="Nome completo:", bg="#f5f5f5")
    SaveAdmLabel.place(x=70, y=50)
    SaveAdmEntry = ttk.Entry(self.RightFrame, width=20)
    SaveAdmEntry.place(x=180, y=50)

    SaveContactLabel = tk.Label(self.RightFrame, text="Contato:", bg="#f5f5f5")
    SaveContactLabel.place(x=70, y=90)
    SaveContactEntry = ttk.Entry(self.RightFrame, width=20)
    SaveContactEntry.place(x=180, y=90)

    SaveUserIdLabel = tk.Label(self.RightFrame, text="ID:", bg="#f5f5f5")
    SaveUserIdLabel.place(x=70, y = 130)
    SaveUserIdEntry = ttk.Entry(self.RightFrame, width=20)
    SaveUserIdEntry.place(x=180, y=130)

    SaveStockLabel = tk.Label(self.RightFrame, text="Estoque vinculado:", bg="#f5f5f5")
    SaveStockLabel.place(x=70, y=170)
    SaveStockEntry = ttk.Entry(self.RightFrame, width=20)
    SaveStockEntry.place(x=180, y= 170)

    SavePassLabel = tk.Label(self.RightFrame, text="Senha:", bg="#f5f5f5")
    SavePassLabel.place(x=70, y=210)
    SavePassEntry = ttk.Entry(self.RightFrame, width=20)
    SavePassEntry.place(x=180, y= 210)   

    SavetButton = ttk.Button(self.RightFrame, text="Salvar dados", command=self.action_register_seller)
    SavetButton.place(x=220, y=350)

    VoltarButton = ttk.Button(self.RightFrame, text="Voltar", command=self.options_manager)
    VoltarButton.place(x=220, y=400)

  # Tentativa de registro de vendedor
  def action_register_seller(self):
    try:
      # Código de validação de login no BD
      Application.limpar(self)
      self.create_widgtes()
      self.create_logo_manager()     

      ContinueLabel = tk.Label(self.RightFrame, text="Vendedor salvo com sucesso!\nClique para continuar", bg="#F5F5F5")
      ContinueLabel.place(x=120, y=100)

      ContinueButton = ttk.Button(self.RightFrame, text="Continuar", width=30, command=self.options_manager)
      ContinueButton.place(x=165, y=170)
    
    except:
      Application.limpar(self)
      self.create_widgtes()
      self.create_logo_manager()

      ErrorLabel = tk.Label(self.RightFrame, text="Erro ao salvar dados, tente novamente!", bg="#F5F5F5")
      ErrorLabel.place(x=120, y=100)
      AgainButton = ttk.Button(self.RightFrame, text="Tente novamente", command=self.register_seller)
      AgainButton.place(x=120, y=150)

  # Listagem de vendedores
  def list_seller(self):
    Application.limpar(self)
    self.create_widgtes()
    self.create_logo_manager()

    # gerenciador = Gerenciador()
    # vendedores = gerenciador.listar_vendedores()

    text_label = tk.Label(self.window, text="Vendedores cadastrados:",  padx=10, pady=10)
    text_label.pack()

    # Criação da barra de rolagem
    scrollbar = ttk.Scrollbar(self.RightFrame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
    # Criação da lista de resultados
    lista_vendedores = tk.Listbox(self.window, yscrollcommand=scrollbar.set, justify='center')
    # lista_vendedpres.pack(side=tk.LEFT, fill=tk.X, expand=True)
    lista_vendedores.pack(fill="x", expand=1)
    
    # for vendedor in vendedores:
    #   lista_vendedores.insert(tk.END, gerente)

    def mostrar_vendedor_selecionado():
      selected_item = lista_vendedores.get(tk.ACTIVE)
      
      Application.limpar(self)
      self.create_widgtes()
      self.create_logo_manager()
      
      item_label = tk.Label(self.RightFrame, text="Vendedor selecionado:", font="Helvetica", padx=10, pady=10)
      item_label.pack()
          
      item_text = tk.Label(self.RightFrame, text=f"Id: {selected_item[0]}\nNome: {selected_item[1]}\Contato: {selected_item[2]}:\nEstoques vinculados: {selected_item[3]}", font="Helvetica", padx=10, pady=10)
      item_text.pack()

      alterar_button = tk.Button(self.RightFrame, text="Alterar", command=lambda: self.update_seller(selected_item))
      alterar_button.pack(pady=10)

      Remover_button = tk.Button(self.RightFrame, text="Remover", command=lambda: self.action_remove_seller(selected_item))
      Remover_button.pack(pady=10)
      
      voltar_button = tk.Button(self.RightFrame, text="Voltar", command=self.list_seller)
      voltar_button.pack(pady=10)
    
    lista_vendedores.bind("<Double-Button-1>", lambda event: mostrar_vendedor_selecionado())

    scrollbar.config(command=lista_vendedores.yview)

    voltar_button = ttk.Button(self.window, text="Voltar", command=self.options_manager)
    voltar_button.place(x=500,y=400)
  
  # Exibição das opções de atualização de denvedor
  def update_seller(self):
    Application.limpar(self)
    self.create_widgtes()
    self.create_logo_manager()

    UpdateAdmLabel = tk.Label(self.RightFrame, text="Nome completo:", bg="#f5f5f5")
    UpdateAdmLabel.place(x=70, y=50)
    UpdateAdmEntry = ttk.Entry(self.RightFrame, width=20)
    UpdateAdmEntry.place(x=180, y=50)

    UpdateContactLabel = tk.Label(self.RightFrame, text="Contato:", bg="#f5f5f5")
    UpdateContactLabel.place(x=70, y=90)
    UpdateContactEntry = ttk.Entry(self.RightFrame, width=20)
    UpdateContactEntry.place(x=180, y=90)

    UpdateUserIdLabel = tk.Label(self.RightFrame, text="ID:", bg="#f5f5f5")
    UpdateUserIdLabel.place(x=70, y = 130)
    UpdateUserIdEntry = ttk.Entry(self.RightFrame, width=20)
    UpdateUserIdEntry.place(x=180, y=130)

    UpdateStockLabel = tk.Label(self.RightFrame, text="Estoque vinculado:", bg="#f5f5f5")
    UpdateStockLabel.place(x=70, y=170)
    UpdateStockEntry = ttk.Entry(self.RightFrame, width=20)
    UpdateStockEntry.place(x=180, y= 170)

    UpdatePassLabel = tk.Label(self.RightFrame, text="Senha:", bg="#f5f5f5")
    UpdatePassLabel.place(x=70, y=210)
    UpdatePassEntry = ttk.Entry(self.RightFrame, width=20)
    UpdatePassEntry.place(x=180, y= 210)   

    UpdateButton = ttk.Button(self.RightFrame, text="Atualizar dados", command=self.action_update_seller)
    UpdateButton.place(x=220, y=350)

    VoltarButton = ttk.Button(self.RightFrame, text="Voltar", command=self.client)
    VoltarButton.place(x=220, y=400)

  # Tentativa de atualização de vendedor
  def action_update_seller(self):
    try:
      # Código de validação de login no BD
      Application.limpar(self)
      self.create_widgtes()
      self.create_logo_manager()     

      ContinueLabel = tk.Label(self.RightFrame, text="Gerente atualizado com sucesso!\nClique para continuar", bg="#F5F5F5")
      ContinueLabel.place(x=120, y=100)

      ContinueButton = ttk.Button(self.RightFrame, text="Continuar", width=30, command=self.options_manager)
      ContinueButton.place(x=165, y=170)
    
    except:
      Application.limpar(self)
      self.create_widgtes()
      self.create_logo_manager()

      ErrorLabel = tk.Label(self.RightFrame, text="Erro ao atualizar dados, tente novamente!", bg="#F5F5F5")
      ErrorLabel.place(x=120, y=100)
      AgainButton = ttk.Button(self.RightFrame, text="Tente novamente", command=self.update_seller)
      AgainButton.place(x=120, y=150)
  
  # Tentativa de remoção de vendedor
  def action_remove_seller(self):
    try:
      # Código de validação de login no BD
      Application.limpar(self)
      self.create_widgtes()
      self.create_logo_manager()     

      ContinueLabel = tk.Label(self.RightFrame, text="Vendedor removido com sucesso!\nClique para continuar", bg="#F5F5F5")
      ContinueLabel.place(x=120, y=100)

      ContinueButton = ttk.Button(self.RightFrame, text="Continuar", width=30, command=self.options_manager)
      ContinueButton.place(x=165, y=170)
    
    except:
      Application.limpar(self)
      self.create_widgtes()
      self.create_logo_manager()

      ErrorLabel = tk.Label(self.RightFrame, text="Erro ao remover dados, tente novamente!", bg="#F5F5F5")
      ErrorLabel.place(x=120, y=100)
      AgainButton = ttk.Button(self.RightFrame, text="Tente novamente", command=self.update_seller)
      AgainButton.place(x=120, y=150)
  
  # Exibição das opções para registro de estoque
  def register_stock(self):
    Application.limpar(self)
    self.create_widgtes()
    self.create_logo_manager()
    
    SaveAdmLabel = tk.Label(self.RightFrame, text="Nome do estoque:", bg="#f5f5f5")
    SaveAdmLabel.place(x=70, y=50)
    SaveAdmEntry = ttk.Entry(self.RightFrame, width=20)
    SaveAdmEntry.place(x=180, y=50)

    SaveContactLabel = tk.Label(self.RightFrame, text="Localização:", bg="#f5f5f5")
    SaveContactLabel.place(x=70, y=90)
    SaveContactEntry = ttk.Entry(self.RightFrame, width=20)
    SaveContactEntry.place(x=180, y=90)

    SaveUserIdLabel = tk.Label(self.RightFrame, text="Gerente(s)", bg="#f5f5f5")
    SaveUserIdLabel.place(x=70, y = 130)
    SaveUserIdEntry = ttk.Entry(self.RightFrame, width=20)
    SaveUserIdEntry.place(x=180, y=130)

    SaveStockLabel = tk.Label(self.RightFrame, text="Data de reposição", bg="#f5f5f5")
    SaveStockLabel.place(x=70, y=170)
    SaveStockEntry = ttk.Entry(self.RightFrame, width=20)
    SaveStockEntry.place(x=180, y= 170)

    SavetButton = ttk.Button(self.RightFrame, text="Salvar dados", command=self.action_register_stock)
    SavetButton.place(x=220, y=350)

    VoltarButton = ttk.Button(self.RightFrame, text="Voltar", command=self.options_manager)
    VoltarButton.place(x=220, y=400)

  # Tentativa de registro de estoque
  def action_register_stock(self):
    try:
      # Código de validação de login no BD
      Application.limpar(self)
      self.create_widgtes()
      self.create_logo_manager()     

      ContinueLabel = tk.Label(self.RightFrame, text="Estoque salvo com sucesso!\nClique para continuar", bg="#F5F5F5")
      ContinueLabel.place(x=120, y=100)

      ContinueButton = ttk.Button(self.RightFrame, text="Continuar", width=30, command=self.options_manager)
      ContinueButton.place(x=165, y=170)
    
    except:
      Application.limpar(self)
      self.create_widgtes()
      self.create_logo_manager()

      ErrorLabel = tk.Label(self.RightFrame, text="Erro ao salvar dados, tente novamente!", bg="#F5F5F5")
      ErrorLabel.place(x=120, y=100)
      AgainButton = ttk.Button(self.RightFrame, text="Tente novamente", command=self.register_stock)
      AgainButton.place(x=120, y=150)

  # Listagem de estoque
  def list_stock(self):
    Application.limpar(self)
    self.create_widgtes()
    self.create_logo_manager()

    # gerenciador = Gerenciador()
    # estoques = gerenciador.listar_estoques()

    text_label = tk.Label(self.window, text="Estoques cadastrados:",  padx=10, pady=10)
    text_label.pack()

    # Criação da barra de rolagem
    scrollbar = ttk.Scrollbar(self.RightFrame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
    # Criação da lista de resultados
    lista_estoques = tk.Listbox(self.window, yscrollcommand=scrollbar.set, justify='center')
    # lista_estoques.pack(side=tk.LEFT, fill=tk.X, expand=True)
    lista_estoques.pack(fill="x", expand=1)
    
    # for estoque in estoques:
    #   lista_estoques.insert(tk.END, lista_estoques)

    def mostrar_estoque_selecionado():
      selected_item = lista_estoques.get(tk.ACTIVE)
      
      Application.limpar(self)
      self.create_widgtes()
      self.create_logo_manager()
      
      item_label = tk.Label(self.RightFrame, text="Estoque selecionado:", font="Helvetica", padx=10, pady=10)
      item_label.pack()
          
      item_text = tk.Label(self.RightFrame, text=f"Nome: {selected_item[0]}\nLocalização: {selected_item[1]}\Gerente(s): {selected_item[2]}:\nData de reposição: {selected_item[3]}", font="Helvetica", padx=10, pady=10)
      item_text.pack()

      alterar_button = tk.Button(self.RightFrame, text="Alterar", command=lambda: self.update_stock(selected_item))
      alterar_button.pack(pady=10)

      Remover_button = tk.Button(self.RightFrame, text="Remover", command=lambda: self.action_remove_stock(selected_item))
      Remover_button.pack(pady=10)
      
      voltar_button = tk.Button(self.RightFrame, text="Voltar", command=self.list_stock)
      voltar_button.pack(pady=10)
    
    lista_estoques.bind("<Double-Button-1>", lambda event: mostrar_estoque_selecionado())

    scrollbar.config(command=lista_estoques.yview)

    voltar_button = ttk.Button(self.window, text="Voltar", command=self.options_manager)
    voltar_button.place(x=500,y=400)

  # Exibição das opções da atualização de estoque
  
  def update_stock(self):
    Application.limpar(self)
    self.create_widgtes()
    self.create_logo_manager()
    
    SaveAdmLabel = tk.Label(self.RightFrame, text="Nome do estoque:", bg="#f5f5f5")
    SaveAdmLabel.place(x=70, y=50)
    SaveAdmEntry = ttk.Entry(self.RightFrame, width=20)
    SaveAdmEntry.place(x=180, y=50)

    SaveContactLabel = tk.Label(self.RightFrame, text="Localização:", bg="#f5f5f5")
    SaveContactLabel.place(x=70, y=90)
    SaveContactEntry = ttk.Entry(self.RightFrame, width=20)
    SaveContactEntry.place(x=180, y=90)

    SaveUserIdLabel = tk.Label(self.RightFrame, text="Gerente(s)", bg="#f5f5f5")
    SaveUserIdLabel.place(x=70, y = 130)
    SaveUserIdEntry = ttk.Entry(self.RightFrame, width=20)
    SaveUserIdEntry.place(x=180, y=130)

    SaveStockLabel = tk.Label(self.RightFrame, text="Data de reposição", bg="#f5f5f5")
    SaveStockLabel.place(x=70, y=170)
    SaveStockEntry = ttk.Entry(self.RightFrame, width=20)
    SaveStockEntry.place(x=180, y= 170)

    SavetButton = ttk.Button(self.RightFrame, text="Salvar dados", command=self.action_update_stock)
    SavetButton.place(x=220, y=350)

    VoltarButton = ttk.Button(self.RightFrame, text="Voltar", command=self.options_manager)
    VoltarButton.place(x=220, y=400)

  # Tentativa de atualização do estoque
  def action_update_stock(self):
    try:
      # Código de validação de login no BD
      Application.limpar(self)
      self.create_widgtes()
      self.create_logo_manager()     

      ContinueLabel = tk.Label(self.RightFrame, text="Estoque atualizado com sucesso!\nClique para continuar", bg="#F5F5F5")
      ContinueLabel.place(x=120, y=100)

      ContinueButton = ttk.Button(self.RightFrame, text="Continuar", width=30, command=self.options_manager)
      ContinueButton.place(x=165, y=170)
    
    except:
      Application.limpar(self)
      self.create_widgtes()
      self.create_logo_manager()

      ErrorLabel = tk.Label(self.RightFrame, text="Erro ao atualizar dados, tente novamente!", bg="#F5F5F5")
      ErrorLabel.place(x=120, y=100)
      AgainButton = ttk.Button(self.RightFrame, text="Tente novamente", command=self.update_stock)
      AgainButton.place(x=120, y=150)

  # Tentativa de remoção do estoque
  def action_remove_stock(self):
    try:
      # Código de validação de login no BD
      Application.limpar(self)
      self.create_widgtes()
      self.create_logo_manager()     

      ContinueLabel = tk.Label(self.RightFrame, text="Estoque removido com sucesso!\nClique para continuar", bg="#F5F5F5")
      ContinueLabel.place(x=120, y=100)

      ContinueButton = ttk.Button(self.RightFrame, text="Continuar", width=30, command=self.options_manager)
      ContinueButton.place(x=165, y=170)
    
    except:
      Application.limpar(self)
      self.create_widgtes()
      self.create_logo_manager()

      ErrorLabel = tk.Label(self.RightFrame, text="Erro ao remover dados, tente novamente!", bg="#F5F5F5")
      ErrorLabel.place(x=120, y=100)
      AgainButton = ttk.Button(self.RightFrame, text="Tente novamente", command=self.update_stock)
      AgainButton.place(x=120, y=150)
  # Fim do loop de gerente

  #---------------------------------------------------------------#
  
  # Início do loop de vendedor
  def seller(self):
    Application.limpar(self)
    self.create_widgtes()
    self.create_logo_seller()

    




if __name__ == "__main__":
  app = Application()