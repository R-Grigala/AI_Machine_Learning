document.addEventListener('DOMContentLoaded', function() {
    // Fetch region data and populate checkboxes
    const regionContainer = document.getElementById('region-container');

    fetch('https://api.real-estate-manager.redberryinternship.ge/api/regions')
        .then(response => response.json())
        .then(regions => {
            // Create rows for checkboxes
            const rows = [document.createElement('div'), document.createElement('div'), document.createElement('div')];
            rows.forEach(row => {
                row.className = 'row mb-4';
                regionContainer.appendChild(row);
            });

            regions.forEach((region, index) => {
                const colDiv = document.createElement('div');
                colDiv.className = 'col d-flex justify-content-start';

                const formCheckDiv = document.createElement('div');
                formCheckDiv.className = 'form-check';

                const checkboxInput = document.createElement('input');
                checkboxInput.className = 'form-check-input';
                checkboxInput.type = 'checkbox';
                checkboxInput.id = region.id;

                const label = document.createElement('label');
                label.className = 'form-check-label checkbox-label';
                label.htmlFor = region.id;
                label.textContent = region.name;

                formCheckDiv.appendChild(checkboxInput);
                formCheckDiv.appendChild(label);
                colDiv.appendChild(formCheckDiv);

                // Determine which row to add the checkbox to
                const rowIndex = Math.floor(index / 4); // Adjust the divisor to change the number of checkboxes per row
                rows[rowIndex].appendChild(colDiv);
            });
        })
        .catch(error => console.error('Error fetching regions:', error));

    // Handle price option clicks
    const priceOptions = document.querySelectorAll('.price-option');

    priceOptions.forEach(option => {
        option.addEventListener('click', function() {
            const price = this.getAttribute('data-price');
            const colIndex = Array.from(this.parentNode.children).indexOf(this) % 2;

            if (colIndex === 0) {
                document.getElementById('priceStart').value = price + ' ₾';
            } else {
                document.getElementById('priceEnd').value = price + ' ₾';
            }
        });
    });
});
