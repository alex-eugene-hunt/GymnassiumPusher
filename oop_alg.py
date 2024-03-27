class TestAlg:

    def __init__(self, alg_name, alg_func):
        self.alg_name = alg_name
        self.alg_func = alg_func

    def out_algo(self):
        print(f"Starting {self.alg_name}...")

    def run_algo(self):
        print(f"Running {self.alg_name}...")
        self.alg_func()

    def graph_algo(self):
        print(f"Graphing {self.alg_name} results...")
