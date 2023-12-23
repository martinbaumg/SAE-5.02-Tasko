import bcrypt


# Fonction pour hacher un mot de passe avec un sel
def hash_password(password):
    # Générer un sel aléatoire
    salt = bcrypt.gensalt()

    # Hacher le mot de passe avec le sel
    hashed_password = bcrypt.hashpw(password.encode("utf-8"), salt)

    return salt, hashed_password


# Fonction pour vérifier un mot de passe
def check_password(input_password, stored_salt, stored_hashed_password):
    # Hacher le mot de passe d'entrée avec le sel stocké
    hashed_input_password = bcrypt.hashpw(input_password.encode("utf-8"), stored_salt)

    # Vérifier si les hachages correspondent
    return hashed_input_password == stored_hashed_password


# Entrer un mot de passe pour le hacher
password_to_hash = input("Entrez le mot de passe à hacher : ")
salt, hashed_password = hash_password(password_to_hash)

print("Mot de passe haché :", hashed_password)
print("Sel utilisé :", salt)

# Entrer un mot de passe pour le vérifier
password_to_check = input("Entrez le mot de passe pour vérification : ")
if check_password(password_to_check, salt, hashed_password):
    print("Mot de passe correct.")
else:
    print("Mot de passe incorrect.")
