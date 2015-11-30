int[][] cells;
int[][] newcells;
int size;
int sizex;
int sizey;

void setup() {
  sizex = 64;
  sizey = 35;
  size = 10;
  size(sizex * size, sizey * size);
  cells = new int[sizex][sizey];
  newcells = new int[sizex][sizey];
  for (int y = 0; y < sizey; y++) {
    for (int x = 0; x < sizex; x++) {
      cells[x][y] = int(random(2));
      newcells[x][y] = 0;
    }
  }
}

int cell(int x, int y) {
  int c = 0;
  if ((x >= 0) && (x < sizex)) {
    if ((y >= 0) && (y < sizey)) {
      c = cells[x][y];
    } 
  } 
  return c;
}

int neighbours(int x, int y) {
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

void draw() {
  background(0);
  for (int y = 0; y < sizey; y++) {
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

  for (int y = 0; y < sizey; y++) {
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

  for (int y = 0; y < sizey; y++) {
    for (int x = 0; x < sizex; x++) {
      cells[x][y] = newcells[x][y];
    }
  }  
}
