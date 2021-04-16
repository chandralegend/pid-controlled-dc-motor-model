import numpy as np
import matplotlib.pyplot as plt
from motor import Motor
from pid import PID


# reference input function
def input_function(t):
    rpm = np.sin(1e-2*t**2 + 1e-3*t + 1)
    return rpm


'''Motor Parameters'''
R = 1  # Resistance (Ohms)
L = 0.35  # Inductance (H)
J = 0.02  # Inertia of the Motor (kgm2)
B = 0.3  # Friction Coefficent of the Motor
Kb = 0.02  # Feedback constant
Kt = 0.1  # Motor Constant
dt = 0.001  # sampling rate

'''PID Parameters'''
Kp = 200
Ki = 60
Kd = 20


if __name__ == '__main__':
    time = []  # time
    speed_rad = []  # reference speed
    errors = [0]  # keep track of errors

    motor = Motor(R, L, B, Kt, J, Kb, dt)  # initialize the motor
    pid = PID(Kp, Ki, Kd, dt)  # initial the PID Controller

    for t in np.arange(dt, 100, dt):
        time.append(t)
        ref_rpm = input_function(t)
        ref_rad = ref_rpm / 9.549297  # rpm to rad conversion
        speed_rad.append(ref_rad)

        error_now = ref_rad - motor.outputs[-1]  # calculating the error
        errors.append(error_now)

        integral, derivative, proportional = pid.calculate(errors)
        v = integral + derivative + proportional
        motor.update(v)

    plt.plot(time, speed_rad, label="Reference",
             color='blue')
    plt.plot(time, motor.get_outputs(), label="Output", color='red')
    plt.xlabel('Time(s)')
    plt.ylabel('Speed (rads-1)')
    plt.legend()
    plt.grid()
    plt.show()
