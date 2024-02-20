# the size of the grid
Lx, Ly, Lz = 10., 2.0, 1.0

# these control subdivision
# set these higher if you want more lines in the same space
nx, ny, nz = 4, 2, 2

# data of a CHS section
D = 0.1  # outer diameter of the tube in m
t = 0.05  # thickness of the tube in m

# value of the concentrated force at the free end in kN
# and the number of load cases to generate
F = 1.0
nCase = 5



from polymesh.space import StandardFrame, PointCloud
from polymesh.grid import gridH8 as grid
from polymesh.utils.topology.tr import H8_to_L2
import numpy as np

# mesh
gridparams = {
    'size': (Lx, Ly, Lz),
    'shape': (nx, ny, nz),
    'origo': (0, 0, 0),
    'start': 0
}

# create a grid of hexagonals
coords, topo = grid(**gridparams)

# turn the hexagonal mesh into lines
coords, topo = H8_to_L2(coords, topo)

GlobalFrame = StandardFrame(dim=3)

# define a pointcloud
points = PointCloud(coords, frame=GlobalFrame).centralize()

# set the origo to the center of the fixed end
dx = - np.array([points[:, 0].min(), 0., 0.])
points.move(dx)

# get the coordinates of the vectors
coords = points.show()



from axisvm.com.client import start_AxisVM
axvm = start_AxisVM(visible=True, daemon=True)
axvm


import axisvm.com.tlb as axtlb

# create new model
modelId = axvm.Models.New()
axm = axvm.Models[modelId]

# material
ndc, material = axtlb.ndcEuroCode, "S 235"
axm.Settings.NationalDesignCode = ndc

# cross section
MaterialIndex = axm.Materials.AddFromCatalog(ndc, material)
CrossSectionIndex = axm.CrossSections.AddCircleHollow('S1', D, t)

# crate nodes
fnc = axm.Nodes.Add
list(map(lambda c: fnc(*c), coords))

# create lines
fnc = axm.Lines.Add
GeomType = axtlb.lgtStraightLine
list(map(lambda x: fnc(x[0], x[1], GeomType), topo + 1))

# set material and cross section
LineAttr = axtlb.RLineAttr(
    LineType=axtlb.ltBeam,
    MaterialIndex=MaterialIndex,
    StartCrossSectionIndex=CrossSectionIndex,
    EndCrossSectionIndex=CrossSectionIndex
)
lineIDs = [i+1 for i in range(axm.Lines.Count)]
attributes = [LineAttr for _ in range(axm.Lines.Count)]
axm.Lines.BulkSetAttr(lineIDs, attributes)

# nodal supports
spring = axtlb.RStiffnesses(x=1e12, y=1e12, z=1e12, xx=1e12, yy=1e12, zz=1e12)
RNonLinearity = axtlb.RNonLinearity(
    x=axtlb.lnlTensionAndCompression,
    y=axtlb.lnlTensionAndCompression,
    z=axtlb.lnlTensionAndCompression,
    xx=axtlb.lnlTensionAndCompression,
    yy=axtlb.lnlTensionAndCompression,
    zz=axtlb.lnlTensionAndCompression
)
RResistances = axtlb.RResistances(x=0, y=0, z=0, xx=0, yy=0, zz=0)
ebcinds = np.where(coords[:, 0] < 1e-12)[0]
for i in ebcinds:
    axm.NodalSupports.AddNodalGlobal(spring, RNonLinearity, RResistances, i+1)

# nodal loads
load_cases = {}
LoadCaseType = axtlb.lctStandard
inds = np.where(coords[:, 0] > Lx - 1e-12)[0] + 1
axm.BeginUpdate()
for case in range(nCase):
    name = 'LC{}'.format(case+1)
    lcid = axm.LoadCases.Add(name, LoadCaseType)
    pid = np.random.choice(inds)
    Fx, Fy, Fz = 0, 0, -F
    force = axtlb.RLoadNodalForce(
        LoadCaseId=lcid,
        NodeId=pid,
        Fx=Fx, Fy=Fy, Fz=Fz,
        Mx=0., My=0., Mz=0.,
        ReferenceId=0
    )
    axm.Loads.AddNodalForce(force)
    load_cases[lcid] = dict(name=name, id=case)
axm.EndUpdate()

# save the model before calculation
fpath = 'the_name_of_your_file.axs'
axm.SaveToFile(fpath, False)
axm