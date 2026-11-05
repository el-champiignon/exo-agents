# Les 5 réponses, copiées depuis la sortie du script :

• Q1 — 5 pos les plus fréquentes dans le train : V 1008, N+Com 786, I+Conj 745, I+Prep 310, A 295.
• Q2 — Formes composées (@ dans pos) : 14,20 % (669 mots sur 4712). Top 5 : N+Com@PRO+Dem 166, I+Prep@N+Com 164, I+Prep@N+Com@PRO+Dem 76, A@PRO+Dem 41, I+Prep@PRO+Dem 37.
• Q3 — pos finissant par @PRO+Dem : 383 mots ; lemma commençant par զ@ : 339 mots.
• Q4 — Étiquettes du train absentes du tagset : 1 seule, PRO+Pos3 (10 occurrences) — conforme à la note de la skill tagset (dans le gold, hors tagset). Les deux pièges sont gérés : .str.strip() sur les noms du tagset et validité des composées par parties (split("@") + isin).
• Q5 — Formes des tests déjà vues dans le train : in-domain 173/300 (57,67 %) ; out-of-domain 168/314 (53,50 %).


# La consigne exacte que vous avez donnée à l'agent.

Utilise le sous-agent agents_analyste.toml pour écrire un script permettant de répondre à des questions sur le corpus arménien (HYE). Une fois le script écrit, demande au sous-agent agents_analyste.toml de l'éxecuter. Le script doit donner les réponses aux questions. Les fonctions pandas autorisées à utiliser pour le script sont dans la skill pandas-tuto, à laquelle le sous-agent a accès. Aucune autre fonction ne doit être utilisée.

# **Une erreur de l'agent** : ce qu'il a fait de travers (mauvais filtre, boucle interdite, fonction hors skill, chiffre inventé…) et ce que vous avez changé dans `AGENTS.md`, le `.toml` ou la skill pour la corriger.

A priori je n'ai pas trouvé d'erreur. Cependant, l'agent n'a réussi à produire un script correct qu'au 2e essai. 

Détail des opérations (explication de l'erreur à la dernière ligne) :
Terminé. J'ai spawné le sous-agent agents_analyste (config .vibe/agents/agents_analyste.toml), qui a écrit scripts/analyser.py, puis je lui ai demandé de l'exécuter via la seule commande autorisée uv run python scripts/analyser.py. J'ai relancé cette commande moi-même : la sortie est identique. Le script n'utilise que des fonctions de la skill pandas-tuto (pd.read_csv(sep="\t"), value_counts, head, isin, unique, drop_duplicates, filtres booléens et méthodes .str sur colonnes entières — aucune boucle for sur les lignes, aucun apply/Counter).

Réponses du script :

• Q1 — 5 pos les plus fréquentes dans le train : V 1008, N+Com 786, I+Conj 745, I+Prep 310, A 295.
• Q2 — Formes composées (@ dans pos) : 14,20 % (669 mots sur 4712). Top 5 : N+Com@PRO+Dem 166, I+Prep@N+Com 164, I+Prep@N+Com@PRO+Dem 76, A@PRO+Dem 41, I+Prep@PRO+Dem 37.
• Q3 — pos finissant par @PRO+Dem : 383 mots ; lemma commençant par զ@ : 339 mots.
• Q4 — Étiquettes du train absentes du tagset : 1 seule, PRO+Pos3 (10 occurrences) — conforme à la note de la skill tagset (dans le gold, hors tagset). Les deux pièges sont gérés : .str.strip() sur les noms du tagset et validité des composées par parties (split("@") + isin).
• Q5 — Formes des tests déjà vues dans le train : in-domain 173/300 (57,67 %) ; out-of-domain 168/314 (53,50 %).

Un point de déroulement : au premier essai, le sous-agent avait un bug dans Q4 (DataFrame.isin avec une Series traité comme un dict) ; il l'a corrigé en passant noms_tagset.unique() et a réussi au 2ᵉ essai, dans la limite des 3 essais autorisés.

# Les fonctions que vous avez ajoutées à la skill `pandas-tuto`, s'il y en a.
Le tableau du notebook était suffisant. 

# En 3 lignes : qu'est-ce que l'agent apporte ici par rapport au notebook ? Qu'est-ce qu'il coûte ?
L'agent n'apporte pas grand-chose : les questions et les fonctions nécessaires pour y répondre sont relativement simples. Ici, l'agent a coûté 27k tokens, et a pris environ 8min.





