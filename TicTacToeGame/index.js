document.addEventListener('DOMContentLoaded', () => {
    const cells = document.querySelectorAll('.cell');
    const resetButton = document.getElementById('reset-button');
    let currentPlayer = 'X';
    let gameActive = true;

    // Add click event listeners to each cell
    cells.forEach(cell => {
        cell.addEventListener('click', () => {
            cell.textContent = 'X'; // Placeholder, you can implement your game logic here
        });
    });

    // Add click event listener to resetButton
    resetButton.addEventListener('click', clear);

    // Define the clear function
    function clear() {
        cells.forEach(cell => {
            cell.textContent = ''; // Clear the content of each cell
        });
    }
});

