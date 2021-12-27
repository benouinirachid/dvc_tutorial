import argparse
import requests

parser = argparse.ArgumentParser()

parser.add_argument(
    "-u", "--url", type=str, dest="url", required=True, help="url of data file."
)

parser.add_argument(
    "-p", "--path", type=str, dest="path", required=True, help="path to save the file."
)

args = parser.parse_args()

path = args.path
url = args.url

if __name__ == "__main__":
    filename = url.split("/")[-1]
    r = requests.get(url, allow_redirects=True)
    if path[-1] != "/":
        path = path + "/"
    full_path = path + filename
    with open(full_path, "wb") as f:
        f.write(r.content)
    print("#INFO: Data is succefully loaded!")
