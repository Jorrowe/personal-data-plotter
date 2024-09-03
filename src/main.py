import numpy as np
from Plotter import DataSet, Plotter


# SAMPLE CODE
intensity = np.array([100, 80, 60, 40, 20])
green_data = DataSet(intensity, [0.833, 0.828, 0.817, 0.804, 0.753], color=(0,1,0), marker="o-", label="green")
blue_data = DataSet(intensity, [1.469, 1.468, 1.468, 1.453, 1.425], color=(0,0,1), marker="o-", label="blue")
violet_data = DataSet(intensity, [1.646, 1.646, 1.642, 1.635, 1.590], color=(0.49803921568, 0, 1), marker="o-", label="violet")

plotter = Plotter(title="Stopping Voltage vs Intensity of Light", xlabel="Intensity (%)", ylabel="Stopping voltage (V)")
plotter.add_dataset([green_data, blue_data, violet_data])
plotter.set_limits((0, 110), (0,2.5))
plotter.plot_all()
plotter.show_plot()