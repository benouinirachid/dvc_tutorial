import argparse
import pandas as pd

parser = argparse.ArgumentParser()

parser.add_argument(
    "-i",
    "--input_data",
    type=str,
    dest="input_data",
    required=True,
    help="input data file.",
)

parser.add_argument(
    "-o",
    "--output_data",
    type=str,
    dest="output_data",
    required=True,
    help="output preprocessed data.",
)

args = parser.parse_args()
input_data = args.input_data
output_data = args.output_data

if __name__ == "__main__":
    # The following processing just make a copy of the data
    # One can use pandas to preprocess the data
    data = pd.read_csv(input_data, sep=";")
    # This will just replace the separator ";" by ",". :) 
    # TDOD: add your processing here.
    data.to_csv(output_data, sep=",", index=False)
    print("#INFO: Data is succefully processed!")
