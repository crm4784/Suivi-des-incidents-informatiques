from flask import Flask, abort, render_template, request
import json

app = Flask(__name__)

def charger_donnees():
    with open("data/data.json", "r", encoding="utf-8") as fichier:
        return json.load(fichier)

@app.route("/")
def index():
    donnees = charger_donnees()


    gravite_filtre = request.args.get('gravite', '')
    traitement_filtre = request.args.get('traitement', '')
    origine_filtre = request.args.get('origine', '')

    donnees_filtrees = []
    for item in donnees:
        if gravite_filtre and item.get("gravite") != gravite_filtre:
            continue
        if traitement_filtre and item.get("traitement") != traitement_filtre:
            continue
        if origine_filtre and item.get("origine") != origine_filtre:
            continue
        
        donnees_filtrees.append(item)


    ordre_gravite = {"Critique": 1, "Majeure": 2, "Mineure": 3}
    donnees_triees = sorted(
        donnees_filtrees, 
        key=lambda item: ordre_gravite.get(item.get("gravite"), 99)
    )

    # 4. Liste des options pour les menus déroulants
    liste_gravites = sorted(list(set(item.get("gravite") for item in donnees if item.get("gravite"))))
    liste_traitements = sorted(list(set(item.get("traitement") for item in donnees if item.get("traitement"))))
    liste_origines = sorted(list(set(item.get("origine") for item in donnees if item.get("origine"))))

    return render_template(
        "index.html",
        donnees=donnees_triees,
        liste_gravites=liste_gravites,
        liste_traitements=liste_traitements,
        liste_origines=liste_origines,
        filtres_actifs={
            'gravite': gravite_filtre,
            'traitement': traitement_filtre,
            'origine': origine_filtre
        }
    )
@app.route("/detail/<int:id>")
def detail(id):
    donnees = charger_donnees()

    element = next(
        (item for item in donnees if item["id"] == id),
        None
    )

    if element is None:
        abort(404)

    return render_template(
        "detail.html",
        element=element
    )

if __name__ == "__main__":
    app.run(debug=True)
