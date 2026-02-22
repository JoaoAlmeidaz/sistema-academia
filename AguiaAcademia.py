import os

listadealunos = [{"nome":"Matheus", "idade":"16", "Plano":"Basico", "ativo":False}, 
                {"nome":"Jonas", "idade":"19", "Plano":"Intermediario", "ativo":True},
                {"nome":"Melchior", "idade":"20", "Plano":"Pro", "ativo":False}]

def exibir_nome_do_programa():
    print("Nome do programa\n")
    print("""
    ▄▀█ █▀▀ █░█ █ ▄▀█   ▄▀█ █▀▀ ▄▀█ █▀▄ █▀▀ █▀▄▀█ █ ▄▀█
    █▀█ █▄█ █▄█ █ █▀█   █▀█ █▄▄ █▀█ █▄▀ ██▄ █░▀░█ █ █▀█
    """)

def exibir_opcoes():
    print("1 - Cadastrar Aluno (Nome, Idade, Plano)")
    print("2 - Listar Aluno")
    print("3 - Ativar/Desativar Aluno\n")
    escolha = int(input("Escolha uma Opção: "))
    if escolha == 1:
        print("Você escolheu a Opção 1")
        input("Aperte enter para continuar")
        cadastrar_aluno()
    elif escolha == 2:
        print("Voce escolheu a Opção 2")
        input("Aperte enter para continuar")
        os.system("cls")
        listar_aluno()
    elif escolha == 3:
        print("Você escolheu a Opção 3")
        input("Aperte enter para continuar")
        os.system("cls")
        ativar_desativar_aluno()
    else:
        print("Opção Invalida")
        input("Aperte enter para reiniciar")
        os.system("cls")
        main()

def cadastrar_aluno():
    os.system("cls")
    print("Cadastrando Aluno")
    nome = input("Digite o nome do Aluno: ")
    idade = input("Digite a idade do Aluno: ")
    print("Escolha o Plano: ")
    print("1 - Básico")
    print("2 - Intermediário")
    print("3 - Pro")
    plano = input("Opção: ")
    planos = {"1": "Basico", "2": "Intermediario", "3": "Pro"}
    dados_aluno = {"nome": nome, "idade": idade, "Plano": planos.get(plano, "Basico"), "ativo": True}
    listadealunos.append(dados_aluno)
    print(f"\nAluno {nome} cadastrado com sucesso!")
    input("\nAperte enter para voltar ao menu")
    main()
    
def listar_aluno():
    os.system("cls")
    print("Listando Alunos\n")
    print(f"{'Nome'.ljust(15)} | {'Idade'.ljust(5)} | {'Plano'.ljust(15)} | Status")
    for aluno in listadealunos:
        ativo = "Ativo" if aluno["ativo"] else "Inativo"
        print(f"{aluno['nome'].ljust(15)} | {str(aluno['idade']).ljust(5)} | {aluno['Plano'].ljust(15)} | {ativo}")
    input("\nAperte enter para voltar ao menu")
    main()

def ativar_desativar_aluno():
    os.system("cls")
    print("Ativar/Desativar Aluno\n")
    nome = input("Digite o nome do aluno: ")
    encontrado = False
    for aluno in listadealunos:
        if aluno["nome"] == nome:
            encontrado = True
            aluno["ativo"] = not aluno["ativo"]
            status = "ativado" if aluno["ativo"] else "desativado"
            print(f"\nAluno {nome} {status} com sucesso!")
    if not encontrado:
        print("Aluno não encontrado!")
    input("\nAperte enter para voltar ao menu")
    main()

def main():
    exibir_nome_do_programa() 
    exibir_opcoes()


if __name__ == "__main__":
    main()
