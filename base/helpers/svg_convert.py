from sympycalcs import pdf_to_svg
import os

# os.chdir("C:/Users/Pascal Gitz/OneDrive - Hochschule Luzern/Master/03_Tragverhalten_von_Stahlbetontragwerken/VM2")

os.chdir("/Users/pascalgitz/Library/CloudStorage/OneDrive-HochschuleLuzern/Master/03_Tragverhalten_von_Stahlbetontragwerken/VM2")
inkscape_path = "/Applications/Inkscape.app/Contents/MacOS/inkscape"
pdf_to_svg("imgs", delete_original=False, inkscape_path=inkscape_path)
pdf_to_svg("imgs/nino", delete_original=False)