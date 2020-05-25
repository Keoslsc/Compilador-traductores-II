class Semantic():
	def __init__(self,tree):
		self._tree = tree
		self.funcTable = []
		self.varTable = []
		self.errors = []
		self.ambit = "global"
		self.current = ""
		self.opActual = ""
		self.quantity = 0
		self.code = ""


	def createTables(self):
		for item in self._tree:
			if(item.name=='DefFunc'):
				self.funcTable.append([item.list[0],item.list[1]])
				self.ambit = item.list[1]
			if(item.name=='definicion'):
				self.ambit = "global"
			if(item.name=='DefVar'):
				self.varTable.append([item.list[0],item.list[1],self.ambit, ''])
			if(item.name=='Parametros' and len(item.list)>0):
				self.varTable.append([item.list[0],item.list[1],self.ambit, ''])
			if(item.name=='ListaParam' and len(item.list)>0):
				self.varTable.append([item.list[1],item.list[2],self.ambit, ''])
			




		

	def checkErrors(self):
		values = []
		self.ambit = "global"
		for item in self.funcTable:
			if item[1] in values:
				self.errors.append('La funcion <'+item[1]+'> ha sido duplicada')
			else:
				values.append(item[1])

		values = []
		for item in self.varTable:
			if item in values:
				self.errors.append('La variable <'+item[1]+'> ya existe en el ambito <'+item[2]+'>')
			else:
				values.append(item)

		for item in self._tree:
			if(item.name=='DefFunc'):
				self.ambit = item.list[1]
			if(item.name=='definicion'):
				self.ambit = "global"


			if item.name == 'Sentencia' or item.name == 'Termino':
				exist = False
				var = item.list[0]
				for lista in self.varTable:
					if (var in lista and (lista[2]==self.ambit or lista[2]=='global')) or var.isdigit():

						exist = True
				if not exist:
					self.errors.append('No existe la variable <'+var+'>')


			if(item.name=='Sentencia' and len(item.list)>1):
				self.current = item.list[0]

			if(item.name=='Expresion' and len(item.list)>1):
				self.opActual = item.list[1]


			if(item.name=='Termino'):
				var = item.list[0]
				for lista in self.varTable:
					if self.current == lista[1]:
						lista[3] += var
						if(self.opActual):
							lista[3] += self.opActual
				self.opActual = ""

				

			
		print('\n\n')
		print('============= Tablas ===============')
		print('Tabla de Funciones')
		for item in self.funcTable:
			print(item)
		print('\n')
		print('Tabla de Variables')
		for item in self.varTable:
			print(item)
				
		print('\n\n')
		print('============= Errores ===============')
		print(self.errors)

		self.code = "section .data\n"
		for item in self.varTable:
			aux = item[3].find('+')
			if aux==-1:
				self.code += item[1]+" dq '"+item[3]+"'\n"
			else:
				self.code += item[1]+" dq '0'\n"

		self.code += "section .text\nglobal _start\n_start:\n"
		for item in self.varTable:
			aux = item[3].find('+')
			if aux>-1:
				aux = item[3].split('+')
				self.code += "mov eax,["+item[1]+"]\n"
				self.code += "sub eax,'0'\n"
				self.code += "mov ebx,["+aux[0]+"]\n"
				self.code += "sub ebx,'0'\n"
				self.code += "add eax,ebx\n"
				self.code += "add eax,'0'\n"
				self.code += "mov ["+item[1]+"],eax\n"
				self.code += "mov eax,["+item[1]+"]\n"
				self.code += "sub eax,'0'\n"
				self.code += "mov ebx,["+aux[1]+"]\n"
				self.code += "sub ebx,'0'\n"
				self.code += "add eax,ebx\n"
				self.code += "add eax, '0'\n"
				self.code += "mov ["+item[1]+"], eax\n"
				self.code += "mov ecx, "+item[1]+"\n"
				self.code += "mov edx, 1\n"
				self.code += "mov ebx, 1\n"
				self.code += "mov eax, 4\n"

		self.code += "int 0x80\nmov eax,1\nint 0x80"

		print('\n\n')
		print('============= Ensamblador ===============')
		print(self.code)






		











