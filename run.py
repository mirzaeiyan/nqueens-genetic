__author__ = 'Alireza Mirzaeiyan'

from nqueens import NQueens

if __name__ == '__main__':
    nqueens = NQueens(dimension=8, population_count=500, mutation_factor=0.2, iteration=2000000)
    nqueens.solve()
