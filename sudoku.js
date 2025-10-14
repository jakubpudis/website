function makeEmptyBoard(){const b=[];for(let r=0;r<9;r++)b[r]=Array(9).fill(0);return b}
function copyBoard(b){return b.map(row=>row.slice())}
function isSafe(board,row,col,num){for(let i=0;i<9;i++){if(board[row][i]===num)return false;if(board[i][col]===num)return false}const sr=Math.floor(row/3)*3, sc=Math.floor(col/3)*3;for(let r=0;r<3;r++)for(let c=0;c<3;c++)if(board[sr+r][sc+c]===num)return false;return true}
function findEmpty(board){for(let r=0;r<9;r++)for(let c=0;c<9;c++)if(board[r][c]===0)return[r,c];return null}
function shuffleArray(arr){for(let i=arr.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[arr[i],arr[j]]=[arr[j],arr[i]]}return arr}
function solveSudoku(board){const pos=findEmpty(board);if(!pos)return true;const[r,c]=pos;for(let num=1;num<=9;num++){if(isSafe(board,r,c,num)){board[r][c]=num;if(solveSudoku(board))return true;board[r][c]=0}}return false}

function generateFullBoard(){const board=makeEmptyBoard();function fillCell(i){if(i>=81)return true;const r=Math.floor(i/9), c=i%9;const nums=shuffleArray([1,2,3,4,5,6,7,8,9].slice());for(const n of nums){if(isSafe(board,r,c,n)){board[r][c]=n;if(fillCell(i+1))return true;board[r][c]=0}}return false}fillCell(0);return board}
function removeNumbers(board,removeCount){const puzzle=copyBoard(board);const cells=[];for(let r=0;r<9;r++)for(let c=0;c<9;c++)cells.push([r,c]);shuffleArray(cells);let removed=0;for(const [r,c] of cells){if(removed>=removeCount)break;const backup=puzzle[r][c];puzzle[r][c]=0;removed++}return puzzle}

const table=document.getElementById('sudokuTable');const message=document.getElementById('message');let solutionBoard=null;let currentPuzzle=null;

function buildTable(board){table.innerHTML='';for(let r=0;r<9;r++){const tr=document.createElement('tr');for(let c=0;c<9;c++){const td=document.createElement('td');const input=document.createElement('input');input.type='number';input.min='1';input.max='9';input.dataset.row=r;input.dataset.col=c;input.setAttribute('inputmode','numeric');input.setAttribute('aria-label',`Riadok ${r+1} Stĺpec ${c+1}`);
    if(board[r][c]!==0){input.value=board[r][c];input.disabled=true}else{input.value='';input.disabled=false}
    input.addEventListener('input',e=>{const v=e.target.value;if(v==='')return;const n=parseInt(v,10);if(isNaN(n)||n<1||n>9)e.target.value='';else e.target.value=n});
    td.appendChild(input);tr.appendChild(td)}table.appendChild(tr)}}

function readUserBoard(){const b=makeEmptyBoard();const inputs=table.querySelectorAll('input');inputs.forEach(inp=>{const r=parseInt(inp.dataset.row,10);const c=parseInt(inp.dataset.col,10);const v=inp.value.trim();b[r][c]=v===''?0:parseInt(v,10)});return b}
function showMessage(txt,isError){message.textContent=txt;message.setAttribute('title',isError?'error':'');}

document.getElementById('newBtn').addEventListener('click',()=>{showMessage('Generujem novú hru...');setTimeout(()=>{const full=generateFullBoard();const puzzle=removeNumbers(full,45);currentPuzzle=puzzle;solutionBoard=copyBoard(full);buildTable(puzzle);showMessage('Nová hra pripravená.');},20)});

document.getElementById('checkBtn').addEventListener('click',()=>{if(!solutionBoard){showMessage('Najprv si vygeneruj alebo načítaj hru.',true);return}const user=readUserBoard();let ok=true;for(let r=0;r<9;r++)for(let c=0;c<9;c++){const pv=currentPuzzle[r][c];if(pv===0){const u=user[r][c];if(u===0)ok=false;else if(u!==solutionBoard[r][c])ok=false}}if(ok)showMessage('Správne! Gratulujem.');else showMessage('Niektoré polia sú chybné alebo prázdne.',true)});

document.getElementById('solveBtn').addEventListener('click',()=>{if(!solutionBoard){showMessage('Najprv vygeneruj hru.',true);return}const inputs=table.querySelectorAll('input');inputs.forEach(inp=>{const r=parseInt(inp.dataset.row,10);const c=parseInt(inp.dataset.col,10);inp.value=solutionBoard[r][c];inp.disabled=true});showMessage('Riešenie zobrazené.')});

document.getElementById('clearBtn').addEventListener('click',()=>{if(!currentPuzzle)return;buildTable(currentPuzzle);showMessage('Vyčistené do počiatočného stavu.')});

table.addEventListener('keydown',e=>{const t=e.target; if(t.tagName!=='INPUT')return;const r=parseInt(t.dataset.row,10);const c=parseInt(t.dataset.col,10);let nr=r,nc=c;if(e.key==='ArrowUp')nr=Math.max(0,r-1);else if(e.key==='ArrowDown')nr=Math.min(8,r+1);else if(e.key==='ArrowLeft')nc=Math.max(0,c-1);else if(e.key==='ArrowRight')nc=Math.min(8,c+1);else return;e.preventDefault();const selector=`input[data-row="${nr}"][data-col="${nc}"]`;const next=table.querySelector(selector);if(next)next.focus()});

(function init(){document.getElementById('newBtn').click()})();