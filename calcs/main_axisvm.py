from axisvm.com.client import start_AxisVM
import axisvm.com.tlb as axtlb
import numpy as np

from polymesh.grid import grid
from polymesh import PolyData, PointData, CartesianFrame
from polymesh.cells import Q4 as CellData


# Starting AxisVM
axvm = start_AxisVM(visible=True, join=True, daemon=True)

# Creating a Model
modelId = axvm.Models.New()
model = axvm.Models[modelId]

axtlb.RPoint3d(0,0,0)
# Creating a grid rect in 2d
nodes_gridparams = {
    'size' : (5,8),
    'shape': (10,10),
    'eshape':(2,2),
    'path':[0,2,3,1]
}

def creating_structure(gridparams: dict = {
    'size' : (500,500),
    'shape': (20,20),
    'eshape':(2,2),
    'path':[0,2,3,1]
}):
    coords, topo = grid(**gridparams)
    # the `grid` function creates a 2d mesh in the x-y plane,
    # but we want a 3d mesh, with zero values for the z axis.
    coords = np.pad(coords, ((0, 0), (0, 1)), mode='constant')

    # create the nodes
    add_nodes = model.Nodes.Add
    list(map(lambda c: add_nodes(*c), coords))
    # # create the lines between    
    add_lines = model.Lines.Add
    GeomType = axtlb.lgtStraightLine
    list(map(lambda x: add_lines(x[0],x[1], GeomType), topo))
    list(map(lambda x: print(x[0],x[1]), topo+1))

creating_structure(nodes_gridparams)
