from sympycalcs import pdf_to_svg
import os

os.chdir("C:/Users/Pascal Gitz/OneDrive - Hochschule Luzern/Master/03_Tragverhalten_von_Stahlbetontragwerken/VM2")
pdf_to_svg("imgs", delete_original=True)
pdf_to_svg("imgs/nino", delete_original=True)