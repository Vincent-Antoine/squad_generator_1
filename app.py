from flask import Flask, render_template, request, jsonify
import random


app = Flask(__name__)
participants = []

# Couleurs d'équipe possibles
team_colors = ['Rouge', 'Bleu', 'Vert', 'Jaune','Violet', 'Rose']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/enregistrer_participant', methods=['POST'])
def enregistrer_participant():
    participant = request.get_json()  # Utilisez get_json() pour obtenir les données
    participant['couleur_equipe'] = random.choice(team_colors)
    participants.append(participant)
    return jsonify({'message': 'Participant enregistré avec succès!', 'couleur_equipe': participant['couleur_equipe']})



def generer_equipes(participants, couleurs_equipes):
    equipes = {couleur: [] for couleur in couleurs_equipes}
    random.shuffle(participants)

    # Calculer le nombre moyen de participants par équipe
    moyenne_participants_par_equipe = len(participants) // len(couleurs_equipes)

    i = 0
    for participant in participants:
        # Répartir les participants en fonction des couleurs d'équipe
        couleur_equipe = couleurs_equipes[i % len(couleurs_equipes)]
        equipes[couleur_equipe].append(participant)

        # Vérifier si l'équipe a atteint la moyenne, passer à l'équipe suivante si nécessaire
        if len(equipes[couleur_equipe]) >= moyenne_participants_par_equipe:
            i += 1

    return equipes

@app.route('/liste_participants', methods=['GET'])
def liste_participants():
    # Utilisez les nouvelles couleurs d'équipe
    equipes = generer_equipes(participants, team_colors)
    return render_template('liste_participants.html', participants=participants, equipes=equipes)


@app.route('/equipe/<nom_participant>', methods=['GET'])
def afficher_couleur_equipe(nom_participant):
    for participant in participants:
        if participant['nom'] == nom_participant:
            return jsonify({'couleur_equipe': participant['couleur_equipe']})

    return jsonify({'message': 'Participant non trouvé.'}), 404

@app.route('/reinitialiser_participants', methods=['POST'])
def reinitialiser_participants():
    participants.clear()
    return jsonify({'message': 'Liste des participants réinitialisée avec succès!'})


@app.route('/enregistrement_mobile', methods=['GET'])
def enregistrement_mobile():
    nom = request.args.get('nom')
    return render_template('enregistrement_mobile.html', nom=nom)


if __name__ == '__main__':
    app.run(debug=True)


