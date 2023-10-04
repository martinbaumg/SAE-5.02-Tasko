// Select all list items representing folders
const folders = document.querySelectorAll('.directory-list > li');

// Add an event handler for each folder
folders.forEach(folder => {
	folder.addEventListener('click', event => {
		// Prevent event propagation to parent elements
		event.stopPropagation();

		// Get the sub-folder of the current list item
		const subFolder = folder.querySelector('ul');
		// Check if there is a sub-folder
		if (subFolder) {
			// Check if it has the 'visible' class
			const isVisible = subFolder.classList.contains('visible');
			// If the sub-folder is visible, hide it; otherwise, show it
			if (isVisible) {
				subFolder.classList.remove('visible');
			} else {
				subFolder.classList.add('visible');
			}
		}
	});
});

// Add an event handler to the document to hide sub-folders when clicked outside of them
document.addEventListener('click', () => {
	folders.forEach(folder => {
		const subFolder = folder.querySelector('ul');
		if (subFolder) {
			subFolder.classList.remove('visible');
		}
	});
});
