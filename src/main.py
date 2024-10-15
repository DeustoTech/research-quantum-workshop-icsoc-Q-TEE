from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_apscheduler import APScheduler

import logging
import threading
import numpy as np

from qiskit import qasm3

from launch_evaluation import QTEE_Experiment

current_experiments = {}

logging.basicConfig(
    filename='logs/flask.logs',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s')

class Config:
    SCHEDULER_API_ENABLED = True

# SETUP APIs
app = Flask(__name__)
app.config.from_object(Config())

# Initialize the scheduler
scheduler = APScheduler()
scheduler.init_app(app)

@ staticmethod
def initialize_app():
    '''Initializes the app'''
    # Enable CORS
    CORS(app)

    # Execute before the first request
    with app.app_context():

        logging.info("Initializing app")

        logging.info("App initialized correctly")

@app.route('/qtee', methods=['POST'])
def qtee():
    data = request.get_json()
    if not data or "ansatz" not in data or "operator_pauli_list" not in data:
        return jsonify({"error":"Invalid request, parameters 'ansatz' and 'operator_pauli_list' are requiered"}), 400
    try:
        data["ansatz"] = qasm3.loads(data["ansatz"])
    except Exception as e:
        logging.error(e)
        return jsonify({"error":"Invalid ansatz"}), 400
    experiment = QTEE_Experiment(**data)
    process = threading.Thread(target=experiment._run)
    process.start()
    current_experiments[experiment.experiment_ID] = experiment
    return jsonify({"experiment_ID": experiment.experiment_ID}), 200
    
@app.route('/qtee-results', methods=['POST'])
def qtee_results():
    try:
        data = request.get_json()
        if not data or "experiment_ID" not in data:
            return jsonify({"error":"Invalid request, parameter 'experiment_ID' is requiered"}), 400
        if data["experiment_ID"] in current_experiments:
            experiment = current_experiments[data["experiment_ID"]]
            if experiment.result is not None:
                del current_experiments[data["experiment_ID"]]
                values = [float(x[0]) for x in experiment.result]
                media = np.mean(values)
                std = np.std(values)
                minimo = np.min(values)
                maximo = np.max(values)
                print(f"Media: {media}, std: {std}, min: {minimo}, max: {maximo}, result: ´{values}")
                if "verbose" not in data or data["verbose"] != True:
                    return jsonify({"status": "DONE", "metrics":{"Media": media, "std": std, "range":{"min": minimo, "max": maximo}}})
                else:
                    return jsonify({"status": "DONE", "metrics":{"Media": media, "std": std, "range":{"min": minimo, "max": maximo}}, "results":list(values)})
            else:
                print(experiment)
                return jsonify({"status": "PENDING"}), 200
        else:
            print(current_experiments, data["experiment_ID"])
            return jsonify({"error": "experiment does nor exist"}), 200
    except Exception as e:
        logging.error(e)
        return jsonify({"error":"Unknown error"}), 500

if __name__ == '__main__':
    initialize_app()
    scheduler.start()
    app.run(host='0.0.0.0', port=5000)