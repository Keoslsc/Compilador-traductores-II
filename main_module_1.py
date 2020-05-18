import Modulo1.modulo1_lexico as module1
import os

def main():
    os.system('clear')
    code = input('Ingresar un texto: ')
    lex = module1.Lex(code)
    lex.nextPosition()

if __name__ == '__main__':
    main()