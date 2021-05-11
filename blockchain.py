import time
from typing import TypeVar, List, Optional, NoReturn
from block import Block

T = TypeVar('T')

class Blockchain():
	def __init__(self):
		self.chain: List[Block] = [] #la cadena de blocks
		self.pending_transactions: List[T] = ['hola', 'adios'] #las transacciones que no estan validadas que añadiremos al proximo bloque
		self.difficulty: int = 2
		self.__create_genesis_block() #debemos crear el bloque inicial, llamado el genesis blocks

	def __create_genesis_block(self):
		genesis_block = Block('0', time.time(), 0, [])
		genesis_block.hash = genesis_block.get_hash()
		self.chain.append(genesis_block)

	def last_block(self) -> Block:
		#funcion que retorno el ultimo block del chain
		return self.chain[-1]

	def increase_difficulty(self) -> NoReturn:
		#aumentamos la dificultad
		self.difficulty += 1		

	def proof_of_work(self, block: Block) -> str:
		#debemos conseguir un nonce que haga que el hash empiece por un cierto numero de ceros, el numero que indica la dificuktad de ese bloque. Con mas y mas bloques, la dificultad aumenta
		block_hash: str = block.get_hash() #conseguimos el hash del bloque
		while block_hash[:self.difficulty] != ('0' * self.difficulty):
			#si el principio no tiene los ceros consecutivos que buscamos cambiamos el nonce hasta que lo obtenemos
			block.nonce += 1
			block_hash = block.get_hash()
		return block_hash	

	def proof_is_valid(self, block: Block, proof: str) -> bool:
		#comprobamos que el numero de ceros al principio coincide con la dificultad y que el proof coincide con el hash del bloque, no es una caddena inventada
		return proof[:self.difficulty] == ('0' * self.difficulty) and proof == block.get_hash() 	

	def add_block(self, block: Block, proof: str) -> NoReturn:
		#antes de añadir el block al chain debemos comprobar que su parametro previous hash coincide con el hash del ultimo bloque del chain
		if block.previous_block_hash == self.last_block().hash:
			#despues debemos comprobar que el proof esta bien hecho, ha encontrado el valor nonce para que empiece el hash por 0 * dificultad y ademas que sea el hash del bloque, no una cadena inventada
			if self.proof_is_valid(block, proof):
				#ya que esta validado, establecemos el hash del bloque como el proof, y añadimos el block a la cadena
				block.hash = proof
				self.chain.append(block)
				#reiniciamos las transacciones que se añadiran al siguente bloque
				self.pending_transactions = []

				#si hemos llegado al bloque ... aumentamos la dificultad
				if len(self.chain) == 2016:
					self.increase_difficulty()	

	def add_transaction(self, transaction: T) -> NoReturn:			
		#añadimos la nueva transaccion a nuestra lisra de transacciones pendientes
		self.pending_transactions.append(transaction)

	def mine(self):
		#solo se minara un bloque si hay transacciones que guardar
		#asi estas transacciones seran confirmadas/validadas, formaran parte del blockchain
		if len(self.pending_transactions) == 0:
			print('Block cannot be mined if no transactions to be added')
		else:
			#creamos un nuevo bloque
			new_block: Block = Block(self.last_block().hash, time.time(), self.last_block().index + 1, self.pending_transactions)

			#ahora se debe conseguir el proof of work para demostrar que se ha conseguido minar un bloque nuevo 
			proof: str = self.proof_of_work(new_block)
			#intentamos añadir el bloque pasando nuestro proof
			self.add_block(new_block, proof)

					


def test():
	#funcion para testear el codigo
	blockchain1 = Blockchain()
	blockchain1.mine()
	print(blockchain1.chain[1].previous_block_hash)	

#omite abajo para no ejecutar la funcion dde test
test()