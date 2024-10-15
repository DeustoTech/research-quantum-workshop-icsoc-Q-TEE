import numpy as np
import time
import hashlib

#from experiment import *
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

from qiskit.quantum_info import Pauli, SparsePauliOp

from qiskit_ibm_runtime.fake_provider import FakeSherbrooke

# Simulator
from qiskit_aer import AerSimulator
from qiskit_ibm_runtime.fake_provider import FakeSherbrooke, FakeTorino, FakeKyiv, FakeBrisbane, FakeKawasaki, FakeQuebec

from qiskit_ibm_runtime import Batch, EstimatorV2, EstimatorOptions

# Transpiler
from qiskit.transpiler import generate_preset_pass_manager

fake_backend_list = {
    'ibm_sherbrooke': FakeSherbrooke(),
    'ibm_torino': FakeTorino(),
    'ibm_kyiv': FakeKyiv(),
    'ibm_brisbane': FakeBrisbane(),
    'ibm_kawasaki': FakeKawasaki(),
    'ibm_quebec': FakeQuebec()
}

def transpile_circuit(circuit, operator, backend):
    pm = generate_preset_pass_manager(optimization_level=3, backend=backend)
    tr_circuit = pm.run(circuit)
    tr_operator = operator.apply_layout(tr_circuit.layout)
    return tr_circuit, tr_operator

class QTEE_Experiment():
    '''
    Class that contains and manages the experiment run to evaluate the trainability and expressivity of an ansatz
    '''

    def __init__(self, operator_pauli_list, ansatz, num_evaluations=500, noise_model='none', operator_coeff_list=None, shots=10_000):
        self.operator = self._generate_operator(operator_pauli_list, operator_coeff_list)
        self.ansatz = ansatz
        self.num_evaluations = num_evaluations
        self.backend = self._generate_backend(noise_model)
        self.param_vectors = np.random.uniform(0, 2*np.pi, (num_evaluations, ansatz.num_parameters))
        self.experiment_ID = self._generate_experiment_id()
        self.shots = shots
        self.result = None
    
    def _generate_experiment_id(self):
        # Get the current time as a string
        current_time = str(time.time())
        str_exp = f"ExpressibilityExperiment({self.ansatz.__class__.__name__}, {self.operator.num_qubits}, {self.num_evaluations})" + current_time
        # Hash the unique string
        experiment_id = hashlib.sha256(str_exp.encode()).hexdigest()
        return experiment_id
    
    def _generate_backend(self, noise_model):
        sim_backend = AerSimulator()
        if noise_model == 'none':
            return sim_backend
        else:
            # Get the fake backend based on noise model
            fake = fake_backend_list.get(noise_model)
            if fake:
                backend = sim_backend.from_backend(fake)
                return backend
            else:
                raise ValueError(f"Noise model '{noise_model}' not found in the available fake backends.")
            
    def _generate_operator(self, pauli_list, coeff_list):
        if coeff_list is None:
            coeff_list = [1+0j]*len(pauli_list)
        return SparsePauliOp(data=pauli_list, coeffs=coeff_list)

    def __str__(self):
        return f"ExpressibilityExperiment({self.experiment_ID})"
    
    def _run(self):
        # Prepare the estimator
        #batch = Batch(backend=backend)
        estimator = EstimatorV2(mode=self.backend, options=EstimatorOptions(default_shots=self.shots))

        qc, observable = transpile_circuit(self.ansatz, self.operator, self.backend)
        # Prepare the PUBs
        pubs = []

        for vector_param in self.param_vectors:
            pub = (qc, observable, vector_param)

            pubs.append(pub)

        # Run the estimator
        job = estimator.run(pubs)

        # Get results
        primitive_result = job.result()
        pub_results = primitive_result._pub_results
        res = [(pub_result.data.evs, pub_result.data.stds) for pub_result in pub_results]

        # Set results
        self.result = res

        return True
    
    def get_metrics(result):
        #TODO
        return None
    
    def get_result(self):
        # IF THREAD IS OPEN THEN RETURN FALSE
        # ELSE RETURN THE RESULT
        return self.result
        
    
    