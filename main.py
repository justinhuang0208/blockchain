import hashlib

class Block():
    def __init__(self, data, previousHash):
        self.data = data
        self.previousHash = previousHash
        self.hash = self.compute_hash()
    
    def compute_hash(self):
        return hashlib.sha256(self.data.encode('utf-8')).hexdigest()

class Chain():
    def __init__(self):
        self.chain = [self.big_bang()]

    def big_bang(self):
        fatherBlock = Block("I am father", "")
        return fatherBlock
    
    def get_latest_block(self):
        return self.chain[-1]
    
    def add_block_to_chain(self, newBlock):
        newBlock.previousHash = self.get_latest_block().hash
        newBlock.hash = newBlock.compute_hash()
        self.chain.append(newBlock)
    
    def validate_chain(self):
        if(len(self.chain) == 1):
            if(self.chain[0].hash != self.chain[0].compute_hash()):
                return False
            else:
                return True
        else:
            for i in range(len(self.chain)):
                if(self.chain[i].hash != self.chain[i].compute_hash()):
                    print("data had been modified")
                    return False
            for i in range(1, len(self.chain)):
                if(self.chain[i].previousHash != self.chain[i-1].hash):
                    print("the connection was broken")
                    return False
            return True
JustinChain = Chain()

block1 = Block("transfer ten dollars", "")
block2 = Block("transfer one hundred dollars", "")
JustinChain.add_block_to_chain(block1)
JustinChain.add_block_to_chain(block2)

JustinChain.chain[1].data = "transfer two hundred dollars"
JustinChain.chain[1].hash = JustinChain.chain[1].compute_hash()
if(JustinChain.validate_chain()):
    print("validated chain")
else:
    print("not validated chain")