import numpy as np
import matplotlib.pyplot as plt

g = 9.81
D = 0.01
rho0 = 1.25
beta = 0.000135

h, v = 120000.0, 7600.0
dt = 0.1
t_max = 280.0

t_hist = [0.0]
h_hist = [h]
v_hist = [v]
g_force = [0.0]

t = 0
crash_time = None

while t < t_max:
    rho = rho0 * np.exp(-beta * h)
    a_drag = 0.5 * D * rho * v**2

    dh_dt = -v
    dv_dt = g - a_drag

    h += dh_dt * dt
    v += dv_dt * dt
    t += dt

    if h <= 0:
        crash_time = t
        print(f"The spacecraft crashed the ground at t = {t:.1f} s!")
        break

    t_hist.append(t)
    h_hist.append(h)
    v_hist.append(v)
    g_force.append(a_drag / g)

fig, axes = plt.subplots(1, 3, figsize = (18, 5))

# Height
axes[0].plot(t_hist, h_hist, color = 'blue', linewidth = 2)
axes[0].set_title("Altitude vs Time")
axes[0].set_xlabel("Time (s)")
axes[0].set_ylabel("Altitude (m)")
axes[0].grid(True)

# Velocity
axes[1].plot(t_hist, v_hist, color = 'green', linewidth = 2)
axes[1].set_title("Velocity vs Time")
axes[1].set_xlabel("Time (s)")
axes[1].set_ylabel("Velocity (m/s)")
axes[1].grid(True)

# G-Force
axes[2].plot(t_hist, g_force, color = 'red', linewidth = 2)
axes[2].set_title("G-Force Load vs Time")
axes[2].set_xlabel("Time (s)")
axes[2].set_ylabel("G-Force (g)")
axes[2].grid(True)

if crash_time:
    for ax in axes:
        ax.axvline(x = crash_time, color = 'black', linestyle = '--', alpha = 0.5)

plt.tight_layout()
plt.show()