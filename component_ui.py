"""
component_ui.py

Note the places you need to change to make it work for you.
They are marked with keyword 'TODO'.
"""

import argparse

#==============================================================================
# make a UI
#==============================================================================
parser = argparse.ArgumentParser(prog='plot_hmmcopy',
                                 description = """
                                 runs hmmcopy plotting functions (R package)""")

parser.add_argument(
                     "--tumour_copy",
                    required = True,
                    help= """
                    The corrected tumour wig
                    """)

parser.add_argument(
                     "--hmmcopy_res",
                    required = True,
                    help= """
                    The corrected normal wig
                    """)

parser.add_argument(
                     "--correction_plots",
                    required = True,
                    help= """
                    The hmmcopy output file
                    """)
parser.add_argument(
                     "--hmmcopy_plots",
                    required = True,
                    help= """
                    The hmmcopy output file
                    """)


args, unknown = parser.parse_known_args()
