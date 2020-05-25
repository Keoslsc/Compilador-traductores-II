import os
from Modulo3.modulo3_stack import Stack
os.system('clear')


m = ([2, 0, 0, 1],
		  [0, 0,-1, 0],
		  [0, 3, -3, 0],
		  [2, 0, 0, 4],
		  [0, 0, -2, 0])


values = {'IDENTIFICADOR':'0', 'PLUS': 1, '$': 2}
rules = {
		   -2: {'nombre': 'E','column':3,'quantity':3},
		   -3: {'nombre': 'E','column':3,'quantity':1}
}

class Syntactic():
	def __init__(self,size):
		self.stack = Stack()
		self.stack.push('$')
		self.stack.push('0')
		self.column = 0
		self.quantity = size
		self.action = ""
		
	def compare(self,token):
		if token in values:
			if(values[token]):
				print('Pila: ', self.stack.get())
				print('Token: ', token)
				self.action = m[int(self.stack.top())][int(values[token])]
				if(self.action == -1):
					print('Cadena valida')
				elif(self.action > 0):
					self.stack.push(self.action)
					print('PUSH \n")
				elif(self.action < 0):
					self.stack.pop(rules[self.action]['quantity'])
					self.stack.push(m[int(self.stack.top())][rules[self.action]['column']])
					print('POP %d elementos'%rules[self.action]['quantity'])
					print('PUSH (regla)\n')
					self.compare('$')
				else: 
					print('Cadena no valida')
					exit()
		else:
			print('Cadena no valida')
			exit()













