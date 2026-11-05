"""Mini-analyste pandas pour le corpus d'arménien classique (HYE).

Ce script est le seul à lire data/ : il charge les fichiers avec
pd.read_csv(sep="\t") et affiche, sous les titres Q1 à Q5, la réponse
aux cinq questions.

Lancement depuis la racine du dépôt : uv run python scripts/analyser.py
"""

import pandas as pd

TRAIN = "data/HYE_train.tsv"
TEST_IN = "data/HYE_test_in-domain.tsv"
TEST_OUT = "data/HYE_test_out-of-domain.tsv"
TAGSET = "data/HYE_tagset.txt"

train = pd.read_csv(TRAIN, sep="\t")
test_in = pd.read_csv(TEST_IN, sep="\t")
test_out = pd.read_csv(TEST_OUT, sep="\t")
tagset = pd.read_csv(TAGSET, sep="\t", header=None)

# ------------------------------------------------------------------ Q1
print("Q1 : 5 categories (pos) les plus fréquentes dans le train")
print(train["pos"].value_counts().head(5))
print()

# ------------------------------------------------------------------ Q2
print("Q2 : formes composées du train (présence de @ dans pos)")
compose = train["pos"].str.contains("@")
print(f"Proportion de formes composées : {compose.mean():.2%} ({int(compose.sum())} mots sur {len(train)})")
print("5 combinaisons les plus fréquentes :")
print(train[compose]["pos"].value_counts().head(5))
print()

# ------------------------------------------------------------------ Q3
print("Q3 : article suffixé et préposition з")
n_article = int(train["pos"].str.endswith("@PRO+Dem").sum())
n_z = int(train["lemma"].str.startswith("զ@").sum())
print(f"Mots du train dont le pos finit par @PRO+Dem : {n_article}")
print(f"Mots du train dont le lemma commence par զ@ : {n_z}")
print()

# ------------------------------------------------------------------ Q4
print("Q4 : étiquettes du train absentes de HYE_tagset.txt")
noms_tagset = tagset[0].str.strip()                      # .strip() : certains noms du tagset finissent par une espace
etiquettes = train[["pos"]].drop_duplicates("pos")       # étiquettes uniques du train
direct = etiquettes["pos"].isin(noms_tagset)             # étiquette présente telle quelle dans le tagset
decoupe = etiquettes["pos"].str.split("@", expand=True)   # parties des étiquettes composées (séparées par @)
n_parts = etiquettes["pos"].str.split("@").str.len()     # nombre de parties de chaque étiquette
dans_tagset = decoupe.isin(noms_tagset.unique())         # True si la partie figure dans le tagset (.unique() : DataFrame.isin veut une liste, pas une Series)
parties_ok = dans_tagset.sum(axis=1) == n_parts          # composée valide si chaque partie l'est
composee = etiquettes["pos"].str.contains("@")
valide = direct | (composee & parties_ok)
invalides = etiquettes[~valide]["pos"]
freq_invalides = train[train["pos"].isin(invalides)]["pos"].value_counts()
print(f"Nombre d'étiquettes du train hors tagset : {len(freq_invalides)}")
if len(freq_invalides) == 0:
    print("Aucune : toutes les étiquettes du train figurent dans HYE_tagset.txt.")
else:
    print("Fréquence de chacune dans le train :")
    print(freq_invalides)
print()

# ------------------------------------------------------------------ Q5
print("Q5 : formes (colonne form) des tests déjà présentes dans le train")
formes_train = train[["form"]].drop_duplicates("form")["form"]
presentes_in = test_in["form"].isin(formes_train)
presentes_out = test_out["form"].isin(formes_train)
print(f"test in-domain    : {int(presentes_in.sum())} mots sur {len(test_in)} ont une forme présente dans le train ({presentes_in.mean():.2%})")
print(f"test out-of-domain : {int(presentes_out.sum())} mots sur {len(test_out)} ont une forme présente dans le train ({presentes_out.mean():.2%})")
