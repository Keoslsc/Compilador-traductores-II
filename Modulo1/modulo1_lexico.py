class Lex():
  def __init__(self, string):
    self.state = 0
    self.string = string
    self.pos = -1
    self.valid = True
    self.size = len(string)

  def assignState(self, symbol):
    #State 0
    if self.state == 0:
      if symbol.isdigit() and int(symbol) >= 0:
        self.state = 1
        self.nextPosition()
      elif symbol == '|':
        self.state = 4
        self.nextPosition()
      elif symbol == '&':
        self.state = 6
        self.nextPosition()
      elif symbol == '*':
        self.state = 8
        self.nextPosition()
      elif symbol == '/':
        self.state = 9
        self.nextPosition()
      elif symbol == '=':
        self.state = 10
        self.nextPosition()
      elif symbol == '<':
        self.state = 12
        self.nextPosition()
      elif symbol == '>':
        self.state = 14
        self.nextPosition()
      elif symbol == '!':
        self.state = 16
        self.nextPosition()
      elif symbol == '(':
        self.state = 18
        self.nextPosition()
      elif symbol == ')':
        self.state = 19
        self.nextPosition()
      elif symbol == '{':
        self.state = 20
        self.nextPosition()
      elif symbol == '}':
        self.state = 21
        self.nextPosition()
      elif symbol == ';':
        self.state = 22
        self.nextPosition()
      elif symbol == '+':
        self.state = 23
        self.nextPosition()
      elif symbol == '-':
        self.state = 24
        self.nextPosition()
      elif symbol == 'i':
        self.state = 25
        self.nextPosition()
      elif symbol == 'w':
        self.state = 28
        self.nextPosition()
      elif symbol == 'r':
        self.state = 33
        self.nextPosition()
      elif symbol == 'e':
        self.state = 39
        self.nextPosition()
      elif symbol == 'f':
        self.state = 45
        self.nextPosition()
      elif symbol == '"':
        self.state = 50
        self.nextPosition()
     
      elif symbol.isalpha():
        self.state = 27
        self.nextPosition()
      else: 
        self.dataType(-1)

    #State 1
    elif self.state == 1:
      if symbol == '.':
        self.state = 2
        self.nextPosition()
      else:
        self.nextPosition()

    #State 2
    elif self.state == 2:
      if symbol.isdigit() and int(symbol) >= 0:
        self.state = 3
        self.nextPosition()
      else: 
        self.dataType(-1)

    #State 4
    elif self.state == 4:
      if symbol == '|':
        self.state = 5
        self.nextPosition()
      else:
        self.dataType(-1)

    #State 6
    elif self.state == 6:
      if symbol == '&':
        self.state = 7
        self.nextPosition()
      else:
        self.dataType(-1)

    #State 10
    elif self.state == 10:
      if symbol == '=':
        self.state = 11
        self.nextPosition()
      else:
        self.dataType(-1)

    #State 12
    elif self.state == 12:
      if symbol == '=':
        self.state = 13
        self.nextPosition()
      else:
        self.dataType(-1)

    #State 14
    elif self.state == 14:
      if symbol == '=':
        self.state = 15
        self.nextPosition()
      else:
        self.dataType(-1)
        
    #State 16
    elif self.state == 16:
      if symbol == '=':
        self.state = 17
        self.nextPosition()
      else:
        self.dataType(-1)


    #State 25
    elif self.state == 25:
      if symbol == 'f':
        self.state = 26
        self.nextPosition()
      elif symbol == 'n':
        self.state = 43
        self.nextPosition()
      else:
        self.state = 27
        self.nextPosition()


    #State 26
    elif self.state == 26:
      if symbol.isdigit() or symbol.isalpha():
        self.state = 27
        self.nextPosition()
      else:
        self.dataType(-1)


    #State 27
    elif self.state == 27:
      if symbol.isdigit() or symbol.isalpha():
        self.state = 27
        self.nextPosition()
      else:
        self.dataType(-1)

    #State 28
    elif self.state == 28:
      if symbol == 'h':
        self.state = 29
        self.nextPosition()
      elif symbol.isdigit() or symbol.isalpha():
        self.state = 27
        self.nextPosition()
      else: 
        self.dataType(-1)

     #State 29
    elif self.state == 29:
      if symbol == 'i':
        self.state = 30
        self.nextPosition()
      elif symbol.isdigit() or symbol.isalpha():
        self.state = 27
        self.nextPosition()
      else: 
        self.dataType(-1)

     #State 30
    elif self.state == 30:
      if symbol == 'l':
        self.state = 31
        self.nextPosition()
      elif symbol.isdigit() or symbol.isalpha():
        self.state = 27
        self.nextPosition()
      else: 
        self.dataType(-1)

    #State 31
    elif self.state == 31:
      if symbol == 'e':
        self.state = 32
        self.nextPosition()
      elif symbol.isdigit() or symbol.isalpha():
        self.state = 27
        self.nextPosition()
      else: 
        self.dataType(-1)

    #State 32
    elif self.state == 32:
      if symbol.isdigit() or symbol.isalpha():
        self.state = 27
        self.nextPosition()
      else:
        self.dataType(-1)

    #State 33
    elif self.state == 33:
      if symbol == 'e':
        self.state = 34
        self.nextPosition()
      elif symbol.isdigit() or symbol.isalpha():
        self.state = 27
        self.nextPosition()
      else: 
        self.dataType(-1)

    #State 34
    elif self.state == 34:
      if symbol == 't':
        self.state = 35
        self.nextPosition()
      elif symbol.isdigit() or symbol.isalpha():
        self.state = 27
        self.nextPosition()
      else: 
        self.dataType(-1)


    #State 35
    elif self.state == 35:
      if (symbol == 'u'):
        self.state = 36
        self.nextPosition()
      elif symbol.isdigit() or symbol.isalpha():
        self.state = 27
        self.nextPosition()
      else: 
        self.dataType(-1)

    #State 36
    elif self.state == 36:
      if symbol == 'r':
        self.state = 37
        self.nextPosition()
      elif symbol.isdigit() or symbol.isalpha():
        self.state = 27
        self.nextPosition()
      else:
        self.dataType(-1)

    #State 37
    elif self.state == 37:
      if symbol == 'n':
        self.state = 38
        self.nextPosition()
      elif symbol.isdigit() or symbol.isalpha():
        self.state = 27
        self.nextPosition()
      else: 
        self.dataType(-1)

    #State 38
    elif self.state == 38:
      if symbol.isdigit() or symbol.isalpha():
        self.state = 27
        self.nextPosition()
      else:
        self.dataType(-1)

    #State 39
    elif self.state == 39:
      if symbol == 'l':
        self.state = 40
        self.nextPosition()
      elif symbol.isdigit() or symbol.isalpha():
        self.state = 27
        self.nextPosition()
      else: 
        self.dataType(-1)

    elif self.state == 40:
      if symbol == 's':
        self.state = 41
        self.nextPosition()
      elif symbol.isdigit() or symbol.isalpha():
        self.state = 27
        self.nextPosition()
      else: 
        self.dataType(-1)


    elif self.state == 41:
      if symbol == 'e':
        self.state = 42
        self.nextPosition()
      elif symbol.isdigit() or symbol.isalpha():
        self.state = 27
        self.nextPosition()
      else: 
        self.dataType(-1)

    
    elif self.state == 42:
      if symbol.isdigit() or symbol.isalpha():
        self.state = 27
        self.nextPosition()
      else:
        self.dataType(-1)

    elif self.state == 43:
      if symbol == 't':
        self.state = 44
        self.nextPosition()
      elif symbol.isdigit() or symbol.isalpha():
        self.state = 27
        self.nextPosition()
      else: 
        self.dataType(-1)

    elif self.state == 44:
      if symbol.isdigit() or symbol.isalpha():
        self.state = 27
        self.nextPosition()
      else:
        self.dataType(-1)

    elif self.state == 45:
      if symbol == 'l':
        self.state = 46
        self.nextPosition()
      elif symbol.isdigit() or symbol.isalpha():
        self.state = 27
        self.nextPosition()
      else: 
        self.dataType(-1)

    elif self.state == 46:
      if symbol == 'o':
        self.state = 47
        self.nextPosition()
      elif symbol.isdigit() or symbol.isalpha():
        self.state = 27
        self.nextPosition()
      else: 
        self.dataType(-1)

    elif self.state == 47:
      if symbol == 'a':
        self.state = 48
        self.nextPosition()
      elif symbol.isdigit() or symbol.isalpha():
        self.state = 27
        self.nextPosition()
      else: 
        self.dataType(-1)

    elif self.state == 48:
      if symbol == 't':
        self.state = 49
        self.nextPosition()
      elif symbol.isdigit() or symbol.isalpha():
        self.state = 27
        self.nextPosition()
      else: 
        self.dataType(-1)

    elif self.state == 49:
      if symbol.isdigit() or symbol.isalpha():
        self.state = 27
        self.nextPosition()
      else:
        self.dataType(-1)

    elif self.state == 50:
      if symbol == '"':
        self.state = 51
        self.nextPosition()
      else:
        self.state = 50
        self.nextPosition()
    else:
      self.nextPosition()




  def nextPosition(self):
    self.pos += 1
    if self.term():
      self.dataType(self.state)
    else:
      if self.newString():
        self.dataType(self.state)
        self.init()
      else:
        self.assignState(self.string[self.pos])
      


  def dataType(self, estado):
    if estado == 1:
        print ('INTNUMB')
    elif estado == 3:
        print ('FLOATNUMB')
    elif estado == 5:
        print('OR')
    elif estado == 7:
        print('AND')
    elif estado == 8:
        print('MULTIPL')
    elif estado == 9:
        print('DIVI')
    elif estado == 10:
        print('ASIGNACION')
    elif estado == 11:
        print('COMPARACION')
    elif estado == 12:
        print('MENOR QUE')
    elif estado == 13:
        print('MENOR O IGUAL QUE')
    elif estado == 14:
        print('MAYOR QUE')
    elif estado == 15:
        print('MAYOR O IGUAL QUE')
    elif estado == 17:
        print('DIFERENTE')
    elif estado == 18:
        print('PAREN DER')
    elif estado == 19:
        print('PAREN IZQ')
    elif estado == 20:
        print('LLAVE IZQ')
    elif estado == 21:
        print('LLAVE DER')
    elif estado == 22:
        print('PUNTO Y COMA')
    elif estado == 23:
        print('PLUS')
    elif estado == 24:
        print('MINUS')
    elif estado == 26:
        print('IF')
    elif estado == 25 or estado == 27 or estado == 28 or estado == 29 or estado == 30 or estado == 31 or estado == 33 or estado == 34 or estado == 35 or estado == 36 or estado == 37 or estado == 39 or estado == 40 or estado == 41 or estado == 43 or estado == 45 or estado == 46 or estado == 47 or estado == 48:
        print('IDENTIFICADOR')
    elif estado == 32:
        print('WHILE')
    elif estado == 38:
        print('RETURN')
    elif estado == 42:
        print('ELSE')
    elif estado == 44:
        print('INT')
    elif estado == 49:
        print('FLOAT')
    elif estado == 51:
        print('CADENA')
    else:
        print ('Invalid')

  def term(self):
    return self.pos >= self.size

  def newString(self):
    if self.string[self.pos] == ' ' and self.pos < self.size:
      return True
    else: 
      return False

  def init(self):
    self.state = 0
    self.valid = True
    self.nextPosition()

