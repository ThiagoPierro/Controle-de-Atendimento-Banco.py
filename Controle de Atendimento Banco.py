def cadastrar_atendimento(atendimentos):
    nome = input("Digite seu nome: ")


    def obter_cpf():
        while True:
            cpf = input("Digite seu CPF (11 dígitos): ")
            if len(cpf) == 11 and cpf.isdigit():
                return cpf
            else:
                print("Entrada inválida. Por favor, digite exatamente 11 dígitos.")

    cpf = obter_cpf()


    def escolher_atendimento():
        print("Escolha o tipo de atendimento: ")
        print("1- Abertura de Conta ")
        print("2- Caixa ")
        print("3- Gerente PF ")
        print("4- Gerente PJ ")

        while True:
            escolha = input("Digite o número correspondente ao tipo de atendimento: ")

            if escolha == "1":
                return "Abertura de Conta"
            elif escolha == "2":
                return "Caixa"
            elif escolha == "3":
                return "Gerente PF"
            elif escolha == "4":
                return "Gerente PJ"
            else:
                print("Opção inválida. Por favor, escolha um número de 1 a 4.")

    tipo_atendimento = escolher_atendimento()

    # Armazena os dados em um dicionário e adiciona à lista de atendimentos
    atendimento = {
        "nome": nome,
        "cpf": cpf,
        "tipo_atendimento": tipo_atendimento
    }

    atendimentos.append(atendimento)
    print(f"{nome}, seu atendimento de {tipo_atendimento} foi cadastrado com sucesso!")


def listar_todos_atendimentos(atendimentos):
    print("\nLista de Atendimentos Cadastrados:")
    for i, atendimento in enumerate(atendimentos, start=1):
        print(f"Atendimento {i}:")
        print(f"Nome: {atendimento['nome']}")
        print(f"CPF: {atendimento['cpf']}")
        print(f"Tipo de Atendimento: {atendimento['tipo_atendimento']}")
        print("===============================\n")



atendimentos = []
while True:
    cadastrar_atendimento(atendimentos)

    continuar = input("Deseja cadastrar outro atendimento? (s/n): ").lower()
    if continuar != 's':
        break

listar_todos_atendimentos(atendimentos)
