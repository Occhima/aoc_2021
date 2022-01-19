#include <fstream>
#include <iostream>
#include <string>

#define USE_EXAMPLE 0
#if USE_EXAMPLE
#define FILE "./example.txt"
#define GRID_SIZE 10
#else
#define FILE "./input.txt"
#define GRID_SIZE 1000
#endif

int count_danger(int *grid) {
  int count = 0;
  for (int i = 0; i < GRID_SIZE; ++i) {
    for (int j = 0; j < GRID_SIZE; ++j) {
      if (grid[i * GRID_SIZE + j] >= 2) {
        ++count;
      }
    }
  }
  return count;
}

void dump_grid(int *grid) {
  for (int x = 0; x < GRID_SIZE; ++x) {
    for (int y = 0; y < GRID_SIZE; ++y) {
      if (grid[y * GRID_SIZE + x] == 0) {
        printf(".");
      } else {
        printf("%d", grid[y * GRID_SIZE + x]);
      }
    }
    printf("\n");
  }
}

void part_one() {
  std::ifstream input(FILE);

  int *grid = (int *)calloc(GRID_SIZE * GRID_SIZE, sizeof(int));

  int x1, y1, x2, y2;
  std::string ignore;
  char ignore2;
  while (input >> x1 && input >> ignore2 && input >> y1 && input >> ignore &&
         input >> x2 && input >> ignore2 && input >> y2) {
    // vertical
    if (x1 == x2) {
      int sy = std::min(y1, y2);
      int ey = std::max(y1, y2);
      for (int y = sy; y <= ey; ++y) {
        ++grid[x1 * GRID_SIZE + y];
      }
    }
    // horizontal
    if (y1 == y2) {
      int sx = std::min(x1, x2);
      int ex = std::max(x1, x2);
      for (int x = sx; x <= ex; ++x) {
        ++grid[x * GRID_SIZE + y1];
      }
    }
  }

  printf("%d\n", count_danger(grid));
  free(grid);
}

void part_two() {
  std::ifstream input(FILE);

  int *grid = (int *)calloc(GRID_SIZE * GRID_SIZE, sizeof(int));

  int x1, y1, x2, y2;
  std::string ignore;
  char ignore2;
  while (input >> x1 && input >> ignore2 && input >> y1 && input >> ignore &&
         input >> x2 && input >> ignore2 && input >> y2) {
    // vertical
    if (x1 == x2) {
      int sy = std::min(y1, y2);
      int ey = std::max(y1, y2);
      for (int y = sy; y <= ey; ++y) {
        ++grid[x1 * GRID_SIZE + y];
      }
      continue;
    }
    // horizontal
    if (y1 == y2) {
      int sx = std::min(x1, x2);
      int ex = std::max(x1, x2);
      for (int x = sx; x <= ex; ++x) {
        ++grid[x * GRID_SIZE + y1];
      }
      continue;
    }

    // 45 diagonal
    int dx = x2 - x1;
    int dy = y2 - y1;
    if (std::abs(dx) == std::abs(dy)) {
      int steps = std::abs(dx);
      int grad_x = dx / steps;
      int grad_y = dy / steps;
      for (int i = 0; i <= steps; ++i) {
        ++grid[(x1 + i * grad_x) * GRID_SIZE + (y1 + i * grad_y)];
      }
      continue;
    }
  }

  printf("%d\n", count_danger(grid));
  free(grid);
}

int main() {
  part_one();
  part_two();
  return 0;
}
