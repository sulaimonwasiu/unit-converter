document.addEventListener('DOMContentLoaded', function() {
    // Add event listeners to tabs
    const tabs = document.querySelectorAll('.tab');
    tabs.forEach(tab => {
        tab.addEventListener('click', function(event) {
            // Prevent the default anchor behavior
            event.preventDefault();

            // Remove active class from all tabs
            tabs.forEach(t => t.classList.remove('active'));

            // Add active class to the clicked tab
            this.classList.add('active');

            // Store the active tab in local storage
            localStorage.setItem('activeTab', this.textContent.trim());

            // Redirect to the new URL
            window.location.href = this.href;
        });
    });
});