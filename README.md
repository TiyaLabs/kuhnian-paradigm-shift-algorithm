# Kuhnian Paradigm Shift Algorithm (KPSA)

KPSA is an experimental philosophy-inspired metaheuristic optimization algorithm based on Thomas Kuhn's theory of scientific revolutions.

Instead of continuously following the current best solution, KPSA monitors search stagnation and introduces a crisis-driven exploration mechanism to escape local optima.

```text
Normal Science
      ↓
   Anomaly
      ↓
    Crisis
      ↓
Paradigm Shift
      ↓
 New Paradigm
```

---

## Core Idea

Traditional optimizers often become trapped in local optima when the population converges too early.

KPSA introduces:

- Paradigm Stability Index (PSI)
- Crisis Detection
- Creative Genius Exploration
- Paradigm Shift Operator
- Population Relocation

to encourage adaptive exploration when progress stalls.

---

## Mathematical Formulation

### Normal Science Update

Agents move toward the current best solution and community consensus:

```math
x_i(t+1)=x_i(t)+\alpha r_1(x_{best}-x_i)+\beta r_2(x_{community}-x_i)+\epsilon
```

where:

- α = Paradigm Attraction
- β = Community Influence
- ε = Local Exploration Noise

### Paradigm Stability Index (PSI)

```math
PSI=0.45 \cdot Stagnation
+0.35 \cdot DiversityCollapse
+0.20 \cdot ExplanatoryFailure
```

### Crisis Trigger

```math
PSI \ge 0.78
```

or prolonged stagnation.

When a crisis is triggered, KPSA activates exploratory agents to search beyond the current paradigm.

---

## Benchmark Functions

The algorithm was evaluated on:

- Sphere
- Rastrigin
- Ackley
- Rosenbrock
- Griewank
- Schwefel
- Levy

Configuration:

| Parameter | Value |
|------------|---------|
| Dimension | 30 |
| Population Size | 50 |
| Iterations | 300 |
| Independent Runs | 30 |
| Baseline | PSO |

---

## Results

### Benchmark Winner (Median Fitness)

| Function | Winner |
|----------|----------|
| Sphere | PSO |
| Rastrigin | KPSA |
| Ackley | KPSA |
| Rosenbrock | KPSA |
| Griewank | PSO |
| Schwefel | PSO |
| Levy | KPSA |

### Median Fitness Comparison

| Function | KPSA | PSO |
|----------|---------:|---------:|
| Rastrigin | **50.31** | 104.02 |
| Ackley | **0.161** | 2.271 |
| Rosenbrock | **74.67** | 1017.60 |
| Levy | **4.74** | 8.67 |

### KPSA Win Rate

| Function | Win Rate |
|----------|---------:|
| Rastrigin | **90.0%** |
| Ackley | **83.3%** |
| Rosenbrock | **73.3%** |
| Levy | **63.3%** |

### Statistical Significance

Wilcoxon Signed-Rank Test:

| Function | p-value |
|----------|---------:|
| Rastrigin | 3.15×10⁻⁷ |
| Ackley | 5.14×10⁻⁶ |
| Rosenbrock | 5.55×10⁻⁴ |
| Levy | 8.71×10⁻³ |

The observed performance differences between KPSA and PSO were statistically significant across all tested benchmark functions.

---

## Key Findings

- KPSA outperformed PSO on **4 of 7 benchmark functions** based on median fitness.
- KPSA performed particularly well on **Rastrigin**, **Ackley**, **Rosenbrock**, and **Levy**.
- The crisis-driven paradigm shift mechanism helped the search escape stagnation and local optima.
- KPSA is not a universal optimizer and still underperforms PSO on Sphere, Griewank, and Schwefel.

---

## Status

🚧 **Research Prototype / Experimental Metaheuristic Algorithm** 🚧

KPSA is currently a proof-of-concept optimizer intended for experimentation and further research.

---

## Future Work

- Ablation study (without PSI, Crisis, Relocation)
- Comparison with GA, DE, GWO, and WOA
- Adaptive crisis thresholds
- Paradigm competition mechanism
- Hyperparameter optimization applications
- Real-world optimization problems

---

## References

Al-Tawaha, A., Cibaku, E., Park, S., Lavaei, J., & Jin, M. (2024). Distributed optimization and learning: A paradigm shift for power systems. *Annual Reviews*.

McEvoy-Halston, P. (2001). *Paradigm shift: An immodest proposal*. Philosophy 220.

Wang, Y., Afzal, M. M., Li, Z., Zhou, J., Feng, C., Guo, S., & Quek, T. Q. S. (2024). Large language model as a catalyst: A paradigm shift in base station siting optimization. *IEEE*.

Zakiah, A., Prihatmanto, A. S., Mahayana, D., & Andrea, R. (2024). The philosophy of smart learning using the approach Thomas Kuhn paradigm shift. *International Journal of Information Engineering and Electronic Business (IJIEEB)*, *16*(1), 54–62. https://doi.org/10.5815/ijieeb.2024.01.05

---

## Author

**Aufatir Diaul Haq**  
