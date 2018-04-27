from Pessoa import Pessoa
from Carro import Carro
from datetime import datetime

class Venda:

    def __init__(self, pessoa, carro):
        self.pessoa = pessoa
        self.carro = carro
        self.data = datetime.now().strftime("%Y-%m-%d %H:%M")