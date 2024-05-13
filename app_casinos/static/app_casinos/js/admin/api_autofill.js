{

    window.apiAutoFill = function (_method, casinoName, dataAutoFill = null) {
        const requestUrls = {
            'POST': '/api/v1/data-autofill-bonus/create/',
            'GET': `/api/v1/data-autofill-bonus/${casinoName}/`,
            'PUT': `/api/v1/data-autofill-bonus/${casinoName}/`,
        };

        let requestOptions = {
            method: _method,
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrf_token,
            }
        };

        if (_method === 'POST' || _method === 'PUT') {
            const dataToSave = { name: casinoName, data: dataAutoFill };
            requestOptions.body = JSON.stringify(dataToSave);
        }

        return new Promise((resolve, reject) => {
            fetch(requestUrls[_method], requestOptions)
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Network response was not ok');
                    }
                    return response.json();
                })
                .then(data => {
                    resolve(data);
                })
                .catch(error => {
                    console.error('!!! There was a problem saving/retrieving the data:', error);
                    reject(error);
                });
        });
    }

}