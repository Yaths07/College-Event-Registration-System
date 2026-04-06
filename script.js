// Wait for the user to click the "Submit" button
document.getElementById('regForm').addEventListener('submit', function(e) {
    e.preventDefault(); // This stops the page from refreshing!

    // 1. Grab the data from the input fields
    const studentData = {
        full_name: document.getElementById('name').value,
        student_id: document.getElementById('sid').value,
        course: document.getElementById('course').value,
        event_name: document.getElementById('event').value
    };

    // 2. Send the data to your Python (Flask) backend
    fetch('/register', {
        method: 'POST',
        headers: { 
            'Content-Type': 'application/json' 
        },
        body: JSON.stringify(studentData)
    })
    .then(response => response.json())
    .then(data => {
        // 3. Show the success message in the <p id="msg"></p> tag
        const messageElement = document.getElementById('msg');
        messageElement.innerText = data.message;
        
        // 4. Clear the form so it's ready for the next person
        document.getElementById('regForm').reset();
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('msg').innerText = "Something went wrong. Check XAMPP!";
        document.getElementById('msg').style.color = "red";
    });
});