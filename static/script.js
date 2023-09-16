function enregistrerParticipant() {
  const nom = document.getElementById("name").value;

  fetch("http://127.0.0.1:5000/enregistrer_participant", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      nom: nom,
    }),
  })
    .then((response) => response.json())
    .then((data) => {
      // Afficher un message incluant la couleur de l'équipe
      alert(
        `Participant enregistré avec succès! Votre couleur d'équipe est : ${data.couleur_equipe}`
      );
      // Rafraîchir la page pour mettre à jour la liste des participants
      location.reload();
    })
    .catch((error) => console.error("Erreur :", error));
}
