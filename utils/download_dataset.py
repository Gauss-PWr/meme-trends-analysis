import kagglehub
import os
def get_path():
    path = kagglehub.dataset_download("podsyp/a-lot-of-memes-info-stats")
    return os.path.join(path, "memes_dataset.csv")

if __name__ == "__main__": #debug
    print(get_path())