from math import sqrt
from random import randrange
from random import seed


# calculate the Euclidean distance between two vectors
def euclidean_distance(row1, row2):
    distance = 0.0
    for i in range(len(row1) - 1):
        distance += (row1[i] - row2[i]) ** 2
    return sqrt(distance)


# Locate the best matching unit
def get_best_matching_unit(prototypes, test_row):
    distances = list()
    for codebook in prototypes:
        dist = euclidean_distance(codebook, test_row)
        distances.append((codebook, dist))
    distances.sort(key=lambda tup: tup[1])
    return distances[0][0]


# Create a random prototype vector
def random_prototype(train_data):
    n_records = len(train_data)
    n_features = len(train_data[0])
    prototype = [train_data[randrange(n_records)][i] for i in range(n_features)]
    return prototype


# Train a set of prototype vectors
def train_codebooks(train, no_of_prototypes, learning_rate, epochs):
    prototypes = [random_prototype(train) for i in range(no_of_prototypes)]
    for epoch in range(epochs):
        rate = learning_rate * (1.0 - (epoch / float(epochs)))
        sum_error = 0.0
        for row in train:
            bmu = get_best_matching_unit(prototypes, row)
            for i in range(len(row) - 1):
                error = row[i] - bmu[i]
                sum_error += error ** 2
                if bmu[-1] == row[-1]:
                    bmu[i] += rate * error
                else:
                    bmu[i] -= rate * error
        print('>epoch=%d, lrate=%.3f, error=%.3f' % (epoch, rate, sum_error))
    return prototypes


# Test the training function
seed(1)
dataset = [[2.7810836, 2.550537003, 0],
           [1.465489372, 2.362125076, 0],
           [3.396561688, 4.400293529, 0],
           [1.38807019, 1.850220317, 0],
           [3.06407232, 3.005305973, 0],
           [7.627531214, 2.759262235, 1],
           [5.332441248, 2.088626775, 1],
           [6.922596716, 1.77106367, 1],
           [8.675418651, -0.242068655, 1],
           [7.673756466, 3.508563011, 1]]
learn_rate = 0.3
n_epochs = 10
n_codebooks = 2
codebooks = train_codebooks(dataset, n_codebooks, learn_rate, n_epochs)
print('Codebooks: %s' % codebooks)
