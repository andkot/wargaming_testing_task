# dimension of sequence
DIMENSION = 10
PRIME_SEQUENCE = [1, 3, 5, 7, 11, 13, 17, 19, 23, 29]

FINALY_SEQUENCE = [0] * DIMENSION
for i in range(DIMENSION):
    FINALY_SEQUENCE[i] = i + 1


def count_hash(sequence):
    hash = 0
    for i in range(DIMENSION):
        hash += PRIME_SEQUENCE[i] ** sequence[i]
    return hash

def parse_to_vertices(array):
    vertices = []
    for el in array:
        vertices.append(el[0])
    return vertices

def parse_to_edges(array):
    edges = []
    for el in array:
        for edge in el[1]:
            edges.append([el[0], edge])
    return edges

FINALY_SEQUENCE_ID = count_hash(FINALY_SEQUENCE)

class Vertices():
    def __init__(self, sequence, ex_array, other=None):
        self.sequence = sequence
        self.id = count_hash(self.sequence)
        self.forward_edges = []
        self.count_edges(self.sequence, ex_array)
        # if other != None:
        #     other.array.append((self.id, self.forward_edges))
        # else:
        #     self.array.append((self.id, self.forward_edges))

        # if not self.forward_edges:
        if self.id != FINALY_SEQUENCE_ID:
            ex_array.append((self.id, self.forward_edges))


    def add_edge(self, edge):
        self.forward_edges.append(edge)

    def count_edges(self, sequence, ex_array):
        for i in range(DIMENSION):
            for j in range(i + 1, DIMENSION):
                if sequence[i] > sequence[j]:
                    tmp_next_seq = list.copy(sequence)
                    tmp_next_seq[i], tmp_next_seq[j] = tmp_next_seq[j], tmp_next_seq[i]
                    self.forward_edges.append(count_hash(tmp_next_seq))
                    Vertices(tmp_next_seq, ex_array, self)
                    # self.__init__(tmp_next_seq)

if __name__ == '__main__':

    print(FINALY_SEQUENCE)
    print(count_hash(FINALY_SEQUENCE))

    print('==========================')
    initial_sequence = [1, 4, 2, 3]
    array = []
    vertices = Vertices(initial_sequence, array)
    print(vertices.id, vertices.forward_edges)
    print(array)
    print('==========================')

    for el in array:
        print(el, '---', el[0], '-', el[1])


    print('==========================')

    print(parse_to_vertices(array))
    print(parse_to_edges(array))

