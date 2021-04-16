# motor object class
class Motor(object):
    def __init__(self, R, L, B, Kt, J, Kb, dt):
        self.R, self.L, self.B, self. Kt, self.J, self.Kb = R, L, B, Kt, J, Kb
        self.dt = dt
        self.outputs = [0, 0]  # stores outputs of the motor

    # updates the output with the pid output
    def update(self, v):
        output_now = (v + (self.L * self.B * self.outputs[-1] / self.dt / self.Kt) + (self.L * self.J * (2 * self.outputs[-1] - self.outputs[-2]) / self.Kt / (self.dt ** 2))+(
            self.R * self.J * self.outputs[-1] / self.Kt)) / ((self.L * self.B / self.dt / self.Kt) + (self.L * self.J / self.Kt / (self.dt**2))+(self.R * (self.B + self.J) / self.Kt) - self.Kb)
        self.outputs.append(output_now)

    def get_outputs(self):
        return self.outputs[2:]
