# PID Object class
class PID(object):
    def __init__(self, Kp, Ki, Kd, dt):
        self.Kp, self.Ki, self.Kd = Kp, Ki, Kd
        self.dt = dt
        self.integral = 0

    def calculate(self, errors):
        integral_new = self.integral + self.Ki * (errors[-1]) * self.dt
        self.integral = integral_new
        derivative = self.Kd * (errors[-1] - errors[-2])/self.dt
        proportional = self.Kp * errors[-1]
        return integral_new, proportional, derivative
