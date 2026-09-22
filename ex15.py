#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
from Bio.PDB import *
from Bio.PDB.NeighborSearch import NeighborSearch
from Bio.PDB.PDBParser import PDBParser
pdbl= PDBList()

#getting arguments
parser= argparse.ArgumentParser(description="Genreates a list of backbone connectivity")
parser.add_argument("pdbid", help="PDB file name (example:1RFA)")
parser.add_argument("--distance","-d", type=float, default=2,help="Distance to use as a maximum")
args=parser.parse_args()

#baixem 
path=pdbl.retrieve_pdb_file(args.pdbid, pdir ="." , file_format="pdb")
parser2 = PDBParser(QUIET=True)
st = parser2.get_structure(args.pdbid, path)

#looking for the atoms and neighbours
cc=[]
for atom in st.get_atoms():
    if atom.id=="C" or atom.id=="N":
        cc.append(atom)
nbsearch= NeighborSearch(cc)
count=1
for at1,at2 in nbsearch.search_all(args.distance):
    res1=int(at1.get_parent().id[1])
    res2= int(at2.get_parent().id[1])
    if at2.id=="N":
        if res2 -res1 ==1:
                print(f"Peptide bond: {count}")
                print(f"at1: {at1}, {res1}, {at1.get_parent().get_resname()}")
                print(f"at2: {at2}, {res2}, {at2.get_parent().get_resname()}")
                print()
                count+=1
            
        
