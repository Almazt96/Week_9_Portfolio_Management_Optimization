# Task 3: Portfolio Optimization & Modern Portfolio Theory (MPT)
from scipy.optimize import minimize
def portfolio_metrics(weights, mean_returns, cov_matrix, risk_free_rate=0.02):
    p_ret = np.sum(mean_returns * weights) * 252
    p_vol = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
    p_sharpe = (p_ret - risk_free_rate) / p_vol
    return p_ret, p_vol, p_sharpe
def optimize_portfolio(daily_returns, target="sharpe", risk_free_rate=0.02):
    mean_returns = daily_returns.mean()
    cov_matrix = daily_returns.cov() * 252
    num_assets = len(daily_returns.columns)
    constraints = ({"type": "eq", "fun": lambda x: np.sum(x) - 1})
    bounds = tuple((0, 1) for _ in range(num_assets))
    init_weights = num_assets * [1.0 / num_assets]
    if target == "sharpe":
    objective = lambda w: -portfolio_metrics(w, mean_returns, cov_matrix,
    risk_free_rate)[2]
    else: # minimize volatility
    objective = lambda w: portfolio_metrics(w, mean_returns, cov_matrix,
    risk_free_rate)[1]
    result = minimize(objective, init_weights, method="SLSQP", bounds=bounds,
    constraints=constraints)
    return result.x
if __name__ == "__main__":

    opt_weights = optimize_portfolio(returns, target="sharpe")
    print("\nOptimal Portfolio Weights (Max Sharpe):")
    for asset, weight in zip(assets, opt_weights):
    print(f"{asset}: {weight:.4f}")