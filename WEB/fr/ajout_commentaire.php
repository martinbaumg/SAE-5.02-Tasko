<?php
// Connexion à la base de données (à remplir avec vos informations de connexion)
$serveur = "45.154.99.10";
$utilisateur = "admin";
$mot_de_passe = "48wGK#t0:ZOx9c";
$base_de_donnees = "commentaires";

$connexion = new mysqli($serveur, $utilisateur, $mot_de_passe, $base_de_donnees);

if ($connexion->connect_error) {
    die("Échec de la connexion : " . $connexion->connect_error);
}

// Récupération des données du formulaire
$nom_utilisateur = $_POST["nom_utilisateur"];
$note = $_POST["note"];
$commentaire = $_POST["commentaire"];

// Évitez les attaques par injection SQL en utilisant des requêtes préparées
$requete = $connexion->prepare("INSERT INTO commentaires (nom_utilisateur, note, commentaire) VALUES (?, ?, ?)");
$requete->bind_param("sis", $nom_utilisateur, $note, $commentaire);

if ($requete->execute()) {
    echo "Commentaire ajouté avec succès.";
} else {
    echo "Échec de l'ajout du commentaire : " . $requete->error;
}

$requete->close();
$connexion->close();
?>
