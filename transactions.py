import logginh
import json
import hashlib
import socket
from random import random
import time
#The transactions will first needed to be held in escrow.
#Miners will then confirm the transaction
#If all is well the transaction will be made

#The transactions will include sender,recpient, amount and the hash type of the coin


class SocketConnection():
	def __init__(self,HOST,PORT):
		try:
			self.HOST = HOST
			self.PORT = PORT
			self.minerSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
			self.tunnel = (HOST,PORT)
			self.minerSocket.connect(tunnel)
			logging.log("The Miner Socket is now ready to accept transactions :)")
		except:
			logging.critical("The miner network is currently experiencing trouble :(")

	@classmethod
	def exe_tunnel(self,TransactionIDJSON):
		# The transaction ID includes json data. 
		# To be safe I will use the sendall permission form socket then make the miner hash the id
		tempData = self.TransactionIDJSON
		socket.sendall(tempData)	#This will send to the miner network in order to be hashed
		logging.log("The transaction has been sent to escrow and is waiting to be fufilled on the network!!\n")


class Transactions():
	def __init__(self,senderInformation,recInformation,amount,hashNonce):
		self.senderInformation = senderInformation		#Will initially have the users information and the receiving users info
														#This will probably just be wallet address as well as public and private keys
		self.recInformation = recInformation			####
		self.amount = amount
		
		self.hashNonce = hashNonce						## A random hash that will contribute for the proof of work that will take place for the miners
		self.coinPricePt = 0.002 #This price is relative to eth, This will randomly fluctuate
		
	
	@property
	def config_sender_info(self):
		#The sender information will contain json data
		#Configure some more information in this section
		self.senderInformation['time_sent'] = time.time()
		self.senderInformation['price/eth'] = self.coinPricePt
		self.senderInformation['exchange'] = ':)'

	@property
	def config_receiver_info(self):
		#Configure some info here
		self.recInformation['time_rec'] = time.time()
		self.recInformation['exchange'] = ':)'


		
	@property
	def fluctuate_price(self):
		self.coinPricePt += random.uniform(-0.0002, 0.9)
		return self.coinPricePt - self.transaction_fee()
	
	#This method will put the transaction into json and hash all of its contents
	@classmethod
	def pack_transaction(self):
		transaction = {'senderName':self.senderInformation['name'],
					   'senderDetails':self.senderInformation,
					   'recName':self.recInformation['name'],
					   'recDetails':self.recInformation
					   }
		return transaction
		

	#This method should be on the mining client				   
	@staticmethod
	def hashingState(transaction):
		transaction_id = hashlib.sha256(transaction)
		return transaction_id

	# The miners will begin to contribute to the merkle root of the transaction which are taking place.
	# A list of transaction would have to be distributed to all of the miners on the network
	# This is where ngrok would be useful to share information over a 'public' localhost

	# In order for the project to bring miners incentive to hash transactions pay them from the network fee

	@property
	def transaction_fee(self):
		# for now this will be static
		return 0.17


# Lets begin by waiting for transactions
# There should be a max amount of transactions per block
# Once this number is met, the consensus will init

# We just need to init sender name and receiver name

while __name__ == '__main__':
	# Lets first init the socket that will connect to the miner network
	
	miner_network = SocketConnection('localhost',1024)	#

	#Sender name will be the ip/client
	# Ill just use the sockets host for now
	sender_name = {'name':miner_network.HOST}
	receiver_name = {'name':miner_network.HOST}

	priceAmount = int(input("Enter the amount you want to send over the network!: $"))
	transaction_data = Transactions(sender_name,receiver_name,priceAmount,9324432)
	transaction_data.config_sender_info()		# get-only
	transaction_data.config_receiver_info()		# get-only
	transaction_data.fluctuate_price()			# property set that simulates price volitity
	json_transaction = transaction_data.pack_transaction()	#The json object of the transaction
	logging.warning("A new transaction has been initialized $$$ on the network")
	logging.critical("Now setting up a connection to the miner network!!")

	miner_network.minerSocket.sendall(json_transaction)
	















