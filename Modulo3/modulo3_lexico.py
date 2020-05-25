class Lex():
  def __init__(self, string):
    self.state = 0
    self.string = string
    self.pos = -1
    self.valid = True
    self.size = len(string)
    self.boolToken = False
    self.token = 0

  def assignState(self, symbol):
    #State 0
    if self.state == 0:
      if symbol.isdigit() and int(symbol) >= 0:
        self.state = 1
      elif symbol == '|':
        self.state = 4
      elif symbol == '&':
        self.state = 6
      elif symbol == '*':
        self.state = 8
      elif symbol == '/':
        self.state = 9
      elif symbol == '=':
        self.state = 10
      elif symbol == '<':
        self.state = 12
      elif symbol == '>':
        self.state = 14
      elif symbol == '!':
        self.state = 16
      elif symbol == '(':
        self.state = 18
      elif symbol == ')':
        self.state = 19
      elif symbol == '{':
        self.state = 20
      elif symbol == '}':
        self.state = 21
      elif symbol == ';':
        self.state = 22
      elif symbol == '+':
        self.state = 23
      elif symbol == '-':
        self.state = 24
      elif symbol == 'i':
        self.state = 25
      elif symbol == 'w':
        self.state = 28
      elif symbol == 'r':
        self.state = 33
      elif symbol == 'e':
        self.state = 39
      elif symbol == 'f':
        self.state = 45
      elif symbol == '"':
        self.state = 50
     
      elif symbol.isalpha():
        self.state = 27
      else: 
        self.dataType(-1)

    #State 1
    elif self.state == 1:
      if symbol == '.':
        self.state = 2

    #State 2
    elif self.state == 2:
      if symbol.isdigit() and int(symbol) >= 0:
        self.state = 3
      else: 
        self.dataType(-1)

    #State 4
    elif self.state == 4:
      if symbol == '|':
        self.state = 5
      else:
        self.dataType(-1)

    #State 6
    elif self.state == 6:
      if symbol == '&':
        self.state = 7
      else:
        self.dataType(-1)

    #State 10
    elif self.state == 10:
      if symbol == '=':
        self.state = 11
      else:
        self.dataType(-1)

    #State 12
    elif self.state == 12:
      if symbol == '=':
        self.state = 13
      else:
        self.dataType(-1)

    #State 14
    elif self.state == 14:
      if symbol == '=':
        self.state = 15
      else:
        self.dataType(-1)
        
    #State 16
    elif self.state == 16:
      if symbol == '=':
        self.state = 17
      else:
        self.dataType(-1)


    #State 25
    elif self.state == 25:
      if symbol == 'f':
        self.state = 26
      elif symbol == 'n':
        self.state = 43
      else:
        self.state = 27


    #State 26
    elif self.state == 26:
      if symbol.isdigit() or symbol.isalpha():
        self.state = 27
      else:
        self.dataType(-1)


    #State 27
    elif self.state == 27:
      if symbol.isdigit() or symbol.isalpha():
        self.state = 27
      else:
        self.dataType(-1)

    #State 28
    elif self.state == 28:
      if symbol == 'h':
        self.state = 29
      elif symbol.isdigit() or symbol.isalpha():
        self.state = 27
      else: 
        self.dataType(-1)

     #State 29
    elif self.state == 29:
      if symbol == 'i':
        self.state = 30
      elif symbol.isdigit() or symbol.isalpha():
        self.state = 27
      else: 
        self.dataType(-1)

     #State 30
    elif self.state == 30:
      if symbol == 'l':
        self.state = 31
      elif symbol.isdigit() or symbol.isalpha():
        self.state = 27
      else: 
        self.dataType(-1)

    #State 31
    elif self.state == 31:
      if symbol == 'e':
        self.state = 32
      elif symbol.isdigit() or symbol.isalpha():
        self.state = 27
      else: 
        self.dataType(-1)

    #State 32
    elif self.state == 32:
      if symbol.isdigit() or symbol.isalpha():
        self.state = 27
      else:
        self.dataType(-1)

    #State 33
    elif self.state == 33:
      if symbol == 'e':
        self.state = 34
      elif symbol.isdigit() or symbol.isalpha():
        self.state = 27
      else: 
        self.dataType(-1)

    #State 34
    elif self.state == 34:
      if symbol == 't':
        self.state = 35
      elif symbol.isdigit() or symbol.isalpha():
        self.state = 27
      else: 
        self.dataType(-1)


    #State 35
    elif self.state == 35:
      if (symbol == 'u'):
        self.state = 36
      elif symbol.isdigit() or symbol.isalpha():
        self.state = 27
      else: 
        self.dataType(-1)

    #State 36
    elif self.state == 36:
      if symbol == 'r':
        self.state = 37
      elif symbol.isdigit() or symbol.isalpha():
        self.state = 27
      else:
        self.dataType(-1)

    #State 37
    elif self.state == 37:
      if symbol == 'n':
        self.state = 38
      elif symbol.isdigit() or symbol.isalpha():
        self.state = 27
      else: 
        self.dataType(-1)

    #State 38
    elif self.state == 38:
      if symbol.isdigit() or symbol.isalpha():
        self.state = 27
      else:
        self.dataType(-1)

    #State 39
    elif self.state == 39:
      if symbol == 'l':
        self.state = 40
      elif symbol.isdigit() or symbol.isalpha():
        self.state = 27
      else: 
        self.dataType(-1)

    elif self.state == 40:
      if symbol == 's':
        self.state = 41
      elif symbol.isdigit() or symbol.isalpha():
        self.state = 27
      else: 
        self.dataType(-1)


    elif self.state == 41:
      if symbol == 'e':
        self.state = 42
      elif symbol.isdigit() or symbol.isalpha():
        self.state = 27
      else: 
        self.dataType(-1)

    
    elif self.state == 42:
      if symbol.isdigit() or symbol.isalpha():
        self.state = 27
      else:
        self.dataType(-1)

    elif self.state == 43:
      if symbol == 't':
        self.state = 44
      elif symbol.isdigit() or symbol.isalpha():
        self.state = 27
      else: 
        self.dataType(-1)

    elif self.state == 44:
      if symbol.isdigit() or symbol.isalpha():
        self.state = 27
      else:
        self.dataType(-1)

    elif self.state == 45:
      if symbol == 'l':
        self.state = 46
      elif symbol.isdigit() or symbol.isalpha():
        self.state = 27
      else: 
        self.dataType(-1)

    elif self.state == 46:
      if symbol == 'o':
        self.state = 47
      elif symbol.isdigit() or symbol.isalpha():
        self.state = 27
      else: 
        self.dataType(-1)

    elif self.state == 47:
      if symbol == 'a':
        self.state = 48
      elif symbol.isdigit() or symbol.isalpha():
        self.state = 27
      else: 
        self.dataType(-1)

    elif self.state == 48:
      if symbol == 't':
        self.state = 49
      elif symbol.isdigit() or symbol.isalpha():
        self.state = 27
      else: 
        self.dataType(-1)

    elif self.state == 49:
      if symbol.isdigit() or symbol.isalpha():
        self.state = 27
      else:
        self.dataType(-1)

    elif self.state == 50:
      if symbol == '"':
        self.state = 51
      else:
        self.state = 50




  def nextPosition(self):
    self.pos += 1
    if self.newString():
      self.dataType(self.state)
      self.init()
    else:
      self.assignState(self.string[self.pos])
      


  def dataType(self, state):
    self.boolToken = True
    if state == 1:
        self.token = 'INT'
    elif state == 3:
        self.token = 'FLOAT'
    elif state == 5:
        self.token = 'OR'
    elif state == 7:
        self.token = 'AND'
    elif state == 8:
        self.token = 'MULTIPL'
    elif state == 9:
        self.token = 'DIVI'
    elif state == 10:
        self.token = 'ASIGNACION'
    elif state == 11:
        self.token = 'COMPARACION'
    elif state == 12:
        self.token = 'MENOR QUE'
    elif state == 13:
        self.token = 'MENOR O IGUAL QUE'
    elif state == 14:
        self.token = 'MAYOR QUE'
    elif state == 15:
        self.token = 'MAYOR O IGUAL QUE'
    elif state == 17:
        self.token = 'DIFERENTE'
    elif state == 18:
        self.token = 'PAREN DER'
    elif state == 19:
        self.token = 'PAREN IZQ'
    elif state == 20:
        self.token = 'LLAVE IZQ'
    elif state == 21:
        self.token = 'LLAVE DER'
    elif state == 22:
        self.token = 'PUNTO Y COMA'
    elif state == 23:
        self.token = 'PLUS'
    elif state == 24:
        self.token = 'MINUS'
    elif state == 26:
        self.token = 'IF'
    elif state == 25 or state == 27 or state == 28 or state == 29 or state == 30 or state == 31 or state == 33 or state == 34 or state == 35 or state == 36 or state == 37 or state == 39 or state == 40 or state == 41 or state == 43 or state == 45 or state == 46 or state == 47 or state == 48:
        self.token = 'IDENTIFICADOR'
    elif state == 32:
        self.token = 'WHILE'
    elif state == 38:
        self.token = 'RETURN'
    elif state == 42:
        self.token = 'ELSE'
    elif state == 44:
        self.token = 'INT'
    elif state == 49:
        self.token = 'FLOAT'
    elif state == 51:
        self.token = 'CADENA'
    else:
        self.token = 'Invalid'

  def term(self):
    return self.pos >= self.size-1

  def newString(self):
    if self.string[self.pos] == ' ' and self.pos < self.size:
      return True
    else: 
      return False

  def init(self):
    self.state = 0
    self.valid = True
    self.nextPosition()

