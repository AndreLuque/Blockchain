import time 
from typing import TypeVar, List, Optional
from hashlib import sha256
import json


class Block():
	def __init__(self, previous_block_hash, timestamp: float, index: int, transactions):
		#contruimos los parametros asociados a todos los bloques
		self.previous_block_hash: str = previous_block_hash #el hash del bloque al que se conecta, el anterior
		self.nonce: int = 0 #numero al que se debe añadir al block para que el hash empiece por 0000
		self.timestamp: float = timestamp #la fecha y hora en la que el bloque es INTEGRADO AL CHAIN
		self.index: int = index #numero de bloque que es
		self.transactions = transactions

	def get_hash(self) -> str:
		#creamos un hash para este block
		hash_string = json.dumps(self.__dict__, sort_keys = True) #self.__dict__ convierte los parametros que tenemos en el constructor con sus valores en un dict. Json.dumps convierte un dict a un json string
		return sha256(hash_string.encode()).hexdigest() #computamos el hash


def test():
	#funcion para testear el codigo
	block1 = Block('0', time.time(), 0, [])
	print(block1.get_hash())

#omitir abajo cnd no quieres testear el codigo
#test()	