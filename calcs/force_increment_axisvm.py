from axisvm.com.client import start_AxisVM
import axisvm.com.tlb as axtlb



# Starting AxisVM
modelfolder = "C://Users//Pascal Gitz//OneDrive - Hochschule Luzern//Master//03_Tragverhalten_von_Stahlbetontragwerken//VM2//calcs//FEM//AxisVM//"
filename = "A3V2_Knotenfedern.axs"
axvm = start_AxisVM(modelfolder+filename, visible=True, join=True)


# Injecting the model
model = axvm.Models[1]

# Adding the nodalload
nodenumber = 12 # hardcoded, can be read from the AxisVM model
force = axtlb.RLoadNodalForce(
    LoadCaseId=1,
    NodeId=nodenumber,
    Fx=0., Fy=0., Fz=-100,
    Mx=0., My=0., Mz=0.,
    ReferenceId=0
)
model.Loads.AddNodalForce(force)


# Calculate nonlinear results

