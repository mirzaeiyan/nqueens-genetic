__author__ = 'Alireza Mirzaeiyan'

import optparse
from nqueens import NQueens

if __name__ == '__main__':
    parser = optparse.OptionParser()
    parser.add_option('-d', dest='dimension', type='int', metavar="Dimension")
    parser.add_option('-p', dest='population_count', type='int', metavar="Population Count")
    parser.add_option('-m', dest='mutation_factor', type='float', metavar="Mutation Factor")
    parser.add_option('-i', dest='iteration', type='int', metavar="Iteration")
    (options, args) = parser.parse_args()

    nqueens = NQueens(options.dimension, options.population_count, options.mutation_factor, options.iteration)
    nqueens.solve()
