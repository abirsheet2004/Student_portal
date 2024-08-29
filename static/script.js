// script.js

document.addEventListener('DOMContentLoaded', function() {
    // Add event listeners when the DOM is fully loaded

    // Function to change the background color on hover
    function highlightRow(event) {
        // Check if the target element is a table row
        if (event.target.tagName.toLowerCase() === 'tr') {
            // Toggle the background color
            event.target.classList.toggle('highlighted');
        }
    }

    // Attach the event listener to the table
    var table = document.querySelector('table');
    if (table) {
        table.addEventListener('mouseover', highlightRow);
        table.addEventListener('mouseout', highlightRow);
    }
});
