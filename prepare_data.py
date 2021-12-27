import argparse
import pandas as pd
from sklearn.model_selection import train_test_split

TEST_SIZE = 0.8
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
    "-p",
    "--path",
    type=str,
    dest="path",
    required=True,
    help="path for saving saving train and test data.",
)

args = parser.parse_args()
input_data = args.input_data
path = args.path

if __name__ == "__main__":
    # In the following we just split the data into train and test sets
    # One can update this script to add a validation set
    data = pd.read_csv(input_data, sep=",")
    file_name = input_data.split("/")[-1]
    if path[-1] != "/":
        path = path + "/"
    # Split the data into training and test sets (0.8, 0.2) split
    train, test = train_test_split(data, test_size=TEST_SIZE)
    train.to_csv(path + "train_" + file_name, index=False)
    test.to_csv(path + "test_" + file_name, index=False)
    print("#INFO: Data is succefully prepared!")
