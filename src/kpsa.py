import numpy as np

def kpsa(
    objective, dim=30, bounds=(-5.12, 5.12), n_agents=50, max_iter=300,
    alpha=0.65, beta=0.15, sigma=0.01,
    crisis_threshold=0.78, patience=25, cooldown=15, seed=42
):
    rng = np.random.default_rng(seed)

    low, high = bounds
    span = high - low

    pop = rng.uniform(low, high, size=(n_agents, dim))
    fitness = np.array([objective(x) for x in pop])

    best_idx = np.argmin(fitness)
    x_best = pop[best_idx].copy()
    f_best = fitness[best_idx]

    init_div = np.mean(np.std(pop, axis=0)) + 1e-12
    history, psi_history = [], []

    crisis_count = 0
    stagnation_count = 0
    cooldown_count = 0

    for t in range(max_iter):
        community = np.mean(pop, axis=0)
        progress_ratio = t / max_iter
        current_sigma = sigma * (1 - progress_ratio) * span

        new_pop = pop.copy()

        for i in range(n_agents):
            r1, r2 = rng.random(dim), rng.random(dim)
            local_noise = rng.normal(0, current_sigma, size=dim)

            new_pop[i] = (
                pop[i]
                + alpha * r1 * (x_best - pop[i])
                + beta * r2 * (community - pop[i])
                + local_noise
            )

        new_pop = np.clip(new_pop, low, high)
        new_fitness = np.array([objective(x) for x in new_pop])

        current_best_idx = np.argmin(new_fitness)
        current_best = new_pop[current_best_idx].copy()
        current_f = new_fitness[current_best_idx]

        if current_f < f_best:
            x_best = current_best.copy()
            f_best = current_f
            stagnation_count = 0
        else:
            stagnation_count += 1

        elite = x_best + rng.normal(0, 0.005 * span, size=(5, dim))
        elite = np.clip(elite, low, high)
        elite_fit = np.array([objective(x) for x in elite])

        if elite_fit.min() < f_best:
            x_best = elite[elite_fit.argmin()].copy()
            f_best = elite_fit.min()
            stagnation_count = 0

        stagnation_score = min(1, stagnation_count / patience)

        div = np.mean(np.std(new_pop, axis=0))
        diversity_collapse = 1 - np.clip(div / init_div, 0, 1)

        median_f = np.median(new_fitness)
        explanatory_failure = np.mean(new_fitness > median_f)

        psi = 0.45*stagnation_score + 0.35*diversity_collapse + 0.20*explanatory_failure

        crisis_allowed = cooldown_count <= 0
        crisis_triggered = ((psi >= crisis_threshold) or (stagnation_count >= patience)) and crisis_allowed

        if crisis_triggered:
            crisis_count += 1
            cooldown_count = cooldown
            stagnation_count = 0

            n_genius = max(4, int(0.25 * n_agents))

            worst_idx = np.argsort(new_fitness)[-n_genius:]
            genius = new_pop[worst_idx].copy()

            genius += rng.normal(0, 0.25 * span, size=genius.shape)
            genius = np.clip(genius, low, high)

            genius_fitness = np.array([objective(x) for x in genius])
            x_creative = genius[np.argmin(genius_fitness)].copy()

            lam = 1.0 + psi
            x_shift = x_creative + lam * (x_creative - x_best)
            x_shift = np.clip(x_shift, low, high)

            candidates = np.vstack([new_pop, genius, x_shift.reshape(1, -1)])
            candidate_fitness = np.array([objective(x) for x in candidates])

            best_candidate_idx = np.argmin(candidate_fitness)

            if candidate_fitness[best_candidate_idx] < f_best:
                x_best = candidates[best_candidate_idx].copy()
                f_best = candidate_fitness[best_candidate_idx]

            delta = 0.03 * span
            elite_count = max(2, int(0.15 * n_agents))

            elite_idx = np.argsort(new_fitness)[:elite_count]
            elites = new_pop[elite_idx].copy()

            relocated = x_best + rng.uniform(-delta, delta, size=(n_agents - elite_count, dim))
            relocated = np.clip(relocated, low, high)

            new_pop = np.vstack([elites, relocated])
            new_fitness = np.array([objective(x) for x in new_pop])

        if cooldown_count > 0:
            cooldown_count -= 1

        pop = new_pop
        fitness = new_fitness

        history.append(f_best)
        psi_history.append(psi)

    return x_best, f_best, np.array(history), np.array(psi_history), crisis_count
