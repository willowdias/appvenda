import sqlite3

# Conectar-se ao banco de dados SQLite
conn = sqlite3.connect('app.db')
cursor = conn.cursor()

# Nome da tabela que deseja exportar
nome_tabela = 'usuario'

# Consultar todos os registros da tabela
cursor.execute(f"SELECT * FROM {nome_tabela}")
registros = cursor.fetchall()

# Nome do arquivo de texto para exportação
nome_arquivo = 'exportacao.txt'

# Exportar registros para o arquivo de texto
with open(nome_arquivo, 'w') as arquivo:
    # Gerar comandos INSERT para cada registro
    for registro in registros:
        colunas = ', '.join(str(coluna) for coluna in registro)
        comando_insert = f"INSERT INTO app.{nome_tabela}(id,name,senha)VALUES ({colunas});"
        arquivo.write(f"{comando_insert}\n")

print(f"A tabela '{nome_tabela}' foi exportada com sucesso para o arquivo '{nome_arquivo}'.")

# Fechar conexão com o banco de dados
conn.close()
