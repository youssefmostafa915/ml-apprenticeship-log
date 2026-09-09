import numpy as np

X = np.array([
    [2, 3, 4],
    [1, 0, 1],
    [5, 5, 5],
])
b = 5
y = np.array([12, 5, 18])


def compute_mse(w, b):
    predictions = X @ w + b
    errors = predictions - y
    return np.mean(errors ** 2)


w = np.array([1.0, 0.0, 2.0])
loss_before = compute_mse(w, b)

nudge = 0.001
w_nudged = w.copy()
w_nudged[0] += nudge
loss_after = compute_mse(w_nudged, b)

slope_estimate = (loss_after - loss_before) / nudge
print(loss_before, loss_after, slope_estimate)
