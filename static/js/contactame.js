
document.getElementById('contactForm').addEventListener('submit', function(event) {
    event.preventDefault();  


    const nombre = document.getElementById('nombre').value;
    const email = document.getElementById('email').value;
    const telefono = document.getElementById('telefono').value;
    const mensaje = document.getElementById('mensaje').value;

    
    const formData = {
        nombre: nombre,
        correo: email,
        telefono: telefono,
        mensaje: mensaje
    };

    
    fetch('/insertar_contacto', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData)
    })
    .then(response => response.json()) 
    .then(data => {
        if (data.success) {
            
            alert('Mensaje enviado correctamente');
        } else {
           
            alert('Hubo un error: ' + data.mensaje);
        }
    })
    .catch(error => {
        
        console.error('Error:', error);
        alert('Hubo un error inesperado');
    });
});
