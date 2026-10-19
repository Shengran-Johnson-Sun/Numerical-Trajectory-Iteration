# Numerical-Trajectory-Iteration
In the final stretch of the space flight, from re-entering the Earth’s atmosphere to the final splashdown, one needs to solve Newton’s equations of motion with an approximately constant gravitational force, $F = -mg$ and a drag force from the air.\
In the simplest possible case, assuming the spacecraft is dropped vertically downwards from orbit (This is not recommended in realistic situations. The graph below should give the reason.), the equations of motion for the altitude $h(t)$ and the downward velocity $v(t)$ of the space capsule can be approximated as a system of two coupled differential equations.\
$$
\begin{aligned}
\frac{dh(t)}{dt} &= -v(t) \\
\frac{dv(t)}{dt} &= g - \frac{1}{2}D\rho_0e^{\beta h(t)}v(t)^2
\end{aligned}
$$
The first term in the equation for $\frac{dv(t)}{dt}$ describes the effect of the approximately constant gravitational force, the second term is the drag term. Here $g$ is the approximate gravitational acceleration, presumed constant over the trajectory, $D$ is a drag parameter, $\beta$ is an atmospheric scale
parameter, and $\rho_0$ is the sea-level atmospheric density.\
Like many differential equations modelling physical systems, this equation does not possess a closed-form analytical solution. To solve it, numerical methods are needed. The simplest of those, is the Euler method, which approximates the differentials by finite small differences.\
Here we take\
Gravitational acceleration: $g = 9.81 \text{ m s}^{-2}$ \
Drag parameter: $D = 0.01 \text{ m}^2 \text{ kg}^{-1}$ \
Sea-level atmospheric density: $\rho_0 = 1.25 \text{ kg m}^{-3}$ \
Atmospheric scale factor: $\beta = 0.000135 \text{ m}^{-1}$ \
$h_0 = h(0) = 120,000 \text{ m}$ \
$v_0 = v(0) = 7600 ms^{-1}$ \
Here is the graph of result:
<img width="1709" height="567" alt="result" src="https://github.com/user-attachments/assets/9587d288-a541-4087-b5a8-766fa5bf3491" />
