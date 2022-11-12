import matplotlib.pyplot as plt

class Highway:
    def __init__(self, directed = True):
        self.directed = True
        self.graph_dict = {}

    def add_cell(self, Cell):
        self.graph_dict[Cell.value] = Cell

    def add_link(self, from_cell, to_cell, weight=0): 
        self.graph_dict[from_cell.value].add_link(to_cell.value, weight)
        if self.directed == False:
            self.graph_dict[to_cell.value].add_link(from_cell.value, weight)
    
    def update_CTM(self):
        lst = []
        for value in self.graph_dict:
            if value == 1 or value == 10:
                pass
            else:
                n = self.graph_dict[value - 1].get_n()
                Q = self.graph_dict[value].get_Q()
                N = self.graph_dict[value].get_w()/self.graph_dict[value].get_v_f()*(self.graph_dict[value].get_N() - self.graph_dict[value].get_n())
                y_in = min(n, Q, N)
                y_out = min(self.graph_dict[value].get_n(), self.graph_dict[value + 1].get_Q(), self.graph_dict[value + 1].get_w()/self.graph_dict[value + 1].get_v_f()*(self.graph_dict[value + 1].get_N() - self.graph_dict[value + 1].get_n()))
                n_t = self.graph_dict[value].get_n() + y_in - y_out
                self.graph_dict[value].set_n(n_t)
                lst.append(n_t)
        return lst       

class Cell: 
    def __init__(self, value, K_cr, K_j, Q = 29,  v_f = 30, delta_l = 300, delta_t = 10, n = 0):
        self.value = value
        self.links = {}
        self.K_cr = K_cr
        self.K_j = K_j
        self.N = K_j * delta_l
        self.Q = Q
        self.v_f = v_f
        self.delta_l = delta_l
        self.delta_t = delta_t
        self.n = n
        
    def set_n(self, value):
        self.n = value

    def get_n(self):
        return self.n
    def get_v_f(self):
        return self.v_f
    def get_w(self):
        w = (self.v_f * self.K_cr) / (self.K_j - self.K_cr)
        return w
    def get_N(self):
        return self.N
    def get_Q(self):
        return self.Q
    def add_link(self, Cell, weight=0):
        self.links[Cell] = weight

highway = Highway()
B_cell = Cell(1, 0.1, 0.30, n = 10000000000)
cell_2 = Cell(2, 0.1, 0.30)
cell_3 = Cell(3, 0.1, 0.30)
cell_4 = Cell(4, 0.1, 0.30)
cell_5 = Cell(5, 0.1, 0.30) 
cell_6 = Cell(6, 0.1, 0.30)
cell_7 = Cell(7, 0.1, 0.30, n = 40)
cell_8 = Cell(8, 0.1, 0.30, n = 40)
cell_9 = Cell(9, 0.1, 0.30, n = 40)
E_cell = Cell(10, 1000, 100000)

highway.add_cell(B_cell)
highway.add_cell(cell_2)
highway.add_cell(cell_3)
highway.add_cell(cell_4)
highway.add_cell(cell_5)
highway.add_cell(cell_6)
highway.add_cell(cell_7)
highway.add_cell(cell_8)
highway.add_cell(cell_9)
highway.add_cell(E_cell)

highway.add_link(B_cell, cell_2)
highway.add_link(cell_2, cell_3)
highway.add_link(cell_3, cell_4)
highway.add_link(cell_4, cell_5)
highway.add_link(cell_5, cell_6)
highway.add_link(cell_6, cell_7)
highway.add_link(cell_7, cell_8)
highway.add_link(cell_8, cell_9)
highway.add_link(cell_9, E_cell)

n_lst = []
for i in range(60):
    lst = highway.update_CTM()
    print(lst)
    n_lst.append(lst)

fig, ax = plt.subplots(nrows=10, ncols=1)
n = 0 
for row in ax:
    row.plot(n_lst[n])
    n += 3
plt.xlabel('Cellen')
plt.ylabel('Aantal voertuigen (n_i)')
plt.suptitle('Verplaatsing van een shockwave')
plt.show()