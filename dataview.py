import numpy as np
import pandas as pd
from utils import read_df


df = read_df("spotfy_tracks_dataset")

print(df.head())
print(df.info())
print(df.columns)
print(df.describe())
print(len(df.artists.unique()))
print(len(df.track_genre.unique()))

