/*
File: index.js
Author: Cody Christensen
Date: 9/10/24
Copyright: Cody Christensen - This work may not be copied for use in Academic Coursework.

I, Cody Christensen, certify that I wrote this code
from scratch and did not copy it in part or whole from another source.
All references used in the completion of the assignments are cited
in my README file.

File Contents
    This file contains the JavaScript code responsible for the backend 
    operations of the project.
*/

let cells = {};
let unmarked = [];
let playerMarked = [];
let gameRunning = true;

//Upon document loaded, add click event listeners to each cell
document.addEventListener('DOMContentLoaded', () => {
    cells = document.querySelectorAll('.cell');
    const resetButton = document.getElementById('reset-button');

    // Add click event listeners to each cell
    cells.forEach(cell => {
        unmarked.push(cell);

        cell.addEventListener('click', () => {
            if(unmarked.length != 0) {
                gameRunning = true;
                cell.textContent = 'X';                 
                let index = unmarked.indexOf(cell);

                if (index !== -1) {
                    unmarked.splice(index, 1); 
                }

                playerMarked.push(cell.id);

                checkWin('X');
            }
            if (unmarked.length != 0 && gameRunning) {
                oppTurn(unmarked);
                checkWin('O');
            }
        });
    });

    // Add click event listener to resetButton
    resetButton.addEventListener('click', clearBoard);
});

/*
Used to clear all the entries on the board and 
reset the board to its initial state.
*/
function clearBoard() {
    unmarked.length = 0;
    playerMarked.length = 0;

    cells.forEach(cell => {
        cell.textContent = ''; 
        gameLoop = false;
        unmarked.push(cell);
    });
}

/*
Used to simulate AI opponents turn, takes its turn and marks
a spot
*/
function oppTurn(unmarked) {
    const randomIndex = Math.floor(Math.random() * unmarked.length);
    let element = unmarked[randomIndex];
    element.textContent = 'O';
    let index = unmarked.indexOf(element);

    if (index !== -1) {
        unmarked.splice(index, 1); 
    }
}

/*
Used to check the game board for a win. AKA, has someone got 
three markings in a row?
*/
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

/*
Handles actions necessary to end the game and display winner.
*/
function endGame(winner) {
    gameRunning = false;
    console.log('alert');
    alert(winner + ' won! Click OK to play another game.');
    clearBoard();
}

