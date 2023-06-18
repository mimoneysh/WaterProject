function predictPotability() {
    var form = document.getElementById("predictionForm");
    var formData = new FormData(form);

    fetch('/predict', {
        method: 'POST',
        body: formData
    })
    .then(function(response) {
        return response.json();
    })
    .then(function(result) {
        var predictionResult = document.getElementById("predictionResult");
        predictionResult.innerHTML = "Water is " + result.prediction;
    })
    .catch(function(error) {
        console.log('Error:', error);
    });
}
