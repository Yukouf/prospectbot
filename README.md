# ProspectBot

Génère en masse des messages de prospection personnalisés pour des commerces locaux, à partir d'un LLM local (Ollama). L'idée : produire des messages courts, naturels et non-insistants, sans données qui quittent la machine.

## Ce que ça fait

1. Tu saisis des commerces (nom, adresse, téléphone) ou tu en colles une liste.
2. Pour chaque commerce, ProspectBot appelle un petit modèle local (`phi3:3.8b` via Ollama) pour rédiger un message de prospection de 2 phrases max.
3. Les messages générés sont affichés pour copier-coller et exportés dans un CSV.

Le modèle est configuré pour :
- rester naturel, comme un vrai message privé (pas du corporate)
- proposer de l'aide pour un site web moderne
- finir par une question simple
- ne pas mentionner de prix, ni être insistant ou commercial

## Prérequis

- Python 3
- [Ollama](https://ollama.com/) installé et lancé
- Le modèle local `phi3:3.8b` (`ollama pull phi3:3.8b`)
- Le paquet `requests`

## Utilisation

```bash
python3 prospectbot.py
```

Suis les invites :
- laisse vide pour terminer la saisie
- aucune saisie → il utilise des exemples de démonstration
- les messages valides sont copiés dans le terminal, tout est exporté dans `prospects.csv`

## Fichiers de données

Les fichiers `prospects.csv`, `prospects.json` et `scraped.json` contiennent des données de prospection réelles (noms, adresses, téléphones). Ils sont **exclus du dépôt** via `.gitignore` pour ne pas diffuser d'informations personnelles ou de données de démarchage.

## Limites et éthique

- Outil de démonstration : à adapter pour respecter les règles (RGPD, opt-out, pratiques de prospection) selon le contexte d'usage.
- Le modèle local produit des textes ; vérifie toujours le fond avant envoi réel.
- Aucune donnée ne quitte ta machine quand tu utilises Ollama en local.

## Auteur

Crée par [Youssef Guerniou](https://github.com/Yukouf) — pour la prospection de commerces locaux sans sortir de la machine.
