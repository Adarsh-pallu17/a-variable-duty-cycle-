import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# define circuit parameters
R = 10e3    # resistor value (ohms)
C = 1e-6    # capacitance value (F)

# define PWM duty cycles
duty_cycles = [0.25, 0.5, 0.75, 1.0]

# simulate circuit for each duty cycle
for duty_cycle in duty_cycles:
    # generate PWM signal
    f = 1000   # PWM frequency (Hz)
    T = 1/f    # PWM period (s)
    t = np.arange(0, 5*T, 1/(10*f))
    pwm = signal.square(2 * np.pi * f * t, duty=duty_cycle)

    # simulate circuit
    vout = signal.lfilter([1], [R*C, 1], pwm)

    # calculate expected analog voltage
    Vmax = 5    # maximum PWM voltage (V)
    Vavg = duty_cycle * Vmax
    Vout = Vavg * (1 - np.exp(-t/(R*C)))

    # plot results
    plt.plot(t, pwm, label='PWM')
    plt.plot(t, vout, label='LTSpice')
    plt.plot(t, Vout, '--', label='Expected')
    plt.xlabel('Time (s)')
    plt.ylabel('Voltage (V)')
    plt.title('Duty Cycle = ' + str(duty_cycle))
    plt.legend()
    plt.show()
