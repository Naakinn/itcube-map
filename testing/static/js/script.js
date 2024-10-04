let dropArea = document.getElementById('drop-area');
let image = document.getElementById('image');

// Prevent default behavior
['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
	dropArea.addEventListener(eventName, preventDefaults, false);
	document.body.addEventListener(eventName, preventDefaults, false);
});

function preventDefaults(e) {
	e.preventDefault();
	e.stopPropagation();
}

['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
	dropArea.addEventListener(eventName, highlight, false);
});

function highlight(e) {
	if (e.type === 'dragenter' || e.type === 'dragover') {
		dropArea.classList.add('highlight');
	} else {
		dropArea.classList.remove('highlight');
	}
}

function handleDrop(e) {
	let dt = e.dataTransfer;
	let files = dt.files;

	if (files.length) {
		handleFiles(files);
	}
}

function handleFiles(files) {
	([...files]).forEach(file => {
		if (file.type.startsWith('image/')) {
			const reader = new FileReader();
			reader.onload = () => {
				image.src = reader.result;
				image.style.display = 'block'; // Show image
				dropArea.style.border = "0px";
				dropArea.innerHTML = ''; // Delete text
				dropArea.appendChild(image); // Replace text with image
			};
			reader.readAsDataURL(file);
		} else {
			alert('Anything beyond image is not allowed here.');
		}
	});
}

dropArea.addEventListener('drop', handleDrop, false);

