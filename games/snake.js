// Definir variáveis globais
var canvas;
var ctx;
var snake;
var apple;
var score;

// Configurar o jogo
function setup() {
  canvas = document.getElementById("canvas");
  ctx = canvas.getContext("2d");
  canvas.width = 400;
  canvas.height = 400;
  snake = new Snake();
  apple = new Apple();
  score = 0;
  // Adicionar evento de teclado para controlar a cobra
  document.addEventListener("keydown", keyDownHandler);
  // Atualizar a tela a cada 100ms
  setInterval(draw, 100);
}

// Desenhar a tela
function draw() {
  // Limpar a tela
  ctx.fillStyle = "black";
  ctx.fillRect(0, 0, canvas.width, canvas.height);
  // Desenhar a cobra e a maçã
  snake.draw();
  apple.draw();
  // Verificar se a cobra comeu a maçã
  if (snake.eat(apple)) {
    apple = new Apple();
    score++;
  }
  // Atualizar a pontuação
  ctx.font = "20px Arial";
  ctx.fillStyle = "white";
  ctx.textAlign = "center";
  ctx.fillText("Score: " + score, canvas.width/2, 30);
  // Verificar se a cobra colidiu com a parede ou com o próprio corpo
  if (snake.checkCollision()) {
    // Reiniciar o jogo
    snake = new Snake();
    apple = new Apple();
    score = 0;
  }
}

// Definir a classe Snake
class Snake {
  constructor() {
    this.body = [{x: 5, y: 5}];
    this.direction = "right";
  }
  draw() {
    // Desenhar cada parte do corpo da cobra
    for (var i = 0; i < this.body.length; i++) {
      ctx.fillStyle = "red";
      ctx.fillRect(this.body[i].x*10, this.body[i].y*10, 10, 10);
    }
    // Mover a cobra
    var head = {x: this.body[0].x, y: this.body[0].y};
    if (this.direction == "right") {
      head.x++;
    } else if (this.direction == "left") {
      head.x--;
    } else if (this.direction == "up") {
      head.y--;
    } else if (this.direction == "down") {
      head.y++;
    }
    this.body.unshift(head);
    this.body.pop();
  }
  eat(apple) {
    // Verificar se a cobra comeu a maçã
    if (this.body[0].x == apple.x && this.body[0].y == apple.y) {
      this.body.push({});
      return true;
    } else {
      return false;
    }
  }
checkCollision() {
  // Verificar se a cobra colidiu com a parede ou com o próprio corpo
  let head = this.body[0];
  if (head.x < 0) {
    head.x = canvas.width/10 - 1;
  } else if (head.x >= canvas.width/10) {
    head.x = 0;
  } else if (head.y < 0) {
    head.y = canvas.height/10 - 1;
  } else if (head.y >= canvas.height/10) {
    head.y = 0;
  }
  for (let i = 1; i < this.body.length; i++) {
    if (head.x == this.body[i].x && head.y == this.body[i].y) {
      return true;
    }
  }
  return false;
}

// Definir a classe Apple
class Apple {
  constructor() {
    this.x = Math.floor(Math.random() * canvas.width/10);
    this.y = Math.floor(Math.random() * canvas.height/10);
  }
  draw() {
    // Desenhar a maçã
    ctx.fillStyle = "yellow";
    ctx.fillRect(this.x*10, this.y*10, 10, 10);
  }
}

// Função para lidar com eventos de teclado
function keyDownHandler(event) {
  if (event.keyCode == 37 && snake.direction != "right") {
    snake.direction = "left";
  } else if (event.keyCode == 38 && snake.direction != "down") {
    snake.direction = "up";
  } else if (event.keyCode == 39 && snake.direction != "left") {
    snake.direction = "right";
  } else if (event.keyCode == 40 && snake.direction != "up") {
    snake.direction = "down";
  }
}