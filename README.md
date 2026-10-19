# Numerical-Trajectory-Iteration
In the final stretch of the space flight, from re-entering the Earth’s atmosphere to the final splashdown, one needs to solve Newton’s equations of motion with an approximately constant gravitational force, $F = −mg$ and a drag force from the air.\
In the simplest possible case, assuming the spacecraft is dropped vertically downwards from orbit (This is not recommended in realistic situations. The graph below should give the reason.), the equations of motion for the altitude $h(t)$ and the downward velocity $v(t)$ of the space capsule can be approximated as a system of two coupled differential equations.\
$$
\frac{dh(t)}{dt} = -v(t) \\
\frac{dv(t)}{t} = g - \frac{1}{2}D\rho_0e^{\beta h(t)}v(t)^2
$$
