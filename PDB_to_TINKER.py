#!/usr/bin/python

import sys, re
from os import path

file_name = sys.argv[1]
file_output = sys.argv[2]

print "Number of atoms:"
number_atoms = int(raw_input())
atoms = []
atom_index = []

print "Give the atom name and atom type (index) from parameter file:"

for i in range(number_atoms):
        atoms.append(str(raw_input()))
        atoms[i] = atoms[i].split(' ')
        if (len(atoms[i]) < 4):
                atoms[i].append(0)
                atoms[i].append(0)

name = file_name.split(".")
document = open(file_name, "r")

fo_lines = document.readlines();
tinker = open(file_output, "w")

atom = []
conect = []

lines = ['ATOM']

for record in fo_lines:
	line = record.split()
	if (line[0] == lines[0]):
		atom.append(line)
		print record


for a_number in range(len(atom)):
        atom_name = re.compile("([a-zA-Z]+)([0-9]+)")
        for atom_no in range(number_atoms):
		if ((atom_name.match(atom[a_number][2]).group(1) == atoms[atom_no][0]) and (atoms[atom_no][2] != 0) and (int(atoms[atom_no][2]) <= int(atom[a_number][1])) and (int(atoms[atom_no][3]) >= int(atom[a_number][1]))):
                        l = int(atoms[atom_no][1])
			atom_index.append(l)
                        break
                elif ((atom_name.match(atom[a_number][2]).group(1) == atoms[atom_no][0]) and atoms[atom_no][2] == 0):
                        l = int(atoms[atom_no][1])
                        atom_index.append(l)
                        break

print atom_index
lines = ['CONECT']

for record in fo_lines:
	line = record.split()
	if (line[0] == lines[0]):
		conect.append(line)
		print record

tinker.write("  %i  %s\n" % (len(atom), name[0]))
for line_number in range(len(atom)):
        print "\t".join(map(str, conect[line_number][2:]))
        tinker.write("  %i  %s\t%f\t%f\t%f\t%i\t%s\n" % (int(atom[line_number][1]), atom_name.match(atom[line_number][2]).group(1), float(atom[line_number][6]), float(atom[line_number][7]), float(atom[line_number][8]), int(atom_index[line_number]), "\t".join(map(str, conect[line_number][2:]))))
