import time
# MENU INICIAL
saldo_atual = 0
numero_saques = 0
extrato = []
def inicio():
    global saldo_atual
    global extrato
    global numero_saques

    menu = int(input(
    """
    ----- ED BANK - IP -----------

    Selecione a opção desejada:

        1. Depositar
        2. Sacar
        3. Ver Extrato
        4. Sair

    ------------------------------
    """
    ))

    # OPERAÇÃO DE DEPOSITO
    if menu == 1:
        while True:
            valor_deposito = input("Quanto você deseja depositar? ")
            if valor_deposito.isnumeric():
                conferir_deposito = int(valor_deposito)
                if conferir_deposito > 0:
                    break
                else:
                    print("     Insira um valor válido.")
            else:
                print("     Insira um valor válido.")
        saldo_atual += int(valor_deposito)
        extrato.append(f"Depósito de R$ {valor_deposito}")
        print(
            f"""
    Deposito realizado com sucesso!
    Seu saldo atual é: R$ {saldo_atual}

    Retornando para o menu inicial...
            """
            )
        time.sleep(5)
        inicio()
    
    elif menu == 2:
        while True:
            valor_saque = input(
                f'''
                ----- ED BANK - IP -----------

                Quanto você deseja sacar?
                Saldo atual: R$ {saldo_atual}



                press "e" to exit
                ------------------------------
                ''')
            if valor_saque == "e":
                inicio()
            else:
                if valor_saque.isnumeric():
                    conferir_saque = int(valor_saque)
                    if conferir_saque > 0:
                        if conferir_saque <= 500:
                            if numero_saques < 3:
                                if conferir_saque <= saldo_atual:
                                    break
                                else:
                                    print("     Você não tem saldo suficiente.")
                            else:
                                print("     Você já realizou o numero máximo de saques diários permitidos.")
                        else:
                            print("     Só é possível realizar saques de até R$ 500 por vez.")
                    else:
                        print("     Insira um valor válido")
                else:
                    print("     Insira um valor válido")
        saldo_atual -= int(valor_saque)
        extrato.append(f"Saque de R$ {valor_saque}")
        numero_saques += 1
        print(
        f"""
    Saque realizado com sucesso!
    Seu saldo atual é: R$ {saldo_atual}

    Retornando para o menu inicial...
        """
        )
        time.sleep(5)
        inicio()
    elif menu == 3:
        if len(extrato) > 0:
            for item in extrato:
                print(item)
            print(f"\nSaldo atual: R$ {saldo_atual}")
            retorno = int(input("Pressione 5 para retornar ao menu inicial. "))
            if retorno == 5:
                inicio()
        else:
            print(
            """
            Não há movimentações recentes.
            
            Retornando para o menu inicial...
            """)
            time.sleep(4)
            inicio()
    elif menu == 4:
        exit
    else:
        print("Insira uma opção válida")
        inicio()

inicio()