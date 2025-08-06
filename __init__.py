"""
ProteinMPNN: Robust deep learning-based protein sequence design

This package provides tools for protein sequence design using message passing neural networks.
"""

__version__ = "1.0.0"
__author__ = "J. Dauparas, I. Anishchenko, N. Bennett, H. Bai, R. J. Ragotte, L. F. Milles, B. I. M. Wicky, A. Courbet, R. J. de Haas, N. Bethel, P. J. Y. Leung, T. F. Huddy, S. Pellock, D. Tischer, F. Chan, B. Koepnick, H. Nguyen, A. Kang, B. Sankaran, A. K. Bera, N. P. King, D. Baker"

# Import main classes and functions for easy access
try:
    from .protein_mpnn_utils import (
        ProteinMPNN,
        StructureDataset,
        StructureDatasetPDB,
        parse_PDB,
        _S_to_seq,
        tied_featurize,
        loss_nll,
        loss_smoothed,
        gather_edges,
        gather_nodes,
        gather_nodes_t,
        cat_neighbors_nodes,
        _scores,
        parse_fasta,
    )
    
    from .protein_mpnn_run import main as run_protein_mpnn
    
except ImportError as e:
    # Handle import errors gracefully for package discovery
    import warnings
    warnings.warn(f"Some ProteinMPNN components could not be imported: {e}")

# Package metadata
__all__ = [
    "ProteinMPNN",
    "StructureDataset", 
    "StructureDatasetPDB",
    "parse_PDB",
    "_S_to_seq",
    "tied_featurize",
    "run_protein_mpnn",
]