#Game of life Duc Anh Dinh , Michał Majek
import tkinter as tk


SIZE = 20
WIDTH, HEIGHT = 800, 800
INITIAL_SPEED = 200
class Cell:
    def __init__(self, canvas, x, y, size):
        self.canvas = canvas
        self.alive = False
        self.x = x
        self.y = y
        self.size = size
        self.rect = canvas.create_rectangle(x, y, x + size, y + size, fill='white')

    def set_alive(self, alive):
        self.alive = alive
        self.canvas.itemconfig(self.rect, fill='black' if self.alive else 'white')

    def toggle(self):
        self.set_alive(not self.alive)

class GameOfLife:
    def __init__(self, root, width, height, size):
        self.root = root
        self.width = width
        self.height = height
        self.size = size
        self.cells = []
        self.running = False
        self.alive_cells = 0
        self.generation = 0
        self.speed_scale = tk.Scale(self.root, from_=50, to=1000, length=400,
                                    label='Speed(ms)', orient='horizontal',
                                    sliderlength=30)
        self.speed_scale.set(INITIAL_SPEED)
        self.speed_scale.pack(side='right')
        self.canvas = tk.Canvas(root, width=self.width, height=self.height, bg='white')
        self.canvas.pack()

        for i in range(0, self.height, self.size):
            row = []
            for j in range(0, self.width, self.size):
                cell = Cell(self.canvas, j, i, self.size)
                row.append(cell)
            self.cells.append(row)

        self.canvas.bind('<Button-1>', self.toggle_cell)

        self.start_button = tk.Button(self.root, text="Start", command=self.start)
        self.start_button.pack(side='left')

        self.stop_button = tk.Button(self.root, text="Stop", command=self.stop)
        self.stop_button.pack(side='left')

        self.reset_button = tk.Button(self.root, text="Reset", command=self.reset)
        self.reset_button.pack(side='left')

        self.alive_cells_label = tk.Label(self.root)
        self.alive_cells_label.pack(side='left')

        self.generation_label = tk.Label(self.root)
        self.generation_label.pack(side='left')

    def toggle_cell(self, event):
        cell_x, cell_y = event.x // self.size, event.y // self.size
        if cell_y < len(self.cells) and cell_x < len(self.cells[0]):
            self.cells[cell_y][cell_x].toggle()

    def start(self):
        self.running = True
        self.root.after(self.speed_scale.get(), self.update)

    def stop(self):
        self.running = False

    def update_alive_cells(self):
        self.alive_cells = sum(cell.alive for row in self.cells for cell in row)
        self.alive_cells_label.config(text=f"Alive cells: {self.alive_cells}")
    def update(self):
        if not self.running:
            return

        new_state = []

        for y, row in enumerate(self.cells):
            new_row = []
            for x, cell in enumerate(row):
                alive_neighbours = self.get_alive_neighbours(x, y)
                new_alive = cell.alive

                if cell.alive and (alive_neighbours < 2 or alive_neighbours > 3):
                    new_alive = False
                elif not cell.alive and alive_neighbours == 3:
                    new_alive = True

                new_row.append(new_alive)
            new_state.append(new_row)

        for y, row in enumerate(self.cells):
            for x, cell in enumerate(row):
                cell.set_alive(new_state[y][x])

        self.update_alive_cells()
        self.generation += 1
        self.generation_label.config(text=f"Generation: {self.generation}")

        self.root.after(self.speed_scale.get(), self.update)

    def get_alive_neighbours(self, x, y):
        count = 0
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if not (i == 0 and j == 0):
                    neighbour_x = (x + j) % len(self.cells[0])
                    neighbour_y = (y + i) % len(self.cells)
                    count += self.cells[neighbour_y][neighbour_x].alive
        return count

    def reset(self):
        for row in self.cells:
            for cell in row:
                cell.set_alive(False)
        self.alive_cells = 0
        self.generation = 0
        self.alive_cells_label.config(text=f"Alive cells: {self.alive_cells}")
        self.generation_label.config(text=f"Generation: {self.generation}")

root = tk.Tk()
game = GameOfLife(root, WIDTH, HEIGHT, SIZE)
root.mainloop()
