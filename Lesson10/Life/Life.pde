int[][] cells; //массив для текущего состояния клеток
int[][] newcells; //массив для будущего состояния клеток
int size; //размер клетки на экране (в пикселах)
int sizex; //количество клеток по x
int sizey; //количество клеток по y

void setup() {
  sizex = 64;
  sizey = 35; //поле 64х35
  size = 10;
  size(sizex * size, sizey * size); //задаем размер экрана исходя из размеров поля
  cells = new int[sizex][sizey]; //создаем пустой двумерный массив для текущего состояния клеток
  newcells = new int[sizex][sizey]; //создаем пустой двумерный массив для будущего состояния клеток
  for (int y = 0; y < sizey; y++) {
    for (int x = 0; x < sizex; x++) {
      cells[x][y] = int(random(2)); //заполняем массив для текущего состояния клеток случайным образом 
      newcells[x][y] = 0; //заполняем массив для будущего состояния клеток нулями
    }
  }
}

int cell(int x, int y) { //эта функция проверяет, не выходят ли x и y за пределы поля и массива.
  int c = 0;
  if ((x >= 0) && (x < sizex)) {
    if ((y >= 0) && (y < sizey)) {
      c = cells[x][y]; //И если не выходят, возвращает содержимое клетки с такими координатами.
    } 
  } 
  return c; //иначе возвращает 0
}

int neighbours(int x, int y) { //эта функция считает количество живых соседей клетки
  int n = 0;
  n += cell(x-1, y-1);
  n += cell(x, y-1);
  n += cell(x+1, y-1);
  n += cell(x-1, y);
  n += cell(x+1, y);
  n += cell(x-1, y+1);
  n += cell(x, y+1);
  n += cell(x+1, y+1);
  return n;
}

void draw() { //функция перерисовки
  background(0); //jчищаем экран
  for (int y = 0; y < sizey; y++) { //рисуем поле согласно массиву текущего состояния клеток
    for (int x = 0; x < sizex; x++) {
      if (cells[x][y] == 0) {
        stroke(64);
        fill(10);
      } else {
        stroke(64);
        fill(200);
      }
      rect(x * size, y * size, size, size);
    }
  }

  for (int y = 0; y < sizey; y++) { // считаем, что будет в новом поколении
    for (int x = 0; x < sizex; x++) {
      newcells[x][y] = cells[x][y];
      int n = neighbours(x, y);
      if (n == 3) {
        newcells[x][y] = 1;
      } else if ((n < 2) || (n > 3)) {
        newcells[x][y] = 0;
      }
    }
  }

  for (int y = 0; y < sizey; y++) { //обновляем массив с текущим состоянием
    for (int x = 0; x < sizex; x++) {
      cells[x][y] = newcells[x][y];
    }
  }  
}
