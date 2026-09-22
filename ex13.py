# -*- coding: utf-8 -*-

import argparse
from Bio.PDB import *
from Bio.PDB.NeighborSearch import NeighborSearch
from Bio.PDB.PDBParser import PDBParser
pdbl= PDBList()
#getting the arguments
parser= argparse.ArgumentParser(description= "Determine all possible hydrogen bonds.")
parser.add_argument("pdbid", help="PDB file name (example: 1RFA)")
parser.add_argument("--distance","-d", type=float, default=3.5, help="Distance to use as a maximum for the hydrogen bonds in Å (by default, distance =3.5)")
args = parser.parse_args()
#getting the pdb file and the structure
path=pdbl.retrieve_pdb_file(args.pdbid, pdir ="." , file_format="pdb")
parser2 = PDBParser(QUIET=True)
st = parser2.get_structure(args.pdbid, path)
#looking for the CA atoms
polaratoms=["O","N","S"]
selected=[]
for at in st.get_atoms():
    if at.id in polaratoms:
        selected.append(at)
        print(f"ATOM: {at.get_parent().get_resname()}, {at.get_parent().id[1]}, {at.id}")
 #searching for the neighbours at the given distance        
nbsearch= NeighborSearch(selected)
nc=1
print("Neighbor Search")
for at1,at2 in nbsearch.search_all(args.distance):
    print(f"Hidrogen bond: {nc}")
    print(f"at1: {at1}, {at1.get_serial_number()}, {at1.get_parent().get_resname()}")
    print(f"at2: {at2}, {at2.get_serial_number()}, {at2.get_parent().get_resname()}")
    print()
    nc+=1
