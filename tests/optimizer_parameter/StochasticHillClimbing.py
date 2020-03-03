# Author: Simon Blanke
# Email: simon.blanke@yahoo.com
# License: MIT License

import numpy as np

from hyperactive import Hyperactive

X, y = np.array([0]), np.array([0])
memory = False
n_iter = 25


def sphere_function(para, X_train, y_train):
    loss = []
    for key in para.keys():
        if key == "iteration":
            continue
        loss.append(para[key] * para[key])

    return -np.array(loss).sum()


search_config = {
    sphere_function: {"x1": np.arange(-3, 3, 0.1), "x2": np.arange(-3, 3, 0.1)}
}


def test_p_down():
    for p_down in [0.0001, 100]:
        opt = Hyperactive(X, y, memory=memory)
        opt.search(
            search_config,
            n_iter=n_iter,
            optimizer={"StochasticHillClimbing": {"p_down": p_down}},
        )