// Add event listener to the buttons
const buttons = document.querySelectorAll('.btn-group button');
buttons.forEach(button => {
    button.addEventListener('click', () => {
        // set this button to btn-secondary and the others to btn-light
        buttons.forEach(btn => {
            btn.classList.remove('btn-secondary');
            btn.classList.add('btn-light');
        });
        button.classList.remove('btn-light');
        button.classList.add('btn-secondary');

        // clear search input
        document.querySelector('#search-input').value = '';

        const selectedCategory = button.dataset.category;
        const rows = document.querySelectorAll('#search-table tbody tr');
        rows.forEach(row => {
            if (row.dataset.category === selectedCategory) {
                row.style.display = '';
            } else {
                row.style.display = 'none';
            }
        });
    });
});