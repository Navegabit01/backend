from io import BytesIO
import numpy as np
import requests
import matplotlib.pyplot as plt
from scipy.ndimage import rotate
from torch.utils.data import TensorDataset, DataLoader
import torch
import torch.nn as nn
import torch.nn.functional as F
from sklearn.model_selection import train_test_split
import pickle

if 'icons' not in locals():
  with open('/content/iconos_train.pkl', 'rb') as handle:
      icons = pickle.load(handle)
