class ci():
	def __init__(self,estadoAtual,fita,posCabecote):

		self.estadoAtual = estadoAtual
		self.fita = fita
		self.posCabecote = posCabecote


	def get_estadoAtual(self):
		return self.estadoAtual	

	def get_posCabecote(self):
		return self.posCabecote

	def get_fita(self):
		return self.fita
	

	def __str__(self):

		return f'estado: {self.estadoAtual} fita: {self.fita} posCabecote: {self.posCabecote}'

			
		