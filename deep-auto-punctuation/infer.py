"""
Perform inference on inputted text.
"""
import utils
import torch
from termcolor import cprint, colored as c
import model
import data
import re
import sys

source = sys.argv[1]

# get an edgt object
def get_edgt():
    input_chars = list(" \nabcdefghijklmnopqrstuvwxyz01234567890")
    output_chars = ["<nop>", "<cap>"] + list(".,;:?!\"'$")

    # torch.set_num_threads(8)
    batch_size = 128

    char2vec = utils.Char2Vec(chars=input_chars, add_unknown=True)
    output_char2vec = utils.Char2Vec(chars = output_chars)
    input_size = char2vec.size
    output_size = output_char2vec.size

    hidden_size = input_size
    layers = 1

    rnn = model.GruRNN(input_size, hidden_size, output_size, batch_size=batch_size, layers=layers, bi=True)
    egdt = model.Engadget(rnn, char2vec, output_char2vec)
    egdt.load('./data/Gru_Engadget_epch-24.tar')
    return egdt


def predict_next(source, in_edgt, gen_length=None, temperature=0.05):
    input_chars = list(" \nabcdefghijklmnopqrstuvwxyz01234567890")
    output_chars = ["<nop>", "<cap>"] + list(".,;:?!\"'$")
    input_text, punc_target = data.extract_punc(source, input_chars, output_chars)
    in_edgt.model.batch_size = 1
    in_edgt.init_hidden_()
    in_edgt.next_([input_text])
    punc_output = in_edgt.output_chars(temperature=temperature)[0]
    result = data.apply_punc(input_text, punc_output)
    # capitalize letters after periods
    for i in range(len(result) - 1):
        if result[i] == '.':
            result = result[:i] + result[i].upper() + result[i + 1:]
    print(result)

predict_next(source, get_edgt())
    




















