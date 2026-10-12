---
title: "How Quickly Does Current Change When You Apply a Voltage?"
description: "Deriving the step response of a series RL circuit, separating time constant from initial slope, and relating the result to PMSM current control."
categories: ["Motor Control & Power Electronics", "Motor Drives"]
tags: [RL Circuit, Circuit Theory, Current Control]
math: true
toc: true
published: false
---

> From RL circuits to PMSM current control · Part 1

Before controlling motor current, it helps to understand what happens when the applied voltage changes. With a resistor alone, Ohm's law relates voltage and current directly. Add an inductor, and we also have to account for **how quickly the current changes**.

We'll start with a simple series RL circuit driven by a constant voltage. Rather than just quoting the step-response equation, I want to separate two different meanings of a "fast" current response: the initial rate of change and the time it takes to approach the final value. Then we'll see how far this simple model carries over to PMSM current control.

## 1. How does an inductor oppose changes in current?

For an ideal linear inductor, voltage is proportional to the rate of change of current.

$$
v_L(t)=L\frac{di(t)}{dt}
$$

With the same voltage across an inductor, a larger inductance gives a smaller rate of change of current. An inductor carrying finite current cannot change that current instantaneously under a finite applied voltage. That doesn't mean the current waits before moving: its slope can change as soon as the voltage changes.

The entire supply voltage isn't necessarily across the inductor, either. Some of it drops across the series resistor. As current rises, that resistive drop grows. This is why the response is exponential rather than a straight line.

## 2. Defining the circuit and its variables

Consider a voltage source, resistor, and inductor connected in series. For $$ t=0 $$ onward, the source holds a constant voltage $$ V $$. The initial current $$ I_0 $$ comes from the preceding operating condition and remains continuous at the switching instant. If $$ I_0=0 $$, we have the familiar case of applying a DC voltage step to an initially unenergized circuit.

| Symbol | Meaning | SI unit |
| --- | --- | --- |
| $$ t $$ | Time since the voltage step | s |
| $$ V $$ | Constant applied voltage after the step | V |
| $$ i(t) $$ | Series current | A |
| $$ I_0 $$ | Initial current, $$ i(0^+)=i(0^-) $$ | A |
| $$ R $$ | Series resistance | Ω |
| $$ L $$ | Inductance | H |

Assume positive, constant resistance and inductance: $$ R>0,\;L>0 $$. We'll ignore saturation, parasitic capacitance, and temperature changes. Taking the passive sign convention for both elements, Kirchhoff's voltage law gives

$$
V=Ri(t)+L\frac{di(t)}{dt}
$$

You can find the same governing equation and step response in [MIT 8.022 Lecture 16 on RL circuits](https://ocw.mit.edu/courses/8-022-physics-ii-electricity-and-magnetism-fall-2004/7b7348480e71d4b842dbc339543bd513_lecture16.pdf).

Rearranging makes the current slope easier to interpret:

$$
\frac{di(t)}{dt}=\frac{V-Ri(t)}{L}
$$

The inductor gets whatever voltage is left after the resistor's drop. With zero initial current and a positive supply voltage, it initially sees the full supply voltage. As the current builds, the resistive drop increases, reducing the slope.

It's worth checking the units:

$$
\frac{\mathrm{V}}{\mathrm{H}}
=\frac{\mathrm{V}}{\mathrm{V}\cdot\mathrm{s}/\mathrm{A}}
=\frac{\mathrm{A}}{\mathrm{s}}
$$

Voltage divided by inductance gives a rate of change of current, not current itself. Since the inductor current is the only state and its behavior follows a first-order differential equation, this is a **first-order circuit**.

## 3. Solving for any initial current

If we hold the voltage long enough for the current to settle, the derivative goes to zero. The steady-state current is therefore

$$
I_\infty=\frac{V}{R}
$$

Define the error from the final value as $$ x(t)=i(t)-I_\infty $$. Substituting this into the original equation removes the constant term:

$$
L\frac{dx(t)}{dt}=-Rx(t)
$$

The larger this error, the faster it decays. The solution is exponential, with initial condition $$ x(0)=I_0-I_\infty $$.

$$
x(t)=(I_0-I_\infty)e^{-Rt/L}
$$

Substituting back gives the general current response:

$$
\boxed{
i(t)=\frac{V}{R}
+\left(I_0-\frac{V}{R}\right)e^{-t/\tau},
\qquad
\tau=\frac{L}{R},
\qquad t\geq 0
}
$$

This is the final current plus the remaining difference from the initial condition. Current rises if it starts below the final value, falls if it starts above it, and stays constant if the two match. A positive applied voltage does not, by itself, guarantee that current will rise.

The familiar zero-initial-current response is just a special case:

$$
i(t)=\frac{V}{R}\left(1-e^{-t/\tau}\right)
$$

## 4. Time constant versus initial slope

The time constant $$ \tau=L/R $$ has units of seconds. If the initial and final currents differ, then after one time constant, the remaining error is $$ e^{-1}\approx 0.368 $$ of its starting value.

$$
i(\tau)-I_\infty=(I_0-I_\infty)e^{-1}
$$

In other words, the current has covered about 63.2% of the distance between its initial and final values. Even after five time constants, about 0.674% of the error remains. The time constant describes the **fraction** of the error that disappears, not the absolute time to reach an arbitrary current target.

We can get the initial slope directly from the differential equation:

$$
\left.\frac{di}{dt}\right|_{0^+}=\frac{V-RI_0}{L}
$$

If the initial current is zero, this simplifies to

$$
\left.\frac{di}{dt}\right|_{0^+}=\frac{V}{L}
$$

Notice that resistance disappears. **For fixed voltage and inductance with zero initial current, increasing resistance does not change the initial slope.** At that instant there is no resistive voltage drop. For nonzero initial current, resistance does affect the slope.

Here's a numerical example, not a measurement from a motor. We'll keep the voltage at 12 V, inductance at 2 mH, and initial current at 0 A.

| Resistance | Time constant | Final current | Initial slope | Current at 1 ms |
| --- | --- | --- | --- | --- |
| 1 Ω | 2 ms | 12 A | 6 A/ms | About 4.722 A |
| 2 Ω | 1 ms | 6 A | 6 A/ms | About 3.793 A |

The 2 Ω circuit approaches its own final value with a shorter time constant. Yet its absolute current after 1 ms is smaller. If the target is 8 A, the second circuit can never reach it under this supply voltage because its steady-state current is only 6 A.

So "more resistance makes current respond faster" is incomplete. We need to say whether we're comparing time constants, initial slopes, or the time to reach the same current target.

## 5. What carries over to PMSM current control?

In a PMSM, we represent three-phase currents using d- and q-axis components in a reference frame rotating with the rotor. These components are not currents flowing through two separate physical windings. They're a coordinate transformation of the same three-phase currents.

Assume sinusoidal flux distribution, balanced three-phase operation, and constant motor parameters. Ignoring the zero-sequence component, the electrical model becomes the following. We'll use the voltage and Park-transform conventions from the [MathWorks PMSM documentation](https://www.mathworks.com/help/simscape-electrical/ref/pmsm.html).

$$
\begin{aligned}
v_d &= R_s i_d+L_d\frac{di_d}{dt}-\omega_e L_q i_q,\\
v_q &= R_s i_q+L_q\frac{di_q}{dt}
       +\omega_e(L_d i_d+\psi_f).
\end{aligned}
$$

Here, $$ R_s $$ is stator resistance, and $$ L_d,L_q $$ are the d- and q-axis inductances. The permanent-magnet flux linkage $$ \psi_f $$ is measured in Wb. The electrical angular speed is $$ \omega_e $$; for $$ p $$ pole pairs, $$ \omega_e=p\omega_m $$. Both angular speeds are in rad/s.

Each equation has the familiar resistive and inductive terms, but also speed-dependent cross-coupling and, on the q axis, permanent-magnet back EMF. A constant applied voltage therefore does not generally produce the simple RL step response derived above.

At standstill, where electrical speed remains zero, the speed-dependent terms vanish. During rotation, suppose we could calculate and cancel the cross-coupling and back-EMF terms perfectly. We could then treat each remaining axis as an RL system. Calling the compensated inputs $$ u_d,u_q $$ gives

$$
L_d\frac{di_d}{dt}+R_s i_d=u_d,
\qquad
L_q\frac{di_q}{dt}+R_s i_q=u_q
$$

For zero initial current, the Laplace-domain voltage-to-current transfer functions are

$$
G_d(s)=\frac{I_d(s)}{U_d(s)}=\frac{1}{L_d s+R_s},
\qquad
G_q(s)=\frac{I_q(s)}{U_q(s)}=\frac{1}{L_q s+R_s}
$$

Here $$ s $$ is the Laplace variable. The [Imperix note on PMSM field-oriented control](https://imperix.com/doc/implementation/field-oriented-control-of-pmsm) also discusses the RL axis models and decoupling terms.

The d- and q-axis inductances need not be equal. A real drive also has mechanical dynamics, inverter PWM, voltage limits, sampling and computation delays, and parameter uncertainty. The $$ L/R $$ value here is the time constant of the simplified plant, not the closed-loop response time after adding a PI controller.

## 6. Comparing the analytical result with NumPy

The code below reproduces the two resistance cases. It calculates the exact solution and integrates the differential equation using forward Euler. The integration step is one-thousandth of each circuit's time constant. You only need Python and NumPy to run it.

```python
import numpy as np

V = 12.0       # V
L = 2e-3       # H
I0 = 0.0       # A


def current_exact(t, R, initial_current):
    t = np.asarray(t)
    i_inf = V / R
    return i_inf + (initial_current - i_inf) * np.exp(-R * t / L)


for R in (1.0, 2.0):
    tau = L / R
    i_inf = V / R
    t = np.linspace(0.0, 5.0 * tau, 5001)
    dt = t[1] - t[0]

    i_exact = current_exact(t, R, I0)
    i_euler = np.empty_like(t)
    i_euler[0] = I0
    for k in range(len(t) - 1):
        i_euler[k + 1] = i_euler[k] + dt * (V - R * i_euler[k]) / L

    max_error = np.max(np.abs(i_euler - i_exact))
    assert np.isclose(i_exact[0], I0)
    assert np.isclose(
        current_exact(tau, R, I0) - i_inf,
        (I0 - i_inf) / np.e,
    )
    assert max_error < 1e-3 * max(1.0, abs(I0 - i_inf))

    slope0 = (V - R * I0) / L
    print(
        f"R={R:.0f} ohm, tau={tau * 1e3:.1f} ms, "
        f"i_inf={i_inf:.1f} A, slope0={slope0 / 1e3:.1f} A/ms, "
        f"i(1 ms)={current_exact(1e-3, R, I0):.3f} A, "
        f"max_error={max_error:.6f} A"
    )
```

It prints the same time constants, final currents, initial slopes, and 1 ms currents as the table. At this step size, the maximum Euler errors relative to the analytical solution are about 0.002208 A and 0.001104 A, respectively. This checks a numerical approximation against an analytical solution; it is not validation on an actual motor.

Before changing the code, try predicting what will happen in three cases:

1. With **I0 = 3.0**, do both resistance cases still have the same initial slope?
2. With **I0 = 15.0**, can current decrease even with positive applied voltage?
3. With **V = 0.0** and **I0 = 3.0**, how do the stored energy and current decay?

If the results surprise you, go back to the initial condition, final current, and signs in the differential equation. Next, we'll look at the transfer function and frequency response before moving on to PI current control.
