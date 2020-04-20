import pandas as pd

tech_comps = ["web","software","mobile","games_video","cleantech","biotech","netwok_hosting","analytics","search",
              "hardware","nanotech"]

dfo = pd.read_csv("OUTPUT/dfo.csv", encoding = "latin-1")

dfc = pd.read_csv("OUTPUT/dfc.csv", encoding = "latin-1")

df_clean = pd.read_csv("OUTPUT/df_clean.csv", encoding = "latin-1")