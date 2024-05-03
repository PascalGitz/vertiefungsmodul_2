# plot_style.py

import matplotlib.pyplot as plt
import numpy as np
import IPython

def set_engineering_style():
    plt.style.use('ggplot')  # Zurücksetzen auf den Matplotlib-Standardstil
    plt.rcParams['lines.linewidth'] = 0.7  # Linienstärke
    
    plt.rcParams['axes.grid'] = True  # Gitterlinien im Plot
    plt.rcParams['grid.color'] = 'lightgray'  # Grid Farbe
    plt.rcParams['grid.alpha'] = '1'  
    # plt.rcParams['grid.linestyle'] = 'dotted'  
    plt.rcParams['grid.linewidth'] = 0.2  # Gitterlinienstärke  
    
    
    plt.rcParams['axes.labelsize'] = 12  # Größe der Achsenbeschriftungen
    plt.rcParams['axes.titlesize'] = 14  # Größe des Plot-Titels
    plt.rcParams['axes.facecolor'] = 'white' # Hintergrund weiß
    plt.rcParams['axes.edgecolor'] = 'k' # Achsen schwarz
    plt.rcParams['axes.labelcolor'] = 'k' # Beschriftung schwarz
   
    plt.rcParams['axes.linewidth'] = 0.5 # Achsen schwarz
    plt.rcParams['axes.spines.right'] = False  # Achse rechts entfernt
    plt.rcParams['axes.spines.top'] = False  # Achse oben entfernt
    
    plt.rcParams['xtick.direction'] = 'in' # Teilstriche innerhalb des Plots
    plt.rcParams['xtick.color'] = 'k' 

    plt.rcParams['ytick.direction'] = 'in'
    plt.rcParams['ytick.color'] = 'k'

    plt.rcParams['xtick.labelsize'] = 10  # Größe der x-Achsenbeschriftungen
    plt.rcParams['ytick.labelsize'] = 10  # Größe der y-Achsenbeschriftungen
    plt.rcParams['legend.fontsize'] = 10  # Größe der Legende
    plt.rcParams['figure.figsize'] = (6.5, 2.5)  # Größe der Figur 6.5 Zoll entspricht der Standardbreite des scrbook latex types
    plt.rcParams.update({
        "font.family": "serif",
        "font.serif": ["Palatino Linotype"],
        "text.usetex": True,
        "font.size": 12,
    })

    plt.rcParams['figure.subplot.bottom'] = 0.2  # Abstand zwischen Plot und unterem Rand

    # creates the plots in Jupyter as svg
    IPython.display.set_matplotlib_formats('svg')