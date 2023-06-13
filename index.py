import tkinter as tk
from classes import *
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import font
import random
from datetime import datetime

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
    
     # Criar o menu "Arquivo"
    barra_menu = tk.Menu(self.window)
    menu_arquivo = tk.Menu(barra_menu, tearoff=0)
    menu_arquivo.add_command(label="Login",font=8,command=self.admin)
    menu_arquivo.add_command(label="Relatorio Gereral",font=8)
    menu_arquivo.add_separator()
    menu_arquivo.add_command(label="Sair", command=self.window,font=8)

    # Adicionar o menu "Arquivo" à barra de menu
    barra_menu.add_cascade(label="Gerencia", menu=menu_arquivo)
    # Adicionar a barra de menu à janela
    self.window.config(menu=barra_menu)
    
    # Textos
    text_font = font.Font(family="Helvetica", size=self.default_font.cget("size") + 4,weight="bold")
    SysLabel = tk.Label(self.RightFrame, text="Seja bem-vindo!", font=text_font, bg="#F5F5F5")
    SysLabel.place(x=140, y=30)

    DescLabel = tk.Label(self.RightFrame, text="Faça login ou inicie suas compras", font=text_font, bg="#F5F5F5")
    DescLabel.place(x=70, y=80)

    ButtonClient = ttk.Button(self.RightFrame, text="Login", width=35, command=self.client)
    ButtonClient.place(x=150, y=170)

    ButtonAdmin = ttk.Button(self.RightFrame, text="Iniciar compras", width=35, command=self.sales_client)
    ButtonAdmin.place(x=150, y=230)
  # Início do loop do cliente
  def client(self):
    Application.limpar(self)
    self.create_widgtes()
    self.create_logo_user()
  
    UserLabel = tk.Label(self.RightFrame, text="Usuário:", bg="#F5F5F5")
    UserLabel.place(x=70, y=50)

    self.UserEntry_Client = ttk.Entry(self.RightFrame, width=20)
    self.UserEntry_Client.place(x=180, y=50)

    PassLabel = tk.Label(self.RightFrame, text="Senha:", bg="#F5F5F5")
    PassLabel.place(x=70, y=100)

    self.PassEntry_Client = ttk.Entry(self.RightFrame, width=20)
    self.PassEntry_Client.place(x=180, y=100)


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
    user = self.UserEntry_Client.get()
    password = self.PassEntry_Client.get()
    autenticado = Usuarios.autenticar_usuario(user, password)
    if autenticado:
      Application.limpar(self)
      self.create_widgtes()
      self.create_logo_user()     

      ContinueLabel = tk.Label(self.RightFrame, text="Login realizado com sucesso!\nClique para continuar", bg="#F5F5F5")
      ContinueLabel.place(x=120, y=100)

      ContinueButton = ttk.Button(self.RightFrame, text="Continuar", width=30, command=lambda: self.options_client(user,password))
      ContinueButton.place(x=165, y=170)
      
    else:
      Application.limpar(self)
      self.create_widgtes()
      self.create_logo_user()

      ErrorLabel = tk.Label(self.RightFrame, text="Erro ao fazer login, tente novamente!", bg="#F5F5F5")
      ErrorLabel.place(x=120, y=100)
      AgainButton = ttk.Button(self.RightFrame, text="Tente novamente", command=self.client)
      AgainButton.place(x=120, y=150)
 # Exibição das opções do cliente
  def options_client(self,usuario_logado,senha_logada):
    Application.limpar(self)
    self.create_widgtes()
    self.create_logo_user()

    TextLabel = tk.Label(self.RightFrame, text="Selecione a opção desejada", bg="#F5F5F5")
    TextLabel.place(x=120, y=100)

    BuyButton = ttk.Button(self.RightFrame, text="Seção de compras", command=self.sales_client)
    BuyButton.place(x=120, y=150)

    UpdateButton = ttk.Button(self.RightFrame, text="Atualize seu usuário", command=lambda: self.update_client(usuario_logado,senha_logada))
    UpdateButton.place(x=120, y=200)

    VoltarButton = ttk.Button(self.RightFrame, text="Voltar", command=self.client)
    VoltarButton.place(x=120, y=400)

  # Opção de atualizar as informações do cliente
  def update_client(self, usuario_logado,senha_logada):
    Application.limpar(self)
    self.create_widgtes()
    self.create_logo_user()
    
    info_cliente= Clientes.pesquisar_cleinte_por_usuario(usuario_logado)
    
    self.UpdateID = info_cliente[0]
    self.UpdateOldUsuario = usuario_logado
    self.UpdateOldSenha = senha_logada
    
    UpdateUserLabel = tk.Label(self.RightFrame, text="Nome:", bg="#f5f5f5")
    UpdateUserLabel.place(x=70, y=50)
    self.UpdateUserEntry = ttk.Entry(self.RightFrame, width=20)
    self.UpdateUserEntry.insert(tk.END, info_cliente[1])
    self.UpdateUserEntry.place(x=180, y=50)

    UpdateContactLabel = tk.Label(self.RightFrame, text="Contato:", bg="#f5f5f5")
    UpdateContactLabel.place(x=70, y=90)
    self.UpdateContactEntry = ttk.Entry(self.RightFrame, width=20)
    self.UpdateContactEntry.insert(tk.END, info_cliente[2])
    self.UpdateContactEntry.place(x=180, y=90)

    UpdateTeamLabel = tk.Label(self.RightFrame, text="Time:", bg="#f5f5f5")
    UpdateTeamLabel.place(x=70, y=130)
    self.UpdateTeamEntry = ttk.Entry(self.RightFrame, width=20)
    self.UpdateTeamEntry.insert(tk.END, info_cliente[3])
    self.UpdateTeamEntry.place(x=180, y= 130)

    UpdateAnimeLabel = tk.Label(self.RightFrame, text="Anime:", bg="#f5f5f5")
    UpdateAnimeLabel.place(x=70, y=170)
    self.UpdateAnimeEntry = ttk.Entry(self.RightFrame, width=20)
    self.UpdateAnimeEntry.insert(tk.END, info_cliente[4])
    self.UpdateAnimeEntry.place(x=180, y=170)

    UpdateAddressLabel = tk.Label(self.RightFrame, text="Endereço:", bg="#f4f4f4")
    UpdateAddressLabel.place(x=70, y=210)
    self.UpdateAdressEntry= ttk.Entry(self.RightFrame, width=20)
    self.UpdateAdressEntry.insert(tk.END, info_cliente[5])
    self.UpdateAdressEntry.place(x=180, y=210)

    UpdateUsuarioLabel = tk.Label(self.RightFrame, text="usuario:", bg="#f5f5f5")
    UpdateUsuarioLabel.place(x=70, y = 250)
    self.UpdateUsuarioEntry = ttk.Entry(self.RightFrame, width=20)
    self.UpdateUsuarioEntry.insert(tk.END, usuario_logado)
    self.UpdateUsuarioEntry.place(x=180, y=250)
    
    UpdateUserSenhaLabel = tk.Label(self.RightFrame, text="Senha:", bg="#f5f5f5")
    UpdateUserSenhaLabel.place(x=70, y = 290)
    self.UpdateUserSenhaEntry = ttk.Entry(self.RightFrame, width=20)
    self.UpdateUserSenhaEntry.insert(tk.END, senha_logada)
    self.UpdateUserSenhaEntry.place(x=180, y=290)

    UpdatetButton = ttk.Button(self.RightFrame, text="Atualizar dados", command=self.action_update_client)
    UpdatetButton.place(x=220, y=350)


    VoltarButton = ttk.Button(self.RightFrame, text="Voltar", command=lambda: self.options_client(usuario_logado,senha_logada))
    VoltarButton.place(x=220, y=400)

  # Inserção e atualização dos dados do cliente
  def action_update_client(self):
    print(self.UpdateID)
    try:
      Clientes.alterar_Clientes(self.UpdateID,self.UpdateUserEntry.get(),self.UpdateContactEntry.get(),self.UpdateTeamEntry.get(),self.UpdateAnimeEntry.get(), self.UpdateAdressEntry.get(),self.UpdateOldUsuario,self.UpdateUsuarioEntry.get(),self.UpdateUserSenhaEntry.get())  
      Application.limpar(self)
      self.create_widgtes()
      self.create_logo_user()     

      ContinueLabel = tk.Label(self.RightFrame, text="Registro atualizado com sucesso!\nClique para continuar", bg="#F5F5F5")
      ContinueLabel.place(x=120, y=100)

      ContinueButton = ttk.Button(self.RightFrame, text="Continuar", width=30, command=lambda: self.options_client(self.UpdateUsuarioEntry.get(),self.UpdateUserSenhaEntry.get()))
      ContinueButton.place(x=165, y=170)
    
    except:
      Application.limpar(self)
      self.create_widgtes()
      self.create_logo_user()

      ErrorLabel = tk.Label(self.RightFrame, text="Erro ao atualizar dados, tente novamente!", bg="#F5F5F5")
      ErrorLabel.place(x=120, y=100)
      AgainButton = ttk.Button(self.RightFrame, text="Tente novamente", command=lambda: self.update_client(self.UpdateOldUsuario,self.UpdateOldSenha))
      AgainButton.place(x=120, y=150)
      
  # Registrar clientes
  def register_client(self):
    Application.limpar(self)
    self.create_widgtes()
    self.create_logo_user()

    SaveUserLabel = tk.Label(self.RightFrame, text="Nome completo:", bg="#f5f5f5")
    SaveUserLabel.place(x=20, y=50)
    self.SaveUserEntry = ttk.Entry(self.RightFrame, width=20)
    self.SaveUserEntry.place(x=180, y=50)

    SaveContactLabel = tk.Label(self.RightFrame, text="Contato:", bg="#f5f5f5")
    SaveContactLabel.place(x=70, y=90)
    self.SaveContactEntry = ttk.Entry(self.RightFrame, width=20)
    self.SaveContactEntry.place(x=180, y=90)

    SaveTeamLabel = tk.Label(self.RightFrame, text="Time:", bg="#f5f5f5")
    SaveTeamLabel.place(x=70, y=130)
    self.SaveTeamEntry = ttk.Entry(self.RightFrame, width=20)
    self.SaveTeamEntry.place(x=180, y= 130)

    SaveAnimeLabel = tk.Label(self.RightFrame, text="Anime:", bg="#f5f5f5")
    SaveAnimeLabel.place(x=70, y=170)
    self.SaveAnimeEntry = ttk.Entry(self.RightFrame, width=20)
    self.SaveAnimeEntry.place(x=180, y=170)

    SaveAddressLabel = tk.Label(self.RightFrame, text="Endereço:", bg="#f5f5f5")
    SaveAddressLabel.place(x=70, y=210)
    self.SaveAdressEntry= ttk.Entry(self.RightFrame, width=20)
    self.SaveAdressEntry.place(x=180, y=210)
    SavetButton = ttk.Button(self.RightFrame, text="Salvar dados", command=self.action_register_client)
    SavetButton.place(x=220, y=350)

    VoltarButton = ttk.Button(self.RightFrame, text="Voltar", command=self.client)
    VoltarButton.place(x=220, y=400)

  # Inserção e registro dos dados dos clientes
  def action_register_client(self):
    nome_cliente = self.SaveUserEntry.get()
    nome_cliente= nome_cliente.split(" ")

    while(True):
      num_aux =random.randint(1, 100000)
      user = Usuarios.pesquisar_usuario(f"{nome_cliente[0]}{num_aux}")
      if(user==None):
        break
    
    try:
      usuario_cliente = f"{nome_cliente[0]}{num_aux}"
      senha_cliente = f"{num_aux}"
      Clientes.inserir_clente(self.SaveUserEntry.get(),self.SaveContactEntry.get(),self.SaveTeamEntry.get(),self.SaveAnimeEntry.get(),self.SaveAdressEntry.get(),usuario_cliente,senha_cliente)      
      Application.limpar(self)      
      self.create_widgtes()
      self.create_logo_user()

      ContinueLabel = tk.Label(self.RightFrame, text="Registro salvo com sucesso!\nClique para continuar", bg="#F5F5F5")
      ContinueLabel.place(x=120, y=100)

      ContinueLabel = tk.Label(self.RightFrame, text=f"Usuario e senha são respectivamente:\nUsuario: {nome_cliente[0]}{num_aux}\nSenha: {num_aux}", bg="#F5F5F5")
      ContinueLabel.place(x=80, y=170)

      ContinueLabel = tk.Label(self.RightFrame, text="Altere como desejar nas configurações, posteriormente", bg="#F5F5F5")
      ContinueLabel.place(x=20, y=300)

      ContinueButton = ttk.Button(self.RightFrame, text="Continuar", width=30, command=lambda: self.options_client(usuario_cliente,senha_cliente))
      ContinueButton.place(x=165, y=390)

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

    self.UserEntry_ADM = ttk.Entry(self.RightFrame, width=20)
    self.UserEntry_ADM.place(x=180, y=50)

    PassLabel = tk.Label(self.RightFrame, text="Senha:", bg="#F5F5F5")
    PassLabel.place(x=70, y=100)

    self.PassEntry_ADM = ttk.Entry(self.RightFrame, width=20)
    self.PassEntry_ADM.place(x=180, y=100)

    LoginButton = ttk.Button(self.RightFrame, text="Login", width=20, command = self.action_login_adm)
    LoginButton.place(x=180, y=140)

    VoltarButton = ttk.Button(self.RightFrame, text="Voltar", command=self.inicio)
    VoltarButton.place(x=220, y=400)
  
  # Tentativa de login do adm
  def action_login_adm(self):
    usuario_logado = self.UserEntry_ADM.get()
    senha_logada = self.PassEntry_ADM.get()
    autenticado = Usuarios.autenticar_usuario(usuario_logado,senha_logada)
    if autenticado:
      Application.limpar(self)
      self.create_widgtes()
      self.create_logo_adm()     
      tipo = Usuarios.pesquisar_usuario(usuario_logado)
      if(tipo[1]=="Vendedor"):
        ContinueLabel = tk.Label(self.RightFrame, text="Login realizado com sucesso!\nClique para continuar", bg="#F5F5F5")
        ContinueLabel.place(x=120, y=100)
        ContinueButton = ttk.Button(self.RightFrame, text="Continuar", width=30, command=lambda: self.options_seller(usuario_logado,senha_logada))
        ContinueButton.place(x=165, y=170)
      elif(tipo[1]=="Gerente"):
        ContinueLabel = tk.Label(self.RightFrame, text="Login realizado com sucesso!\nClique para continuar", bg="#F5F5F5")
        ContinueLabel.place(x=120, y=100)
        ContinueButton = ttk.Button(self.RightFrame, text="Continuar", width=30, command=self.options_manager)
        ContinueButton.place(x=165, y=170)
      elif(tipo[1]=="Administrador"):
        ContinueLabel = tk.Label(self.RightFrame, text="Login realizado com sucesso!\nClique para continuar", bg="#F5F5F5")
        ContinueLabel.place(x=120, y=100)
        ContinueButton = ttk.Button(self.RightFrame, text="Continuar", width=30, command=self.options_adm)
        ContinueButton.place(x=165, y=170)
      else:
        ContinueLabel = tk.Label(self.RightFrame, text="Area restrita, somente funcionarios", bg="#F5F5F5")
        ContinueLabel.place(x=120, y=100)
        ContinueButton = ttk.Button(self.RightFrame, text="Voltar para o menu principal", width=30, command=self.options_adm)
        ContinueButton.place(x=165, y=170)
    else:
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

    VoltarButton = ttk.Button(self.RightFrame, text="Voltar para o menu inicial", command=self.inicio)
    VoltarButton.place(x=120, y=400)

  # Exibição das opções para registro de gerente
  def register_manager(self):
    Application.limpar(self)
    self.create_widgtes()
    self.create_logo_adm()

    SaveGerenetLabel = tk.Label(self.RightFrame, text="Nome completo:", bg="#f5f5f5")
    SaveGerenetLabel.place(x=10, y=50)
    SaveGerenetEntry = ttk.Entry(self.RightFrame, width=20)
    SaveGerenetEntry.place(x=180, y=50)

    SaveGerenetContactLabel = tk.Label(self.RightFrame, text="Contato:", bg="#f5f5f5")
    SaveGerenetContactLabel.place(x=70, y=90)
    SaveGerenetContactEntry = ttk.Entry(self.RightFrame, width=20)
    SaveGerenetContactEntry.place(x=180, y=90)

    SaveGerenetStockLabel = tk.Label(self.RightFrame, text="Estoque:", bg="#f5f5f5")
    SaveGerenetStockLabel.place(x=70, y=130)
    # Supondo que você tenha uma lista de estoques chamada 'stock_list'
    stock_list = Estoques.listar_todos_estoques()

    # Crie um StringVar para armazenar o estoque selecionado
    estoque_selecionado = tk.StringVar()

    # Crie um widget Combobox e preencha-o com a stock_list
    SaveStockCombobox = ttk.Combobox(self.RightFrame, textvariable=estoque_selecionado, values=stock_list, width=17)
    SaveStockCombobox.place(x=180, y=130)
    SaveStockCombobox.current(0)  # Defina o estoque selecionado padrão

    # Use estoque_selecionado.get() para obter o valor do estoque selecionado
    SaveGerenetUserIdLabel = tk.Label(self.RightFrame, text="Usuario:", bg="#f5f5f5")
    SaveGerenetUserIdLabel.place(x=70, y = 170)
    SaveGerenetUserIdEntry = ttk.Entry(self.RightFrame, width=20)
    SaveGerenetUserIdEntry.place(x=180, y=170)

    SaveGerenetPassLabel = tk.Label(self.RightFrame, text="Senha:", bg="#f5f5f5")
    SaveGerenetPassLabel.place(x=70, y=210)
    SaveGerenetPassEntry = ttk.Entry(self.RightFrame, width=20)
    SaveGerenetPassEntry.place(x=180, y= 210)   

    SavetButton = ttk.Button(self.RightFrame, text="Salvar dados", command=lambda: self.action_register_manager(SaveGerenetEntry.get(),SaveGerenetContactEntry.get(),estoque_selecionado.get(),SaveGerenetUserIdEntry.get(),SaveGerenetPassEntry.get()))
    SavetButton.place(x=220, y=350)

    VoltarButton = ttk.Button(self.RightFrame, text="Voltar", command=self.options_adm)
    VoltarButton.place(x=220, y=400)

  # Tentativa de registro de gerente
  def action_register_manager(self,nome, contato,estoque_selecionado,usuario, senha):
    try:     
      Gerente.inserir_gerente(nome, contato,estoque_selecionado[0],usuario, senha)
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
  def update_manager(self,id_gerente):
    Application.limpar(self)
    self.create_widgtes()
    self.create_logo_adm()
    info_gerent=Gerente.pesquisar_por_id_gerente(id_gerente)
    
    
    UpdateAdmLabel = tk.Label(self.RightFrame, text="Nome:", bg="#f5f5f5")
    UpdateAdmLabel.place(x=70, y=50)
    self.UpdateAdm_Nome_grentEntry = ttk.Entry(self.RightFrame, width=20)
    self.UpdateAdm_Nome_grentEntry.insert(tk.END, info_gerent[1])
    self.UpdateAdm_Nome_grentEntry.place(x=180, y=50)

    self.UpdateContact_GerentLabel = tk.Label(self.RightFrame, text="Contato:", bg="#f5f5f5")
    self.UpdateContact_GerentLabel.place(x=70, y=90)
    self.UpdateContact_GerentEntry = ttk.Entry(self.RightFrame, width=20)
    self.UpdateContact_GerentEntry.insert(tk.END, info_gerent[2])
    self.UpdateContact_GerentEntry.place(x=180, y=90)

    UpdateStockLabel = tk.Label(self.RightFrame, text="Estoque:", bg="#f5f5f5")
    UpdateStockLabel.place(x=70, y=130)
    
    # Supondo que você tenha uma lista de estoques chamada 'stock_list'
    stock_list = Estoques.listar_todos_estoques()

    # Crie um StringVar para armazenar o estoque selecionado
    estoque_selecionado = tk.StringVar()

    # Crie um widget Combobox e preencha-o com a stock_list
    SaveStockCombobox = ttk.Combobox(self.RightFrame, textvariable=estoque_selecionado, values=stock_list, width=17)
    SaveStockCombobox.place(x=180, y=130)
    SaveStockCombobox.current(0)  # Defina o estoque selecionado padrão
    
    
    # Use estoque_selecionado.get() para obter o valor do estoque selecionado
    UpdateGerenetUserIdLabel = tk.Label(self.RightFrame, text="Usuario:", bg="#f5f5f5")
    UpdateGerenetUserIdLabel.place(x=70, y = 170)
    self.UpdateGerenetUserIdEntry = ttk.Entry(self.RightFrame, width=20)
    self.UpdateGerenetUserIdEntry.insert(tk.END, info_gerent[6])
    self.UpdateGerenetUserIdEntry.place(x=180, y=170)
    
    self.old_user = info_gerent[6]
    
    UpdateGerenetPassLabel = tk.Label(self.RightFrame, text="Senha:", bg="#f5f5f5")
    UpdateGerenetPassLabel.place(x=70, y=210)
    self.UpdateGerenetPassEntry = ttk.Entry(self.RightFrame, width=20)
    self.UpdateGerenetPassEntry.insert(tk.END, "****************")
    self.UpdateGerenetPassEntry.place(x=180, y= 210)   

    UpdateButton = ttk.Button(self.RightFrame, text="Atualizar dados", command=lambda: self.action_update_manager(id_gerente,self.UpdateAdm_Nome_grentEntry.get(),self.UpdateContact_GerentEntry.get(),self.old_user,estoque_selecionado.get(),self.UpdateGerenetUserIdEntry.get(),self.UpdateGerenetPassEntry.get()))
    UpdateButton.place(x=220, y=350)

    VoltarButton = ttk.Button(self.RightFrame, text="Voltar", command=self.list_manager)
    VoltarButton.place(x=220, y=400)
    
  # Tentativa de atualização de gerente
  def action_update_manager(self,id, nome, contato,old_usuario,Estoques_id, usuario, senha):

    try:
      if((senha=="****************" )):
        senha=None
      Gerente.alterar_Gerente(id, nome, contato,old_usuario,int(Estoques_id[0]), usuario, senha)
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
      AgainButton = ttk.Button(self.RightFrame, text="Tente novamente", command=lambda: self.update_manager(id))
      AgainButton.place(x=120, y=150)

  # Tentativa de remoção de gerente
  def action_remove_manager(self,id_gerente):
    #try:
    Gerente.remover_gerente(id_gerente)
    Application.limpar(self)
    self.create_widgtes()
    self.create_logo_adm()     

    ContinueLabel = tk.Label(self.RightFrame, text="Gerente removido com sucesso!\nClique para continuar", bg="#F5F5F5")
    ContinueLabel.place(x=120, y=100)

    ContinueButton = ttk.Button(self.RightFrame, text="Continuar", width=30, command=self.options_adm)
    ContinueButton.place(x=165, y=170)
    '''
    except:
      Application.limpar(self)
      self.create_widgtes()
      self.create_logo_adm()

      ErrorLabel = tk.Label(self.RightFrame, text="Erro ao remover dados, tente novamente!", bg="#F5F5F5")
      ErrorLabel.place(x=120, y=100)
      AgainButton = ttk.Button(self.RightFrame, text="Tente novamente", command=self.update_manager)
      AgainButton.place(x=120, y=150)
      '''
  # Listagem de gerentes
  def list_manager(self):
    Application.limpar(self)
    self.create_widgtes()
    self.create_logo_adm()
    resultados_lista_gerentes = Gerente.listar_todos_os_gerentes()
    text_label = tk.Label(self.window, text="Gerentes cadastrados:",bg= "#FFFFFF",padx=10, pady=10)
    text_label.pack()

    # Criação da barra de rolagem
    scrollbar = ttk.Scrollbar(self.RightFrame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Criação da lista de resultados
    lista_gerentes = tk.Listbox(self.window, yscrollcommand=scrollbar.set, justify='center')
    lista_gerentes.pack(fill="x", expand=1)

    for gerente in resultados_lista_gerentes:
        lista_gerentes.insert(tk.END, f"Id: {gerente[0]} Nome: {gerente[1]} Estoque: {gerente[5]}")

    def mostrar_gerente_selecionado(id):
        selected_item = lista_gerentes.get(tk.ACTIVE)
        Application.limpar(self)
        self.create_widgtes()
        self.create_logo_adm()
        text_font = font.Font(family="Helvetica", size=self.default_font.cget("size") + 4,weight="bold")

        text_label = tk.Label(self.RightFrame, text="Gerentes cadastrados:",font=text_font,bg="#F5F5F5")
        text_label.place(x=140, y=30)
        
        item_text = tk.Label(self.RightFrame, text=f"{selected_item}", font=("Helvetica", 16),bg="#F5F5F5")
        item_text.place(x=60, y=130)
        
        alterar_button = tk.Button(self.RightFrame, text="Alterar",width=35,command=lambda: self.update_manager(id))
        alterar_button.place(x=50, y=190)

        remover_button = tk.Button(self.RightFrame, text="Remover",width=35, command=lambda: self.action_remove_manager(id))
        remover_button.place(x=50, y=250)

        voltar_button = tk.Button(self.RightFrame, text="Voltar",width=35, command=self.list_manager)
        voltar_button.place(x=50, y=310)

    lista_gerentes.bind("<Double-Button-1>", lambda event: mostrar_gerente_selecionado(gerente[0]))

    scrollbar.config(command=lista_gerentes.yview)

    voltar_button = ttk.Button(self.RightFrame, text="Voltar", command=self.options_adm)
    voltar_button.place(x=500, y=400)

  # Fim do loop do administrador

  #---------------------------------------------------------------#

  # Início do loop de gerente
  # Exibição das opções do gerente
  def options_manager(self):
    Application.limpar(self)
    self.create_widgtes()
    self.create_logo_manager()

    TextLabel = tk.Label(self.RightFrame, text="Selecione a opção desejada", bg="#F5F5F5")
    TextLabel.place(x=120, y=50)

    SellerButton = ttk.Button(self.RightFrame, text="Cadastrar novo vendedor", command=self.register_seller)
    SellerButton.place(x=120, y=100)

    UpdateSellerButton = ttk.Button(self.RightFrame, text="Gerenciar vendedores", command=self.list_seller)
    UpdateSellerButton.place(x=120, y=150)

    StockButton = ttk.Button(self.RightFrame, text="Cadastrar novo estoque", command=self.register_stock)
    StockButton.place(x=120, y=200)

    UpdateStockButton = ttk.Button(self.RightFrame, text="Gerenciar estoques", command=self.list_stock)
    UpdateStockButton.place(x=120, y=250)
    
    UpdateForncedorButton = ttk.Button(self.RightFrame, text="Cadastrar novo Fornecedor", command=self.register_supplier)
    UpdateForncedorButton.place(x=120, y=300)
    
    UpdateForncedorButton = ttk.Button(self.RightFrame, text="Gerenciar Fornecedores", command=self.list_supplier)
    UpdateForncedorButton.place(x=120, y=350)

    VoltarButton = ttk.Button(self.RightFrame, text="Voltar", command=self.admin)
    VoltarButton.place(x=120, y=400)

  # Exibição das opções para registro de vendedores
  def register_seller(self):
    Application.limpar(self)
    self.create_widgtes()
    self.create_logo_manager()
    
    SaveAdmLabel = tk.Label(self.RightFrame, text="Nome:", bg="#f5f5f5")
    SaveAdmLabel.place(x=70, y=50)
    SaveAdmEntry = ttk.Entry(self.RightFrame, width=20)
    SaveAdmEntry.place(x=180, y=50)

    SaveContactLabel = tk.Label(self.RightFrame, text="Contato:", bg="#f5f5f5")
    SaveContactLabel.place(x=70, y=90)
    SaveContactEntry = ttk.Entry(self.RightFrame, width=20)
    SaveContactEntry.place(x=180, y=90)
    
    SaveStockLabel = tk.Label(self.RightFrame, text="Estoque :", bg="#f5f5f5")
    SaveStockLabel.place(x=70, y=130)
    
    # Supondo que você tenha uma lista de estoques chamada 'stock_list'
    stock_list = Estoques.listar_todos_estoques()

    # Crie um StringVar para armazenar o estoque selecionado
    estoque_selecionado = tk.StringVar()

    # Crie um widget Combobox e preencha-o com a stock_list
    SaveStockCombobox = ttk.Combobox(self.RightFrame, textvariable=estoque_selecionado, values=stock_list, width=17)
    SaveStockCombobox.place(x=180, y=130)
    SaveStockCombobox.current(0)  # Defina o estoque selecionado padrão

    # Use estoque_selecionado.get() para obter o valor do estoque selecionado

    SaveUserIdLabel = tk.Label(self.RightFrame, text="Usuario:", bg="#f5f5f5")
    SaveUserIdLabel.place(x=70, y = 170)
    SaveUserIdEntry = ttk.Entry(self.RightFrame, width=20)
    SaveUserIdEntry.place(x=180, y=170)

    SavePassLabel = tk.Label(self.RightFrame, text="Senha:", bg="#f5f5f5")
    SavePassLabel.place(x=70, y=210)
    SavePassEntry = ttk.Entry(self.RightFrame, width=20)
    SavePassEntry.place(x=180, y= 210)   

    SavetButton = ttk.Button(self.RightFrame, text="Salvar dados", command=lambda: self.action_register_seller(SaveAdmEntry.get(),SaveContactEntry.get(),estoque_selecionado.get(),SaveUserIdEntry.get(),SavePassEntry.get()))
    SavetButton.place(x=220, y=350)

    VoltarButton = ttk.Button(self.RightFrame, text="Voltar", command=self.options_manager)
    VoltarButton.place(x=220, y=400)

  # Tentativa de registro de vendedor
  def action_register_seller(self,nome, contato, Estoques_id, usuario, senha):
    try:
      Vendedores.cadastrar_Vendedor(nome, contato,int(Estoques_id[0]), usuario, senha)
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

    resultados_lista_vendedores = Vendedores.listar_todos_os_vendedores()
    text_label = tk.Label(self.window, text="Vendedores cadastrados:", bg= "#FFFFFF" ,padx=10, pady=10)
    text_label.pack()

    # Criação da barra de rolagem
    scrollbar = ttk.Scrollbar(self.RightFrame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
    # Criação da lista de resultados
    lista_vendedores = tk.Listbox(self.window, yscrollcommand=scrollbar.set, justify='center')
    # lista_vendedpres.pack(side=tk.LEFT, fill=tk.X, expand=True)
    lista_vendedores.pack(fill="x", expand=1)
    
    for vendedor in resultados_lista_vendedores:
      lista_vendedores.insert(tk.END,f"Id: {vendedor[0]} Nome: {vendedor[1]} Estoque: {vendedor[5]}" )

    def mostrar_gerente_selecionado(id):
        selected_item = lista_vendedores.get(tk.ACTIVE)
        Application.limpar(self)
        self.create_widgtes()
        self.create_logo_manager()
        text_font = font.Font(family="Helvetica", size=self.default_font.cget("size") + 4,weight="bold")

        text_label = tk.Label(self.RightFrame, text="Vendedores cadastrados:",font=text_font,bg="#F5F5F5")
        text_label.place(x=140, y=30)
        
        item_text = tk.Label(self.RightFrame, text=f"{selected_item}", font=("Helvetica", 16),bg="#F5F5F5")
        item_text.place(x=60, y=130)
        
        alterar_button = tk.Button(self.RightFrame, text="Alterar",width=35,command=lambda: self.update_seller(id))
        alterar_button.place(x=50, y=190)

        remover_button = tk.Button(self.RightFrame, text="Remover",width=35, command=lambda: self.action_remove_seller(id))
        remover_button.place(x=50, y=250)

        voltar_button = tk.Button(self.RightFrame, text="Voltar",width=35, command=self.list_manager)
        voltar_button.place(x=50, y=310)

    lista_vendedores.bind("<Double-Button-1>", lambda event: mostrar_gerente_selecionado(vendedor[0]))

    scrollbar.config(command=lista_vendedores.yview)

    voltar_button = ttk.Button(self.RightFrame, text="Voltar", command=self.options_adm)
    voltar_button.place(x=500, y=400)
  
  # Exibição das opções de atualização de denvedor
  def update_seller(self,id_seller):
    Application.limpar(self)
    self.create_widgtes()
    self.create_logo_manager()
    info_seller=Vendedores.pesquisar_por_id_do_vendedor(id_seller)
    
    old_usuario = info_seller[-1]
    UpdateAdmLabel = tk.Label(self.RightFrame, text="Nome :", bg="#f5f5f5")
    UpdateAdmLabel.place(x=70, y=50)
    UpdateAdmEntry = ttk.Entry(self.RightFrame, width=20)
    UpdateAdmEntry.insert(tk.END, info_seller[1])
    UpdateAdmEntry.place(x=180, y=50)

    UpdateContactLabel = tk.Label(self.RightFrame, text="Contato:", bg="#f5f5f5")
    UpdateContactLabel.place(x=70, y=90)
    UpdateContactEntry = ttk.Entry(self.RightFrame, width=20)
    UpdateContactEntry.insert(tk.END, info_seller[2])
    UpdateContactEntry.place(x=180, y=90)

    UpdateStockLabel = tk.Label(self.RightFrame, text="Estoque :", bg="#f5f5f5")
    UpdateStockLabel.place(x=70, y=130)
    
    # Supondo que você tenha uma lista de estoques chamada 'stock_list'
    stock_list = Estoques.listar_todos_estoques()

    # Crie um StringVar para armazenar o estoque selecionado
    estoque_selecionado = tk.StringVar()

    # Crie um widget Combobox e preencha-o com a stock_list
    SaveStockCombobox = ttk.Combobox(self.RightFrame, textvariable=estoque_selecionado, values=stock_list, width=17)
    SaveStockCombobox.place(x=180, y=130)
    SaveStockCombobox.current(0)  # Defina o estoque selecionado padrão
    
    
    # Use estoque_selecionado.get() para obter o valor do estoque selecionado
    
    
    UpdateUserIdLabel = tk.Label(self.RightFrame, text="Usuario:", bg="#f5f5f5")
    UpdateUserIdLabel.place(x=70, y = 170)
    UpdateUserIdEntry = ttk.Entry(self.RightFrame, width=20)
    UpdateUserIdEntry.insert(tk.END, info_seller[-1])
    UpdateUserIdEntry.place(x=180, y=170)
    
    UpdatePassLabel = tk.Label(self.RightFrame, text="Senha:", bg="#f5f5f5")
    UpdatePassLabel.place(x=70, y=210)
    UpdatePassEntry = ttk.Entry(self.RightFrame, width=20)
    UpdatePassEntry.insert(tk.END, "****************")
    UpdatePassEntry.place(x=180, y= 210)   

    UpdateButton = ttk.Button(self.RightFrame, text="Atualizar dados", command=lambda: self.action_update_seller(id_seller,UpdateAdmEntry.get(),UpdateContactEntry.get(),old_usuario,estoque_selecionado.get(),UpdateUserIdEntry.get(),UpdatePassEntry.get()))
    UpdateButton.place(x=220, y=350)

    VoltarButton = ttk.Button(self.RightFrame, text="Voltar", command=self.client)
    VoltarButton.place(x=220, y=400)

  # Tentativa de atualização de vendedor
  def action_update_seller(self,id, nome, contato, old_usuario, Estoques_id, usuario, senha):
    try:
      if((senha=="****************" )):
        senha=None
      Vendedores.alterar_Vendedor(id, nome, contato,old_usuario, int(Estoques_id[0]), usuario, senha)
      Application.limpar(self)
      self.create_widgtes()
      self.create_logo_manager()     

      ContinueLabel = tk.Label(self.RightFrame, text="Vendedor atualizado com sucesso!\nClique para continuar", bg="#F5F5F5")
      ContinueLabel.place(x=120, y=100)

      ContinueButton = ttk.Button(self.RightFrame, text="Continuar", width=30, command=self.options_manager)
      ContinueButton.place(x=165, y=170)

    except:
      Application.limpar(self)
      self.create_widgtes()
      self.create_logo_manager()

      ErrorLabel = tk.Label(self.RightFrame, text="Erro ao atualizar dados, tente novamente!", bg="#F5F5F5")
      ErrorLabel.place(x=120, y=100)
      AgainButton = ttk.Button(self.RightFrame, text="Tente novamente", command=lambda: self.update_seller(id))
      AgainButton.place(x=120, y=150)

  # Tentativa de remoção de vendedor
  def action_remove_seller(self,id_seller):
    try:
      Vendedores.remover_vendedor(id_seller)
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
    def validate_date(entry):
      # Obtém o valor digitado pelo usuário
      date_str = entry.get()

      # Verifica se a data está no formato adequado (DD/MM/AAAA)
      if len(date_str) == 10 and date_str[2] == '/' and date_str[5] == '/':
          day = int(date_str[:2])
          month = int(date_str[3:5])
          year = int(date_str[6:])
          
          # Verifica se a data é válida
          if 1 <= day <= 31 and 1 <= month <= 12 and 1900 <= year <= 2100:
              return True

      # Se a data não estiver no formato adequado ou for inválida, mostra uma mensagem de erro
      entry.config(foreground='gray')
      print("Data inválida!")
      entry.delete(0, tk.END)
      return False
    
    SaveAdmLabel = tk.Label(self.RightFrame, text="Nome:", bg="#f5f5f5")
    SaveAdmLabel.place(x=70, y=50)
    SaveAdmEntry = ttk.Entry(self.RightFrame, width=20)
    SaveAdmEntry.place(x=180, y=50)

    SaveContactLabel = tk.Label(self.RightFrame, text="Localização:", bg="#f5f5f5")
    SaveContactLabel.place(x=20, y=90)
    SaveContactEntry = ttk.Entry(self.RightFrame, width=20)
    SaveContactEntry.place(x=180, y=90)

    SaveUserIdLabel = tk.Label(self.RightFrame, text="Data reposição", bg="#f5f5f5")
    SaveUserIdLabel.place(x=10, y = 130)
    SaveUserIdEntry = ttk.Entry(self.RightFrame, width=20,validate='focusout', validatecommand=lambda: validate_date(SaveUserIdEntry))
    SaveUserIdEntry.place(x=180, y=130)

    SaveStockLabel = tk.Label(self.RightFrame, text="Reposição Futura:", bg="#f5f5f5")
    SaveStockLabel.place(x=10, y=170)
    SaveStockEntry = ttk.Entry(self.RightFrame,  width=20,validate='focusout', validatecommand=lambda: validate_date(SaveStockEntry))
    SaveStockEntry.place(x=180, y= 170)
    
    # Função para formatar automaticamente o texto digitado no campo de entrada de data
    def format_date(event):
        entry = event.widget
        text = entry.get()
        length = len(text)
        if length == 2 or length == 5:
            if event.keysym != 'BackSpace':
                entry.insert(tk.END, '/')
        elif length > 10:
            entry.delete(10, tk.END)

    # Adiciona a dica de entrada (placeholder) no campo de entrada de data
    SaveUserIdEntry.config(foreground='gray')
    SaveStockEntry.config(foreground='gray')

    # Configura os eventos de teclado para formatar automaticamente o texto no campo de entrada de data
    SaveUserIdEntry.bind('<Key>', format_date)
    SaveStockEntry.bind('<Key>', format_date)

    SavetButton = ttk.Button(self.RightFrame, text="Salvar dados", command=lambda: self.action_register_stock(SaveContactEntry.get(), SaveAdmEntry.get(), SaveUserIdEntry.get(), SaveStockEntry.get()))
    SavetButton.place(x=220, y=350)

    VoltarButton = ttk.Button(self.RightFrame, text="Voltar", command=self.options_manager)
    VoltarButton.place(x=220, y=400)

  # Tentativa de registro de estoque
  def action_register_stock(self,localizacao, nome_estoque, ultima_data_reposicao, data_reposicao_futura):
    data1_obj = datetime.strptime(ultima_data_reposicao, "%d/%m/%Y")
    data2_obj = datetime.strptime(data_reposicao_futura, "%d/%m/%Y")
    diferenca = data1_obj - data2_obj 
    if(diferenca.days > 0):
      Application.limpar(self)
      self.create_widgtes()
      self.create_logo_manager()

      ErrorLabel = tk.Label(self.RightFrame, text="Erro ao salvar dados, tente novamente!", bg="#F5F5F5")
      ErrorLabel.place(x=120, y=100)
      AgainButton = ttk.Button(self.RightFrame, text="Tente novamente", command=self.register_stock)
      AgainButton.place(x=120, y=150)
    else:
      try:
        
        Estoques.inserir_novo_estoque(localizacao, nome_estoque, ultima_data_reposicao, data_reposicao_futura)
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

    estoques = Estoques.listar_todos_estoques()

    text_label = tk.Label(self.window, text="Estoques cadastrados:", bg= "#FFFFFF",padx=10, pady=10)
    text_label.pack()

    # Criação da barra de rolagem
    scrollbar = ttk.Scrollbar(self.RightFrame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
    # Criação da lista de resultados
    lista_estoques = tk.Listbox(self.window, yscrollcommand=scrollbar.set, justify='center')
    # lista_estoques.pack(side=tk.LEFT, fill=tk.X, expand=True)
    lista_estoques.pack(fill="x", expand=1)
    
    for estoque in estoques:
      lista_estoques.insert(tk.END, f"Id: {estoque[0]} Nome: {estoque[1]} Localização: {estoque[2]}")

    def mostrar_estoque_selecionado(id):
      selected_item = lista_estoques.get(tk.ACTIVE)
      
      Application.limpar(self)
      self.create_widgtes()
      self.create_logo_manager()
      text_font = font.Font(family="Helvetica", size=self.default_font.cget("size") + 4,weight="bold")
      text_label = tk.Label(self.RightFrame, text="Estoques cadastrados:",font=text_font,bg="#F5F5F5")
      text_label.place(x=140, y=30)
      
      item_text = tk.Label(self.RightFrame, text=f"{selected_item}", font=("Helvetica", 16),bg="#F5F5F5")
      item_text.place(x=60, y=130)

      alterar_button = tk.Button(self.RightFrame, text="Alterar",width=35,command=lambda: self.update_stock(id))
      alterar_button.place(x=50, y=190)

      remover_button = tk.Button(self.RightFrame, text="Remover",width=35, command=lambda: self.action_remove_stock(id))
      remover_button.place(x=50, y=250)
      
      voltar_button = tk.Button(self.RightFrame, text="Voltar",width=35, command=self.list_stock)
      voltar_button.place(x=50, y=310)
    
    lista_estoques.bind("<Double-Button-1>", lambda event: mostrar_estoque_selecionado(estoque[0]))

    scrollbar.config(command=lista_estoques.yview)

    voltar_button = ttk.Button(self.window, text="Voltar", command=self.options_manager)
    voltar_button.place(x=500,y=400)

  # Exibição das opções da atualização de estoque
  
  def update_stock(self,id_stock):
    Application.limpar(self)
    self.create_widgtes()
    self.create_logo_manager()
    info_stock = Estoques.pesquisar_por_id_estoque(id_stock)
    def validate_date(entry):
      # Obtém o valor digitado pelo usuário
      date_str = entry.get()

      # Verifica se a data está no formato adequado (DD/MM/AAAA)
      if len(date_str) == 10 and date_str[2] == '/' and date_str[5] == '/':
          day = int(date_str[:2])
          month = int(date_str[3:5])
          year = int(date_str[6:])
          
          # Verifica se a data é válida
          if 1 <= day <= 31 and 1 <= month <= 12 and 1900 <= year <= 2100:
              return True

      # Se a data não estiver no formato adequado ou for inválida, mostra uma mensagem de erro
      entry.config(foreground='gray')
      print("Data inválida!")
      entry.delete(0, tk.END)
      return False
    
    SaveAdmLabel = tk.Label(self.RightFrame, text="Nome :", bg="#f5f5f5")
    SaveAdmLabel.place(x=70, y=50)
    SaveAdmEntry = ttk.Entry(self.RightFrame, width=20)
    SaveAdmEntry.insert(tk.END, info_stock[2])
    SaveAdmEntry.place(x=180, y=50)

    SaveContactLabel = tk.Label(self.RightFrame, text="Localização:", bg="#f5f5f5")
    SaveContactLabel.place(x=20, y=90)
    SaveContactEntry = ttk.Entry(self.RightFrame, width=20)
    SaveContactEntry.insert(tk.END, info_stock[1])
    SaveContactEntry.place(x=180, y=90)

    SaveUserIdLabel = tk.Label(self.RightFrame, text="Data reposição:", bg="#f5f5f5")
    SaveUserIdLabel.place(x=10, y = 130)
    SaveUserIdEntry = ttk.Entry(self.RightFrame,  width=20,validate='focusout', validatecommand=lambda: validate_date(SaveUserIdEntry))
    SaveUserIdEntry.insert(tk.END, info_stock[4])
    SaveUserIdEntry.place(x=180, y=130)

    SaveStockLabel = tk.Label(self.RightFrame, text="Reposição futura:", bg="#f5f5f5")
    SaveStockLabel.place(x=10, y=170)
    SaveStockEntry = ttk.Entry(self.RightFrame,width=20,validate='focusout', validatecommand=lambda: validate_date(SaveStockEntry))
    SaveStockEntry.insert(tk.END, info_stock[5])
    SaveStockEntry.place(x=180, y= 170)
    def format_date(event):
        entry = event.widget
        text = entry.get()
        length = len(text)
        if length == 2 or length == 5:
            if event.keysym != 'BackSpace':
                entry.insert(tk.END, '/')
        elif length > 10:
            entry.delete(10, tk.END)

    # Adiciona a dica de entrada (placeholder) no campo de entrada de data
    SaveUserIdEntry.config(foreground='gray')
    SaveStockEntry.config(foreground='gray')

    # Configura os eventos de teclado para formatar automaticamente o texto no campo de entrada de data
    SaveUserIdEntry.bind('<Key>', format_date)
    SaveStockEntry.bind('<Key>', format_date)
    
    
    SavetButton = ttk.Button(self.RightFrame, text="Salvar dados", command=lambda:self.action_update_stock(id_stock, SaveContactEntry.get(), SaveAdmEntry.get(), SaveUserIdEntry.get(), SaveStockEntry.get()))
    SavetButton.place(x=220, y=350)

    VoltarButton = ttk.Button(self.RightFrame, text="Voltar", command=self.options_manager)
    VoltarButton.place(x=220, y=400)

  # Tentativa de atualização do estoque
  def action_update_stock(self,id, localizacao, nome_estoque, ultima_data_reposicao, data_reposicao_futura):
    data1_obj = datetime.strptime(ultima_data_reposicao, "%d/%m/%Y")
    data2_obj = datetime.strptime(data_reposicao_futura, "%d/%m/%Y")
    diferenca = data1_obj - data2_obj 
    if(diferenca.days > 0):
      Application.limpar(self)
      self.create_widgtes()
      self.create_logo_manager()

      ErrorLabel = tk.Label(self.RightFrame, text="Erro ao salvar dados, tente novamente!", bg="#F5F5F5")
      ErrorLabel.place(x=120, y=100)
      AgainButton = ttk.Button(self.RightFrame, text="Tente novamente", command=self.register_stock)
      AgainButton.place(x=120, y=150)
    else:
      try:
        Estoques.alterar_estoque(id, localizacao, nome_estoque, ultima_data_reposicao, data_reposicao_futura)
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
        AgainButton = ttk.Button(self.RightFrame, text="Tente novamente", command=self.update_stock(id))
        AgainButton.place(x=120, y=150)

  # Tentativa de remoção do estoque
  def action_remove_stock(self,estoque_id):
    try:
      Estoques.remover_estoque(estoque_id)
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
  
  def register_supplier(self):
    Application.limpar(self)
    self.create_widgtes()
    self.create_logo_manager()
    
    SaveAdmLabel = tk.Label(self.RightFrame, text="Nome:", bg="#f5f5f5")
    SaveAdmLabel.place(x=70, y=50)
    SaveAdmEntry = ttk.Entry(self.RightFrame, width=20)
    SaveAdmEntry.place(x=180, y=50)

    SaveContactLabel = tk.Label(self.RightFrame, text="localizacao:", bg="#f5f5f5")
    SaveContactLabel.place(x=70, y=90)
    SaveContactEntry = ttk.Entry(self.RightFrame, width=20)
    SaveContactEntry.place(x=180, y=90)
    
    SavetButton = ttk.Button(self.RightFrame, text="Salvar dados", command=lambda: self.action_register_supplier(SaveAdmEntry.get(),SaveContactEntry.get()))
    SavetButton.place(x=220, y=250)

    VoltarButton = ttk.Button(self.RightFrame, text="Voltar", command=self.options_manager)
    VoltarButton.place(x=220, y=300)
  
  def action_register_supplier(self,nome, localizacao):
    try:
      Fabricantes.inserir(nome, localizacao)
      Application.limpar(self)
      self.create_widgtes()
      self.create_logo_manager()     

      ContinueLabel = tk.Label(self.RightFrame, text="Fornecedor salvo com sucesso!\nClique para continuar", bg="#F5F5F5")
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
  
  def list_supplier(self):
    Application.limpar(self)
    self.create_widgtes()
    self.create_logo_manager()
    resultados_lista_fornecedores = Fabricantes.listar_todos()
    text_label = tk.Label(self.window, text="Fornecedores cadastrados:", bg= "#FFFFFF" ,padx=10, pady=10)
    text_label.pack()
    # Criação da barra de rolagem
    scrollbar = ttk.Scrollbar(self.RightFrame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
    # Criação da lista de resultados
    lista_fornecedores = tk.Listbox(self.window, yscrollcommand=scrollbar.set, justify='center')
    # lista_vendedpres.pack(side=tk.LEFT, fill=tk.X, expand=True)
    lista_fornecedores.pack(fill="x", expand=1)
    
    for fornecedores in resultados_lista_fornecedores:
      lista_fornecedores.insert(tk.END,f"Id: {fornecedores[0]} Nome: {fornecedores[1]} Localização: {fornecedores[3]}" )
    def mostrar_gerente_selecionado(id):
        selected_item = lista_fornecedores.get(tk.ACTIVE)
        Application.limpar(self)
        self.create_widgtes()
        self.create_logo_manager()
        text_font = font.Font(family="Helvetica", size=self.default_font.cget("size") + 4,weight="bold")

        text_label = tk.Label(self.RightFrame, text="Fornecedores cadastrados:",font=text_font,bg="#F5F5F5")
        text_label.place(x=140, y=30)
        
        item_text = tk.Label(self.RightFrame, text=f"{selected_item}", font=("Helvetica", 16),bg="#F5F5F5")
        item_text.place(x=60, y=130)
        
        alterar_button = tk.Button(self.RightFrame, text="Alterar",width=35,command=lambda: self.update_supplier(id))
        alterar_button.place(x=50, y=190)

        remover_button = tk.Button(self.RightFrame, text="Remover",width=35, command=lambda: self.action_remove_seller(id))
        remover_button.place(x=50, y=250)

        voltar_button = tk.Button(self.RightFrame, text="Voltar",width=35, command=self.list_manager)
        voltar_button.place(x=50, y=310)

    lista_fornecedores.bind("<Double-Button-1>", lambda event: mostrar_gerente_selecionado(fornecedores[0]))

    scrollbar.config(command=lista_fornecedores.yview)

    voltar_button = ttk.Button(self.RightFrame, text="Voltar", command=self.options_adm)
    voltar_button.place(x=500, y=400)
  
  def update_supplier(self,id):
    Application.limpar(self)
    self.create_widgtes()
    self.create_logo_manager()
    info_supplier=Fabricantes.pesquisar_por_id(id)
    
    UpdateAdmLabel = tk.Label(self.RightFrame, text="Nome :", bg="#f5f5f5")
    UpdateAdmLabel.place(x=70, y=50)
    UpdateAdmEntry = ttk.Entry(self.RightFrame, width=20)
    UpdateAdmEntry.insert(tk.END, info_supplier[1])
    UpdateAdmEntry.place(x=180, y=50)

    UpdateContactLabel = tk.Label(self.RightFrame, text="Localização:", bg="#f5f5f5")
    UpdateContactLabel.place(x=30, y=90)
    UpdateContactEntry = ttk.Entry(self.RightFrame, width=20)
    UpdateContactEntry.insert(tk.END, info_supplier[3])
    UpdateContactEntry.place(x=180, y=90)
    UpdateButton = ttk.Button(self.RightFrame, text="Atualizar dados", command=lambda: self.action_update_seller(id,UpdateAdmEntry.get(),UpdateContactEntry.get()))
    UpdateButton.place(x=220, y=130)
    VoltarButton = ttk.Button(self.RightFrame, text="Voltar", command=self.list_supplier)
    VoltarButton.place(x=220, y=160)
  
  def action_update_seller(self,id,nome, localizacao):
    try:
      Fabricantes.alterar(id,nome, localizacao)
      Application.limpar(self)
      self.create_widgtes()
      self.create_logo_adm()     

      ContinueLabel = tk.Label(self.RightFrame, text="Gerente atualizado com sucesso!\nClique para continuar", bg="#F5F5F5")
      ContinueLabel.place(x=120, y=100)

      ContinueButton = ttk.Button(self.RightFrame, text="Continuar", width=30, command=self.options_manager)
      ContinueButton.place(x=165, y=170)

    except:
      Application.limpar(self)
      self.create_widgtes()
      self.create_logo_adm()

      ErrorLabel = tk.Label(self.RightFrame, text="Erro ao atualizar dados, tente novamente!", bg="#F5F5F5")
      ErrorLabel.place(x=120, y=100)
      AgainButton = ttk.Button(self.RightFrame, text="Tente novamente", command=lambda: self.update_supplier(id))
      AgainButton.place(x=120, y=150)

  # Fim do loop de gerente

  #---------------------------------------------------------------#
  
  # Início do loop de vendedor

  # Exibição das opções do vendedor
  def options_seller(self,usuario,senha):
    self.User_Seller = usuario
    self.Pass_seller = senha
    Application.limpar(self)
    self.create_widgtes()
    self.create_logo_seller()

    TextLabel = tk.Label(self.RightFrame, text="Selecione a opção desejada", bg="#F5F5F5")
    TextLabel.place(x=120, y=100)

    BuyButton = ttk.Button(self.RightFrame, text="Cadastrar novo material", command=lambda: self.register_material(self.User_Seller,self.Pass_seller))
    BuyButton.place(x=120, y=150)

    UpdateButton = ttk.Button(self.RightFrame, text="Gerenciar materiais", command=lambda:self.list_material(self.User_Seller,self.Pass_seller))
    UpdateButton.place(x=120, y=200)

    VoltarButton = ttk.Button(self.RightFrame, text="Voltar", command=self.admin)
    VoltarButton.place(x=120, y=400)

  # Exibição das opções para registro de material
  def register_material(self,usuario,senha):
    Application.limpar(self)
    self.create_widgtes()
    self.create_logo_seller()

    SaveAdmLabel = tk.Label(self.RightFrame, text="Nome:", bg="#f5f5f5")
    SaveAdmLabel.place(x=70, y=50)
    SaveAdmEntry = ttk.Entry(self.RightFrame, width=20)
    SaveAdmEntry.place(x=180, y=50)

    SaveContactLabel = tk.Label(self.RightFrame, text="Descrição:", bg="#f5f5f5")
    SaveContactLabel.place(x=70, y=90)
    SaveContactEntry = ttk.Entry(self.RightFrame, width=20)
    SaveContactEntry.place(x=180, y=90)

    SaveUserIdLabel = tk.Label(self.RightFrame, text="Preço:", bg="#f5f5f5")
    SaveUserIdLabel.place(x=70, y = 130)
    SaveUserIdEntry = ttk.Entry(self.RightFrame, width=20)
    SaveUserIdEntry.place(x=180, y=130)

    SaveStockQtdLabel = tk.Label(self.RightFrame, text="Quantidade em estoque:", bg="#f5f5f5")
    SaveStockQtdLabel.place(x=70, y=170)
    SaveStockQtdEntry = ttk.Entry(self.RightFrame, width=20)
    SaveStockQtdEntry.place(x=180, y= 170)

    SavePassLabel = tk.Label(self.RightFrame, text="Fabricante:", bg="#f5f5f5")
    SavePassLabel.place(x=70, y=210)
    # Supondo que você tenha uma lista de estoques chamada 'stock_list'
    stock_list = Fabricantes.listar_todos()

    # Crie um StringVar para armazenar o estoque selecionado
    estoque_selecionado = tk.StringVar()

    # Crie um widget Combobox e preencha-o com a stock_list
    SaveStockCombobox = ttk.Combobox(self.RightFrame, textvariable=estoque_selecionado, values=stock_list, width=17)
    SaveStockCombobox.place(x=180, y= 210) 
    SaveStockCombobox.current(0)  # Defina o estoque selecionado padrão

    # Use estoque_selecionado.get() para obter o valor do estoque selecionado 

    SavetButton = ttk.Button(self.RightFrame, text="Salvar dados", command=lambda: self.action_register_material(usuario,senha,SaveAdmEntry.get(),SaveContactEntry.get(),SaveUserIdEntry.get(),SaveStockQtdEntry.get(),estoque_selecionado.get()))
    SavetButton.place(x=220, y=350)

    VoltarButton = ttk.Button(self.RightFrame, text="Voltar", command=lambda: self.options_seller(self.User_Seller,self.Pass_seller))
    VoltarButton.place(x=220, y=400)

  # Tentativa de registro de material
  def action_register_material(self,usuario,senha,Nome, Descrição, Preço, Quantidade_estoque, Fabricante_id):
    try:
      seller = Vendedores(usuario,senha)
      seller.inserir_material(Nome, Descrição, int(Preço), int(Quantidade_estoque), int(Fabricante_id[0]))
      Application.limpar(self)
      self.create_widgtes()
      self.create_logo_seller()     

      ContinueLabel = tk.Label(self.RightFrame, text="Produto salvo com sucesso!\nClique para continuar", bg="#F5F5F5")
      ContinueLabel.place(x=120, y=100)

      ContinueButton = ttk.Button(self.RightFrame, text="Continuar", width=30, command=lambda: self.options_seller(usuario,senha))
      ContinueButton.place(x=165, y=170)

    except:
      Application.limpar(self)
      self.create_widgtes()
      self.create_logo_seller()

      ErrorLabel = tk.Label(self.RightFrame, text="Erro ao salvar dados, tente novamente!", bg="#F5F5F5")
      ErrorLabel.place(x=120, y=100)
      AgainButton = ttk.Button(self.RightFrame, text="Tente novamente", command=lambda: self.register_material(usuario,senha))
      AgainButton.place(x=120, y=150)

  # Exibição das opções para atualização de material
  def update_material(self):
    Application.limpar(self)
    self.create_widgtes()
    self.create_logo_seller()

    SaveAdmLabel = tk.Label(self.RightFrame, text="Nome:", bg="#f5f5f5")
    SaveAdmLabel.place(x=70, y=50)
    SaveAdmEntry = ttk.Entry(self.RightFrame, width=20)
    SaveAdmEntry.place(x=180, y=50)

    SaveContactLabel = tk.Label(self.RightFrame, text="Descrição:", bg="#f5f5f5")
    SaveContactLabel.place(x=70, y=90)
    SaveContactEntry = ttk.Entry(self.RightFrame, width=20)
    SaveContactEntry.place(x=180, y=90)

    SaveUserIdLabel = tk.Label(self.RightFrame, text="Preço:", bg="#f5f5f5")
    SaveUserIdLabel.place(x=70, y = 130)
    SaveUserIdEntry = ttk.Entry(self.RightFrame, width=20)
    SaveUserIdEntry.place(x=180, y=130)

    SaveStockQtdLabel = tk.Label(self.RightFrame, text="Quantidade em estoque:", bg="#f5f5f5")
    SaveStockQtdLabel.place(x=70, y=170)
    SaveStockQtdEntry = ttk.Entry(self.RightFrame, width=20)
    SaveStockQtdEntry.place(x=180, y= 170)

    SavePassLabel = tk.Label(self.RightFrame, text="Fabricante:", bg="#f5f5f5")
    SavePassLabel.place(x=70, y=210)
    SavePassEntry = ttk.Entry(self.RightFrame, width=20)
    SavePassEntry.place(x=180, y= 210) 

    SaveStockLabel = tk.Label(self.RightFrame, text="Estoque armazenado:", bg="#f5f5f5")
    SaveStockLabel.place(x=70, y=170)
    SaveStockEntry = ttk.Entry(self.RightFrame, width=20)
    SaveStockEntry.place(x=180, y= 170)  

    SavetButton = ttk.Button(self.RightFrame, text="Salvar dados", command=self.action_update_material)
    SavetButton.place(x=220, y=350)

    VoltarButton = ttk.Button(self.RightFrame, text="Voltar", command=self.seller)
    VoltarButton.place(x=220, y=400)
    
  # Tentativa de atualização de material
  def action_update_material(self):
    try:
      # Código de validação de login no BD
      Application.limpar(self)
      self.create_widgtes()
      self.create_logo_seller()     

      ContinueLabel = tk.Label(self.RightFrame, text="Produto atualizado com sucesso!\nClique para continuar", bg="#F5F5F5")
      ContinueLabel.place(x=120, y=100)

      ContinueButton = ttk.Button(self.RightFrame, text="Continuar", width=30, command=self.options_seller)
      ContinueButton.place(x=165, y=170)
    
    except:
      Application.limpar(self)
      self.create_widgtes()
      self.create_logo_adm()

      ErrorLabel = tk.Label(self.RightFrame, text="Erro ao atualizar dados, tente novamente!", bg="#F5F5F5")
      ErrorLabel.place(x=120, y=100)
      AgainButton = ttk.Button(self.RightFrame, text="Tente novamente", command=self.update_material)
      AgainButton.place(x=120, y=150)

  # Tentativa de remoção de material
  def action_remove_material(self):
    try:
      # Código de validação de login no BD
      Application.limpar(self)
      self.create_widgtes()
      self.create_logo_seller()     

      ContinueLabel = tk.Label(self.RightFrame, text="Produto removido com sucesso!\nClique para continuar", bg="#F5F5F5")
      ContinueLabel.place(x=120, y=100)

      ContinueButton = ttk.Button(self.RightFrame, text="Continuar", width=30, command=self.options_seller)
      ContinueButton.place(x=165, y=170)
    
    except:
      Application.limpar(self)
      self.create_widgtes()
      self.create_logo_seller()

      ErrorLabel = tk.Label(self.RightFrame, text="Erro ao remover dados, tente novamente!", bg="#F5F5F5")
      ErrorLabel.place(x=120, y=100)
      AgainButton = ttk.Button(self.RightFrame, text="Tente novamente", command=self.update_seller)
      AgainButton.place(x=120, y=150)

  # Listagem de materiais
  def list_material(self,usuario,senha):
    # gerenciador = Gerenciador()
    # materiais = gerenciador.listar_materiais()
    
    Application.limpar(self)
    self.create_widgtes()
    self.create_logo_seller()
    seller = Vendedores(usuario,senha)
    materiais = seller.listar_materiais()
    text_label = tk.Label(self.window, text="Materiais cadastrados:",bg= "#FFFFFF",  padx=10, pady=10)
    text_label.pack()

    # Criação da barra de rolagem
    scrollbar = ttk.Scrollbar(self.RightFrame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
    # Criação da lista de resultados
    lista_materiais = tk.Listbox(self.window, yscrollcommand=scrollbar.set, justify='center')
    lista_materiais.pack(fill="x", expand=1)
    
    for material in materiais:
      lista_materiais.insert(tk.END, f"Id: {material[0]} Nome: {material[1]} Preço: {material[3]} Quantidade_estoque: {material[4]} ")

    def mostrar_material_selecionado():
      selected_item = lista_materiais.get(tk.ACTIVE)
      
      Application.limpar(self)
      self.create_widgtes()
      self.create_logo_seller()
      
      item_label = tk.Label(self.RightFrame, text="Material selecionado:", font="Helvetica", padx=10, pady=10)
      item_label.pack()
          
      item_text = tk.Label(self.RightFrame, text=f"Id: {selected_item[0]}\nNome: {selected_item[1]}\nDescrição: {selected_item[2]}:\nPreço: {selected_item[3]}\Quantidade em estoque: {selected_item[4]}\Fabricante: {selected_item[5]}\nEstoque: {selected_item[6]}", font="Helvetica", padx=10, pady=10)
      item_text.pack()

      alterar_button = tk.Button(self.RightFrame, text="Alterar", command=lambda: self.update_material(selected_item))
      alterar_button.pack(pady=10)

      Remover_button = tk.Button(self.RightFrame, text="Remover", command=lambda: self.action_remove_material(selected_item))
      Remover_button.pack(pady=10)
      
      voltar_button = tk.Button(self.RightFrame, text="Voltar", command=self.list_material)
      voltar_button.pack(pady=10)
    
    lista_materiais.bind("<Double-Button-1>", lambda event: mostrar_material_selecionado())

    scrollbar.config(command=lista_materiais.yview)

    voltar_button = ttk.Button(self.window, text="Voltar", command=self.options_seller)
    voltar_button.place(x=500,y=400)
  # Fim do loop do vendedor
    



# Iniciar aplicação
if __name__ == "__main__":
  app = Application()
