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

// Récupération des commentaires depuis la base de données
$requete = "SELECT nom_utilisateur, note, commentaire FROM commentaires";
$resultat = $connexion->query($requete);

if ($resultat->num_rows > 0) {
    while ($row = $resultat->fetch_assoc()) {
        echo "<div class='commentaire'>";
        echo "<strong>Utilisateur : " . $row["nom_utilisateur"] . "</strong><br>";
        echo "Note : " . $row["note"] . "/5<br>";
        echo "Commentaire : " . $row["commentaire"];
        echo "</div>";
    }
} else {
    echo "Aucun commentaire n'a été trouvé.";
}

$connexion->close();
?>
