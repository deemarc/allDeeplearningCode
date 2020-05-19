"""
We try to clean out the lab one code and restructure it.
so, it is easier to review and modify
"""

from vocabDict import VocabDict
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, LSTM, BatchNormalization, Embedding
import pandas as pd

# Optimization parameters:
num_training_iterations = 2000  # Increase this to train longer
batch_size = 4  # Experiment between 1 and 64
seq_length = 100  # Experiment between 50 and 500
learning_rate = 5e-3  # Experiment between 1e-5 and 1e-1
embedding_dim = 256 


def buil_model(vocab_size):
    model = Sequential()
    # Layer 1: Embedding layer to transform indices into dense vectors 
    #   of a fixed embedding size
    model.add(vocab_size, embedding_dim, input_shape=(train_x.shape[1:]))
    model.add(LSTM(128, activation='relu',return_sequences=True))
    model.add(Dropout(0.1))
    model.add(BatchNormalization())
    model.add(Dense(vocab_size, activation='softmax'))
    return model

def pipeline(songs):
    # Join our list of song strings into a single string containing all songs
    songs_joined = "\n\n".join(songs) 

    # Find all unique characters in the joined string
    vocab = sorted(set(songs_joined))
    print("There are", len(vocab), "unique characters in the dataset")
    print(set(songs_joined))

    vocab_dict = VocabDict(vocab)

    vectorized_songs = vocab_dict.vectorize_string(songs_joined)

    pd.DataFrame





