# Numerical-Trajectory-Iteration

### Background

In the final stretch of the space flight, from re-entering the Earth’s atmosphere to the final splashdown, one needs to solve Newton’s equations of motion with an approximately constant gravitational force, $F = -mg$ and a drag force from the air.

In the simplest possible case, assuming the spacecraft is dropped vertically downwards from orbit (This is not recommended in realistic situations. The graph below should give the reason.), the equations of motion for the altitude $h(t)$ and the downward velocity $v(t)$ of the space capsule can be approximated as a system of two coupled differential equations.

$$
\begin{aligned}
\frac{dh(t)}{dt} &= -v(t) \\
\frac{dv(t)}{dt} &= g - \frac{1}{2}D\rho_0e^{\beta h(t)}v(t)^2
\end{aligned}
$$

The first term in the equation for $\frac{dv(t)}{dt}$ describes the effect of the approximately constant gravitational force, the second term is the drag term. Here $g$ is the approximate gravitational acceleration, presumed constant over the trajectory, $D$ is a drag parameter, $\beta$ is an atmospheric scale
parameter, and $\rho_0$ is the sea-level atmospheric density.

Like many differential equations modelling physical systems, this equation does not possess a closed-form analytical solution. To solve it, numerical methods are needed. The simplest of those, is the Euler method, which approximates the differentials by finite small differences.

Here we take

$$
\begin{aligned}
\text{Gravitational acceleration: } &g = 9.81 \text{ m s}^{-2} \\
\text{Drag parameter: } &D = 0.01 \text{ m}^2 \text{ kg}^{-1} \\
\text{Sea-level atmospheric density: } &\rho_0 = 1.25 \text{ kg m}^{-3} \\
\text{Atmospheric scale factor: } &\beta = 0.000135 \text{ m}^{-1}
\end{aligned}
$$

$h_0 = h(0) = 120,000 \text{ m}$ \
$v_0 = v(0) = 7600 \text{ m s}^{-1}$

### Graph of Result

<img width="1709" height="567" alt="result" src="https://github.com/user-attachments/assets/9587d288-a541-4087-b5a8-766fa5bf3491" />

### Analysis Report

1. Evolution of Altitude and Velocity
   - High-Altitude Phase ($h \g 30$km): The spacecraft descends at an extremely high initial velocity of 7600 m/s. Because the atmospheric density $\rho = \rho_0 e^{-\beta h}$ decays exponentially, it is practically zero at this stage. Consequently, air drag is negligible. The velocity curve is almost horizontal (only slightly accelerated by gravity $g$), and the altitude decreases linearly.
   - Low-Altitude Transition Phase (dense atmosphere): When the spacecraft plummets into the dense atmosphere (roughly below 20-30 km) within a very short time, the atmospheric density surges. Since drag $F_d \propto \rho v^2$, the drag term instantly dominates, causing the velocity $v(t)$ to experience catastrophic cliff-edge drop (rapid deceleration).

2. Peak lethal G-Force\
   The cliff-edge drop in velocity implies an enormous deceleration.
   - By calculating $\frac{a_{drag}}{g}$, we observe a drastically steep spike in the G-force curve just before impact.
   - Without a buffering flight path angle, the simulated instantaneous deceleration peaks at en extreme value (typically reaching tens or even hundreds of $g$'s).

3. Problematic for the Capsule and Astronauts
   - Physiological Limits: the tolerance of a human body to sustained positive G-force is generally $5g ~ 10g$. If subjected to instantaneous deceleration of tens of $g$'s, blood is violently forced from the head to the lower extremities. This leads to cerebral ischemia, loss of vision, and loss of consciousness within seconds, potentially causing fatal internal organ rupture or hemorrhage.
   - Structural & Thermal Protections: Under such violent deceleration, the massive dynamic pressure ($q = \frac{1}{2}\rho v^2$) generates enormous aerodynamic stress, which would instantly disintegrate the capsule's hull. Furthermore, this extreme deceleration is accompanied by intense aerodynamic heating, which would incinerate the spacecraft instantly.

4. From a Numerical Perspective
   - Step-size Sensitivity: Because $\frac{dv}{dt}$ changes so violently in the peak region, using $Delta t = 0.1$s is necessary. If one uses a coarse step like $\Delta t = 1$s with the forward Euler method, the algorithm might easily "step over" the peak, resulting in an underestimated G-force and potentially yielding massive negative altitudes (tunneling).
   - The problem assumes a constant $g$. In reality, at an altitude of 120 km, the gravitational acceleration is less than at sea level. However, because the non-linear drag term $v^2$ is so overwhelmingly destructive in this model, the constant $g$ assumption does not change the overall conclusion (immediate crash).

### Conclusion

Vertical descent without lift is physically infeasible due to extreme peak deceleration. Real spacecraft require a shallow re-entry angle to spread the energy dissipation over a longer period.

















