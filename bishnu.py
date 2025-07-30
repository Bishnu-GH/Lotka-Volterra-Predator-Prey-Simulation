# Imported necessary libraries
import numpy as np                      # For numerical operations like linspace and arrays
import matplotlib.pyplot as plt         # For plotting graphs
from scipy.integrate import odeint      # For solving ordinary differential equations numerically

# Defined constants for the Lotka-Volterra model
alpha = 1.5   # Growth rate of prey (e.g., rabbits)
beta = 1      # Rate at which predators consume prey
gamma = 3     # Death rate of predators (e.g., foxes)
delta = 1     # Reproduction rate of predators per prey eaten

# Defined the system of differential equations
def f(popu, t):
    x, y = popu                          # x = prey population, y = predator population
    dxdt = alpha * x - beta * x * y     # Rate of change of prey
    dydt = -gamma * y + delta * x * y   # Rate of change of predators
    return [dxdt, dydt]                 # Returned the rate of changes as a list

# Set initial populations of prey and predators
ini_population = [5, 5]                 # Starting with 5 rabbits and 5 foxes

# Created a time array from 0 to 10 with 500 points
time = np.linspace(0, 10, 500)

# Solved the differential equations using odeint
t = odeint(f, ini_population, time)     # t[:, 0] = prey values, t[:, 1] = predator values

# Plotted population vs. time
plt.figure(1)                           # Created the first figure
plt.plot(time, t[:, 0], label="Rabbit") # Plotted prey (rabbit) population over time
plt.plot(time, t[:, 1], label="Fox")    # Plotted predator (fox) population over time
plt.xlabel("Time")                      # X-axis label
plt.ylabel("Population")                # Y-axis label
plt.legend()                            # Added legend
plt.show()                              # Displayed the time vs. population plot

# Plotted the phase-space diagram (Prey vs Predator)
plt.figure(2)                           # Created the second figure
plt.plot(t[:, 0], t[:, 1])              # Plotted predator population vs. prey population
plt.xlabel("Rabbits")                   # X-axis label
plt.ylabel("Foxes")                     # Y-axis label
plt.title("Phase-Space Plot")           # Added plot title
plt.show()                              # Displayed the phase-space plot
