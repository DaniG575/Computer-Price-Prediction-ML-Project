document.getElementById('price-prediction-form').addEventListener('submit', function(event) {
    event.preventDefault();

    const form = document.getElementById('price-prediction-form');
    const formData = new FormData(form);

    fetch('/api/predict_price', {
        method: 'POST',
        body: formData
    })
    .then(response => {
        console.log('Response received:', response);
        if (!response.ok) {
            throw new Error(`Network response was not ok: ${response.statusText}`);
        }
        return response.json();
    })
    .then(data => {
        console.log('Data received:', data);
        if (data.predictedPrice !== undefined) {
            document.getElementById('price').textContent = `Predicted Price: $${data.predictedPrice}`;
        } else {
            throw new Error('Price prediction not available.');
        }
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('price').textContent = `Error: ${error.message}`;
    });
});

