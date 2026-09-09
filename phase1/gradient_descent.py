import numpy as np

np.random.seed(0)
x = np.linspace(0, 10, 50)
true_w = 3.0
true_b = 7.0
noise = np.random.normal(0, 2, size=50)
y = true_w * x + true_b + noise

X = x.reshape(-1, 1)
n = len(y)

w = np.array([0.0])
b = 0.0
learning_rate = 0.01

for i in range(1000):
    predictions = X @ w + b
    errors = predictions - y

    grad_w = (2 / n) * (X.T @ errors)
    grad_b = (2 / n) * np.sum(errors)

    w = w - learning_rate * grad_w
    b = b - learning_rate * grad_b

loss = np.mean((X @ w + b - y) ** 2)
print("gradient descent:", w, b, loss)

poly_w, poly_b = np.polyfit(x, y, 1)
print("np.polyfit:      ", poly_w, poly_b)
