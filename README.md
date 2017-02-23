# PDB-to-TINKER

This code converts any PDB file to TINKER input files with the added benefit of customizing **"index"** numbers for any atom from the PDB. But such customized "index" number must also be specified in the "Parameter" **(\*.prm)** file of corresponding "force-field" file.

Things to keep in mind before running the code.
a.  Keep in hand the number **(and their order of apperance in PDB)** of different types of atoms (not the total number of atoms). for example: if PDB contains **C** and **O** then we have two different types of atoms.

b.  If the **same** atoms have **different** types of connectivity then they are considered as different atom types. for example: **C** double bonded with **O** is different from **C** bonded with **OH**. This applies to any type of atom.

**This is where it gets complicated so pay attention!! In the future versions I'll try to make it less complicated and more user-friendly.**

c.  In the PDB file, if same type of atom/(s) rather than being one after another, are separated by another type of atom/(s) then they must be considered as different types.

Example: The following is an example of a typical PDB file. The detailed explanation is below this snippet.

HEADER    Example
COMPND    UNNAMED
AUTHOR    NONE
CRYST1    8.705    5.163   10.952  90.00  90.00  90.00 P c a 21      4
ATOM      1  O1  UNK 0   1       4.105   5.625  -2.099  1.00  0.00
ATOM      2  O2  UNK 0   1       4.992   4.069   0.283  1.00  0.00
ATOM      3  H1  UNK 0   1       4.548   4.755   0.348  1.00  0.00
ATOM      4  O3  UNK 0   1       6.534   1.804  -0.658  1.00  0.00
ATOM      5  H2  UNK 0   1       6.507   2.023   0.133  1.00  0.00
ATOM      6  O4  UNK 0   1       6.647   1.864  -3.517  1.00  0.00
ATOM      7  O5  UNK 0   1       5.128   4.152  -4.506  1.00  0.00
ATOM      8  C1  UNK 0   1       4.765   4.612  -2.112  1.00  0.00
ATOM      9  C2  UNK 0   1       5.226   3.819  -0.975  1.00  0.00
ATOM     10  C3  UNK 0   1       5.971   2.730  -1.385  1.00  0.00
ATOM     11  C4  UNK 0   1       6.062   2.695  -2.826  1.00  0.00
ATOM     12  C5  UNK 0   1       5.292   3.881  -3.336  1.00  0.00
CONECT    1    8
CONECT    2    3    9
CONECT    3    2
CONECT    4    5   10
CONECT    5    4
CONECT    6   11
CONECT    7   12
CONECT    8    1    9   12
CONECT    9    2    8   10
CONECT   10    4    9   11
CONECT   11    6   10   12
CONECT   12    7    8   11
MASTER        0    0    0    0    0    0    0    0   12    0   12    0
END

In order to generate TINKER input file, we have to focus only on the atoms.
Let me explain the type of atoms for this case: The best way to look for types of atoms is by viewing this PDB file in a Molecular Visulization program.

By doing so we can see that, **C1, C4 and C5** are of one type while **C2 and C3** are of different type of Carbon. Similarly **O1, O4 and O5** are of one type and **O2 and O3** are of another.



HOW TO RUN?
1.  >>>python PDB_to_TINKER.py **\<YOUR PDB FILE\>** **\<OUTPUT FILE\>** 
**NOTE:** The output file will be in the format of \*.xyz and can directly be used for TINKER calculations.
2.  
