from src.pyion.objects.PyionUnit import *
import matplotlib.pyplot as plt
import numpy as np


def graph_single(data_source: PyionUnit) -> None:
    if data_source is None:
        raise Exception("Data source cannot be null.")
    if type(data_source.value) is not list:
        raise Exception("Data source must be a list and not a single value.")

    t = np.arange(1, len(data_source.value)+1, 1)
    s = data_source.value
    plt.plot(t, s, 'bo')
    plt.title(f"{data_source.name} Graphed Over {len(data_source.value)} Iterations")
    plt.xlabel("Iterations")
    plt.xticks(t)
    plt.ylabel(f"{data_source.name}({data_source.unit})")
    plt.show()
