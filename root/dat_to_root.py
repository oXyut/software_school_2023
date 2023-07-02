import os
import glob
import array
import argparse


import ROOT

def read_dat_file(file_name):
    data = []
    with open(file_name, 'r') as f:
        for line in f:
            if line.strip():
                data.append(int(line.strip()))
    return data


def dat_to_root(dir:str, filename:str)->None:
    # Read all dat files in the directory
    data_files = glob.glob(os.path.join(dir, "*.dat"))
    print(f"Found {len(data_files)} dat files in {dir}...")

    # Create a new ROOT file
    root_file = ROOT.TFile(filename, "RECREATE")
    print(f"Created ROOT file {filename}...")

    # Create a TTree
    tree = ROOT.TTree("MPPC", "ADC count at each applied voltage of MPPC")
    print(f"Created TTree {tree.GetName()}...")

    # Loop over the data files and create branches
    branches = {}
    for file in data_files:
        # Read data from the dat file
        data = read_dat_file(file)

        # Create a branch for this data
        branch_name = os.path.splitext(os.path.basename(file))[0]
        branches[branch_name] = {
            "data": data,
            "array": array.array('i', [0])
        }
        tree.Branch(branch_name, branches[branch_name]["array"], f"{branch_name}/I")

    # Determine the number of entries based on the smallest dataset
    n_entries = min([len(branch_data["data"]) for branch_data in branches.values()])
    print(f"Created {len(branches)} branches with {n_entries} entries...")

    # Loop over the data and fill the branches
    for i in range(n_entries):
        for branch_name, branch_data in branches.items():
            branch_data["array"][0] = branch_data["data"][i]

        tree.Fill()

    # Write the TTree to the output ROOT file
    tree.Write()
    root_file.Close()

    print("Done!")

if __name__ == "__main__":
    # Parse the command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("dir", help="Directory containing the dat files")
    parser.add_argument("-o", "--output", help="Output ROOT file", default="output.root")
    args = parser.parse_args()

    # Convert the dat files to a ROOT file
    dat_to_root(args.dir, args.output)

    """
    Usage:
        python dat_to_root.py /path/to/dat/files -o output.root
    """
