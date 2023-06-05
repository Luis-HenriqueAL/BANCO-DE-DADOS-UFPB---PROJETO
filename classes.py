import sqlite3
import hashlib
import re

class Conectar_BD:
    @staticmethod
    def conectar():
        conexao = sqlite3.connect("D:/UFPB/BD/BD_2/Materiais_de_Construcao.db")
        return conexao


class Usuarios:
    @staticmethod
    def criar_hash(senha):
        return hashlib.sha256(senha.encode()).hexdigest()

    @staticmethod
    def verificar_hash(senha, hash_senha):
        return Usuarios.criar_hash(senha) == hash_senha

    @staticmethod
    def cadastrar_usuario(tipo, usuario, senha):
        hash_senha = Usuarios.criar_hash(senha)
        conn = Conectar_BD.conectar()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Usuarios (Tipo, Usuario, Senha) VALUES (?, ?, ?)", (tipo, usuario, hash_senha))
        conn.commit()
        conn.close()
        return cursor.lastrowid

    @staticmethod
    def obter_hash_senha(usuario):
        conn = Conectar_BD.conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT Senha FROM Usuarios WHERE Usuario = ?", (usuario,))
        result = cursor.fetchone()
        conn.close()
        if result:
            return result[0]
        return None

    @staticmethod
    def autenticar_usuario(usuario, senha):
        hash_senha = Usuarios.obter_hash_senha(usuario)
        if hash_senha is not None:
            return Usuarios.verificar_hash(senha, hash_senha)
        return False

    @staticmethod
    def alterar_senha(usuario, nova_senha):
        hash_senha = Usuarios.criar_hash(nova_senha)
        conn = Conectar_BD.conectar()
        cursor = conn.cursor()
        cursor.execute("UPDATE Usuarios SET Senha = ? WHERE Usuario = ?", (hash_senha, usuario))
        conn.commit()
        conn.close()
        return cursor.rowcount
    
    @staticmethod
    def pesquisar_usuario(usuario):
        conn = Conectar_BD.conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Usuarios WHERE Usuario = ?", (usuario,))
        result = cursor.fetchone()
        conn.close()
        return result
    @staticmethod
    def remover_usuario(usuario):
        conexao = Conectar_BD.conectar()
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM Usuarios WHERE Usuario = ?", (usuario,))
        conexao.commit()
        conexao.close()
'''
# classe Usuarios

# Cadastrar um novo usuário
Usuarios.cadastrar_usuario('Administrador', 'admin', '1234')

# Autenticar um usuário
autenticado = Usuarios.autenticar_usuario('admin', '1234')
if autenticado:
    print("Usuário autenticado com sucesso!")
    tipo = Usuarios.pesquisar_usuario("admin")
    print(tipo[1]) # Aqui mostra o tipo dele gerente, Adminstrador ou vendeddor
else:
    print("Usuário ou senha inválidos.")

# Alterar a senha de um usuário
#Usuarios.alterar_senha('admin', 'novasenha456')
'''
class Clientes:
    def __init__(self, usuario_id,usuario, senha):
        self.id = usuario_id
        self.usuario =usuario
        self.senha=senha

    @staticmethod
    def inserir_clente(Nome_completo, Contato, Time, animes_favoritos, endereco,usuario, senha):
        conexao = Conectar_BD.conectar()
        cursor = conexao.cursor()
        Usuarios.cadastrar_usuario("Cliente", usuario, senha)
        Usuario_id = Usuarios.pesquisar_usuario(usuario)
        cursor.execute('''
        INSERT INTO Clientes (Nome_completo, Contato, Time, Animes_Favoritos, Endereco, Usuario_id)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (Nome_completo.lower(), Contato, Time.lower(), animes_favoritos.lower(), endereco, Usuario_id[0]))
        conexao.commit()
        conexao.close()

    @staticmethod
    def pesquisar_por_nome_do_Clientes(nome):
        conexao = Conectar_BD.conectar()
        cursor = conexao.cursor()
        cursor.execute(f"SELECT * FROM Clientes WHERE Nome_completo LIKE '%{nome}%'")
        materiais = cursor.fetchall()
        conexao.close()
        return materiais
    def alterar_Clientes(self,id,Nome_completo,Contato,Time,Animes_Favoritos,Endereco,usuario=None,senha=None):
        conexao = Conectar_BD.conectar()
        Usuario_id = Usuarios.pesquisar_usuario(usuario)
        if(usuario!=None and senha!=None):
            Usuarios.alterar_senha(usuario,senha)
        cursor = conexao.cursor()
        cursor.execute(f"UPDATE Clientes SET Nome_completo = '{Nome_completo}', Contato = '{Contato}', Time = '{Time}', Animes_Favoritos = '{Animes_Favoritos}', Endereco = '{Endereco}',Usuario_id = '{Usuario_id[0]}' WHERE Id = {id}")
        conexao.commit()
        conexao.close()

    @staticmethod
    def remover_clente(id):
        conexao = Conectar_BD.conectar()
        cursor = conexao.cursor()
        cursor.execute(f"SELECT Usuario FROM Usuarios WHERE id IN (SELECT Usuario_id FROM Clientes WHERE id = {id})")
        Usuario = cursor.fetchall()
        Usuarios.remover_usuario(Usuario[0][0])
        cursor.execute(f"DELETE FROM Clientes WHERE Id = {id}")
        conexao.commit()
        conexao.close()

    def pesquisar_all(texto, preco_min, preco_max):
        conexao = Conectar_BD.conectar()
        cursor = conexao.cursor()
        palavras = re.split(',|;', texto)
        materiais_encontrados = set()
        fabricantes_encontrados = set()

        for palavra in palavras:
            # Verificar se a palavra é um nome de material da tabela "Materiais"
            cursor.execute('SELECT id, Nome, Preço FROM Materiais WHERE Nome = ?', (palavra,))
            resultado_material = cursor.fetchone()

            if resultado_material:
                id_material = resultado_material[0]
                nome_material = resultado_material[1]
                preco_material = resultado_material[2]
                materiais_encontrados.add((id_material, nome_material, preco_material))

            # Verificar se a palavra é um nome de fabricante da tabela "Fabricante"
            cursor.execute('SELECT id, Nome FROM Fabricante WHERE Nome = ?', (palavra,))
            resultado_fabricante = cursor.fetchone()

            if resultado_fabricante:
                id_fabricante = resultado_fabricante[0]
                nome_fabricante = resultado_fabricante[1]
                fabricantes_encontrados.add((id_fabricante, nome_fabricante))

        # Consulta SQL para recuperar produtos dentro da faixa de preço e seus fabricantes
        query = '''
            SELECT Materiais.id, Materiais.Nome, Materiais.Preço, Fabricante.Nome
            FROM Materiais
            INNER JOIN Fabricante ON Materiais.Fabricante_id = Fabricante.id
            WHERE (Materiais.Nome IN ({}) OR Fabricante.Nome IN ({}))
            AND Materiais.Preço >= ? AND Materiais.Preço <= ?
        '''.format(','.join('?' * len(materiais_encontrados)), ','.join('?' * len(fabricantes_encontrados)))

        parametros = [item for sublist in materiais_encontrados for item in sublist] + [item for sublist in fabricantes_encontrados for item in sublist] + [preco_min, preco_max]
        cursor.execute(query, parametros)
        resultados = cursor.fetchall()

        # Exibindo os materiais encontrados
        if materiais_encontrados:
            print("Materiais encontrados:")
            for material in materiais_encontrados:
                id_material = material[0]
                nome_material = material[1]
                preco_material = material[2]
                print(f"ID: {id_material}, Material: {nome_material}, Preço: {preco_material}")

        # Exibindo os fabricantes encontrados
        if fabricantes_encontrados:
            print("Fabricantes encontrados:")
            for fabricante in fabricantes_encontrados:
                id_fabricante = fabricante[0]
                nome_fabricante = fabricante[1]
                print(f"ID: {id_fabricante}, Fabricante: {nome_fabricante}")

        # Exibindo os resultados da junção entre Materiais e Fabricante
        Lista_encontrada = ""
        if resultados:
            print("Resultados:")
            for resultado in resultados:
                id_material = resultado[0]
                nome_material = resultado[1]
                preco_material = resultado[2]
                nome_fabricante = resultado[3]
                print(f"ID: {id_material}, Material: {nome_material}, Preço: {preco_material}, Fabricante: {nome_fabricante}")
                Lista_encontrada = Lista_encontrada + f"ID: {id_material}, Material: {nome_material}, Preço: {preco_material}, Fabricante: {nome_fabricante}"
        else:
            print("Nenhum resultado encontrado.")
        return Lista_encontrada

        conexao.close()

    def efetivar_compra(quantidade, id_material, id_cliente, id_vendedor, data_compra, forma_pagamento):
        conn = sqlite3.connect('D:/UFPB/BD/BD_2/Materiais_de_Construcao.db')
        cursor = conn.cursor()

        # Check available stock
        cursor.execute('''
            SELECT Quantidade_estoque FROM Materiais WHERE id = ?
        ''', (id_material,))
        estoque = cursor.fetchone()[0]

        if (estoque < quantidade) or (estoque==0):
            conn.close()
            return "Erro: Produto sem estoque suficiente."

        # Obter informações do cliente
        cursor.execute('''
            SELECT * FROM Clientes WHERE id = ?
        ''', (id_cliente,))
        cliente = cursor.fetchone()

        # Verificar se o cliente tem direito a desconto
        if cliente[3] == 'flamengo' or 'one piece' in cliente[4] or  'Sousa' in cliente[1]:
            desconto = 0.1  # Desconto de 10%
        else:
            desconto = 0

        # Calcular o preço com desconto
        cursor.execute('''
            SELECT Preço FROM Materiais WHERE id = ?
        ''', (id_material,))
        preco = cursor.fetchone()[0]
        preco_desconto = preco - (preco * desconto)

        # Inserir o registro de compra na tabela
        cursor.execute('''
            INSERT INTO Vendedores_Clientes_Compra (Quantidade_de_itens, Material_id, Cliente_id, Vendedor_id, Data_da_Compra, Forma_de_Pagamento, Preço_desconto)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (quantidade, id_material, id_cliente, id_vendedor, data_compra, forma_pagamento, preco_desconto))

        # Atualizar quantidade de estoque
        novo_estoque = estoque - quantidade
        cursor.execute('''
            UPDATE Materiais SET Quantidade_estoque = ? WHERE id = ?
        ''', (novo_estoque, id_material))

        conn.commit()
        conn.close()

        return "Compra realizada com sucesso."


# class Clientes
'''
Cliente = Clientes()
Cliente.inserir_clientes('João', 'joao@example.com', 'São Paulo FC', 'One Piece, Naruto', 'Rua A, 123', "Netinho3", "12345")
'''

class Vendedores(Clientes):
    def __init__(self, usuario_id,usuario, senha):
        self.id = usuario_id
        self.usuario =usuario
        self.senha=senha    

    @staticmethod
    def cadastrar_Vendedor(nome, contato, Estoques_id, usuario, senha):
        try:
            conexao = Conectar_BD.conectar()
            cursor = conexao.cursor()
            Usuarios.cadastrar_usuario("Vendedor", usuario, senha)

            query = '''
                INSERT INTO Vendedores (Nome, Contato, Usuario_id, Estoques_id)
                SELECT ?, ?, Usuarios.id, Estoques.id
                FROM Usuarios
                INNER JOIN Estoques ON Estoques.id = ?
                WHERE Usuarios.Usuario = ?
            '''

            cursor.execute(query, (nome, contato, Estoques_id, usuario))
            conexao.commit()
            print("Vendedor inserido com sucesso.")
            conexao.close()
        except:
            print(f"Usuário já existe,vendedor {usuario}")
            return

    @staticmethod
    def alterar_Vendedor(id, nome, contato, Estoques_id, usuario=None, senha=None):
        conexao = Conectar_BD.conectar()
        cursor = conexao.cursor()

        if usuario and senha:
            Usuarios.alterar_senha(usuario, senha)

        query = '''
            UPDATE Vendedores
            SET Nome = ?, Contato = ?, Usuario_id = Usuarios.id, Estoques_id = ?
            FROM Usuarios
            INNER JOIN Estoques ON Vendedores.Estoques_id = Estoques.id
            WHERE Vendedores.Id = ?
        '''

        cursor.execute(query, (nome, contato, Estoques_id, id))
        conexao.commit()
        conexao.close()

    @staticmethod
    def listar_todos_os_vendedores():
        conexao = Conectar_BD.conectar()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM Vendedores")
        Vend = cursor.fetchall()
        conexao.close()
        return Vend   
    @staticmethod
    def pesquisar_por_nome_do_vendedor(nome):
        conexao = Conectar_BD.conectar()
        cursor = conexao.cursor()
        cursor.execute(f"SELECT * FROM Vendedores WHERE Nome LIKE '%{nome}%'")
        Vend = cursor.fetchall()
        conexao.close()
        return Vend
    @staticmethod
    def remover_vendedor(id):
        conexao = Conectar_BD.conectar()
        cursor = conexao.cursor()
        cursor.execute(f"SELECT Usuario FROM Usuarios WHERE id IN (SELECT Usuario_id FROM Vendedores WHERE id = {id})")
        Usuario = cursor.fetchall()
        Usuarios.remover_usuario(Usuario[0][0])
        cursor.execute(f"DELETE FROM Vendedores WHERE id = {id}")
        conexao.commit()        
        conexao.close()

    #Materiais------------------------------------------
    def inserir_material(self,Nome, Descrição, Preço, Quantidade_estoque, Fabricante_id):
        material_novo = Material(self.id,self.usuario,self.senha)
        conexao = Conectar_BD.conectar()
        cursor = conexao.cursor()
        cursor.execute(f"SELECT Tipo FROM Usuarios WHERE id = {self.id}")
        tipo_id = cursor.fetchall()
        if(tipo_id=="Vendedor"):
            cursor.execute(f"SELECT Estoques_id FROM Vendedores WHERE Usuario_id IN (SELECT id FROM Usuarios WHERE Usuario = '{self.usuario}')")
            Estoque_id = cursor.fetchone()
        else:
            cursor.execute(f"SELECT Estoques_id FROM Gerentes WHERE Usuario_id IN (SELECT id FROM Usuarios WHERE Usuario = '{self.usuario}')")
            Estoque_id = cursor.fetchone()
        material_novo.inserir(Nome, Descrição, Preço, Quantidade_estoque, Fabricante_id, int(Estoque_id[0]))

    @staticmethod
    def listar_materiais():
        return Material.listar_todos()
   
    def remover_material(self, id):
        material = Material(self.id,self.usuario,self.senha)
        material.remover(id)
    
    def alterar_material(self,Nome, Descrição, Preço, Quantidade_estoque, Fabricante_id):
        material = Material(self.id,self.usuario,self.senha)
        conexao = Conectar_BD.conectar()
        cursor = conexao.cursor()
        cursor.execute(f"SELECT Tipo FROM Usuarios WHERE id = {self.id}")
        tipo_id = cursor.fetchall()
        if(tipo_id=="Vendedor"):
            cursor.execute(f"SELECT Estoques_id FROM Vendedores WHERE Usuario_id IN (SELECT id FROM Usuarios WHERE Usuario = '{self.usuario}')")
            Estoque_id = cursor.fetchone()
        else:
            cursor.execute(f"SELECT Estoques_id FROM Gerentes WHERE Usuario_id IN (SELECT id FROM Usuarios WHERE Usuario = '{self.usuario}')")
            Estoque_id = cursor.fetchone()
        material.alterar(Nome, Descrição, Preço, Quantidade_estoque, Fabricante_id, int(Estoque_id[0]))

    
'''
# class Vendedores

vendedor = Vendedores(1,'admin', '1234')
vendedor.inserir_clente('João', 'joao@example.com', 'São Paulo FC', 'One Piece, Naruto', 'Rua A, 123', "Netinho3", "12345")
'''


class Gerente(Vendedores):
    def __init__(self, usuario_id,usuario, senha):
        self.id = usuario_id
        self.usuario =usuario
        self.senha=senha
    
    @staticmethod
    def atualiza_estoque(Estoques_id):
        conexao = Conectar_BD.conectar()
        cursor = conexao.cursor()
        cursor.execute(f"SELECT Nome,Contato FROM Gerentes WHERE id IN (SELECT Gerentes_id FROM Estoques_Gerentes WHERE Estoques_id = '{Estoques_id}')")
        Gerent = cursor.fetchall()
        lista_gerent = ''
        for i in Gerent:
            lista_gerent = lista_gerent +f"Nome do Gerente: {i[0]}\nContato: {i[1]}\n"
        cursor.execute(f"UPDATE Estoques SET Gerente_s = '{lista_gerent}' WHERE id = {Estoques_id}" )
        conexao.commit()
        conexao.close()

    @staticmethod
    def inserir_gerente(nome, contato,Estoques_id,usuario, senha):
        try:
            conexao = Conectar_BD.conectar()
            cursor = conexao.cursor()
            Usuarios.cadastrar_usuario("Gerente", usuario, senha)
            query = '''
                INSERT INTO Gerentes (Nome, Contato, Usuario_id, Estoques_id)
                SELECT ?, ?, Usuarios.id, Estoques.id
                FROM Usuarios
                INNER JOIN Estoques ON Estoques.id = ?
                WHERE Usuarios.Usuario = ?
                '''
            cursor.execute(query, (nome, contato, Estoques_id, usuario))
            conexao.commit()
            print("Gerente inserido com sucesso.")
            grent_id = cursor.lastrowid
            cursor.execute('INSERT INTO Estoques_Gerentes(Estoques_id,Gerentes_id) VALUES (?, ?)', (Estoques_id,grent_id))
            conexao.commit()
            Gerente.atualiza_estoque(Estoques_id)
            conexao.close()
        except:
            print(f"Usuário já existe, gerente {usuario}")
        return
       
    def alterar_Gerente(self, id, nome, contato,Estoques_id=None, usuario=None, senha=None):
        conexao = Conectar_BD.conectar()
        cursor = conexao.cursor()
        
        if usuario is not None and senha is not None:
            Usuarios.alterar_senha(usuario, senha)
        

        query = '''
            UPDATE Gerentes
            SET Nome = ?, Contato = ?, Usuario_id = Usuarios.id, Estoques_id = ?
            FROM Usuarios
            INNER JOIN Estoques ON Gerentes.Estoques_id = Estoques.id
            WHERE Gerentes.Id = ?
        '''
        
        cursor.execute(query, (nome, contato, Estoques_id, id))
        conexao.commit()
        conexao.close()

    @staticmethod
    def listar_todos():
        conexao = Conectar_BD.conectar()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM Gerentes")
        Gerent = cursor.fetchall()
        conexao.close()
        return Gerent
    
    @staticmethod
    def pesquisar_por_nome(nome):
        conexao = Conectar_BD.conectar()
        cursor = conexao.cursor()
        cursor.execute(f"SELECT * FROM Gerentes WHERE Nome LIKE '%{nome}%'")
        Gerent = cursor.fetchall()
        conexao.close()
        return Gerent
    
    @staticmethod
    def remover(id):
        conexao = Conectar_BD.conectar()
        cursor = conexao.cursor()
        cursor.execute(f"SELECT Usuario FROM Usuarios WHERE id IN (SELECT Usuario_id FROM Gerentes WHERE id = {id})")
        Usuario = cursor.fetchall()
        Usuarios.remover_usuario(Usuario[0][0])
        cursor.execute(f"SELECT Estoques_id FROM Gerentes WHERE Id = {id}")
        Estoques_id = cursor.fetchone()
        Gerente.atualiza_estoque(int(Estoques_id))
        cursor.execute(f"DELETE FROM Gerentes WHERE Id = {id}")
        Gerente.atualiza_estoque(Estoques_id[0])
        conexao.commit()
        conexao.close()
    #Fabricante---------------------------------------------------------
    def cadastrar_fornecedor(self,nome,localizacao):
        fornecedor= Fabricantes(self.id,self.usuario,self.senha)
        fornecedor.inserir(nome, localizacao)
    def remover_fornecedor(self,id):
        fornecedor= Fabricantes(self.id,self.usuario,self.senha)
        fornecedor.remover(id)

    def pesquisar_fornecedor_por_nome(nome):
        return Fabricantes.pesquisar_por_nome(nome)
    
    def listar_todos_fabricante(self,):
        return Fabricantes.listar_todos()
    
    def alterar_fabricante(self,nome, produtos_fornecidos, localizacao, contato_gerente):
        fornecedor= Fabricantes(self.id,self.usuario,self.senha)
        fornecedor.alterar(nome, produtos_fornecidos, localizacao, contato_gerente)
'''
#class Gerente

gerente = Gerente(1,'admin', '1234')
gerente.cadastrar_Vendedor("João", "joao@example.com", "Netinho12", "12345")
gerente.alterar_Vendedor(1,"vito", "joao", "Netinho12","12345")
'''

class Estoques:
    def __init__(self, usuario_id,usuario, senha):
        self.id = usuario_id
        self.usuario =usuario
        self.senha=senha
    
    def inserir_novo_estoque(self, localizacao, nome_estoque, ultima_data_reposicao, data_reposicao_futura):
        conexao = Conectar_BD.conectar()
        cursor = conexao.cursor()

        # Em seguida, insira o estoque na tabela Estoques
        cursor.execute('''
            INSERT INTO Estoques (Localização, Nome_estoque, Última_data_reposição, Data_reposição_futura)
            VALUES (?, ?, ?, ?)
        ''', (localizacao, nome_estoque, ultima_data_reposicao, data_reposicao_futura))

        conexao.commit()
        print("Novo estoque inserido com sucesso!")
        conexao.close()

    def remover_estoque(self, estoque_id):
        conexao = Conectar_BD.conectar()
        cursor = conexao.cursor()
        cursor.execute('DELETE FROM Estoques WHERE id = ?', (estoque_id,))
        conexao.commit()
        print("Estoque removido com sucesso!")
    
    def alterar_estoque(self, id, localizacao, nome_estoque, ultima_data_reposicao, data_reposicao_futura):
        conexao = Conectar_BD.conectar()
        cursor = conexao.cursor()

        query = '''
            UPDATE Estoques
            SET Localização = ?,
                Nome_estoque = ?,
                Última_data_reposição = ?,
                Data_reposição_futura = ?
            WHERE Estoques.Id = ?
        '''
        cursor.execute(query, (localizacao, nome_estoque, ultima_data_reposicao, data_reposicao_futura, id))
        conexao.commit()
        conexao.close()
    @staticmethod
    def pesquisar_por_nome_estoque(nome):
        conexao = Conectar_BD.conectar()
        cursor = conexao.cursor()
        cursor.execute(f"SELECT * FROM Estoques WHERE Nome_estoque LIKE '%{nome}%'")
        Estoq = cursor.fetchall()
        return Estoq
'''
# classe Estoques
estoques = Estoques(2,'admin', '1234')
estoques.inserir_novo_estoque("Local A", "Estoque A", 1, "2023-05-26", "2023-05-28")
#estoques.remover_estoque(1)
'''
class Fabricantes:
    def __init__(self, usuario_id,usuario, senha):
        self.usuario_id = usuario_id
        self.usuario =usuario
        self.senha=senha
    def inserir(self, nome, localizacao):
        conexao = Conectar_BD.conectar()
        cursor = conexao.cursor()
        cursor.execute('''
            INSERT INTO Fabricante (Nome, Localização)
            VALUES (?, ?)
        ''', (nome,localizacao))
        conexao.commit()
        conexao.close()

    def alterar(self,id,nome, produtos_fornecidos, localizacao, contato_gerente):
        conexao = Conectar_BD.conectar()
        cursor = conexao.cursor()
        cursor.execute(f"UPDATE Fabricante SET Nome = '{nome}', Produtos_fornecidos = {produtos_fornecidos}, Localização = '{localizacao}', Contato_gerente = {contato_gerente} WHERE Id = {id}")
        conexao.commit()
        conexao.close()
    @staticmethod
    def listar_todos():
        conexao = Conectar_BD.conectar()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM Fabricante")
        Fabrican = cursor.fetchall()
        conexao.close()
        return Fabrican
    @staticmethod
    def pesquisar_por_nome(nome):
        conexao = Conectar_BD.conectar()
        cursor = conexao.cursor()
        cursor.execute(f"SELECT * FROM Fabricante WHERE Nome LIKE '%{nome}%'")
        Fabrican = cursor.fetchall()
        conexao.close()
        return Fabrican
    def remover(self,id):
        conexao = Conectar_BD.conectar()
        cursor = conexao.cursor()
        cursor.execute(f"DELETE FROM Fabricante WHERE Id = {id}")
        conexao.commit()
        conexao.close()

'''
# classe Fabricantes
fabricantes = Fabricantes(2,'admin', '1234')
lista = fabricantes.listar_todos()
print(lista)
fabricantes.pesquisar_por_nome('Fabricante A')
fabricantes.remover(2)
'''
class Material:
    def __init__(self, usuario_id,usuario, senha):
        self.usuario_id = usuario_id
        self.usuario =usuario
        self.senha=senha

    @staticmethod
    def atualiza_fabricante(Fabricante_id):
        conexao = Conectar_BD.conectar()
        cursor = conexao.cursor()
        cursor.execute(f"SELECT Nome FROM Materiais WHERE id IN (SELECT Material_id FROM Materiais_Fabricantes WHERE Fabricante_id = '{Fabricante_id}')")
        MAT = cursor.fetchall()
        lista_Materiais = ''
        for i in MAT:
            lista_Materiais = lista_Materiais +f"Nome do Item: {i[0]}"
        cursor.execute(f"UPDATE Fabricante SET Produtos_fornecidos = '{lista_Materiais}' WHERE id = {Fabricante_id}" )
        conexao.commit()
        conexao.close()

    def inserir(self, Nome, Descrição, Preço, Quantidade_estoque, Fabricante_id,Estoque_id):
        conexao = Conectar_BD.conectar()
        cursor = conexao.cursor()
        if(type(Preço)!=int or type(Quantidade_estoque)!= int or type(Fabricante_id)!=int or type(Estoque_id)!=int):
            print("campos errados")
            return
        query = '''
            INSERT INTO Materiais (Nome, Descrição, Preço, Quantidade_estoque, Fabricante_id, Estoque_id)
            SELECT ?, ?, ?, ?, Fabricante.id, Estoques.id
            FROM Fabricante
            INNER JOIN Estoques ON Estoques.id = ?
            WHERE Fabricante.id = ?
        '''
        cursor.execute(query, (Nome, Descrição, Preço, Quantidade_estoque, Estoque_id, Fabricante_id))
        conexao.commit()
        novo_material_id = cursor.lastrowid
        cursor.execute('INSERT INTO Materiais_Fabricantes (Material_id,Fabricante_id) VALUES (?, ?)', (novo_material_id,Fabricante_id))
        conexao.commit()
        Material.atualiza_fabricante(Fabricante_id)
        conexao.close()

    @staticmethod
    def listar_todos():
        conexao = Material.conectar()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM Materiais")
        materiais = cursor.fetchall()
        conexao.close()
        return materiais

    @staticmethod
    def exibir_um(id):
        conexao = Material.conectar()
        cursor = conexao.cursor()
        cursor.execute(f"SELECT * FROM Materiais WHERE Id = {id}")
        material = cursor.fetchone()
        conexao.close()
        return material

    def alterar(self, Nome, Descrição, Preço, Quantidade_estoque, Fabricante_id, Estoque_id):
        conexao = Conectar_BD.conectar()
        cursor = conexao.cursor()

        query = '''
            UPDATE Materiais
            SET Nome = ?, Descrição = ?, Preço = ?, Quantidade_estoque = ?, Fabricante_id = ?, Estoque_id = ?
            FROM Fabricante
            INNER JOIN Estoques ON Estoques.id = ?
            WHERE Materiais.id = ?
            AND Fabricante.id = ?
        '''
        cursor.execute(query, (Nome, Descrição, Preço, Quantidade_estoque, Fabricante_id, Estoque_id, Estoque_id, self.id, Fabricante_id))
        Material.atualiza_fabricante(Fabricante_id)
        conexao.commit()
        conexao.close()

    def remover(self,id):
        conexao = Conectar_BD.conectar()
        cursor = conexao.cursor()
        cursor.execute(f"SELECT Fabricante_id FROM Materiais WHERE Id = {id}")
        Fabricante_id = cursor.fetchone()
        Material.atualiza_fabricante(int(Fabricante_id[0]))
        cursor.execute(f"DELETE FROM Materiais WHERE Id = {id}")
        conexao.commit()
        conexao.close()


class ADM:
    @staticmethod
    def iniciar():
        Usuarios.cadastrar_usuario('Administrador', 'admin', '1234')
        estq = Estoques(1,'admin', '1234')
        estq.inserir_novo_estoque("CASA", "MINHA CASA.COM", "12/11/2011", "15/08/2027")
        gere = Gerente(1,'admin', '1234')
        gere.inserir_gerente("João", "joao@example.com",1,"gerent12", "12345")
        gere.cadastrar_Vendedor("João", "joao@example.com",1,"Netinho12", "12345")
        gere.inserir_gerente("João2", "joao@example.com",1,"gerent122", "12345")
        gere.cadastrar_fornecedor("JORGE","LONGE")
        gere = Gerente(2,"gerent12", "12345")
        gere.inserir_material("Nome1", "Descrição2", 12, 1, 1)
        print(Estoques.pesquisar_por_nome_estoque("minha"))
        gere.inserir_clente('João', 'joao@example.com', 'São Paulo FC', 'One Piece, Naruto', 'Rua A, 123', "Netinho3", "12345")
        


    def testes():
        nome_estoque = "minha"
        #print(Estoques.pesquisar_por_nome_estoque(nome_estoque))
        gere = Gerente(2,"gerent12", "12345")
        vend= Vendedores(3,"Netinho12", "12345")
        #gere.inserir_material("Nome1", "Descrição2", 12, 1, 1)
        #gere.inserir_gerente("João2", "joao@example.com", 1,None,"gerent122", "12345")
        #gere.inserir_clente('João', 'joao@example.com', 'São Paulo FC', 'One Piece, Naruto', 'Rua A, 123', "Netinho3", "12345")
        #gere.remover_vendedor(1)
        #gere.remover_clente(1)
        
            

ADM.iniciar()
