import random

def gerar_numeros_loteria():
    numeros = []
    while len(numeros) < 6:
        num = random.randint(1, 60)
        if num not in numeros:
            numeros.append(num)
    return numeros

def obter_numeros_usuario():
    numeros_inteiros = []
    while len(numeros_inteiros) < 6:
        num = input("Escolha um número de 1 a 60: ")
        try:
            numero = int(num)
            if 1 <= numero <= 60 and numero not in numeros_inteiros:
                numeros_inteiros.append(numero)
            else:
                print("Esse número é inválido ou já foi escolhido. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")
    return numeros_inteiros

def verificar_ganhador(numeros_usuario, numeros_loteria):
    acertos = []
    for num in numeros_usuario:
        if num in numeros_loteria:
            acertos.append(num)
    return acertos

def main():
    print("Seja bem-vindo ao Jogo da Loteria!")
    
    numeros_usuario = obter_numeros_usuario()
    numeros_loteria = gerar_numeros_loteria()
    
    print(f"Números da Loteria: {sorted(numeros_loteria)}")
    
    acertos = verificar_ganhador(numeros_usuario, numeros_loteria)

    if acertos:
        print(f"Você acertou os números: {sorted(acertos)}")
        print(f"Total de acertos: {len(acertos)}")
    else:
        print("Infelizmente você não acertou nenhum número. Tente novamente!")

if __name__ == "__main__":
    main()