#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
from Bio.PDB import *
from Bio.PDB.PDBParser import PDBParser
pdbl= PDBList()
#GETTIG ARGUMENTS
parser= argparse.ArgumentParser(description= "Generates a list of all CA atoms of a given residue type.")
parser.add_argument("pdbid",help="PDB file name (example: 1RFA)" )
parser.add_argument("restype", help="Give a residue type")
args= parser.parse_args()

#getting pdb file and structure
path=pdbl.retrieve_pdb_file(args.pdbid, pdir=".", file_format="pdb")
parser2= PDBParser(QUIET=True)
st = parser2.get_structure(args.pdbid,path)

#looking for CA atom and their resiudes
selected=[]
for model in st:
    for chain in model:
        for res in chain:
            if res.get_resname() ==args.restype:
                for atom in res:
                    if atom.id=="CA":
                        selected.append(atom)
at=1               
for atom in selected:
    print(f"CA {at} --> Coordinates = {atom.coord}")
    at+=1
                        
            
                



