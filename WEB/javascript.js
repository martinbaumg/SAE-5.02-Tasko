const langSelectFooter = document.getElementById('lang-select-footer');

// Permet de savoir si il y a changement de langue au sein du site 
langSelectFooter.addEventListener('change', function() {
    const selectedLang = langSelectFooter.value;
});

// Je met la langue du site en français de base
langSelectFooter.value = 'fr';




