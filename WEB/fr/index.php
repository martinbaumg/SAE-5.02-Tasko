<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="cssfile.css">
    <title>Tasko</title>
</head>
<body>
    <header>
        <nav class="navbar">
            <picture class="logo">
                <source media="(min-width: 320px)" srcset="Tasko_320.png">
                <source media="(min-width: 641px)" srcset="Tasko_320.png">
                <source media="(min-width: 961px)" srcset="Tasko_461.png">
                <source media="(min-width: 1025px)" srcset="Tasko_461.png">
                <source media="(min-width: 1281px)" srcset="Tasko_461.png">
                <img src="Tasko_320.png">
            </picture>
            <ul class="links">
              <li class="under-menu"><a href="file:///home/sthomas/Documents/GitHub/SAE-5.02-Tasko/WEB/fr/index.php">Acceuil</a>
              </li>
              <li class="under-menu"><a href="Tasko.html">Produit </a>
                <ul class="under-menu-under">
                  <li><a href="file:///home/sthomas/Documents/GitHub/SAE-5.02-Tasko/Tasko.html">Tasko</a></li>
                </ul>
              </li>
              <li><a href="mailto:tasko@totor.pro">Contact</a></li>
              <li class="under-menu"><a href="#">A propos</a>
                <ul class="under-menu-under">
                    <li><a href="file:///home/sthomas/Documents/GitHub/SAE-5.02-Tasko/WEB/fr/taskoteam.html">L'équipe du projet</a></li>
                </ul>
              </li>  
                <li class="under-menu"><a href="#">Langue &ensp;</a>
                    <ul class="under-menu-under">
                        <li><a href="/WEB/fr/index.html"><img class="imglg" src="france.png" alt=Drapeau Français> French</a></li>
                        <li><a href="/WEB/de/index.html"><img class="imglg" src="germany.png" alt="Drapeau Allemand"> Deutsch</a></li>
                        <li><a href="/WEB/en/index.html"><img class="imglg" src="etats-unis.png" alt="Drapeau Englais"> English</a></li>
                        <li><a href="/WEB/es/index.html"><img class="imglg" src="espagnol.png" alt="Drapeau Espagnol"> Español</a></li>
                        <li><a href="/WEB/jp/index.html"><img class="imglg" src="japon.png" alt="Drapeau Japonais"> 日本語</a></li>
                        <li><a href="/WEB/ru/index.html"><img class="imglg" src="russie.png" alt="Drapeau Russe"> русский</a></li>
                    </ul>
                </li>    
            </ul>
          </nav>
          
    </header>
    
    <main>
    <div class="about_us">
            <h1 class="titre2">A propos de nous</h1>
            <p class="texte">Tasko est une application de gestion de tâches qui vous permet de gérer vos tâches quotidiennes, hebdomadaires et mensuelles. Vous pouvez également créer des tâches récurrentes et des tâches à durée limitée. Tasko vous permet de gérer vos tâches de manière simple et efficace. </p>
            


        </div>
        
        <div class="comment_app">
            <h1 class="titre1">Commentaire</h1>
            <form action="ajout_commentaire.php" method="post">
                <label for="nom_utilisateur">Nom d'utilisateur :</label>
                <input type="text" id="nom_utilisateur" name="nom_utilisateur" required>
        
                <label for="note">Note (de 1 à 5) :</label>
                <input type="number" id="note" name="note" min="1" max="5" required>
        
                <label for="commentaire">Commentaire :</label>
                <textarea id="commentaire" name="commentaire" required></textarea>
        
                <button type="submit">Ajouter le commentaire</button>
            </form>
        </div>
        <!--Afficher les commentaires dans la BDD -->
        <div class="afficher_commentaire">
            <h1 class="titre2">Commentaires</h1>
            <?php
               include 'afficher_commentaire.php';
            ?>



    </main>


    <footer>
        <div class="link_project_github"><p>© 2023 Tasko <a href="https://github.com/martinbaumg/SAE-5.02-Tasko">Voir le projet sur GitHub</a></p></div>
    </footer>
    <script src="javascript.js"></script>





</body>
</html>
