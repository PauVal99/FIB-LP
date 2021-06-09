antlr4 -Dlanguage=Python3 -no-listener -visitor Logo3D.g
python3.7 Logo3D.py program.l3d

El programa ha de abortar quan es dona:
 + divisió per zero
 + crida a procediment no definit
 + repetició de procediment ja definit
 + nombre de paràmetres incorrectes
 + noms de paràmetres formals repetits 