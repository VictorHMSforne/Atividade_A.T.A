import sqlite3

def criar_tabela():
    conex = sqlite3.connect("TabAta.db")
    cursor = conex.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tabAta(ataCod INTEGER PRIMARY KEY AUTOINCREMENT,
            Titulo TEXT,
            Data_Início DATE,
            Data_Término INTEGER,
            Pauta TEXT
        )
    ''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS tabParticipantes(participante_ID INTEGER PRIMARY KEY,
                   Nome TEXT,
                   Ata_ID INTEGER,
                   FOREIGN KEY (Ata_ID) REFERENCES tabAta (Ata_ID)
    
         ) 
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tabFuncionario(funciCod INTEGER PRIMARY KEY AUTOINCREMENT,
            Nome TEXT,
            cpf TEXT
        )
    ''')
    
    conex.commit()
    cursor.close()
    conex.close()

criar_tabela()
