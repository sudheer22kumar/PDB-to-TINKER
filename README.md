# PDB-to-TINKER

This code converts any PDB file to TINKER input files with the added benefit of customizing **"index"** numbers for any atom from the PDB. But such customized "index" number must also be specified in the "Parameter" **(\*.prm)** file of corresponding "force-field" file.

Things to keep in mind before running the code.
a.  Keep in hand the number of different types of atoms (not the total number of atoms). for example: if PDB contains **C** and **O** then we have two different types of atoms.
b.  If the **same** atoms have **different** types of connectivity then they are considered as different atom types. for example: **C** double bonded with **O** is different from **C** bonded with **OH**. This applies to any type of atom.
c.  

HOW TO RUN?
1.  >>>python PDB_to_TINKER.py **\<YOUR PDB FILE\>** **\<OUTPUT FILE\>** 
**NOTE:** The output file will be in the format of \*.xyz and can directly be used for TINKER calculations.
2.  
