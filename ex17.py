#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 20:03:01 2026

@author: zarlac
"""
import argparse
from Bio.PDB import *
from Bio.PDB.NeighborSearch import NeighborSearch
from Bio.PDB.PDBParser import PDBParser
pdbl= PDBList()
#arguments
parser= argparse.ArgumentParser(description= "Computes the distance between all atoms pairs of two residues.")
parser.add_argument("pbid",help="PDB file name (example : 1rfa)")
parser.add_argument("res1",help="Introduce the first resiude (example: A10)")
parser.add_argument("res2", help="Introduce the second residue (example: A20)")
args= parser.parse_args()

#downloading the structure
path= pdbl.retrieve_pdb_file(args.pbid, pdir=".", file_format="pdb")
parser2= PDBParser(QUIET=True)
st= parser2.get_structure(args.pbid, path)

#selection of the reisudes
chain1, res_num1 = args.res1[0], int(args.res1[1:])
chain2, res_num2 = args.res2[0], int(args.res2[1:])
resf1 = st[0][chain1][(' ', res_num1, ' ')]
resf2 = st[0][chain2][(' ', res_num2, ' ')]
print("First residue is", resf1.get_resname())
print("Second residue is", resf2.get_resname())

#computuing distances
for at1 in resf1.get_atoms():
    for at2 in resf2.get_atoms():
        dist = at2 - at1
        print(f"Atom 1 = {at1.get_id()} | Atom 2 = {at2.get_id()} | Distance = {dist:.3f}")
        
