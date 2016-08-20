import nltk
from Dijkstra import dijkstra

# function for information extraction from document.
# And returns two graph for path and direction and also returns path source and destination
def ie_preprocess(document):

    graph = {}
    dir_graph = {}
    directions = []
    sentences = nltk.sent_tokenize(document)
    words = [nltk.word_tokenize(sent) for sent in sentences]
    part_of_speech = [nltk.pos_tag(word) for word in words]

    for index in range(len(part_of_speech)):
        direction = [token for token, pos in part_of_speech[index] if
             pos.startswith('J') | pos.startswith('VBN')]
        directions.extend(direction)

    for index in range(len(sentences) - 1):
        tokens = [token for token, pos in nltk.pos_tag(nltk.word_tokenize(sentences[index])) if
               pos.startswith('N')]

        if tokens[0] in graph:
            graph[tokens[0]].update({tokens[1]: 1})
            dir_graph[tokens[0]].update({tokens[1]: get_opposite(directions[index])})
        else:
            graph.update({tokens[0]: {tokens[1]: 1}})
            dir_graph.update({tokens[0]: {tokens[1]: get_opposite(directions[index])}})

        if tokens[1] in graph:
            graph[tokens[1]].update({tokens[0]: 1})
            dir_graph[tokens[1]].update({tokens[0]: directions[index]})
        else:
            graph.update({tokens[1]: {tokens[0]: 1}})
            dir_graph.update({tokens[1]: {tokens[0]: directions[index]}})

    source = nltk.pos_tag(nltk.word_tokenize(nltk.sent_tokenize(document)[-1]))[-4]
    dest = nltk.pos_tag(nltk.word_tokenize(nltk.sent_tokenize(document)[-1]))[-2]
    return graph, dir_graph, source[0], dest[0]

# function that returns opposite direction of given input direction
def get_opposite(dir):
    if dir == 'north':
        return 'south'
    elif dir == 'south':
        return 'north'
    elif dir == 'west':
        return 'east'
    elif dir == 'east':
        return 'west'
    elif dir == 'north-east':
        return 'south-west'
    elif dir == 'north-west':
        return 'south-east'
    elif dir == 'south-west':
        return 'north-east'
    elif dir == 'south-east':
        return 'north-west'


# Please enter all sentences in one line only
str = raw_input()
graphPath, graphDirection, source, dest = ie_preprocess(str)

path = dijkstra(graphPath, dest, source)

print "Follow these steps to reach the destination."
total_hops = len(path) - 1
for index, hop in enumerate(path):

    if index == total_hops:
        continue

    next_hop = path[index + 1]
    for neighbor in graphDirection[hop]:

        if neighbor == next_hop:
            print "%d. From %s, Go to %s to reach %s." % \
                  (index + 1, hop, graphDirection[hop][neighbor], neighbor)
