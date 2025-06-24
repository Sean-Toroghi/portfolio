# general data manipulation/preprocessing 
import numpy as np
import pandas as pd
import polars as pl
import matplotlib.pyplot as plt

# sklearn
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# models
import xgboost as xgb

# utilities and seed
import random, gc, os, warnings
from tqdm import tqdm
from pathlib import Path

seed = 42
np.random.seed(seed)
random.seed(seed)
warnings.filterwarnings("ignore", category=RuntimeWarning)
