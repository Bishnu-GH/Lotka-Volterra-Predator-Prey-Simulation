# 🐇🦊 Lotka–Volterra Predator–Prey Model

This project implements the **Lotka–Volterra model**, a system of first-order non-linear differential equations that describe the dynamics of two interacting species in an ecosystem:

- **Prey** (e.g., rabbits 🐇)
- **Predator** (e.g., foxes 🦊)

It simulates how these populations change over time and influence each other through a predator–prey relationship.

---

## 📘 Problem Statement

We solve the following system of coupled differential equations:


dx/dt = α · x − β · x · y  
dy/dt = −γ · y + δ · x · y

Where:

| Symbol | Meaning                          |
|--------|----------------------------------|
| `x`    | Number of prey (rabbits)         |
| `y`    | Number of predators (foxes)      |
| `α`    | Growth rate of prey              |
| `β`    | Rate at which predators eat prey |
| `γ`    | Death rate of predators          |
| `δ`    | Reproduction rate of predators   |

---

## 🔧 Parameters

The model uses the following constants:

- α = 1.5  
- β = 1  
- γ = 3  
- δ = 1  

### Initial Conditions:

- Rabbits (`x`) = 10  
- Foxes (`y`) = 4  

---

## 📊 Output

The simulation generates:

- A **time series plot** of both rabbit and fox populations
- A **phase-space plot** showing the relationship between predator and prey over time

---


