def main():
    while(True):
            opt = 0
            num = 0
            while opt not in range(1, 4):
                try:
                    opt = int(input('\nCifra de César:\n\n\t1 - Criptografar\n\t2 - Descriptografar\n\t3 - Sair\n\n\t>'))
                    exit(0) if opt == 3 else None
                    if opt not in range(1, 4):
                        raise ValueError 
                    else:
                        break
                except ValueError:
                    print('\n\nValor inválido, tente novamente.\n\n')

            
            phrase = input('\n\nDigite a frase a ser cifrada: \n\n\t')
            
            while num < 1:
                try:
                    num = int(input('\n\nNúmero de caracteres a serem pulados (zero não é permitido): \n\n\t'))
                    if num < 1:
                        raise ValueError 
                    else:
                        break
                except ValueError:
                    print('\n\nValor inválido, tente novamente.\n\n')

            if opt == 1:
                criptCesar(phrase, num, True)
            elif opt == 2:
                criptCesar(phrase, num, False)


def criptCesar(phrase: str, num: int, order: bool):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    new_phrase = ''
    for i in range(len(phrase)):
        if phrase[i].lower() in alphabet:
            index_of = alphabet.find(phrase[i])
            new_index =  index_of + num if order else index_of - num  # Caso ordem seja para encriptar soma, senão diminui
            if new_index >= len(alphabet):
                new_index = (new_index % len(alphabet))  # Caso a nova posição seja maior que o número de letras no alfabeto, recebe o resto da divisão
            new_phrase += alphabet[new_index]
        else:
            new_phrase += phrase[i]

    print(new_phrase)
    


main()