#!/usr/bin/env python3
"""ProspectBot - Genere des messages de prospection personnalises en masse."""

import os, csv, json, re, time
from datetime import datetime

# ─── CONFIG ───
CSV_FILE = "prospects.csv"

def bienvenu():
    print("=" * 50)
    print("  PROSPECTBOT")
    print("  Genere des messages de prospection en masse")
    print("=" * 50)

def saisir_commerces():
    """Permet a l'utilisateur de saisir ou coller ses prospects."""
    print("\nEntre les commerces a prospecter.")
    print("2 formats possibles :")
    print("")
    print("  Format simple : Nom du commerce")
    print("  Format complet : Nom | Adresse | Telephone")
    print("")
    print("Exemples :")
    print("  Boulangerie Paris Centre")
    print("  Pizzeria Chez Mario | 15 Rue Principale, Paris | 01 23 45 67 89")
    print("")
    print("(laisse vide pour terminer)")
    print("")

    commerces = []
    i = 1
    while True:
        ligne = input(f"  #{i}: ").strip()
        if not ligne:
            break
        parts = [p.strip() for p in ligne.split("|")]
        nom = parts[0] if len(parts) > 0 else ""
        adresse = parts[1] if len(parts) > 1 else ""
        telephone = parts[2] if len(parts) > 2 else ""
        if nom:
            commerces.append({
                "nom": nom,
                "adresse": adresse,
                "telephone": telephone,
                "message": "",
                "contacte": False,
            })
            i += 1

    return commerces


def generer_message(commerce):
    """Genere un message de prospection via le LLM local."""
    prompt = f"""Tu es un commercial qui contacte des petites entreprises.

Entreprise: {commerce['nom']}
Adresse: {commerce['adresse']}

Ecris un message de prospection de 2 phrases maximum.
Le message doit:
- Etre naturel, comme un vrai message prive (pas un mail corporate)
- Proposer de les aider a avoir un site web moderne
- Finir par une question simple
- Ne PAS mentionner de prix
- Ne PAS etre insistant ou commercial

Genere UNIQUEMENT le message, rien d'autre."""

    try:
        import requests
        r = requests.post("http://localhost:11434/api/generate",
            json={"model": "phi3:3.8b", "prompt": prompt,
                  "stream": False, "options": {"num_predict": 150}},
            timeout=60)
        resp = r.json()
        if "response" in resp:
            msg = resp["response"].strip()
            msg = re.sub(r'\s+', ' ', msg)
            return msg[:300]
        return f""
    except:
        return ""


def exporter(commerces):
    """Exporte le CSV."""
    with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["Nom", "Adresse", "Telephone", "Message", "Contacte"])
        for c in commerces:
            w.writerow([c["nom"], c["adresse"], c["telephone"],
                       c.get("message", ""), c.get("contacte", False)])
    print(f"\n  Fichier: {CSV_FILE} ({len(commerces)} lignes)")


def afficher(commerces):
    """Affiche le rapport."""
    valides = [c for c in commerces if c.get("message") and len(c["message"]) > 10]
    
    print(f"\n{'='*50}")
    print(f"  RAPPORT - {datetime.now().strftime('%d/%m/%Y %H:%M')}")
    print(f"{'='*50}")
    print(f"\n  Total commerces : {len(commerces)}")
    print(f"  Messages generes : {len(valides)}/{len(commerces)}")
    
    if valides:
        print(f"\n{'='*50}")
        print(f"  MESSAGES PRETS A ENVOYER (copier-coller)")
        print(f"{'='*50}")
        for c in valides[:5]:
            print(f"\n  --- {c['nom']} ---")
            print(f"  {c['message']}")
            print()
        if len(valides) > 5:
            print(f"  ... et {len(valides)-5} autres dans le CSV")
    
    exporter(commerces)


def main():
    bienvenu()
    
    # Saisie
    commerces = saisir_commerces()
    
    if not commerces:
        print("  Aucun commerce saisi. Utilisation des exemples...")
        commerces = [
            {"nom": "Boulangerie Paris Centre", "adresse": "1 Rue de Rivoli, Paris", "telephone": "", "message": "", "contacte": False},
            {"nom": "Pizzeria Chez Mario", "adresse": "15 Rue Principale, Paris", "telephone": "", "message": "", "contacte": False},
            {"nom": "Garage Auto Paris Sud", "adresse": "45 Avenue d'Italie, Paris", "telephone": "", "message": "", "contacte": False},
            {"nom": "Epicerie Fine Bastille", "adresse": "12 Rue du Faubourg, Paris", "telephone": "", "message": "", "contacte": False},
            {"nom": "Coiffure Mixte Paris 11", "adresse": "8 Rue de la Roquette, Paris", "telephone": "", "message": "", "contacte": False},
        ]
    
    print(f"\n  {len(commerces)} commerces a traiter")
    
    # Generation des messages
    print(f"\n  Generation des messages (phi3 local)...")
    for i, c in enumerate(commerces):
        print(f"    [{i+1}/{len(commerces)}] {c['nom']}...", end=" ", flush=True)
        msg = generer_message(c)
        if msg:
            c["message"] = msg
            print("OK")
        else:
            print("erreur")
        time.sleep(0.3)
    
    # Rapport
    afficher(commerces)


if __name__ == "__main__":
    # Install requests si besoin
    try:
        import requests
    except ImportError:
        os.system("pip install requests -q")
    main()
