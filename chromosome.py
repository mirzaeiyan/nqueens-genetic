__author__ = 'Alireza Mirzaeiyan'

import random


class Chromosome:
    def __init__(self, genes):
        self.dimension = genes
        self.genes = []
        for n in range(0, genes):
            self.genes.append(random.choice(range(0, genes)))

    def fitness(self):
        n = len(self.genes)
        fitness = 0

        for i in range(0, n):
            for j in range(0, n):
                if i != j:
                    if self.genes[i] == self.genes[j]:
                        fitness += 1

        for c in range(0, n):
            for i in range(0, n):
                for j in range(0, n):
                    if i - c == j - self.genes[c] and self.genes[i] == j and self.genes[i] != self.genes[c]:
                        fitness += 1

        for c in range(0, n):
            for i in range(0, n):
                for j in range(0, n):
                    if i + j == self.genes[c] + c and self.genes[i] == j and self.genes[i] != self.genes[c]:
                        fitness += 1

        return ((self.dimension * (self.dimension - 1)) / 2) - (fitness / 2)

    def normalize(self, total_fitness):
        if self.fitness() > 0:
            return round(float(self.fitness()) / total_fitness, 3)
        else:
            return 0
