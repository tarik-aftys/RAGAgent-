# RAG Agent - Retrieval-Augmented Generation System

Un système RAG (Retrieval-Augmented Generation) professionnel qui combine la recherche sémantique avec la génération de texte pour fournir des réponses précises basées sur des documents.

##  Fonctionnalités

- **Recherche sémantique** : Utilise des embeddings pour trouver les documents les plus pertinents
- **Génération de réponses** : Génère des réponses basées sur le contexte récupéré
- **Similarité cosinus** : Calcule la pertinence des documents par rapport à la requête
- **Structure modulaire** : Code organisé et professionnel

##  Utilisation

### Structure du projet

```
RAGAgent/
├── data/
│   ├── documents/      # Documents à indexer
│   │   ├── Doc1.txt
│   │   ├── Doc2.txt
│   │   └── Doc3.txt
│   └── queries/        # Requêtes
│       └── query.txt
├── output/             # Résultats générés (créé automatiquement)
├── src/
│   └── rag/
│       ├── __init__.py
│       └── RAG.py      # Code principal
├── main.py             # Point d'entrée
└── requirements.txt
```

### Exécution

Exécutez simplement :
```bash
python main.py
```

Le système va :
1. Charger les documents depuis `data/documents/`
2. Charger la requête depuis `data/queries/query.txt`
3. Récupérer les documents les plus pertinents
4. Générer une réponse basée sur le contexte
5. Sauvegarder les résultats dans `output/`

### Résultats

Les résultats sont sauvegardés dans le dossier `output/` :
- `retrieved_context.txt` : Documents récupérés avec leurs scores de similarité
- `generated_answer.txt` : Réponse générée par le modèle

### Modèles utilisés

- **Embedding** : `sentence-transformers/all-MiniLM-L6-v2`
- **Génération** : `google/flan-t5-base`

### Paramètres

Vous pouvez modifier les paramètres dans `src/rag/RAG.py` :
- `DEFAULT_TOP_K` : Nombre de documents à récupérer (défaut: 3)
- Modèles d'embedding et de génération

##  Exemple

1. Placez vos documents dans `data/documents/`
2. Créez votre requête dans `data/queries/query.txt`
3. Exécutez `python main.py`
4. Consultez les résultats dans `output/`

##  Architecture

- **RAGAgent** : Classe principale qui orchestre le processus RAG
- **embed()** : Convertit les textes en vecteurs numériques
- **retrieve()** : Trouve les documents les plus pertinents
- **generate()** : Génère la réponse finale
- **save_outputs()** : Sauvegarde les résultats

##  Dépendances

- `sentence-transformers` : Pour les embeddings
- `transformers` : Pour la génération de texte
- `numpy` : Calculs numériques





