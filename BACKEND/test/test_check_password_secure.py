import database_connection
import bcrypt

try:
    db = database_connection.DatabaseConnection()
    db.connect()

    mail = "louis@example.com"
    user_password = "password123"  # Renamed to user_password for clarity

    query = "SELECT password FROM `USER` WHERE mail = %s"
    values = (mail,)

    print(f"Executing query: {query} with values {values}")

    db.execute_query(query, values)
    result = db.get_result(query, values)

    if result:
        hashed_password = result[0][0]  # Get the hashed password from the result
        if bcrypt.checkpw(user_password.encode(), hashed_password.encode()):
            print("Le mot de passe est correct.")
        else:
            print("Le mot de passe est incorrect.")
    else:
        print("Aucun utilisateur trouvé avec cet e-mail.")

    db.disconnect()

except Exception as e:
    print(f"Une erreur s'est produite : {e}")
