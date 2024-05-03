import os
import pandas as pd


## Pfad anpassen
workspace_dir = "/Users/pascalgitz/Library/CloudStorage/OneDrive-HochschuleLuzern/Master/03_Tragverhalten_von_Stahlbetontragwerken/VM2"
os.chdir(workspace_dir)

## Einheiten
# from sympycalcs import to_float, to_convert, dict_to_table, display_eq, to_dict, to_subs
import sympy as sp



# Kräfte
# setattr(unit, "kilonewton", unit.Quantity("kilonewton", abbrev="kN", is_prefixed=True))
# setattr(unit, "kN", getattr(unit, "kilonewton"))
# getattr(unit, "kilonewton").set_global_relative_scale_factor(unit.kilo, unit.newton)
sp.init_printing(use_latex="mathjax", latex_mode="equation*", mat_symbol_style="bold")


## Numerische Berechnungen
import numpy as np

# numeric operations
from numpy import sqrt, pi, tan

# Unit handling
from pint import UnitRegistry

ureg = UnitRegistry()
ureg.default_format = "~P"

mm = ureg.mm
cm = ureg.cm
dm = ureg.dm
m = ureg.m
km = ureg.km

N = ureg.N
kN = ureg.kN
MN = ureg.MN

rad = ureg.rad
deg = ureg.degree

percent = ureg.percent
s = ureg.s

MPa = ureg.MPa
los = ureg.dimensionless



import scipy.integrate as integrate
from scipy.optimize import fsolve
from scipy.misc import derivative
import handcalcs.render

## Plotting und display

import matplotlib.pyplot as plt
from base.style.plotstyle import set_engineering_style  # Plotstyle
set_engineering_style()

## Printing
from IPython.display import Latex, Markdown

import matplotlib.pyplot as plt




# # Parameter

# params_kragarm = {
#     'l_Kragarm':5*unit.meter,
#     'F1':-10000*unit.N,
#     'F2':-21500*unit.N,
#     'E':10000*unit.N/unit.mm**2,
#     'h':400*unit.mm,
#     'b':200*unit.mm,
#     'k_1': 100000*unit.N/unit.meter,
#     'k_2':10000*unit.N/unit.meter,
#     'z': 400*unit.mm,
# }

# params_value_kragarm = to_float(params_kragarm)

# params_a3v2 = {
#     'l':2.62*unit.meter, 
#     'F_max':-320*unit.kN, 
#     'l_spring':2.*unit.mm,
# }

# params_value_a3v2 = to_float(params_a3v2)


