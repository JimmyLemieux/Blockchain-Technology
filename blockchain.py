#!/usr/bin/python
import hashlib
import json
from time import time
from random import random
class blockChain:
	def __init__(self):

		#This is to be considered the block header
		#All this will be hashed to make the block hash


		self.chain = []
		self.block_transactions = []
		self.proof_hash = '0'

		#make the genesis block
		#self.create_block(0,time(),'root',0)
		self.genesis_block()

		
	#In a bitcoinblock chain a blocks header would contain ->
	#Block hash,merkleroot,nonce,timestamp,version,previoushash

	def create_block(self,index,timestamp):
		block = {
			'index':index,
			'timestamp':timestamp,
			'previousHash':self.latest_block['block_hash'],
			'proof':0,
		}

		block['proof'] = self.proof_of_work(block,0)
		block['merkleroot'] = self.merkle_root_gen(self.block_transactions)
		block['block_hash'] = self.hashAlg(block)
		self.chain.append(block)

		#The block transactions are now nulled
		self.block_transactions = []


	@staticmethod
	def hashAlg(block):
		block_string = json.dumps(block,sort_keys=True).encode()
		return hashlib.sha256(block_string).hexdigest()

	def genesis_block(self):
		gen_block = {
			'index':1,
			'timestamp':time(),
			'merkleroot':'root',
			'proof':1,
			'previousHash':self.hashAlg({'gen_block':432424324342343466636462663}),
		}
		gen_block['block_hash'] = self.hashAlg(gen_block)
		self.chain.append(gen_block)

		print self.block_transactions
		#The transactions in the block are now nulled
		self.block_transactions = []

	@property
	def latest_block(self):
		return self.chain[-1]

	#While the block is being mined, the transactions should be processed
	def proof_of_work(self,block,proof):
		#Keep trying the hash until you acheive the requirement
		#We can make a targethash that requires a certain nonce
		while self.hashAlg(block)[:4] != '0000':
			#print 'mining ' + str(proof)
			proof += 1
			block['proof'] = proof
			#We can add transactions in here
			self.new_transaction(random(),random(),random()) 
			#print block['merkleroot']
		return proof

	#These ransactions will take place in the block
	def new_transaction(self,rec,enterLink,amount):
		#We can hash all of this information together to make the transaction id hash
		trans = {
			'recpient':rec,
			'sender':enterLink,
			'amount':amount,

		}

		transactionID = self.hashAlg(trans);
		self.block_transactions.append(transactionID)

	def merkle_root_gen(self,block_transactions):
		if len(block_transactions) == 1:
			return block_transactions[0]
		new_hash_transactions = []
		if(len(block_transactions) % 2 != 0):
			new_hash = self.hashAlg(block_transactions[-1] + block_transactions[-1])
			new_hash_transactions.append(new_hash)
		for i in range(0,len(block_transactions) - 1,2):
			new_hash = self.hashAlg(block_transactions[i] + block_transactions[i+1])
			new_hash_transactions.append(new_hash)
		
		return self.merkle_root_gen(new_hash_transactions)



blockchain = blockChain()
blockchain.genesis_block()

#print blockchain.chain[-1]['merkleroot']
while __name__ == '__main__':
	print 'new block being mined!'
	blockchain.create_block(len(blockchain.chain),time())
	print blockchain.chain[-1]

#76d0b7da03f400f53a63a8b09108049de59ea3e9f00bcdd9f7cdcede0a7eda24








