# by Kami Bigdely
# Rename Method
# Reference: https://parade.com/1039985/marynliles/pick-up-lines/

def calc_area_of_graph(graph):   # TODO: Rename this function to reflect what it's doing.
    """Calculate the area under the input graph."""
    # bla bla bla.
    pass

#####################

def max_value(array):  # TODO: Rename this function to reflect what it's doing.
    max_val = array[0]
    for value in array:
        if value > max_val:
            max_val = value
    return max_val


li = [5, -1, 43, 32, 87, -100]
print(max_value(li))

############################
def split_sentence_into_words(sentence):  # TODO: Rename this function to reflect what it's doing.
    words = sentence[0:].split(' ')
    return words

print(split_sentence_into_words('If you were a vegetable, you’d be a ‘cute-cumber.'))
