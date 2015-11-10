__author__ = 'Alireza Mirzaeiyan'

from nqueens import NQueens

if __name__ == '__main__':
    nqueens = NQueens(dimension=8, population_count=300, mutation_factor=0.3, iteration=2000000)
    nqueens.solve()
