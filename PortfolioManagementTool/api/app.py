from flask import Flask, request, jsonify
import pandas as pd
from optimization.utils import mean_variance_optimization

app = Flask(__name__)

@app.route('/optimize', methods=['POST'])
def optimize():
    data = request.get_json()
    returns = pd.DataFrame(data['returns'])
    risk_aversion = data['risk_aversion']
    weights = mean_variance_optimization(returns.values, risk_aversion)
    return jsonify(weights.tolist())

if __name__ == '__main__':
    app.run(debug=True)

