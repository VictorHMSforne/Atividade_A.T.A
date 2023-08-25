import os
import Cadastro,exibir
resposta = 's'

while resposta == 's':
    menu = ''' ======== REGISTRAR ATAS ========
      \r 1-Cadastro de Funcionários
      \r 2-Realizar Registro de ATA
      \r 3-Exibir ATA Registradas
      \r 4-Exibir Funciónarios Cadastrados
      \r 5-Exibir Partipantes das ATAS
    '''
    print(menu)
    
    opcao = int(input("Entre com uma opção:"))
    if opcao == 1:
        os.system("cls")
        Cadastro.cadastrar_funcionario()
    if opcao == 2:
        Cadastro.cadastrar_ata()
    if opcao == 3:
        exibir.atas_registradas()
    if opcao == 4:
        exibir.funcionarios_registrados()
    if opcao == 5:
        exibir.ptc_ATAS()
    resposta = input("Gostaria de continuar? s/n ").lower()



