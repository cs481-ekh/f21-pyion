from src.pyion.objects.PyionUnit import PyionUnit
from tabulate import tabulate
from src.pyion.objects.PyionUnit import Temperature

def classChecker(self):
    if isinstance(self, (PyionUnit, Temperature)) is True:
        return True

    return False


class PyionData:
    def __init__(self):
        self.voltage = PyionUnit("Voltage", "mV", [])
        self.ci = PyionUnit("Ci", "mM", [])
        self.vi = PyionUnit("Vi", "uL", [])
        self.cs = PyionUnit("Cs", "mM", [])
        self.v_add = PyionUnit("Volume Added", "uL", [])
        self.temp = PyionUnit("Temperature", "C", [])

    def add_entry(self, var_name: str, name: str, unit: str, value) -> None:
        self.__dict__[var_name] = PyionUnit(name, unit, value)

    def create_table(self):
        data_fmt = {}
        for k in self.__dict__.keys():
            v = self.__dict__[k]
            if classChecker(v) is True:
                data_fmt[f"{v.name}({v.unit})"] = v.value if type(v.value) is list else [v.value]
        return tabulate(data_fmt, headers="keys")