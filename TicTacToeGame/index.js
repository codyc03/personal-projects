let cells = {};
let marked = ['cell-0','cell-1','cell-2','cell-3','cell-4',,'cell-5','cell-6',,'cell-7','cell-8'];

document.addEventListener('DOMContentLoaded', () => {
    cells = document.querySelectorAll('.cell');
    const resetButton = document.getElementById('reset-button');

    // Add click event listeners to each cell
    cells.forEach(cell => {
        cell.addEventListener('click', () => {
            cell.textContent = 'X'; // Placeholder, you can implement your game logic here
            marked.pop(cell.getAttribute('id'));
            oppTurn();
        });
    });

    // Add click event listener to resetButton
    resetButton.addEventListener('click', clear);

    // Define the clear function
    function clear() {
        cells.forEach(cell => {
            cell.textContent = ''; // Clear the content of each cell
            gameLoop = false;
        });
    }
});

function oppTurn() {
    marked = false
    max = marked.length
    min = 0
    let rand = Math.floor(Math.random() * (max - min + 1)) + min;
    let temp = document.getElementById(marked[rand]);
    temp.textContent = 'O';
}