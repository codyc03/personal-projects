let cells = {};
// let marked = ['cell-0','cell-1','cell-2','cell-3','cell-4','cell-5','cell-6','cell-7','cell-8'];
let unmarked = [];
let playerMarked = [];
let gameRunning = true;

document.addEventListener('DOMContentLoaded', () => {
    cells = document.querySelectorAll('.cell');
    const resetButton = document.getElementById('reset-button');

    // Add click event listeners to each cell
    cells.forEach(cell => {
        unmarked.push(cell);

        cell.addEventListener('click', () => {
            if(unmarked.length != 0) {
                gameRunning = true;
                console.log('Player turn');
                cell.textContent = 'X'; // Placeholder, you can implement your game logic here
                // unmarked.pop(cell);
                
                let index = unmarked.indexOf(cell);
                if (index !== -1) {
                    unmarked.splice(index, 1); // Remove 1 element at index `index`
                }

                playerMarked.push(cell.id);

                console.log(unmarked.length);
                checkWin('X');
            }
            if(unmarked.length != 0 && gameRunning) 
                oppTurn(unmarked);
                checkWin('O');       
        });
    });

    // Add click event listener to resetButton
    resetButton.addEventListener('click', clearBoard);


});

// Define the clear function
function clearBoard() {
    cells.forEach(cell => {
        cell.textContent = ''; // Clear the content of each cell
        gameLoop = false;
    });
}

function oppTurn(unmarked) {
    console.log('Bot turn');

    const randomIndex = Math.floor(Math.random() * unmarked.length);
    let element = unmarked[randomIndex];
    console.log(unmarked.length);   
    element.textContent = 'O';


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

function checkWin(player) {
    if(cells[0].textContent === player && cells[1].textContent === player && cells[2].textContent === player )
        endGame(player)
    else if(cells[3].textContent === player && cells[4].textContent === player && cells[5].textContent === player )
        endGame(player)
    else if(cells[6].textContent === player && cells[7].textContent === player && cells[8].textContent === player )
        endGame(player)
    else if(cells[0].textContent === player && cells[3].textContent === player && cells[6].textContent === player )
        endGame(player)
    else if(cells[1].textContent === player && cells[4].textContent === player && cells[7].textContent === player )
        endGame(player)
    else if(cells[2].textContent === player && cells[5].textContent === player && cells[8].textContent === player )
        endGame(player)
    else if(cells[0].textContent === player && cells[4].textContent === player && cells[8].textContent === player )
        endGame(player)
    else if(cells[2].textContent === player && cells[4].textContent === player && cells[6].textContent === player )
        endGame(player)
}

function endGame(winner) {
    gameRunning = false;
    console.log(winner + ' won!'); 
    clearBoard();
}

