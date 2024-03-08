function runPageSpeedTest() {
    const urlInput = document.getElementById('urlInput').value;
    const deviceSelect = document.getElementById('deviceSelect').value;
    const throttleSelect = document.getElementById('throttleSelect').value;
    const resultsDiv = document.getElementById('results');

    // Check if URL is provided
    if (!urlInput) {
        resultsDiv.innerHTML = "<p>Please enter a valid URL.</p>";
        return;
    }

    // Clear previous results
    resultsDiv.innerHTML = "<p>Loading...</p>";

    // Get current date and time
    const currentDate = new Date();
    const dateTimeString = currentDate.toLocaleString();

    // Display date and time
    let resultsHTML = `<p>Test Run on: ${dateTimeString}</p>`;

    // Make API request with device and throttling parameters
    const apiUrl = `/api/pagespeed?url=${encodeURIComponent(urlInput)}&device=${deviceSelect}&throttle=${throttleSelect}`;
    fetch(apiUrl)
        .then(response => response.json())
        .then(data => {
            // Display overall score
            const score = data.lighthouseResult.categories.performance.score;
            resultsHTML += `<p>Overall Score: ${score}</p>`;

            // Display individual metrics
            for (const metric in data.lighthouseResult.audits) {
                const metricValue = data.lighthouseResult.audits[metric].numericValue;
                resultsHTML += `<div class="result">
                                    <div class="metric">
                                        <strong>${metric}</strong>: ${metricValue !== undefined ? metricValue : 'N/A'}
                                    </div>
                                </div>`;
            }

            // Display results
            resultsDiv.innerHTML = resultsHTML;
        })
        .catch(error => {
            console.error("Error fetching data:", error);
            resultsDiv.innerHTML = "<p>Error fetching data. Please try again.</p>";
        });
}



// function runPageSpeedTest() {
//     const urlInput = document.getElementById('urlInput').value;
//     const deviceSelect = document.getElementById('deviceSelect').value;
//     const throttleInput = document.getElementById('throttleInput').value;
//     const resultsDiv = document.getElementById('results');
//     const loadingDiv = document.querySelector('.loading');

//     if (!urlInput) {
//         resultsDiv.innerHTML = "<p>Please enter a valid URL.</p>";
//         return;
//     }

//     // Show loading animation
//     loadingDiv.style.display = 'inline-block';

//     // Clear previous results
//     resultsDiv.innerHTML = "<p>Loading...</p>";

//     // Format the current date and time
//     const dateTime = new Date().toLocaleString();

//     // Make API request with emulated device and throttling parameters
//     const apiUrl = `/api/pagespeed?url=${encodeURIComponent(urlInput)}&device=${deviceSelect}&throttle=${throttleInput}`;
//     fetch(apiUrl)
//         .then(response => response.json())
//         .then(data => {
//             // Hide loading animation
//             loadingDiv.style.display = 'none';

//             // Display results
//             const score = data.lighthouseResult.categories.performance.score;
//             const metrics = data.lighthouseResult.audits;

//             let resultsHTML = `<p>Overall Score: ${score}</p>`;
//             resultsHTML += `<p>Emulated Device: ${deviceSelect}</p>`;
//             resultsHTML += `<p>Throttle: ${throttleInput} ms</p>`;
//             resultsHTML += `<p>Date/Time: ${dateTime}</p>`;
//             resultsHTML += "<h2>Metrics:</h2>";

//             // Display individual metrics
//             for (const metric in metrics) {
//                 const metricValue = metrics[metric].numericValue;
//                 resultsHTML += `<div class="result">
//                                     <div class="metric">
//                                         <strong>${metric}</strong>: ${metricValue !== undefined ? metricValue : 'N/A'}
//                                     </div>
//                                 </div>`;
//             }

//             resultsDiv.innerHTML = resultsHTML;
//         })
//         .catch(error => {
//             console.error("Error fetching data:", error);
//             // Hide loading animation
//             loadingDiv.style.display = 'none';
//             resultsDiv.innerHTML = "<p>Error fetching data. Please try again.</p>";
//         });
// }
