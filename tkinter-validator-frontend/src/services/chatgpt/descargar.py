import pickle

if 'icons' not in locals():
  with open('/content/iconos_train.pkl', 'rb') as handle:
      icons = pickle.load(handle)
