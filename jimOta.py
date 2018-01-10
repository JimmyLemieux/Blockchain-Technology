#!/usr/bin/python
import hashlib
import json
from time import time
class BlockChain:
	def __init__(self):
		self.chain = []

		#Create the genesis block of the chain
		self.new_block(1,100)



	def new_block(self,previousHash,hashSet):


		block = {
			'index':len(self.chain) + 1,
			'time':time(),
			'merkleRoot':hashSet,
			'previousHash':previousHash or self.hash(self.chain[-1]),
		}


		block['blockHash'] = self.hash(block)
		#Add the block to the block chain
		self.chain.append(block)
		return block


	@property
	def last_block(self):
		return self.chain[-1]


	@staticmethod
	def hash(block):
		block_string = json.dumps(block,sort_keys=True).encode()
		return hashlib.sha256(block_string).hexdigest()

	def proof_of_work(self,pastProof):
		currentProof = 0
		while validate_proof(pastProof,currentProof) is False:
			currentProof += 1
		return currentProof

	
	@staticmethod
	def validate_proof(pastProof,currentProof):
		#To validate a block on the block chain
		#The block chain is validated in this way
		#This is so users can't go through the whole block chain and revalidate it
		mine = f'{pastProof}{currentProof}'.encode()
		mine_hash = hashlib.sha256(mine).hexdigest()
		return mine_hash[:4] == '0000' 



blockchain = BlockChain()

for i in range(20):	
	last_block = blockchain.last_block['blockHash']
	#Run through the proof
	proof = blockchain.proof_of_work
	blockchain.new_block(last_block,proof)

for i in blockchain.chain:
	print i