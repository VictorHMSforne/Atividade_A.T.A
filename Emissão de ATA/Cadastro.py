import os, sqlite3
import Criar_BD
from datetime import date
from datetime import datetime

db= "TabAta.db"

def cadastrar_funcionario():
    
    os.system("cls")
    dados_funci =[]
    print("=========CADASTRAR FUNCIONÁRIO=========")
    nome = input("Digite seu nome: ")
    cpf = int(input("Digite seu CPF: "))
    dados_funci = [nome,cpf]
    
    conex = sqlite3.connect(db)
    cursor = conex.cursor()
    
    cursor.execute('''INSERT INTO tabFuncionario(Nome,cpf)
                   VALUES(?,?)''',dados_funci)
    conex.commit()
    cursor.close()
    conex.close()



def cadastrar_ata():
   
    participantes = []
    
    print("==========CADASTRO DE ATAS===========")
    titulo = input("Digite o Título da ATA: ")
    data_H= date.today()
    data_inserida= input("Digite a data de Término da Reunião, no formato(YYYY-MM-DD): ")
    pauta = input("Digite a Pauta da Reunião:\n ")

    quantidade_participantes = int(input("Digite o número de participantes da reunião: "))
    if (quantidade_participantes < 2):
        os.system("cls")
        print("É necessário DOIS ou MAIS participantes para criar uma ATA!!!")
        cadastrar_ata()
    else:
        for i in range(quantidade_participantes):
         nome_participante = input(f"Digite o Nome do {i+1}°: ")
         participantes.append(nome_participante)
    
    conex = sqlite3.connect(db)
    cursor = conex.cursor()
    cursor.execute('''INSERT INTO tabAta(Titulo,Data_Início,Data_Término,Pauta) 
                   VALUES(?,?,?,?) ''',(titulo,data_H,data_inserida,pauta))
    
    ata_id = cursor.lastrowid
    for participante in participantes:
        cursor.execute('''INSERT INTO tabParticipantes(Nome,Ata_ID) VALUES (?,?)''', (participante, ata_id))
    


    conex.commit()
    cursor.close()
    conex.close()

    




            