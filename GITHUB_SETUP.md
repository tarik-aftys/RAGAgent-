# Guide de déploiement sur GitHub

## Étapes pour publier votre projet sur GitHub

### 1. Initialiser Git (si pas déjà fait)
```bash
git init
```

### 2. Ajouter tous les fichiers
```bash
git add .
```

### 3. Créer le premier commit
```bash
git commit -m "Initial commit: RAG Agent system"
```

### 4. Créer un repository sur GitHub
1. Allez sur https://github.com
2. Cliquez sur le bouton "+" en haut à droite
3. Sélectionnez "New repository"
4. Donnez un nom (ex: `RAGAgent`)
5. Ne cochez PAS "Initialize with README" (vous avez déjà un README)
6. Cliquez sur "Create repository"

### 5. Lier votre projet local à GitHub
Remplacez `VOTRE_USERNAME` et `RAGAgent` par vos valeurs :
```bash
git remote add origin https://github.com/VOTRE_USERNAME/RAGAgent.git
```

### 6. Pousser le code sur GitHub
```bash
git branch -M main
git push -u origin main
```

## Commandes complètes (copier-coller)

```bash
# Initialiser Git
git init

# Ajouter les fichiers
git add .

# Premier commit
git commit -m "Initial commit: RAG Agent system"

# Ajouter le remote (remplacez VOTRE_USERNAME et RAGAgent)
git remote add origin https://github.com/VOTRE_USERNAME/RAGAgent.git

# Pousser sur GitHub
git branch -M main
git push -u origin main
```

## Notes importantes

- Le fichier `.gitignore` exclut automatiquement :
  - Les fichiers de sortie dans `output/`
  - Les fichiers Python compilés (`__pycache__`)
  - Les environnements virtuels
  - Les fichiers de cache des modèles

- Les fichiers inclus dans le repository :
  - Code source (`src/`)
  - Documents d'exemple (`data/`)
  - `requirements.txt`
  - `README.md`
  - `main.py`

## Après le déploiement

Vous pouvez mettre à jour votre README.md avec le lien réel vers votre repository GitHub.

