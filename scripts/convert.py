import os
import pdfkit


file_list = [('./html/Fisio2-MCM.html', 'Fisio2'),
             ('./html/Fisio2-UF.html', 'Fisio2'),
             ('./html/Fisio2-LC.html', 'Fisio2'),
             ('./html/Fisiopato-AC.html', 'Fisiopato'),
             ('./html/Fisiopato-AP.html', 'Fisiopato'),
             ('./html/Fisiopato-LC.html', 'Fisiopato'),
             ('./html/Microbio-LR.html', 'Microbio'),
             ('./html/Microbio-AL.html', 'Microbio'),
             ('./html/Microbio-MP.html', 'Microbio'),
             ('./html/Semeiotica-FF.html', 'Semeiotica'),
             ('./html/Semeiotica-GDC.html', 'Semeiotica'),
             ('./html/Semeiotica-SC.html', 'Semeiotica')]

for file, subject in file_list:
    path = os.path.abspath(file)
    with open(path, 'r') as file:
        code = file.read()
        pdfkit.from_string(code, f'pdf/{str(file).split("/")[-1].split(".")[0]}.pdf')
