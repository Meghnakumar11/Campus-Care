document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('contactform');
    
    if (form) {
        form.addEventListener('submit', async function(event) {
            event.preventDefault();
            
            const data = {
                name: document.getElementById('name').value,
                rollno: document.getElementById('rollno').value,
                service: document.getElementById('service').value,
                email: document.getElementById('email').value,
                message: document.getElementById('message').value
            };

            try {
                const response = await fetch('http://localhost:5000/consultation', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(data)
                });
                const result = await response.json();

                if (response.ok) {
                    alert('✅ Thank you! Your consultation request has been submitted successfully.');
                    form.reset();
                } else {
                    alert('❌ Error: ' + (result.error || 'Something went wrong'));
                }
            } catch (error) {
                console.error('Error:', error);
                alert('❌ Could not connect to the server. Please make sure the backend is running.');
            }
        });
    }
});