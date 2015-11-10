__author__ = 'Alireza Mirzaeiyan'

from nqueens import NQueens

if __name__ == '__main__':
    nqueens = NQueens(dimension=8, population_count=40000, mutation_factor=0.4, iteration=200)
    nqueens.solve()
