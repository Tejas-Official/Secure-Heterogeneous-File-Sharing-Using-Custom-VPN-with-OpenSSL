async function uploadFiles() {
    const formData = new FormData();
    const fileInput = document.getElementById('fileInput');
    
    for (const file of fileInput.files) {
        formData.append('files', file);
    }

    try {
        const response = await fetch('http://your-server-address/api/upload', {
            method: 'POST',
            body: formData,
            headers: {
                'Access-Control-Allow-Origin': '*'
            }
        });

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        const result = await response.json();
        console.log('Success:', result);
    } catch (error) {
        console.error('Error:', error);
    }
}
