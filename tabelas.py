import sqlite3
conn = sqlite3.connect('D:/UFPB/BD/BD_2/Materiais_de_Construcao.db')
cursor = conn.cursor()
# Criar tabela Materiais
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Materiais (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Nome TEXT,
        Descrição TEXT,
        Preço REAL,
        Quantidade_estoque INTEGER,
        Fabricante_id INTEGER,
        Estoque_id INTEGER,
        FOREIGN KEY (Fabricante_id) REFERENCES Fabricante(id),
        FOREIGN KEY (Estoque_id) REFERENCES Estoques(id)
    )
''')
# Criar tabela Fabricante
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Fabricante (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Nome TEXT,
        Produtos_fornecidos TEXT DEFAULT NULL,
        Localização TEXT
    )
''')

# Criar tabela Estoques
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Estoques (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Localização TEXT,
        Nome_estoque TEXT,
       Gerente_s TEXT DEFAULT NULL,
        Última_data_reposição TEXT,
        Data_reposição_futura TEXT
    )
''')

# Criar tabela Gerentes
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Gerentes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Nome TEXT,
        Contato TEXT,
        Usuario_id INTEGER DEFAULT NULL,
        Estoques_id INTEGER DEFAULT NULL,
        FOREIGN KEY (Usuario_id) REFERENCES Usuarios(id),
        FOREIGN KEY (Estoques_id) REFERENCES Estoques(id)
        
    )
''')

# Criar tabela Clientes
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Nome_completo TEXT NOT NULL,
        Contato TEXT,
        Time TEXT DEFAULT NULL,
        Animes_Favoritos TEXT DEFAULT NULL,
        Endereco TEXT,
        Usuario_id INTEGER DEFAULT NULL,
        FOREIGN KEY (Usuario_id) REFERENCES Usuarios(id)
    )
''')
# Criar tabela Vendedores
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Vendedores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Nome TEXT,
        Contato TEXT,
        Usuario_id INTEGER,
        Estoques_id INTEGER,
        FOREIGN KEY (Usuario_id) REFERENCES Usuarios(id),
        FOREIGN KEY (Estoques_id) REFERENCES Estoques(id)
    )
''')
# Criando a tabela de associação Materiais_Fabricantes
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Materiais_Fabricantes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Material_id INTEGER DEFAULT NULL,
        Fabricante_id INTEGER DEFAULT NULL,
        FOREIGN KEY (Material_id) REFERENCES Materiais(id),
        FOREIGN KEY (Fabricante_id) REFERENCES Fabricante(id)
    )
''')
# Criando a tabela de associação Vendedores_Clientes_Compra
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Vendedores_Clientes_Compra (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Quantidade_de_itens INTEGER,
        Material_id INTEGER,
        Cliente_id INTEGER,
        Vendedor_id INTEGER,
        Data_da_Compra TEXT,
        Forma_de_Pagamento TEXT,
        FOREIGN KEY (Material_id) REFERENCES Materiais(id),
        FOREIGN KEY (Cliente_id) REFERENCES Clientes(id),
        FOREIGN KEY (Vendedor_id) REFERENCES Vendedores(id)
    )
''')
# Criando a tabela de associação de Usuarios
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Tipo TEXT,
        Usuario TEXT NOT NULL UNIQUE,
        Senha TEXT NOT NULL
    )
''')

# Criando a tabela de associação de Estoques_Gerentes
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Estoques_Gerentes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Estoques_id INTEGER DEFAULT NULL,
        Gerentes_id INTEGER DEFAULT NULL,
        FOREIGN KEY (Estoques_id) REFERENCES Estoques(id),
        FOREIGN KEY (Gerentes_id) REFERENCES Gerentes(id)
    )
''')
conn.commit()
conn.close()
