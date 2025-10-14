// DOM prvky
const boardEl = document.getElementById('board');
const statusEl = document.getElementById('status');
const resetBtn = document.getElementById('resetBtn');
const undoBtn = document.getElementById('undoBtn');
const scoreXEl = document.getElementById('scoreX');
const scoreOEl = document.getElementById('scoreO');
const scoreTieEl = document.getElementById('scoreTie');

// Herné premenné
let boardState = Array(9).fill(null);
let currentPlayer = 'X';
let isGameOver = false;
let history = [];
let scores = JSON.parse(localStorage.getItem('ttt-scores')) || { X: 0, O: 0, T: 0 };

// Výherné kombinácie
const WIN_COMBOS = [
  [0, 1, 2],
  [3, 4, 5],
  [6, 7, 8],
  [0, 3, 6],
  [1, 4, 7],
  [2, 5, 8],
  [0, 4, 8],
  [2, 4, 6],
];

// Vytvorenie hracej dosky
function createBoard() {
  for (let i = 0; i < 9; i++) {
    const cell = document.createElement('div');
    cell.classList.add('cell');
    cell.dataset.index = i;
    cell.addEventListener('click', () => {
      if (!isGameOver && !boardState[i]) makeMove(i);
    });
    boardEl.appendChild(cell);
  }
}

// Spracovanie ťahu
function makeMove(index) {
  boardState[index] = currentPlayer;
  history.push(index);
  render();

  if (checkWin(currentPlayer)) {
    statusEl.textContent = `Hráč ${currentPlayer} vyhral!`;
    highlightWinningCells(currentPlayer);
    scores[currentPlayer]++;
    saveScores();
    updateScoreUI();
    isGameOver = true;
    return;
  }

  if (boardState.every(cell => cell)) {
    statusEl.textContent = "Remíza!";
    scores.T++;
    saveScores();
    updateScoreUI();
    isGameOver = true;
    return;
  }

  currentPlayer = currentPlayer === 'X' ? 'O' : 'X';
  statusEl.textContent = `Hráč ${currentPlayer} na ťahu`;
  undoBtn.disabled = false;
}

// Kontrola výhry
function checkWin(player) {
  return WIN_COMBOS.some(combo => {
    return combo.every(i => boardState[i] === player);
  });
}

// Zvýraznenie výherných políčok
function highlightWinningCells(winner) {
  for (const combo of WIN_COMBOS) {
    const [a, b, c] = combo;
    if (
      boardState[a] === winner &&
      boardState[b] === winner &&
      boardState[c] === winner
    ) {
      [a, b, c].forEach(i => {
        const cell = boardEl.querySelector(`[data-index='${i}']`);
        if (cell) cell.classList.add('highlight');
      });
    }
  }
}

// Vykreslenie dosky
function render() {
  for (let i = 0; i < 9; i++) {
    const cell = boardEl.querySelector(`[data-index='${i}']`);
    cell.textContent = boardState[i] || '';
    cell.classList.toggle('x', boardState[i] === 'X');
    cell.classList.toggle('o', boardState[i] === 'O');
  }
}

// Reset dosky
function resetBoard() {
  boardState = Array(9).fill(null);
  currentPlayer = 'X';
  isGameOver = false;
  history = [];
  statusEl.textContent = `Hráč ${currentPlayer} na ťahu`;
  Array.from(boardEl.children).forEach(c => c.classList.remove('highlight'));
  render();
  undoBtn.disabled = true;
}

// Späť (undo)
function undo() {
  if (history.length === 0 || isGameOver) return;
  const last = history.pop();
  boardState[last] = null;
  currentPlayer = currentPlayer === 'X' ? 'O' : 'X';
  statusEl.textContent = `Hráč ${currentPlayer} na ťahu`;
  render();
  if (history.length === 0) undoBtn.disabled = true;
}

// Uloženie skóre
function saveScores() {
  localStorage.setItem('ttt-scores', JSON.stringify(scores));
}

// Aktualizácia skóre
function updateScoreUI() {
  scoreXEl.textContent = scores.X;
  scoreOEl.textContent = scores.O;
  scoreTieEl.textContent = scores.T;
}

// --- Inicializácia ---
createBoard();
render();
updateScoreUI();

// Event listenery
resetBtn.addEventListener('click', () => resetBoard());
undoBtn.addEventListener('click', () => undo());

// Klávesnica: čísla 1-9 mapujú na bunky
window.addEventListener('keydown', e => {
  if (e.key >= '1' && e.key <= '9') {
    const idx = Number(e.key) - 1;
    if (!isGameOver && !boardState[idx]) makeMove(idx);
  }
  if (e.key === 'r' || e.key === 'R') resetBoard();
});

// API pre rozšírenia
window.TicTacToe = {
  reset: resetBoard,
  getState: () => ({ boardState: [...boardState], currentPlayer, isGameOver }),
};
