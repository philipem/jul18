import random
import sys

lista = []

def main():
    print('Välkommen! Detta program kräver att du matar in ett totalantal som är jämt för att kunna ge en jämn presentfördelning')
    print('Skriv ett namn: ')
    x = input()
    x.lower()
    lista.append(x)
    while x != 'klar':
            print('Skriv ett till namn eller klar: ')
            x = input()
            if x != 'klar':
                x.lower()
                lista.append(x)

    if len(lista) % 2 != 0:
        print('Det antal du matade in var inte jämt, alternativt 0! Var god försök igen.')
        sys.exit(0)

    print(lista)
    print(rand(lista))

    return lista

def rand(receiver):
    giver = receiver[:]
    lista_med_par = []

    for i in range(len(receiver)):
        lista_med_par.append([])
    print(lista_med_par)

    for index, value in enumerate(giver):
        lista_med_par[index].append(value)
        print('Givare ', giver, 'och mottagare ', receiver)

        for tuples in lista_med_par:
            if len(tuples) == 2:
                if tuples[1] in receiver:
                    receiver.remove(tuples[1])

        if value in receiver:
            receiver.remove(value)
            put_in = random.choice(receiver)
            lista_med_par[index].append(put_in)
            receiver.append(value)
        else:
            lista_med_par[index].append(random.choice(receiver))

    return lista_med_par




main()