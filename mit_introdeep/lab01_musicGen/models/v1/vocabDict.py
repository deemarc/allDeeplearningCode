import numpy as np
class VocabDict():
    def __init__(self, vacab_list):
        vocab = vacab_list
        self.char2idx = {u:i for i, u in enumerate(vocab)}
        self.idx2char = np.array(vocab)
    
    def vectorize_string(self,string):
        vector = []
        for char in string:
            vector.append(self.char2idx[char])
        return  np.array(vector)