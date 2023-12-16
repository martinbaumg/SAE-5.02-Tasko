// Fonction pour ouvrir le modal
function openModal() {
  var modal = document.getElementById('popup-modal');
  if (modal) {
    modal.classList.remove('hidden');
  } else {
    console.error("L'élément avec l'ID 'popup-modal' n'a pas été trouvé.");
  }
}

// Fonction pour fermer le modal
function closeModal() {
  var modal = document.getElementById('popup-modal');
  if (modal) {
    modal.classList.add('hidden');
  } else {
    console.error("L'élément avec l'ID 'popup-modal' n'a pas été trouvé.");
  }
}

// Associer les fonctions aux boutons
var openBtn = document.getElementById('openModalBtn');
var closeBtn = document.getElementById('closeModalBtn');

if (openBtn) {
  openBtn.addEventListener('click', openModal);
} else {
  console.error("L'élément avec l'ID 'openModalBtn' n'a pas été trouvé.");
}

if (closeBtn) {
  closeBtn.addEventListener('click', closeModal);
} else {
  console.error("L'élément avec l'ID 'closeModalBtn' n'a pas été trouvé.");
}
