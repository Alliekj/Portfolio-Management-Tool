import numpy as np
import pandas as pd
import cvxpy as cp

def mean_variance_optimization(returns, risk_aversion):
    """
    Perform mean-variance optimization to find the optimal portfolio weights.

    Parameters:
    returns (ndarray): Matrix of returns where each column represents an asset.
    risk_aversion (float): Risk aversion parameter.

    Returns:
    ndarray: Optimal weights for the assets.
    """
    n = returns.shape[1]
    expected_returns = np.mean(returns, axis=0)
    cov_matrix = np.cov(returns.T)
    
    # Define optimization variables
    weights = cp.Variable(n)
    
    # Define the objective function
    objective = cp.Maximize(expected_returns @ weights - risk_aversion * cp.quad_form(weights, cov_matrix))
    
    # Define the constraints
    constraints = [cp.sum(weights) == 1, weights >= 0]
    
    # Define and solve the problem
    problem = cp.Problem(objective, constraints)
    problem.solve()
    
    return weights.value

