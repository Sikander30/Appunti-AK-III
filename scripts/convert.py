import os
import pdfkit


file_list = [('./html/Fisiologia Umana II/MCM.html', 'Fisio2'),
             ('./html/Fisiologia Umana II/UF.html', 'Fisio2'),
             ('./html/Fisiologia Umana II/LC.html', 'Fisio2'),
             ('./html/Fisiopatologia Generale e Patologia Clinica/AC.html', 'Fisiopato'),
             ('./html/Fisiopatologia Generale e Patologia Clinica/AP.html', 'Fisiopato'),
             ('./html/Microbiologia/LR.html', 'Microbio'),
             ('./html/Microbiologia/AL.html', 'Microbio'),
             ('./html/Microbiologia/MP.html', 'Microbio'),
             ('./html/Semeiotica e Metodologia Clinica/FF.html', 'Semeiotica'),
             ('./html/Semeiotica e Metodologia Clinica/GDC.html', 'Semeiotica'),
             ('./html/Semeiotica e Metodologia Clinica/SC.html', 'Semeiotica')]

for file, subject in file_list:
    with open(file, 'r') as file:
        code = file.read()
        pdfkit.from_string(code, f'pdf/{subject}-{file.split("/")[-1].split(".")[0]}.pdf')
