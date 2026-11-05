# Mini-analyste pandas : arménien classique (HYE)
Répondre à des questions sur le corpus arménien (HYE) en écrivant et en lançant un script pandas.

## Règles
- Python : utiliser `uv run python scripts/<script>`. Jamais `pip`, `python` seul ni `python -c`
- Tous les chiffres doivent venir de pandas, en passant par le script : `analyser.py`
- Ne jamais lire `data/` ou `.env`. Passer par les scripts.

## Rôles
- analyser le corpus avec pandas et répondre aux questions : agents_analyste.toml.
- aucun autre sous-agent ne doit être créé.

## Repères
- Données : `data/HYE_train.tsv`, `data/HYE_test_in-domain.tsv`, `data/HYE_test_out-of-domain.tsv`, colonnes `text_form form lemma pos`.
- Tagset : `data/HYE_tagset.txt` (étiquette, tabulation, définition).