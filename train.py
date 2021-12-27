import argparse
import pandas as pd
from sklearn.linear_model import ElasticNet
import pickle


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
    "-m",
    "--model_path",
    type=str,
    dest="model_path",
    required=True,
    help="path for saving trained model.",
)

args = parser.parse_args()
input_data = args.input_data
model_path = args.model_path

if __name__ == "__main__":
    # Training a simple model to fit the training data
    alpha = 0.6
    l1_ratio = 0.4
    data = pd.read_csv(input_data, sep=",")
    # The predicted column is "quality" which is a scalar [3, 9]
    train_x = data.drop(["quality"], axis=1)
    train_y = data[["quality"]]
    lr = ElasticNet(alpha=alpha, l1_ratio=l1_ratio, random_state=42)
    lr.fit(train_x, train_y)
    pickle.dump(lr, open(model_path, 'wb'))
    print("#INFO: Model is succefully processed!")
