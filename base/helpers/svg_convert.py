from sympycalcs import pdf_to_svg
import os

inkscape_path = "/Applications/Inkscape.app/Contents/MacOS/inkscape"
try:
    pdf_to_svg("imgs", delete_original=False, inkscape_path=inkscape_path)
    pdf_to_svg("imgs/nino", delete_original=False, inkscape_path=inkscape_path)
except:
    pdf_to_svg("imgs", delete_original=False)
    pdf_to_svg("imgs/nino", delete_original=False)