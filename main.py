# This will host the setup environment; running gym, mujoco, and what not...

# ... from pyFile import pyFile_Function

# general idea is to use OOP for each different implementation of ML

from oop_alg import TestAlg

from setup import run_algorithms

def main():

    for algo_name, algo_func in run_algorithms:

        algo_inst = TestAlg(algo_name, algo_func)

        algo_inst.out_algo()
        algo_inst.run_algo()
        algo_inst.graph_algo()

if __name__ == "__main__":
    main()