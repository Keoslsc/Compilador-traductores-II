from Modulo2.modulo2_lexico import Lex
from Modulo2.modulo2_syntactic import Syntactic
import os

def main():
    os.system('clear')
    code = input('Ingresar un texto: ')
    lex = Lex(code)
    tokens = list()
    while(lex.term() == False):
        lex.nextPosition()
        if(lex.boolToken):
            tokens.append(lex.token)
            lex.boolToken = False

    lex.dataType(lex.state)
    tokens.append(lex.token)
    tokens.append('$')

    syntactic = Syntactic(len(tokens)-1)
    for token in tokens:
        syntactic.compare(token)

if __name__ == '__main__':
    main()