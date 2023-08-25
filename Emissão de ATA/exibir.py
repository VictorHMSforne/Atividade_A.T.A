import os
import sqlite3

def atas_registradas():
    os.system("cls")
    conex = sqlite3.connect("TabAta.db")
    cursor = conex.cursor()

    cursor.execute('''SELECT * FROM tabAta''')

    resultados = cursor.fetchall()
    print("=================================")
    print("====     ATAS REGISTRADAS     ===")
    print("=================================")
    for tela in resultados:
        print(tela)
    
    conex.commit()
    cursor.close()
    conex.close()


def funcionarios_registrados():
    os.system("cls")
    conex = sqlite3.connect("TabAta.db")
    cursor = conex.cursor()

    cursor.execute("SELECT * FROM tabFuncionario")

    resultados = cursor.fetchall()


    print("=================================")
    print("===  FUNCIOnÁRIOS REGISTRADOS ===")
    print("=================================")
    for tela in resultados:
        print(resultados)
    
    conex.commit()
    cursor.close()
    conex.close()


def ptc_ATAS():
    os.system("cls")
    conex = sqlite3.connect("TabAta.db")
    cursor = conex.cursor()

    cursor.execute('''SELECT * FROM tabParticipantes''')

    resultados = cursor.fetchall()
    print("=================================")
    print("====  PARTICIPANTES DAS ATAS  ===")
    print("=================================")
    print("CÓDIGO  NOME  ATA(participou)")
    for tela in resultados:
        print(tela)

    conex.commit()
    cursor.close()
    conex.close()

