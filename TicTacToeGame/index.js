let cells = {};
// let marked = ['cell-0','cell-1','cell-2','cell-3','cell-4','cell-5','cell-6','cell-7','cell-8'];
let unmarked = [];

document.addEventListener('DOMContentLoaded', () => {
    cells = document.querySelectorAll('.cell');
    const resetButton = document.getElementById('reset-button');

    // Add click event listeners to each cell
    cells.forEach(cell => {
        unmarked.push(cell);

        cell.addEventListener('click', () => {
            console.log('Player turn');
            cell.textContent = 'X'; // Placeholder, you can implement your game logic here
            // unmarked.pop(cell);
            
            let index = unmarked.indexOf(cell);
            if (index !== -1) {
                unmarked.splice(index, 1); // Remove 1 element at index `index`
            }

            console.log(unmarked.length);
            oppTurn(unmarked);
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

function oppTurn(unmarked) {
    console.log('Bot turn');

    if (unmarked.length != 0) {
        let element = unmarked.pop()
        console.log(unmarked.length);   
        element.textContent = 'O';
    }   

    

    // let fullCheck = 0;
    // max = marked.length

    // console.log(max)

    // min = 0
    // // let element = findEmpty();
    // element.textContent = 'O';
    // marked.pop(element.getAttribute('id'));

    // function findEmpty() {
    //     fullCheck++;

    //     if(fullCheck == 9)
    //         console.log('game over')

    //     let rand = Math.floor(Math.random() * (max - min + 1)) + min;
    //     let element = document.getElementById(marked[rand]);

    //     console.log('pre-null');
    //     if(element.textContent === '') {
    //         console.log('post-null');
    //         return element;
    //     }
    //     else
    //         findEmpty()
    // }
}