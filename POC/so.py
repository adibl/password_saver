"""
name:
date:
description
"""


list = ['In', 'a', 'gesture', 'sure', 'to', 'rattle', 'the', 'Chinese', 'Government', ',', 'Steven', 'Spielberg', 'pulled', 'out', 'of', 'the', 'Beijing', 'Olympics', 'to', 'protest', 'against', 'China', '_s', 'backing', 'for', 'Sudan', '_s', 'policy', 'in', 'Darfur', '.']

seq0 = "Steven Spielberg"
seq1 = "the Chinese Government"
seq2 = "the Beijing Olympics"

def seq_in_list(seq, list):
    seq =seq.split(' ')
    if list.count(seq[0]) > 0:
        index = list.index(seq[0])
        print index
        if all(list.index(word) == index for word, index in zip(seq, range(index, len(seq0) + index))):
            print index
        else:
            print 'sequesnce not found'
    else:
        print 'sequesnce not found'

seq_in_list(seq0, list)

seq_in_list(seq1, list)
seq_in_list(seq2, list)

