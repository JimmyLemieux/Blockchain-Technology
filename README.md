# Blockchain-Technology
*It should be noted that this is not a working blockchain but rather a well simulated clone of a blockchain.*
The concept of the blockchain is fairly simple and effective. Blocks contain what is called a *block header* which contains specific information about the block that is to be appended to the blockchain.
#Block Headers
*The following is a lightweight example of a block header being initialized*
```python
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
 ```
 One of the more important things about a block is that each block contains the sha256 hash of the previous block. This is so that each block is related to each other. If someone were to attempt to tamper with a block in the blockchain. The entire blockchain proceeding that block will be invalidated.
 
#Hashing
*Using the hashlib library to use the sha256 hashset to encrypt the block header of each block*
```python
@staticmethod
	def hashAlg(block):
	 block_string = json.dumps(block,sort_keys=True).encode()
	 return hashlib.sha256(block_string).hexdigest()
```
#Mining
The mining network is currently a work in progress. For now the mining network would be ran over a p2p network with a socket. The purpose of the miners is to hash all the transactions that are being made in the current block. These transactions are hashed into one single transaction called the *merkle root*
![MERKLEROOT](https://i.stack.imgur.com/ExJSC.png)
*The merkle root will be included in the blockheader hash*
*How the merkle root is calculated*
```python
#Hash the pairs of the id's recursively unitl a root value
def merkleSet(hashList):      # Every other pair of transactions are hashed into each other
                              # This would be one of the purposes of the minor
     if len(hashList) == 1:   # The hashlist is a list of transactionID Hashes
          return hashList[0]
     #We loop through the transactions in the list two at a time
     newHashList = []
     for i in range(0, len(hashList) - 1,2):
          newHashList.append(hash(hashList[i],hashList[i+1]))
     if len(hashList) % 2 != 0:
          newHashList.append(hash(hashList[-1],hashList[-1]))
     return merkleSet(newHashList)
```
#Transactions
For now the transactions will be held over a peer to peer network. The transaction data will be connected to a miner network in which miners will be listening for the transaction data. The miners will then begin the hashing session.
```python
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
```
The transactions will contain basic information such as the sender name, timestamp, recpient name, amount sent and the exchange kei in which they used
This part of the project is still in development..
