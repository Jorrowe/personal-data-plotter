import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class DataSet:
    def __init__(self, x, y, filepath="", sheet_name="", marker="o", point_size=5, color=(0,0,0), label="plot", x_errors=(0), y_errors=(0)):
        self.x = self.load_data(x, filepath, sheet_name)
        self.y = self.load_data(y, filepath, sheet_name)
        self.sheet_name = sheet_name
        self.marker = marker
        self.point_size = point_size
        self.color = color
        self.label = label
        self.x_errors = self.load_data(x_errors, filepath, sheet_name)
        self.y_errors = self.load_data(y_errors, filepath, sheet_name)

    def load_data(self, data, filepath="", sheet_name=""):
        if (isinstance(data, str)):
            if ("google" in filepath):
                return self.load_data_from_google_sheets(data, filepath, sheet_name)
            else:
                return self.load_data_from_excel(data, filepath, sheet_name)
        else:
            return np.array(data)

    def load_data_from_excel(self, data, filepath, sheet_name):
        df = pd.read_excel(filepath, sheet_name)
        return df[data].values

    def load_data_from_google_sheets(self, data, link, sheet_name=""):
        sheet_id = link.split("/")[5]
        df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv")
        return df[data].values

    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y

    def get_x_errors(self):
        return self.x_errors
    
    def get_y_errors(self):
        return self.y_errors

    def get_marker(self):
        return self.marker
    
    def get_point_size(self):
        return self.point_size

    def get_color(self):
        return self.color

    def get_label(self):
        return self.label


class Plotter:
    def __init__(self, title="y vs x", xlabel="x", ylabel="y"):
        self.datasets = []
        self.fig, self.ax = plt.subplots()
        self.title = title
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.xlim = None
        self.ylim = None

    def add_dataset(self, dataset):
        if (isinstance(dataset, list)):
            self.datasets.extend(dataset)
        else:
            self.datasets.append(dataset)

    def plot_all(self):
        for dataset in self.datasets:
            x_data = dataset.get_x()
            y_data = dataset.get_y()
            xerr = dataset.get_x_errors()
            yerr = dataset.get_y_errors()
            marker = dataset.get_marker()
            point_size = dataset.get_point_size()
            color = dataset.get_color()
            label = dataset.get_label()
            plt.plot(x_data, y_data, marker, markersize=point_size, c=color, label=label)
            plt.errorbar(x_data, y_data, xerr=xerr, yerr=yerr, ecolor=color, fmt='none')

    def show_plot(self):
        self.ax.set_title(self.title)
        self.ax.set_xlabel(self.xlabel)
        self.ax.set_ylabel(self.ylabel)
        self.ax.set_xlim(self.xlim)
        self.ax.set_ylim(self.ylim)
        self.ax.legend()
        plt.show()

    def set_title(self, title):
        self.title = title

    def set_xlabel(self, xlabel):
        self.xlabel = xlabel

    def set_ylabel(self, ylabel):
        self.ylabel = ylabel

    def set_limits(self, xlim, ylim):
        self.xlim = xlim
        self.ylim = ylim


class CurveFitter:
    pass

