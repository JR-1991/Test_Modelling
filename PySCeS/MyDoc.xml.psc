# Generated by PySCeS 1.0.2 (2022-07-12 09:49)
 
# Keywords
Description: MyDoc
Modelname: MyDoc
Output_In_Conc: True
Species_In_Conc: True
 
# GlobalUnitDefinitions
UnitSubstance: mole, 1.0, 0, 1
UnitVolume: litre, 1.0, 0, 1
UnitTime: second, 1.0, 0, 1
UnitLength: metre, 1.0, 0, 1
UnitArea: metre, 1.0, 0, 2
 
# Compartments
Compartment: v0, 10.0, 3 
 
# Reactions
r0@v0:
    s0 > s1
    s0*r0_a+r0_b
# r0 has modifier(s): p0  
 
# Fixed species
 
# Variable species
p0@v0 = 10.0
s0@v0 = 200.0
s1@v0 = 0.0
 
# Parameters
r0_b = 10.0
r0_a = 2.0
 

