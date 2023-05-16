// Define canvas variables
const canvas = document.getElementById("canvas");
const ctx = canvas.getContext("2d");

// Define snake variables
let snake = [{ x: 10, y: 10 }];
let dx = 10;
let dy = 0;

// Define food variables
let food = { x: 0, y: 0 };

// Define score variable
let score = 0;

// Draw snake function
function drawSnake() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  snake.forEach((segment) => {
    // Draw border
    ctx.fillStyle = "black";
    ctx.fillRect(segment.x, segment.y, 10, 10);

    // Draw snake segment
    ctx.fillStyle = "green";
    ctx.fillRect(segment.x + 1, segment.y + 1, 8, 8);
  });
}

// Move snake function
function moveSnake() {
  const head = { x: snake[0].x + dx, y: snake[0].y + dy };
  snake.unshift(head);
  snake.pop();
}

// Generate food function
function generateFood() {
  food.x = Math.floor(Math.random() * canvas.width);
  food.y = Math.floor(Math.random() * canvas.height);
  ctx.fillStyle = "red";
  ctx.fillRect(food.x, food.y, 10, 10);
}

// Detect collisions function
function detectCollisions() {
  if (snake[0].x < 0) {
    snake[0].x = canvas.width - 10;
  } else if (snake[0].x > canvas.width - 10) {
    snake[0].x = 0;
  } else if (snake[0].y < 0) {
    snake[0].y = canvas.height - 10;
  } else if (snake[0].y > canvas.height - 10) {
    snake[0].y = 0;
  }

  if (snake[0].x === food.x && snake[0].y === food.y) {
    // Snake ate food
    score++;
    generateFood();
  }
}

// Update score function
function updateScore() {
  document.getElementById("score").innerHTML = score;
}

// Event listeners for user input
document.addEventListener("keydown", (event) => {
  if (event.code === "ArrowLeft") {
    dx = -10;
    dy = 0;
  } else if (event.code === "ArrowRight") {
    dx = 10;
    dy = 0;
  } else if (event.code === "ArrowUp") {
    dx = 0;
    dy = -10;
  } else if (event.code === "ArrowDown") {
    dx = 0;
    dy = 10;
  }
});

// Game loop
function gameLoop() {
  drawSnake();
  moveSnake();
  detectCollisions();
  updateScore();
  requestAnimationFrame(gameLoop);
}

// Start game
generateFood();
gameLoop();

// Detect collisions function
function detectCollisions() {
  if (
    snake[0].x < 0 ||
    snake[0].x > canvas.width - 10 ||
    snake[0].y < 0 ||
    snake[0].y > canvas.height - 10
  ) {
    // Game over
    gameOver();
  }

  if (snake[0].x === food.x && snake[0].y === food.y) {
    // Snake ate food
    score++;
    generateFood();
  }
}

// Game over function
function gameOver() {
  alert("Game over!");
  location.reload();
}