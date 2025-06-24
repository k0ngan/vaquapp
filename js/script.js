function toggleSidebar() {
  document.querySelector('.sidebar').classList.toggle('closed');
}

// Scroll suave para anclas
document.querySelectorAll('a[href^="#"]').forEach(link => {
  link.addEventListener('click', e => {
    e.preventDefault();
    const target = document.querySelector(link.getAttribute('href'));
    if (target) {
      target.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  });
});

// Ejemplo de conexión con backend Python (Flask/FastAPI)
function consultarBackend() {
  fetch('localhost:8501')
    .then(response => response.json())
    .then(data => {
      console.log('Respuesta del backend:', data);
      alert('Respuesta del backend: ' + JSON.stringify(data));
    })
    .catch(error => {
      console.error('Error al conectar con el backend:', error);
      alert('No se pudo conectar con el backend.');
    });
}
