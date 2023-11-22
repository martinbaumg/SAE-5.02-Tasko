from methods_list import MethodList

# Créer une instance de la classe MethodList
methods = MethodList()

mail = "louis@example.com"
user_password = "password123"

# Appeler get_user sur l'instance créée
methods.check_password_secure(mail, user_password)
