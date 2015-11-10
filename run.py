__author__ = 'Alireza Mirzaeiyan'

from nqueens import NQueens

if __name__ == '__main__':
    nqueens = NQueens(dimension=8, population_count=100, mutation_factor=0.1, iteration=2000000)
    nqueens.solve()
