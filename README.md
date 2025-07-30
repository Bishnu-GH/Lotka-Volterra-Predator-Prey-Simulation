# 🐇🦊 Lotka-Volterra Predator-Prey Model

This project implements the **Lotka–Volterra model**, a set of first-order non-linear differential equations that describe the dynamics between two interacting species in an ecosystem:

- **Prey** (e.g., rabbits 🐇)
- **Predator** (e.g., foxes 🦊)

The model simulates how these populations evolve over time and how they influence each other's growth and decline.

---

## 📘 Problem Statement

Solve the following system of coupled differential equations:

$$
\frac{dx}{dt} = \alpha x - \beta x y
$$
\[
\frac{dy}{dt} = -\gamma y + \delta x y
\]

Where:

| Variable | Meaning                          |
|----------|----------------------------------|
| \( x \)  | Number of prey (rabbits)         |
| \( y \)  | Number of predators (foxes)      |
| \( \alpha \) | Growth rate of prey (rabbits)     |
| \( \beta \)  | Rate at which predators destroy prey |
| \( \gamma \) | Death rate of predators            |
| \( \delta \) | Reproduction rate of predators by consuming prey |

---

## 🔧 Parameters

- \( \alpha = 1.5 \)
- \( \beta = 1 \)
- \( \gamma = 3 \)
- \( \delta = 1 \)

### Initial Conditions:

- Number of rabbits: **10**
- Number of foxes: **4**

---

## 📊 Output

The simulation provides:
- **Time series plot** of both prey and predator populations.
- **Phase-space plot** showing the relationship between rabbit and fox populations over time.

---

## 📂 Files

- `lotka_volterra.py` – Python script implementing the model and plotting the results.
- `README.md` – This file.

---

## ▶️ How to Run

```bash
python lotka_volterra.py
