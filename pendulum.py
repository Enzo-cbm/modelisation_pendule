import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# time grid
t = np.arange(0, 20, 0.1)

# physical parameters
g = 9.81
m = 1
k = 40
l0 = 1

# initial conditions [l, theta, dl/dt, dtheta/dt]
c_i = [l0, 3*np.pi/4, 0, 0]


def derive(t, ci, g, m, k, l0):

    l, theta, d_l, d_theta = ci

    d2_theta = -(1/l) * (g*np.sin(theta) + 2*d_theta*d_l)
    d2_l = (1/m) * (m*l*(d_theta)**2 - k*(l - l0) + m*g*np.cos(theta))

    return [d_l, d_theta, d2_l, d2_theta]


# numerical integration
sol = solve_ivp(
    derive,
    y0=c_i,
    t_span=(0, 20),
    t_eval=t,
    args=(g, m, k, l0)
)


# cartesian coordinates
cx = sol.y[0] * np.sin(sol.y[1])
cy = -sol.y[0] * np.cos(sol.y[1])


# position vs time
fig, ax = plt.subplots(1, 2, figsize=(16, 8))

ax[0].plot(sol.t, cx)
ax[0].grid()
ax[0].set(xlabel="time", ylabel="x", title="x(t)")

ax[1].plot(sol.t, cy)
ax[1].grid()
ax[1].set(xlabel="time", ylabel="y", title="y(t)")


# trajectory
fig, ax = plt.subplots(figsize=(8, 8))
ax.plot(cx, cy)
ax.set(xlabel="x", ylabel="y", title="trajectory")


# energies
U = -m*g*sol.y[0]*np.cos(sol.y[1]) + 0.5*k*(sol.y[0]-l0)**2
T = 0.5*m*(sol.y[2]**2 + (sol.y[0]*sol.y[3])**2)

energy_total = U + T

energy_initial = (
    -m*g*c_i[0]*np.cos(c_i[1])
    + 0.5*k*(c_i[0]-l0)**2
    + 0.5*m*(c_i[2]**2 + (c_i[0]*c_i[3])**2)
)

plt.figure(figsize=(16, 8))

plt.plot(sol.t, U, label="potential energy")
plt.plot(sol.t, T, label="kinetic energy")

plt.legend()
plt.grid()


plt.figure()

plt.plot(sol.t, energy_total - energy_initial)
plt.grid()
plt.title("energy conservation error")


# multiple simulations
nb_simul = 1000
results = np.empty((nb_simul, 2, len(t)))

for i in range(nb_simul):

    c_i[1] = np.random.uniform(0, np.pi/2)

    sol_bis = solve_ivp(
        derive,
        y0=c_i,
        t_span=(0, 20),
        t_eval=t,
        args=(g, m, k, l0)
    )

    results[i, 0] = sol_bis.y[0] * np.sin(sol_bis.y[1])
    results[i, 1] = -sol_bis.y[0] * np.cos(sol_bis.y[1])


# phase-space exploration
plt.figure(figsize=(8, 8))

plt.hist2d(*np.concatenate(results, axis=1), bins=100)

plt.axis("image")
plt.xlabel("x [m]")
plt.ylabel("y [m]")

plt.colorbar()

plt.show()
