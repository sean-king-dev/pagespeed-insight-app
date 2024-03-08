// Your JavaScript code goes here
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

    // v3
    fetch(`/api/pagespeed?url=${encodeURIComponent(urlInput)}`)
    .then(response => response.json())
    .then(data => {
        const score = data.lighthouseResult.categories.performance.score;
        const audits = data.lighthouseResult.audits;

        let resultsHTML = `<p>Overall Score: ${score}</p>`;
        resultsHTML += "<h2>Metrics:</h2>";

        // Define variables for specific metrics
        const bootupTime = audits['bootup-time'].numericValue;
        const criticalRequestChains = audits['critical-request-chains'].numericValue;
        const cumulativeLayoutShift = audits['cumulative-layout-shift'].numericValue;
        const diagnostics = audits['diagnostics'].numericValue;
        const domSize = audits['dom-size'].numericValue;
        const duplicatedJavascript = audits['duplicated-javascript'].numericValue;
        const efficientAnimatedContent = audits['efficient-animated-content'].numericValue;
        const finalScreenshot = audits['final-screenshot'].numericValue;

        // Display specific metrics if available
        if (bootupTime !== undefined) {
            resultsHTML += `<p>Bootup Time: ${bootupTime} seconds</p>`;
        }

        if (criticalRequestChains !== undefined) {
            resultsHTML += `<p>Critical Request Chains: ${criticalRequestChains} seconds</p>`;
        }

        if (cumulativeLayoutShift !== undefined) {
            resultsHTML += `<p>Cumulative Layout Shift: ${cumulativeLayoutShift}</p>`;
        }

        if (diagnostics !== undefined) {
            resultsHTML += `<p>Diagnostics: ${diagnostics}</p>`;
        }

        if (domSize !== undefined) {
            resultsHTML += `<p>DOM Size: ${domSize}</p>`;
        }

        if (duplicatedJavascript !== undefined) {
            resultsHTML += `<p>Duplicated Javascript: ${duplicatedJavascript}</p>`;
        }

        if (efficientAnimatedContent !== undefined) {
            resultsHTML += `<p>Efficient Animated Content: ${efficientAnimatedContent}</p>`;
        }

        if (finalScreenshot !== undefined) {
            resultsHTML += `<p>Final Screenshot: ${finalScreenshot}</p>`;
        }

        // Display other metrics with undefined values
        const undefinedMetrics = {
            // Add more metrics as needed
        };

        // Display metrics with undefined values
        Object.keys(undefinedMetrics).forEach(metricKey => {
            const metricValue = undefinedMetrics[metricKey];
            resultsHTML += `<p>${metricKey}: ${metricValue !== undefined ? metricValue : 'N/A'}</p>`;
        });

        resultsDiv.innerHTML = resultsHTML;
    })
    .catch(error => {
        console.error("Error fetching data:", error);
        resultsDiv.innerHTML = "<p>Error fetching data. Please try again.</p>";
    });


    // v2
    // fetch(`/api/pagespeed?url=${encodeURIComponent(urlInput)}`)
    // .then(response => response.json())
    // .then(data => {
    //     // Display results
    //     const score = data.lighthouseResult.categories.performance.score;
    //     const audits = data.lighthouseResult.audits;

    //     let resultsHTML = `<p>Overall Score: ${score}</p>`;
    //     resultsHTML += "<h2>Metrics:</h2>";

    //     // Extract specific metrics
    //     const firstContentfulPaint = audits['first-contentful-paint'].numericValue;
    //     const largestContentfulPaint = audits['largest-contentful-paint'].numericValue;
    //     const totalBlockingTime = audits['total-blocking-time'].numericValue;

    //     resultsHTML += `<p>First Contentful Paint: ${firstContentfulPaint} seconds</p>`;
    //     resultsHTML += `<p>Largest Contentful Paint: ${largestContentfulPaint} seconds</p>`;
    //     resultsHTML += `<p>Total Blocking Time: ${totalBlockingTime} milliseconds</p>`;

    //     // Display individual metrics dynamically
    //     for (const metric in audits) {
    //         const metricValue = audits[metric].numericValue;

    //         if (metricValue !== undefined) {
    //             resultsHTML += `<div class="result">
    //                                 <div class="metric">
    //                                     <strong>${metric}</strong>: ${metricValue}
    //                                 </div>
    //                             </div>`;
    //         } else {
    //             resultsHTML += `<div class="result">
    //                                 <div class="metric">
    //                                     <strong>${metric}</strong>: N/A
    //                                 </div>
    //                             </div>`;
    //         }
    //     }

    //     resultsDiv.innerHTML = resultsHTML;
    // })
    // .catch(error => {
    //     console.error("Error fetching data:", error);
    //     resultsDiv.innerHTML = "<p>Error fetching data. Please try again.</p>";
    // });


    // v1
    // fetch(`/api/pagespeed?url=${encodeURIComponent(urlInput)}`)
    //     .then(response => response.json())
    //     .then(data => {
    //         // Hide loading animation
    //         loadingDiv.style.display = 'none';

    //         // Display results
    //         const score = data.lighthouseResult.categories.performance.score;
    //         const metrics = data.lighthouseResult.audits;

    //         let resultsHTML = `<p>Overall Score: ${score}</p>`;
    //         resultsHTML += "<h2>Metrics:</h2>";

    //         // Display individual metrics
    //         for (const metric in metrics) {
    //             const metricValue = metrics[metric].numericValue;
    //             // resultsHTML += `<p>${metric}: ${metricValue}</p>`;
    //             resultsHTML += `<div class="result">
    //                                 <div class="metric">
    //                                     <strong>${metric}</strong>: ${metricValue}
    //                                 </div>
    //                             </div>`;
    //         }

    //         resultsDiv.innerHTML = resultsHTML;
    //     })
    //     .catch(error => {
    //         console.error("Error fetching data:", error);

            // Hide loading animation
            // loadingDiv.style.display = 'none';

            resultsDiv.innerHTML = "<p>Error fetching data. Please try again.</p>";
        });
}
