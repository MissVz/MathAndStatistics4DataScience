# CS506 HOS10A – Text Generation Using LSTM
# Topic: Automatic Text Generation using LSTM

# === IMPORTS ===
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

from keras.models import Sequential  # type: ignore
from keras.layers import Input, Dense, Dropout, LSTM  # type: ignore
from keras.optimizers import RMSprop  # type: ignore
import numpy as np
import random
import sys
from matplotlib import pyplot as plt

# === LOAD DATA ===
filename = "Trading with Mexico.txt"
raw_text = open(filename, 'r', encoding='utf-8').read()
raw_text = raw_text.lower()
print(raw_text[0:1000])

# === CLEAN DATA ===
raw_text = ''.join(c for c in raw_text if not c.isdigit())
chars = sorted(list(set(raw_text)))  # List of every character

# === CHARACTER MAPPING ===
char_to_int = dict((c, i) for i, c in enumerate(chars))
int_to_char = dict((i, c) for i, c in enumerate(chars))

# === CHARACTER COUNTS ===
n_chars = len(raw_text)
n_vocab = len(chars)
print("Total Characters in the text; corpus length:", n_chars)
print("Total Vocab: ", n_vocab)

# === CREATE SEQUENCES ===
seq_length = 60  # Length of each input sequence
step = 10  # Instead of moving 1 letter at a time, try skipping a few.
sentences = []  # X values (Sentences)
next_chars = []  # Y values. The character that follows the sentence defined as X

for i in range(0, n_chars - seq_length, step):  # step=1 means each sentence is offset just by a single letter
    sentences.append(raw_text[i: i + seq_length])  # Sequence in
    next_chars.append(raw_text[i + seq_length])  # Sequence out

n_patterns = len(sentences)
print('Number of sequences:', n_patterns)

# === VECTORIZATION ===
x = np.zeros((len(sentences), seq_length, n_vocab), dtype=np.bool_)
y = np.zeros((len(sentences), n_vocab), dtype=np.bool_)
for i, sentence in enumerate(sentences):
    for t, char in enumerate(sentence):
        x[i, t, char_to_int[char]] = 1
    y[i, char_to_int[next_chars[i]]] = 1

print(x.shape)
print(y.shape)
print(y[0:10])

# === MODEL BUILDING ===
# model = Sequential()
# model.add(LSTM(128, input_shape=(seq_length, n_vocab)))
# model.add(Dense(n_vocab, activation='softmax'))
model = Sequential()
model.add(Input(shape=(seq_length, n_vocab)))
model.add(LSTM(128))
model.add(Dense(n_vocab, activation='softmax'))

optimizer = RMSprop(learning_rate=0.01)
model.compile(loss='categorical_crossentropy', optimizer=optimizer)
model.summary()

# === CHECKPOINT CALLBACK ===
from keras.callbacks import ModelCheckpoint
filepath = "saved_weights-{epoch:02d}-{loss:.4f}.keras"
checkpoint = ModelCheckpoint(filepath, monitor='loss', verbose=1, save_best_only=True, mode='min')
callbacks_list = [checkpoint]

# === FIT THE MODEL ===
history = model.fit(x, y,
                    batch_size=128,
                    epochs=50,
                    callbacks=callbacks_list)
model.save('my_saved_weights_50epochs.keras')

# === PLOT TRAINING LOSS ===
loss = history.history['loss']
epochs = range(1, len(loss) + 1)
plt.plot(epochs, loss, 'y', label='Training loss')
plt.title('Training loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.show()

# === SAMPLE FUNCTION ===
def sample(preds):
    preds = np.asarray(preds).astype('float64')
    preds = np.log(preds)
    exp_preds = np.exp(preds)  # exp of log(x), isn't this same as x??
    preds = exp_preds / np.sum(exp_preds)
    probas = np.random.multinomial(1, preds, 1)
    return np.argmax(probas)

# === GENERATE TEXT ===
import glob
latest_model = sorted(glob.glob("saved_weights-50-*.keras"))[-1]
model.load_weights(latest_model)
print(f"Loaded model weights from: {latest_model}")

# Pick a random sentence from the text as seed.
start_index = random.randint(0, n_chars - seq_length - 1)

# Initiate generated text and keep adding new predictions and print them out
generated = ''
sentence = raw_text[start_index: start_index + seq_length]
generated += sentence
print('----- Seed for our text prediction: "' + sentence + '"')
sys.stdout.write(generated)

# Number of characters including spaces
for i in range(400):
    x_pred = np.zeros((1, seq_length, n_vocab))
    for t, char in enumerate(sentence):
        x_pred[0, t, char_to_int[char]] = 1.

    preds = model.predict(x_pred, verbose=0)[0]
    next_index = sample(preds)
    next_char = int_to_char[next_index]

    generated += next_char
    sentence = sentence[1:] + next_char

    sys.stdout.write(next_char)
    sys.stdout.flush()
print()

# REFERENCE:
# OpenAI. (2025). ChatGPT’s assistance with CS506 HOS10A LSTM text generation example [Large language model]. https://openai.com/chatgpt