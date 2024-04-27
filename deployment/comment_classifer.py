from keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle
try:
    model_loaded = load_model('LSTM_model.h5')
    with open('token.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)
    print("Model and tokenizer loaded successfully.")
except Exception as e:
    print(f"An error occurred: {e}")

maxlen = 200


def classify(inp: list):
    shi = tokenizer.texts_to_sequences(inp)
    shit = pad_sequences(shi, maxlen=maxlen)
    out = model_loaded.predict(shit)
    out = out > .5
    return out.astype(int)
