import os

## Pfad anpassen
workspace_dir = "C:/Users/Pascal Gitz/OneDrive - Hochschule Luzern/Master/03_Tragverhalten_von_Stahlbetontragwerken/VM2"
os.chdir(workspace_dir)

## Einheiten
import sympy.physics.units as u
from sympycalcs import params_value, dict_to_table
import sympy as sp
sp.init_printing(use_latex="mathjax", latex_mode="equation", mat_symbol_style="bold")


## Numerische Berechnungen
import numpy as np
import scipy.integrate as integrate
from scipy.optimize import fsolve
import astropy.units as un

## Plotting und display

import matplotlib.pyplot as plt
from base.style.plotstyle import set_engineering_style  # Plotstyle
set_engineering_style()

## Printing
from IPython.display import Latex, Markdown

import matplotlib.pyplot as plt




# Parameter

params_kragarm = {
    'l_Kragarm':5*u.meter,
    'F1':-10000*u.N,
    'F2':-21500*u.N,
    'E':10000*u.N/u.mm**2,
    'h':400*u.mm,
    'b':200*u.mm,
    'k_1': 100000*u.N/u.meter,
    'k_2':10000*u.N/u.meter
}

params_value_kragarm = params_value(params_kragarm)



