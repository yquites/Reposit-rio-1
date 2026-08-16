#Login de site simples:

usuario_salvo = "funcionario1"
senha_salva = 123456

def logindosite():

    usuario = input("Digite seu nome de usúario: ")

    while usuario != usuario_salvo:
        print("Usuário inexistente! Tente Novamente.\n")
        usuario = input("Digite seu nome de usúario: ")

    tentativas = 3

    while tentativas > 0:

        try:
            senha = int(input("Digite sua senha (apenas números): "))

            if senha == senha_salva:
                print("Login realizado com sucesso!")
                return
                
            else:
                tentativas -= 1

                if tentativas > 0:
                    print(f"Senha icorreta! Você tem mais {tentativas} chance(s): ")
                else:
                    print("Chances zeradas! Tente novamente mais tarde.")

        except ValueError:
            tentativas -= 1

            if tentativas > 0:
                print(f"Entrada inválida! Você tem mais {tentativas} chance(s): ")
            else:
                print("Chances zeradas! Tente novamente mais tarde.")

logindosite()