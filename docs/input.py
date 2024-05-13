import os
import pandas as pd


## Pfad anpassen

os.chdir(os.path.join(os.getcwd(),".."))

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
from numpy import sqrt, pi, tan, arctan, cos, sin, arccos, arcsin

# Unit handling
from pint import UnitRegistry

ureg = UnitRegistry()
ureg.default_format = "~P"

kg = ureg.kg

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
from scipy.ndimage import gaussian_filter
from scipy.optimize import curve_fit

import handcalcs.render

## Plotting und display

import matplotlib.pyplot as plt
from base.style.plotstyle import set_engineering_style  # Plotstyle
set_engineering_style()

## Printing
from IPython.display import Latex, Markdown

import matplotlib.pyplot as plt


