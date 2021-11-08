class PyionUnit:
    def __init__(self, name, unit, value):
        self.name = name
        self.unit = unit
        self.value = value

    def __str__(self):
        return f"{self.name}({self.unit}): {self.value}"

    def c_to_k(self, temp):
        return temp + 273.15

#Temperature class, which is a subclass of PyionUnit

class Temperature(PyionUnit):
    def __init__(self, name, unit, value):
        super().__init__(name, unit, value)

    def c_to_k(self, temp):
        PyionUnit.c_to_k(self, temp)