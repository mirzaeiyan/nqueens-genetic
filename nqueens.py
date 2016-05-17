from operator import attrgetter

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
        return sum([chromosome.fitness for chromosome in self.population])

    def weighted_random_choice(self, choices):
        max = sum(choices.values())
        pick = random.uniform(0, max)
        current = 0
        for key, value in choices.items():
            current += value
            if current > pick:
                return key

    # Choose better fitness using roulette wheels
    def select(self):
        random.shuffle(self.population)
        new_population = []
        choices = {chromosome: chromosome.fitness for chromosome in self.population}
        for i in range(0, self.population_count):
            new_population.append(self.weighted_random_choice(choices))
        self.population = new_population

    def crossover(self):
        for i in range(0, len(self.population) if len(self.population) % 2 == 0 else len(self.population) - 1, 2):
            point = random.choice(range(0, self.dimension))
            parent_right1 = self.population[i].genes[point:self.dimension]
            parent_right2 = self.population[i + 1].genes[point:self.dimension]
            chromosome1 = self.population[i]
            chromosome2 = self.population[i + 1]
            chromosome1.genes[point:self.dimension] = parent_right2
            chromosome2.genes[point:self.dimension] = parent_right1
            self.population.extend([chromosome1, chromosome2])

    def mutate(self):
        for chromosome in self.population:
            if random.random() < self.mutation_factor:
                chromosome.genes[random.randint(0, self.dimension - 1)] = random.randint(0, self.dimension - 1)

    def solve(self):
        for n in range(0, self.iteration):
            self.select()
            self.crossover()
            self.mutate()
            maximum_chromosome = max(self.population, key=attrgetter('fitness'))
            maximum = maximum_chromosome.fitness
            print 'Generation=>', n + 1, 'Maximum Fitness=>', maximum
            if maximum == (self.dimension * (self.dimension - 1)) / 2:
                print maximum_chromosome.genes, 'Fitness=>', maximum
                break
