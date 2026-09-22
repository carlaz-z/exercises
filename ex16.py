#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
from Bio.PDB import *
from Bio.PDB.NeighborSearch import NeighborSearch
from Bio.PDB.PDBParser import PDBParser
pdbl= PDBList()
#arguments
parser= argparse.ArgumentParser(description= "Generates a list of disulphide bonds.")
parser.add_argument("pbid",help="PDB file name (example: 1rfa)")
parser.add_argument("--distance", type=float,default=2.5, help="Distance to use as a maximum")
args= parser.parse_args()

#downloading the structure
path= pdbl.retrieve_pdb_file(args.pbid, pdir=".", file_format="pdb")
parser2= PDBParser(QUIET=True)
st= parser2.get_structure(args.pbid, path)

#llokinf for the disulphide bonds
ss=[]
for atom in st.get_atoms():
    if atom.id=="SG":
        ss.append(atom)
nbsearch= NeighborSearch(ss)
count=1
for at1,at2 in nbsearch.search_all(args.distance):
    res1=at1.get_parent().get_resname() 
    res2=at2.get_parent().get_resname()
    if res1 and res2 =="CYS":
        print(f"disulphide bond: {count}")
        print(f"at1: {at1}, {at1.get_parent().id[1]}, {at1.get_parent().get_resname()}")
        print(f"at2: {at2}, {at2.get_parent().id[1]}, {at2.get_parent().get_resname()}")
        print()
        count+=1


