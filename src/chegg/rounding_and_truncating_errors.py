from math import sin, cos, pow


# Actual f(x)
def f(x):
    return pow(x, 2) + sin(pow(x, 3))


# Exact derivative of f(x)
def f_derivative(x):
    return 2 * x + cos(pow(x, 3)) * (3 * pow(x, 2))


# Finding the approximation with several values of h
def f_derivative_approximate(x, h):
    return (f(x + h) - f(x)) / h


# Just outputting nicely
def visualize(logs):
    # Finding the maximum length of h so that output can be printed nicely
    max_len = 0
    for log in logs:
        max_len = max(max_len, len(str(log[0])), len(str(log[1])))

    # Now printing the logs
    for log in logs:
        for value in log:
            print(str(value).ljust(max_len + 5), end=" ")
        # Just giving the new line
        print()


# Main programme goes here. Let's start the value of h with 1

x = 2
h = 1

exact_derivative = f_derivative(x)  # 2.2539995942966375
approximate_derivative = f_derivative_approximate(x, h)  # 4.967017681781122

error = abs(exact_derivative - approximate_derivative)
max_allowed_error = 2e-12

logs = [['h', 'Truncation error']]

try:
    while error > max_allowed_error:
        h = h / 2
        approximate_derivative = f_derivative_approximate(x, h)
        error = abs(exact_derivative - approximate_derivative)
        cur = [h, error]
        logs.append(cur)
except ZeroDivisionError:
    # By the time the execution comes here value of h is incredibly small
    pass

# Visualizing the logs
visualize(logs)
