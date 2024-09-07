fetch('https://coordinates-fb940-default-rtdb.asia-southeast1.firebasedatabase.app/coordinates.json')
        .then(response => response.json())
        .then(data => {
            console.log(data); // Log the retrieved data to the console
        })
        .catch(error => console.error('Error retrieving data:', error));