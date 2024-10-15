from qiskit_optimization.applications import Maxcut
import numpy as np
import networkx as nx


from launch_evaluation import QTEE_Experiment

ExpressibilityExperiment = QTEE_Experiment

class MaxCutQUBO():

    def __init__(self, graph):
        self.graph = graph
        self.size = len(graph.nodes)
        maxcut = Maxcut(graph)
        self.maxcut = maxcut
        qubo = maxcut.to_quadratic_program()
        self.qubo = qubo
        operator, offset = qubo.to_ising()
        self.operator = operator
        self.offset = offset

    def __str__(self):
        return f"MaxCutQUBO({self.size})"


class ExperimentHandler():

    def __init__(self, sizes, ansatz_types, n_times_per_size, n_individuals_per_experiment):
        self.sizes = sizes
        self.ansatz_types = ansatz_types
        self.n_times_per_size = n_times_per_size
        self.n_individuals_per_experiment = n_individuals_per_experiment
        self.maxcut_experiments = []
        self.experiments = []

    def generate_maxcuts(self):
        for size in self.sizes:
            for _ in range(self.n_times_per_size):
                # FIXME ¿is there a better way?
                graph = nx.gnp_random_graph(size, 0.5)
                maxcut = MaxCutQUBO(graph)
                self.maxcut_experiments.append(maxcut)

    def generate_experiments(self):
        for maxcut in self.maxcut_experiments:
            for AnsatzClass in self.ansatz_types:
                # TODO: generación de los ansatz
                ansatz = AnsatzClass(maxcut.size, reps=1, flatten=True)
                experiment = ExpressibilityExperiment(maxcut.operator, ansatz,
                                                      self.n_individuals_per_experiment)
                self.experiments.append(experiment)
