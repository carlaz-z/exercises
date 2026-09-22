# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 19:54:43 2026

@author: zarlac
"""
import argparse
from Bio.PDB import *
from Bio.PDB.PDBParser import PDBParser
pdbl= PDBList()
parser= argparse.ArgumentParser(description="Generates a list of all atoms of a given residue number")
parser.add_argument("pdbid", help="PDB file name (ex:1RFA)")
parser.add_argument("residue_num", help= "Residue number")
parser.add_argument("--chain_name", "-c", default=None, help="Optional, introduce the chain name." )
args=parser.parse_args()
#getting the pdb file and the structure
path=pdbl.retrieve_pdb_file(args.pdbid, pdir ="." , file_format="pdb")
parser2 = PDBParser(QUIET=True)
st = parser2.get_structure(args.pdbid, path)
##residues= st.get_residues()
num= int(args.residue_num)
selected=[]

for atom in st.get_atoms():
    res=atom.get_parent()
    chain= res.get_parent()
    if args.chain_name and chain.get_id() != args.chain_name:
        continue
    if res.get_id()[1]== num:
        selected.append(atom)
        
print(selected)
        