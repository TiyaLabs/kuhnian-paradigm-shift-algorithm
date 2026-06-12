import numpy as np

def pso(objective, dim=30, bounds=(-5.12, 5.12), n_particles=50, max_iter=300, w=0.7, c1=1.5, c2=1.5, seed=42):
    rng = np.random.default_rng(seed)

    low, high = bounds
    span = abs(high - low)

    x = rng.uniform(low, high, size=(n_particles, dim))
    v = rng.uniform(-span, span, size=(n_particles, dim)) * 0.1

    pbest = x.copy()
    pbest_fit = np.array([objective(i) for i in x])

    g_idx = np.argmin(pbest_fit)
    gbest = pbest[g_idx].copy()
    gbest_fit = pbest_fit[g_idx]

    hist = []

    for _ in range(max_iter):
        r1, r2 = rng.random((n_particles, dim)), rng.random((n_particles, dim))

        v = w*v + c1*r1*(pbest-x) + c2*r2*(gbest-x)
        x = np.clip(x+v, low, high)

        fit = np.array([objective(i) for i in x])
        improved = fit < pbest_fit

        pbest[improved] = x[improved]
        pbest_fit[improved] = fit[improved]

        g_idx = np.argmin(pbest_fit)

        if pbest_fit[g_idx] < gbest_fit:
            gbest = pbest[g_idx].copy()
            gbest_fit = pbest_fit[g_idx]

        hist.append(gbest_fit)

    return gbest, gbest_fit, np.array(hist)
