import os
from Modulo5.modulo5_stack import Stack
import Modulo5.modulo5_matriz as m
os.system('clear')

matriz = m.matriz 
values = m.values
rules = m.rules

class nodo():
	def __init__(self, name, rule, list_p):
		self.name = name
		self.rule = rule
		self.list = list_p

class Syntactic():
	def __init__(self,size):
		self.stack = Stack()
		self.stack.push('$')
		self.stack.push('0')
		self.column = 0
		self.quantity = size
		self.action = ""
		self.list_tmp = list()
		self.tree = []
		
	def compare(self,token,valor):
		if(values[token]):
			self.action = matriz[int(self.stack.top())][int(values[token])]
			print('Pila: ', self.stack.get())
			print('Token: ', token)
			if(self.action == -1):
				print('Cadena valida\n')
				print('==== Arbol ====')
				self.tree = self.tree[::-1]
				for item in self.tree:
					item.list = item.list[::-1]
					print(item.rule,'==> ',item.list)


			elif(self.action > 0):
				self.stack.push(self.action)
				self.list_tmp.append(valor)
				print('Accion: PUSH')
				print('\n')

			elif(self.action < 0):
				self.stack.pop(rules[self.action]['quantity'])
				self.stack.push(matriz[int(self.stack.top())][rules[self.action]['column']])
				print('-----GENERA REGLA-----')
				print('Accion: POP %d elementos'%rules[self.action]['quantity'])
				print('Accion: PUSH de la rule')
				print('Nombre: ', rules[self.action]['name'])
				print('\n')
				list_aux = []
				if(rules[self.action]['quantity'] > 0):
					print('Lista:' ,self.list_tmp)
					aux = rules[self.action]['quantity']
					for i in range(aux):
						aux = self.list_tmp.pop(-1)
						list_aux.append(aux)

				self.tree.append(nodo(rules[self.action]['name'], rules[self.action]['rule'], list_aux))
				self.list_tmp.append(rules[self.action]['rule'])
				self.compare(token,valor)

			else: 
				print('Invalid')
				exit()
			
