__author__ = 'Alireza Mirzaeiyan'

import random

from chromosome import Chromosome


class NQueens:
    def __init__(self, dimension, population_count, mutation_factor, iteration):
        self.mutation_factor = mutation_factor
        self.population_count = population_count
        self.dimension = dimension
        self.iteration = iteration
        self.population = []

        for n in range(0, population_count):
            chromosome = Chromosome(dimension)
            self.population.append(chromosome)

    def total_fitness(self):
        sumation = 0
        for chromosome in self.population:
            sumation += chromosome.fitness()
        return sumation

    # Choose better fitness using roulette wheels
    def select(self):
        new_population = []
        for i in range(0, self.population_count):
            sumation = 0
            for chromosome in self.population:
                total = chromosome.normalize(self.total_fitness())
                if sum <= random.random() < (total + sumation):
                    new_population.append(chromosome)
                    break
                sumation += total
        if len(new_population) == self.population_count:
            self.population = new_population

    def crossover(self):
        population = []
        for i in range(0, len(self.population) if len(self.population) % 2 == 0 else len(self.population) - 1, 2):
            point = random.choice(range(0, self.dimension))
            parent_right1 = self.population[i].genes[point:self.dimension]
            parent_right2 = self.population[i + 1].genes[point:self.dimension]
            self.population[i].genes[point:self.dimension] = parent_right2
            self.population[i + 1].genes[point:self.dimension] = parent_right1

    def mutate(self):
        for chromosome in self.population:
            if random.random() < self.mutation_factor:
                chromosome.genes[random.randint(0, self.dimension - 1)] = random.randint(0, self.dimension - 1)

    def solve(self):
        found = False
        result = ""
        for n in range(0, self.iteration):
            self.crossover()
            self.mutate()
            print 'Generation=>', n + 1
            for chromosome in self.population:
                if chromosome.fitness() == (self.dimension * (self.dimension - 1)) / 2:
                    found = True
                    result = chromosome.genes, 'Fitness=>', chromosome.fitness()
            if found:
                print result
                break
