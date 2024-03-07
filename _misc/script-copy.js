function runPageSpeedTest() {
    const urlInput = document.getElementById('urlInput').value;
    const resultsDiv = document.getElementById('results');
    const loadingDiv = document.querySelector('.loading');

    if (!urlInput) {
        resultsDiv.innerHTML = "<p>Please enter a valid URL.</p>";
        return;
    }

    // Show loading animation
    loadingDiv.style.display = 'inline-block';

    // Clear previous results
    resultsDiv.innerHTML = "<p>Loading...</p>";

    // Make API request
    fetch(`/api/pagespeed?url=${encodeURIComponent(urlInput)}`)
        .then(response => response.json())
        .then(data => {
            // Hide loading animation
            loadingDiv.style.display = 'none';

            // Display results
            const score = data.lighthouseResult.categories.performance.score;
            const metrics = data.lighthouseResult.audits;

            let resultsHTML = `<p>Overall Score: ${score}</p>`;
            resultsHTML += "<h2>Metrics:</h2>";

            // Display individual metrics
            for (const metric in metrics) {
                const metricValue = metrics[metric].numericValue;
                resultsHTML += `<p>${metric}: ${metricValue}</p>`;
            }

            resultsDiv.innerHTML = resultsHTML;
        })
        .catch(error => {
            console.error("Error fetching data:", error);

            // Hide loading animation
            loadingDiv.style.display = 'none';

            resultsDiv.innerHTML = "<p>Error fetching data. Please try again.</p>";
        });
}
