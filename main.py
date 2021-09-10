import hashlib

class Block():
    def __init__(self, data, previousHash):
        self.data = data
        self.previousHash = previousHash
        self.nonce = 1
        self.hash = self.compute_hash()
    
    def compute_hash(self):
        material = self.data + self.previousHash + str(self.nonce)
        return hashlib.sha256(material.encode('utf-8')).hexdigest()
    
    def print_nonce(self):
        print(self.nonce)
    
    def get_answer(self, difficulty):
        answer = ""
        for i in range(difficulty):
            answer = answer + "0"
        return answer

    def mine(self, difficulty):
        while True:
            self.hash = self.compute_hash()
            if self.hash[0:difficulty] != self.get_answer(difficulty):
                self.nonce += 1
                self.hash = self.compute_hash()
            else:
                break
        #print("done", self.hash)


class Chain():
    def __init__(self):
        self.chain = [self.big_bang()]
        self.difficulty = 5

    def big_bang(self):
        fatherBlock = Block("I am father", "")
        return fatherBlock
    
    def get_latest_block(self):
        return self.chain[-1]
    
    def add_block_to_chain(self, newBlock):
        newBlock.previousHash = self.get_latest_block().hash
        newBlock.mine(self.difficulty)
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

for i in range(len(JustinChain.chain)):
    print(JustinChain.chain[i].hash)
for i in range(len(JustinChain.chain)):
    print(JustinChain.chain[i].previousHash)


if(JustinChain.validate_chain()):
    print("validated chain")
else:
    print("not validated chain")