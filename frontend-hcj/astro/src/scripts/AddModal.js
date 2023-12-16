// Fonction pour ouvrir le modal
function openModal() {
   var modal = document.getElementById('crud-modal');
   if (modal) {
     modal.classList.remove('hidden');
   } else {
     console.error("L'élément avec l'ID 'crud-modal' n'a pas été trouvé.");
   }
 }
 
 // Fonction pour fermer le modal
 function closeModal() {
   var modal = document.getElementById('crud-modal');
   if (modal) {
     modal.classList.add('hidden');
   } else {
     console.error("L'élément avec l'ID 'crud-modal' n'a pas été trouvé.");
   }
 }
 
 // Associer les fonctions aux boutons
 var openBtn = document.getElementById('openCrudModal');
 var closeBtn = document.getElementById('closeCrudModal');
 
 if (openBtn) {
   openBtn.addEventListener('click', openModal);
 } else {
   console.error("L'élément avec l'ID 'openCrudModal' n'a pas été trouvé.");
 }
 
 if (closeBtn) {
   closeBtn.addEventListener('click', closeModal);
 } else {
   console.error("L'élément avec l'ID 'closeCrudModal' n'a pas été trouvé.");
 }
 