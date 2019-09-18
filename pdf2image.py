PDFTOPPMPATH = r"C:\PortSoft\poppler-0.68.0\bin\pdftoppm.exe"
PDFFILE = "in.pdf"

import subprocess
subprocess.Popen('"%s" -png "%s" out' % (PDFTOPPMPATH, PDFFILE))