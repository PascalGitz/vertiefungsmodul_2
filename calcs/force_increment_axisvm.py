from axisvm.com.client import start_AxisVM
import axisvm.com.tlb as axtlb


# Starting AxisVM
axvm = start_AxisVM(visible=True, join=True, daemon=True)

# Creating a Model
modelId = axvm.Models.New()
model = axvm.Models[modelId]