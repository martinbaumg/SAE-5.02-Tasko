import flet as ft
import bcrypt 
import mysql.connector as mysql
from mysql.connector import Error

# ID de l'utilisateur actuellement connecté
logged_in_user_id = None


# Classe de connexion à la base de données
class DatabaseConnection:
    def __init__(self):
        # Informations de connexion à la base de données
        self.host = "45.154.99.10"
        self.database = "tasko"
        self.user = "admin"
        self.password = "48wGK#t0:ZOx9c"
        self.connection = None
        self.cursor = None

    # Fonction de connexion à la base de données
    def get_connection(self):
        try:
            # Connexion à la base de données
            connection = mysql.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password,
                connect_timeout=100,
            )
            # Vérification de la connexion
            if connection.is_connected():
                return connection
        # Gestion des erreurs
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None

    # Fonction d'exécution des requêtes
    def execute_query(self, query, values, return_lastrowid=False):
        # Connexion à la base de données
        conn = self.get_connection()
        try:
            # Exécution de la requête
            cursor = conn.cursor()
            print(f"Executing query: {query} with values {values}")
            cursor.execute(query, values)
            conn.commit()
            print("Query committed successfully.")
            # Renvoie de la dernière ligne insérée
            if return_lastrowid:
                return cursor.lastrowid 
            # True si la requête a été exécutée avec succès
            return cursor.rowcount > 0
        # Gestion des erreurs
        except Exception as e:
            print(f"Query execution error: {e}")
            conn.rollback()
            print("Query rolled back due to error.")
            return False
        # Fermeture de la connexion
        finally:
            cursor.close()
            conn.close()
            print("Database connection closed.")

    # Fonction d'exécution des requêtes de sélection
    def execute_select_query(self, query, values):
        # Connexion à la base de données
        conn = self.get_connection()
        try:
            # Exécution de la requête
            cursor = conn.cursor()
            print(f"Executing select query: {query} with values {values}")
            cursor.execute(query, values)
            result = cursor.fetchall()  # Fetch all results
            return result
        # Gestion des erreurs
        except Exception as e:
            print(f"Select query execution error: {e}")
            return None
        # Fermeture de la connexion
        finally:
            cursor.close()
            conn.close()
            print("Database connection closed for select query.")

    # Fonction de déconnexion de la base de données
    def disconnect(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
            self.connection = None  # Set to None after closing
            print("MySQL Database connection closed")

if __name__ == "__main__":
    db = DatabaseConnection()
    connection = db.get_connection()
    if connection:
        db.disconnect()



# Classe pour la page de tâches
class ToDO(ft.UserControl):
    # Constructeur de la classe
    def __init__(self):
        super().__init__()
        self.main_container = ft.Ref[ft.Column]()
        self.tasks_view = ft.Ref[ft.Column]()
        self.text_field = ft.Ref[ft.TextField]()
        self.tabs = ft.Ref[ft.Tabs]()
        self.delete_dialog = self.create_delete_dialog()
        self._actual_deleted_item = None
    # Fonction de création de la boîte de dialogue de suppression
    def create_delete_dialog(self):
        return ft.AlertDialog(
            modal=True,
            title=ft.Text("Veuillez confirmer"),
            content=ft.Text("Voulez-vous vraiment supprimer cet élément ?"),
            actions=[
                ft.TextButton("Oui", on_click=self.delete_confirmed),
                ft.TextButton("Non", on_click=self.close_dialog),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
            on_dismiss=lambda e: print("Fermeture de la boîte de dialogue"),
        )

    # Fonction de fermeture de la boîte de dialogue
    def close_dialog(self, e):
        """Lorsque le bouton "Non" du dialogue de suppression est activé, le dialogue est simplement fermé"""
        self.delete_dialog.open = False
        e.page.update()

    # Fonction de suppression confirmée
    def delete_confirmed(self, e):
        """
        Lorsque le bouton "Oui" de la boîte de dialogue de suppression est activé,
        l'élément est supprimé et la boîte de dialogue de suppression est fermée.
        """
        self.delete_item_callback(self._actual_deleted_item)
        self.delete_dialog.open = False
        e.page.update()
        e.page.show_snack_bar(
            ft.SnackBar(
                ft.Text("Tâche supprimée avec succès"),
                action="OK!",
                open=True
            )
        )

    # Fonction d'ouverture de la boîte de dialogue de suppression
    def open_delete_dialog(self, item):
        """ouvre la boîte de dialogue de suppression et conserve une référence à l'élément qui l'a déclenchée (self._actual_deleted_item)"""
        item.page.dialog = self.delete_dialog
        item.page.dialog.open = True
        self._actual_deleted_item = item
        item.page.update()

    # Fonction de rafraîchissement de l'interface utilisateur
    def refresh_ui(self):
        self.update()

    # Fonction de mise à jour de l'interface utilisateur
    def update(self):
        index = self.tabs.selected_index

        for todo_item_control in self.tasks_view.controls:
            # Vérifie si l'élément de la tâche et sa case à cocher sont correctement initialisés
            if todo_item_control and todo_item_control.item_checkbox and todo_item_control.item_checkbox.current:
                checkbox_value = todo_item_control.item_checkbox.current.value
                # Mise à jour de la visibilité en fonction de l'index de l'onglet sélectionné
                todo_item_control.visible = (index == 0 or
                                            (index == 1 and not checkbox_value) or
                                            (index == 2 and checkbox_value))
            else:
                print("La case à cocher ou l'élément de todo n'est pas correctement initialisé")

        super().update()

    # Fonction de suppression d'un élément
    def delete_item_callback(self, item):
        """
        Elle supprime l'élément de la liste des contrôles de la vue courante, puis met à jour la vue
        :param item : L'élément à supprimer
        """
        task_id = item.task_id
        method_list = MethodList()
        if method_list.delete_task(task_id):
            self.tasks_view.controls.remove(item)  # Directly access controls
            self.update()
        else:
            print(f"Erreur lors de la suppression de la tâche avec l'id : {task_id}.")
    
    # Fonction de soumission d'un élément
    def submit_item(self, e: ft.ControlEvent):
        """
        Elle supprime l'élément de la liste des contrôles de la vue courante, puis met à jour la vue
        :param item : L'élément à supprimer
        """
        global logged_in_user_id
        task_name = self.text_field.value
        task_description = "Description"
        task_due_date = "2023-01-01"

        if task_name and logged_in_user_id is not None:
            method_list = MethodList()
            if method_list.add_task(task_name, task_description, task_due_date, logged_in_user_id):
                self.page.show_snack_bar(
                    ft.SnackBar(
                        ft.Text("Tâche ajoutée avec succès"),
                        action="OK",
                        open=True
                    )
                )
                self.refresh_tasks()
            else:
                self.page.show_snack_bar(
                    ft.SnackBar(
                        ft.Text("Erreur lors de l'ajout de la tâche"),
                        action="OK",
                        open=True
                    )
                )

            self.text_field.value = ""
            e.page.update()

    # Fonction de rafraîchissement des tâches
    def clear_and_reload_tasks(self):
        # Effacer les tâches existantes
        self.tasks_view.current.controls.clear()

        # Recharger les tâches de la base de données
        self.load_tasks()
        self.update()
        
    # Fonction de rafraîchissement des tâches
    def refresh_tasks(self):
        """ Effacer et recharger les tâches """
        self.tasks_view.controls.clear()  # Accès direct aux contrôles
        self.load_tasks()

    # Fonction de changement d'onglet
    def tabs_change(self, e):
        """
        Il met à jour l'interface utilisateur lorsque l'utilisateur change d'onglet

        :param e : L'objet de l'événement (ControlEvent)
        """
        self.update()

    # Fonction de changement de texte du compteur
    def counter_text_change(self, e: ft.ControlEvent):
        """
        Elle met à jour le texte du compteur du champ de texte.

        :param e : L'objet de l'événement (ControlEvent)
        """
        self.text_field.counter_text = f'{len(e.data)} caractères'
        self.text_field.update()

    # Fonction de déconnexion
    def logout(self, e):
        """ Déconnexion de l'utilisateur actuel et affichage de la page de connexion. """
        global logged_in_user_id
        logged_in_user_id = None
        show_login_page()

    # Fonction de construction de la page
    def build(self):
        # Création des champs de texte
        self.text_field = ft.TextField(
            helper_text="Que comptez-vous faire ?",
            hint_text="Exemple : Avoir une bonne note",
            counter_text='0 caractères',
            keyboard_type=ft.KeyboardType.TEXT,
            label="Nouvelle tâche",
            expand=True,
            text_size=20,
            tooltip="Champ pour les nouveaux éléments",
            prefix_icon=ft.icons.LIST_ALT_ROUNDED,
            autofocus=True,
            on_change=self.counter_text_change,
            on_submit=self.submit_item
        )
        
        # Création de la vue des tâches
        self.tasks_view = ft.Column(scroll=ft.ScrollMode.ALWAYS)
        
        # Création des onglets
        self.tabs = ft.Tabs(
            tabs=[
                ft.Tab(text='Tous', icon=ft.icons.CHECKLIST_OUTLINED),
                ft.Tab(text='Pas encore fait', icon=ft.icons.CHECK),
                ft.Tab(text='Fait', icon=ft.icons.DONE_ALL)
            ],
            selected_index=0,
            on_change=self.tabs_change
        )

        # Création du bouton de déconnexion
        logout_button = ft.ElevatedButton(
            text="Deconnexion",
            on_click=self.logout
        )

        # Reconstruire le conteneur principal avec le bouton de déconnexion
        self.main_container = ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.Text("Tasko", size=30, weight=ft.FontWeight.BOLD),
                        logout_button,
                    ],
                ),
                ft.Row(
                    controls=[
                        self.text_field,
                        ft.FloatingActionButton(
                            icon=ft.icons.ADD,
                            tooltip="Ajouter une tâche",
                            on_click=self.submit_item
                        )
                    ]
                ),
                self.tabs,
                self.tasks_view
            ],
            spacing=24,
            width=630
        )

        return self.main_container  # Retourner directement le conteneur principal

    # Fonction de chargement des tâches
    def load_tasks(self):
        global logged_in_user_id
        if logged_in_user_id is not None:
            method_list = MethodList()
            tasks = method_list.fetch_tasks(logged_in_user_id)
            if tasks:
                self.tasks_view.controls.clear()
                for task in tasks:
                    task_id, task_name, task_description, task_due_date = task
                    formatted_date = task_due_date.strftime("%Y-%m-%d") if task_due_date else ""
                    todo_item = TodoItem(task_id, task_name, task_description, formatted_date, self, self.update, self.open_delete_dialog)
                    self.tasks_view.controls.append(todo_item)
                self.update()
            else:
                print("Aucune tâches trouvé pour l'utilisateur.")
        else:
            print("Aucun utilisateur connecté.")

# Classe pour les objects de type To-Do Item
class TodoItem(ft.UserControl):
    def __init__(self, task_id, item_text, item_description, item_due_date, todo_page_instance, checkbox_change, delete_dialog_callback):
        """
        La fonction prend sept arguments : task_id, item_text, item_description, item_due_date, todo_page_instance, checkbox_change et delete_dialog_callback. Elle appelle ensuite la fonction
        super(), qui est une fonction spéciale permettant d'appeler une méthode de la classe mère.

        :param task_id : L'identifiant de la tâche
        :param item_text : Le texte qui sera affiché dans l'élément
        :param item_description : La description de l'élément
        :param item_due_date : La date d'échéance de l'élément
        :param todo_page_instance : Il s'agit d'une référence à l'instance de la page ToDO.
        :param checkbox_change : Il s'agit d'une fonction de rappel qui sera appelée lorsque la valeur de la case à cocher changera.
        :param delete_dialog_callback : Il s'agit d'une fonction qui sera appelée lorsque le bouton d'effacement d'un élément est pressé.
        """
        super().__init__()
        self.task_id = task_id
        self.item_text = item_text
        self.item_description = item_description
        self.item_due_date = item_due_date
        self.todo_page_instance = todo_page_instance  # Reference to ToDO instance
        self.open_delete_dialog = delete_dialog_callback
        self.checkbox_change = checkbox_change
        self.normal_view = ft.Ref[ft.Row]()
        self.edit_view = ft.Ref[ft.Row]()
        self.item_checkbox = ft.Ref[ft.Checkbox]()
        self.text_field = ft.Ref[ft.TextField]()
        self.description_field = ft.Ref[ft.TextField]()
        self.due_date_field = ft.Ref[ft.TextField]()

    # Fonction de copie d'un élément
    def copy_item(self, e):
        """
        Copie le texte d'un élément de tâche dans le presse-papiers.

        :param e : L'événement qui a déclenché cette fonction (ControlEvent)
        """
        e.page.set_clipboard(self.item_checkbox.current.label)
        e.page.show_snack_bar(
            ft.SnackBar(
                ft.Text("Contenu copié dans le presse-papiers"),
                action="OK!",
                open=True
            )
        )

    # Fonction d'édition d'un élément
    def edit_item(self, e):
        # Remplir les champs d'édition avec les données actuelles
        self.text_field.current.value = self.item_text
        self.description_field.current.value = self.item_description
        self.due_date_field.current.value = self.item_due_date
        self.normal_view.current.visible = False
        self.edit_view.current.visible = True
        self.text_field.current.autofocus = True
        self.update()

    # Fonction de sauvegarde d'une édition
    def save_edit(self, e):
        # Recueillir des données actualisées
        updated_name = self.text_field.current.value
        updated_description = self.description_field.current.value
        updated_due_date = self.due_date_field.current.value

        # Mise à jour de la base de données
        method_list = MethodList()
        if method_list.update_task(self.task_id, updated_name, updated_description, updated_due_date):
            # Montre un message de succès à l'utilisateur
            e.page.show_snack_bar(ft.SnackBar(ft.Text("Tâche mise à jour avec succès"), action="OK!", open=True))
            self.todo_page_instance.refresh_tasks()
        else:
            # Montre un message d'erreur à l'utilisateur
            e.page.show_snack_bar(ft.SnackBar(ft.Text("Erreur lors de la mise à jour de la tâche"), action="OK!", open=True))

        # Fermer la vue d'édition et afficher la vue normale
        self.normal_view.current.visible = True
        self.edit_view.current.visible = False
        self.update()

    # Fonction de suppression d'un élément
    def delete_item(self, e):
        """
        Elle appelle la fonction delete_callback qui supprimera cet élément de la liste des tâches (tasks_view).

        :param e : L'événement qui a déclenché le rappel (ControlEvent)
        """
        self.open_delete_dialog(self)

    # Fonction de changement de valeur de la case à cocher
    def item_checkbox_value_change(self, e):
        """
        Écoute les changements de la valeur (bool) de notre case à cocher.
        Pour tout changement, nous mettons à jour l'interface utilisateur pour afficher correctement l'élément dans l'onglet correspondant.

        :param e : L'objet événement (ControlEvent)
        """
        self.checkbox_change()

    # Fonction de construction de l'élément
    def build(self):
        """
    Construction de l'interface utilisateur d'un élément à faire.

                            Row(Checkbox et une Row avec deux IconButtons)
        :return : Column --<
                            Ligne (Champ de texte et bouton de mise à jour)
        """
        return ft.Column(
            controls=[
                ft.Row(
                    # La vue normale est visible par défaut
                    ref=self.normal_view,
                    controls=[
                        ft.Checkbox(
                            ref=self.item_checkbox,
                            label=self.item_text,
                            value=False,
                            on_change=self.item_checkbox_value_change),
                        ft.Text(self.item_description),  # Affiche la description de l'élément
                        ft.Text(self.item_due_date if self.item_due_date else ""),  # Affiche la date d'échéance de l'élément
                        ft.Row(
                            controls=[
                                # Création des boutons d'actions
                                ft.IconButton(
                                    icon=ft.icons.COPY,
                                    icon_color=ft.colors.GREEN_300,
                                    tooltip="copier",
                                    on_click=self.copy_item,
                                ),
                                ft.IconButton(
                                    icon=ft.icons.EDIT,
                                    icon_color=ft.colors.GREEN_500,
                                    on_click=self.edit_item,
                                    tooltip="modifier",
                                ),
                                ft.IconButton(
                                    icon=ft.icons.DELETE_FOREVER,
                                    icon_color=ft.colors.RED_300,
                                    tooltip="supprimer",
                                    on_click=self.delete_item,
                                ),
                            ]
                        )
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                ),
                # La vue d'édition est invisible par défaut
                ft.Row(
                    ref=self.edit_view,
                    visible=False,
                    controls=[
                        ft.TextField(
                            ref=self.text_field,
                            value=self.item_text,
                            tooltip="Champ pour modifier l'élément",
                            autofocus=False,
                            label="Modifier l'élément",
                            expand=True,
                            on_submit=self.save_edit,
                            suffix=ft.ElevatedButton(text="Modifier l'élément", on_click=self.save_edit)),
                            ft.TextField(
                                ref=self.description_field,
                                label="Description",
                                value=self.item_description,
                                expand=True
                            ),
                            ft.TextField(
                                ref=self.due_date_field,
                                label="Date d'échéance",
                                value=self.item_due_date,
                                expand=True
                            )
                    ],
                )
            ],
        )

# Classe pour les requêtes
class RequestList:
    # Fonction d'ajout d'un utilisateur
    @staticmethod
    def add_user(mail, name, hashed_password, salt):
        rights_id = 1  # 1 = user, 2 = admin

        # Utilisation de paramètres de requête pour éviter les attaques par injection SQL
        query = "INSERT INTO USER (mail, password, name, rights_id, salt) VALUES (%s, %s, %s, %s, %s)"

        # Transmettre les valeurs sous forme de tuple pour les paramètres de la requête
        values = (mail, hashed_password, name, rights_id, salt)

        return query, values

    # Fonction d'authentification d'un utilisateur
    @staticmethod
    def authenticate_user(mail):
        return "SELECT password, salt FROM USER WHERE mail = %s", (mail,)
    
# Classe pour les méthodes
class MethodList:
    # Constructeur de la classe
    def __init__(self):
        self.db = DatabaseConnection()

    # Fonction d'ajout d'un utilisateur
    def register_user(self, mail, name, password):
        self.db.get_connection()
        try:
            # Hacher le mot de passe
            salt = bcrypt.gensalt()
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

            # Convertir le hachage et le sel en chaînes de caractères
            salt_str = salt.decode('utf-8')
            hashed_password_str = hashed_password.decode('utf-8')

            # Préparer et exécuter la requête
            query, values = RequestList.add_user(mail, name, hashed_password_str, salt_str)
            
            # Enregistrer la requête et les valeurs
            print(f"Tentative d'enregistrement d'un utilisateur avec une requête : {query} et valeurs : {values}")

            result = self.db.execute_query(query, values)
            if result is not None:
                print("Enregistrement de l'utilisateur réussi.")
                print(f"Resultat: {result}")
            else:
                print("L'enregistrement de l'utilisateur a échoué - aucun résultat n'a été obtenu.")
        except Exception as e:
            print(f"Une erreur s'est produite lors de l'enregistrement de l'utilisateur : {e}")
        finally:
            self.db.disconnect()

    # Fonction d'authentification d'un utilisateur
    def login_user(self, mail, password):
        self.db.get_connection()
        query, values = RequestList.authenticate_user(mail)
        result = self.db.execute_select_query(query, values)
        if result:
            stored_password, salt = result[0]
            if bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8')):
                query = "SELECT id FROM USER WHERE mail = %s"
                user_id_result = self.db.execute_select_query(query, (mail,))
                user_id = user_id_result[0][0] if user_id_result else None
                self.db.disconnect()
                print(f"L'utilisateur avec l'identifiant {user_id} s'est connecté avec succès.")
                return True, user_id
            else:
                print("Mot de passe incorrect.")
                self.db.disconnect()
                return False, None
        else:
            print("L'utilisateur n'existe pas.")
            self.db.disconnect()
            return False, None
    
    # Fonction de récupération des tâches
    def fetch_tasks(self, user_id):
        self.db.get_connection()
        try:
            query = """
                SELECT TASK.id, TASK.name, TASK.description, TASK.due_date
                FROM TASK
                JOIN TASK_USER ON TASK.id = TASK_USER.task_id
                WHERE TASK_USER.user_id = %s
            """
            values = (user_id,)
            tasks = self.db.execute_select_query(query, values)
            return tasks
        except Exception as e:
            print(f"Une erreur s'est produite lors de la récupération des tâches : {e}")
            return []
        finally:
            self.db.disconnect()
    
    def delete_task(self, task_id):
        self.db.get_connection()
        try:
            # On commence par supprimer les liens entre la tâche et les utilisateurs dans TASK_USER
            task_user_query = "DELETE FROM TASK_USER WHERE task_id = %s"
            task_user_values = (task_id,)
            if not self.db.execute_query(task_user_query, task_user_values):
                print(f"Failed to delete task-user linkage for task id {task_id}.")
                return False

            # Ensuite, on supprime la tâche elle-même
            task_query = "DELETE FROM TASK WHERE id = %s"
            task_values = (task_id,)

            if self.db.execute_query(task_query, task_values):
                print(f"La tâche avec l'identifiant {task_id} a été supprimée avec succès..")
                return True
            else:
                print(f"Échec de la suppression de la tâche avec l'identifiant : {task_id}.")
                return False
        except Exception as e:
            print(f"Une erreur s'est produite lors de la suppression d'une tâche : {e}")
            return False
        finally:
            self.db.disconnect()

    # Fonction de mise à jour d'une tâche
    def update_task(self, task_id, name, description, due_date):
        self.db.get_connection()
        try:
            query = "UPDATE TASK SET name = %s, description = %s, due_date = %s WHERE id = %s"
            values = (name, description, due_date, task_id)
            result = self.db.execute_query(query, values)
            return result  # Renverra True si la requête a été exécutée avec succès
        except Exception as e:
            print(f"Une erreur s'est produite lors de la mise à jour des tâches : {e}")
            return False
        finally:
            self.db.disconnect()

    # Fonction d'ajout d'une tâche
    def add_task(self, name, description, due_date, user_id):
        self.db.get_connection()
        try:
            # Ajout dans la table TASK
            task_query = "INSERT INTO TASK (name, description, due_date) VALUES (%s, %s, %s)"
            task_values = (name, description, due_date)
            task_result = self.db.execute_query(task_query, task_values, return_lastrowid=True)
            
            if task_result:
                task_id = task_result

                # Ajout dans la table TASK_USER
                task_user_query = "INSERT INTO TASK_USER (task_id, user_id) VALUES (%s, %s)"
                task_user_values = (task_id, user_id)
                self.db.execute_query(task_user_query, task_user_values)

                return True
            else:
                return False
        except Exception as e:
            print(f"Une erreur s'est produite lors de l'ajout d'une tâche : {e}")
            return False
        finally:
            self.db.disconnect()


# Classe pour la page de connexion
class LoginPage(ft.UserControl):
    # Constructeur de la classe
    def __init__(self, on_login_success, on_signup_page):
        super().__init__()
        self.email_input = ft.Ref[ft.TextField]()
        self.password_input = ft.Ref[ft.TextField]()
        self.on_login_success = on_login_success
        self.on_signup_page = on_signup_page

    # Fonction de construction de la page
    def build(self):
        return ft.Column(
            controls=[
                ft.Text("Connexion", size=50, weight=ft.FontWeight.BOLD),
                ft.Text("Content de vous revoir sur Tasko !", size=20),
                ft.TextField(ref=self.email_input, hint_text="Email"),
                ft.TextField(ref=self.password_input, hint_text="Mot de passe", password=True),
                ft.Row(
                    controls=[
                        ft.ElevatedButton(text="Connexion", on_click=self.on_login_click),
                        ft.TextButton(
                            "Vous n'avez pas de compte ? S'inscrire ici",
                            on_click=lambda e: self.on_signup_page()
                        )
                    ],
                    spacing=10
                )
            ],
            spacing=24,
            width=630
        )
    
    # Fonction de connexion
    def on_login_click(self, e):
        email = self.email_input.current.value
        password = self.password_input.current.value
        method_list = MethodList()
        login_success, user_id = method_list.login_user(email, password)
        if login_success:
            global logged_in_user_id
            logged_in_user_id = user_id
            self.on_login_success()
        else:
            e.page.show_snack_bar(ft.SnackBar(ft.Text("Erreur lors de la connexion"), action="OK!", open=True))

# Classe pour la page d'inscription
class SignupPage(ft.UserControl):
    # Constructeur de la classe
    def __init__(self, on_login_page):
        super().__init__()
        self.on_login_page = on_login_page
        self.email_input = ft.Ref[ft.TextField]()
        self.name_input = ft.Ref[ft.TextField]()
        self.password_input = ft.Ref[ft.TextField]()
        self.confirm_password_input = ft.Ref[ft.TextField]()
        self.error_dialog = ft.Ref[ft.AlertDialog]()

    # Fonction de construction de la page
    def build(self):
        return ft.Column(
            controls=[
                ft.Text("S'inscrire", size=50, weight=ft.FontWeight.BOLD),
                ft.Text("Bienvenue sur Tasko !", size=20),
                ft.TextField(ref=self.email_input, hint_text="Email"),
                ft.TextField(ref=self.name_input, hint_text="Nom"),
                ft.TextField(ref=self.password_input, hint_text="Mot de passe", password=True),
                ft.TextField(ref=self.confirm_password_input, hint_text="Confirmez votre mot de passe", password=True),
                ft.Row(
                    controls=[
                        ft.ElevatedButton(text="S'inscrire", on_click=self.on_signup_click),
                        ft.TextButton(
                            "Vous avez déjà un compte ? Se connecter ici",
                            on_click=lambda e: self.on_login_page()
                        )
                    ],
                    spacing=10
                )
            ],
            spacing=24,
            width=630
        )
    # Fonction d'inscription
    def on_signup_click(self, e):
        email = self.email_input.current.value
        name = self.name_input.current.value
        password = self.password_input.current.value
        confirm_password = self.confirm_password_input.current.value
        
        # Vérifier si un des champs est vide
        if not all([email, name, password, confirm_password]):
            e.page.show_snack_bar(ft.SnackBar(ft.Text("Erreur : Tous les champs doivent être remplis."), action="OK!", open=True))
            print("Tous les champs doivent être remplis.")
            return  # Arrêter l'exécution si un champ est vide
        
        if password == confirm_password:
            MethodList().register_user(email, name, password)
            e.page.show_snack_bar(ft.SnackBar(ft.Text("Enregistrement avec succès."), action="OK!", open=True))
            self.on_login_page()  # Naviguer vers la page de connexion après l'inscription
        else:
            e.page.show_snack_bar(ft.SnackBar(ft.Text("Erreur : Les mots de passe ne sont pas les mêmes."), action="OK!", open=True))
            print("Les mots de passe ne sont pas les mêmes.")

# Fonction principale
def main(page: ft.Page):
    # Définir les propriétés de la page
    global show_todo_page, show_login_page, show_signup_page
    page.title = "Application TASKO"
    page.window_width = 900
    page.window_height = 700
    page.horizontal_alignment = "center"
    page.vertical_alignment = "start"
    page.fonts = {
        "SF-simple": "/fonts/San-Francisco/SFUIDisplay-Light.ttf",
        "SF-bold": "/fonts/San-Francisco/SFUIDisplay-Bold.ttf"
    }
    page.theme_mode = "light"
    page.theme = ft.Theme(
        font_family="SF-simple",
        use_material3=True,
        visual_density=ft.ThemeVisualDensity.COMPACT,
        color_scheme_seed='green',
    )

    # Définir les fonctions de navigation
    def show_todo_page():
        global todo_page
        try:
            todo_page = ToDO()
            if todo_page is not None:
                page.controls.clear()
                page.add(todo_page)
                todo_page.load_tasks()
            else:
                print("Erreur : todo_page est None.")
        except Exception as e:
            print(f"Erreur dans show_todo_page : {e}")

    # Définir les fonctions de navigation
    def show_login_page():
        login_page = LoginPage(on_login_success=show_todo_page, on_signup_page=show_signup_page)
        page.controls.clear()
        page.add(login_page)

    # Définir les fonctions de navigation
    def show_signup_page():
        signup_page = SignupPage(on_login_page=show_login_page)
        page.controls.clear()
        page.add(signup_page)

    show_login_page()

# Lancement de l'application
ft.app(target=main, assets_dir="assets")