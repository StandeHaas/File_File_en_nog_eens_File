# test with s+
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('HS5_data_TEST_EXPERIMENT_3.csv')
q_data = {} # v/h
lst_Q = [] # v/hr_index
for i in range(1, 16):
    q_data[i] = [float(df.iloc[j][i]) for j in range(0,24)]
lst_lambda = [df.iloc[27][i] for i in range(1,16)] # number of lanes
lst_delta_l = [int(df.iloc[55][i])/1000 for i in range(1,16)] # km 
for i in range(1,16):
    q_data[i] = [float(q_data[i][j]) / int(lst_lambda[i - 1]) for j in range(0,24)]
    lst_Q.append(max(q_data[i]) * 1.2)  

v_data = {} # km/h
lst_v_f = []
for i in range(1, 16):
    v_data[i] = [int(df.iloc[j][i]) for j in range(30,54)]
    lst_v_f.append(max(v_data[i]))

K_data = {} # v/km
lst_K_cr = [] # v/km
lst_K_j = [] #v/km
for i in range(len(q_data)):
    i += 1
    K_data[i] = [q_data[i][j] / v_data[i][j] for j in range(0,24)]
for i in range(len(lst_Q)):
    j = q_data[i + 1].index(lst_Q[i] / 1.2) 
    lst_K_cr.append(K_data[i + 1][j])

for i in range(len(lst_K_cr)):
    lst_K_j.append(lst_K_cr[i] * 5) 
highway = Highway(2.5)

cell_1 = Cell(  1, 1, lst_delta_l,q_data,lst_Q, lst_v_f,lst_K_cr, lst_K_j,lst_lambda,n = 0,r = False,r_index = 0,s = False,s_index = 0,B_cell = True , E_cell = False, RM = False, K_r = 0, VSL = False)
cell_2 = Cell(  2, 2, lst_delta_l,q_data,lst_Q, lst_v_f,lst_K_cr, lst_K_j,lst_lambda,n = 0,r = False,r_index = 0,s = False,s_index = 0,B_cell = False, E_cell = False, RM = False, K_r = 0, VSL = False)
cell_3 = Cell(  3, 3, lst_delta_l,q_data,lst_Q, lst_v_f,lst_K_cr, lst_K_j,lst_lambda,n = 0,r = False,r_index = 0,s = False,s_index = 0,B_cell = False, E_cell = False, RM = False, K_r = 0, VSL = False)
cell_4 = Cell(  4, 4, lst_delta_l,q_data,lst_Q, lst_v_f,lst_K_cr, lst_K_j,lst_lambda,n = 0,r = False,r_index = 0,s = False,s_index = 0,B_cell = False, E_cell = False, RM = False, K_r = 0, VSL = False)
cell_5 = Cell(  5, 5, lst_delta_l,q_data,lst_Q, lst_v_f,lst_K_cr, lst_K_j,lst_lambda,n = 0,r = False,r_index = 0,s = False,s_index = 0,B_cell = False, E_cell = False, RM = False, K_r = 0, VSL = False)
cell_6 = Cell( 6,6,   lst_delta_l,q_data,lst_Q, lst_v_f,lst_K_cr, lst_K_j,lst_lambda,n = 0,r = False,r_index = 0,s = False,s_index = 0,B_cell = False, E_cell = False, RM = False, K_r = 0, VSL = False)
cell_7 = Cell( 7,7,   lst_delta_l,q_data,lst_Q, lst_v_f,lst_K_cr, lst_K_j,lst_lambda,n = 0,r = False,r_index = 0,s = False,s_index = 0,B_cell = False, E_cell = False, RM = False, K_r = 0, VSL = False)
cell_8 = Cell( 8,8,   lst_delta_l,q_data,lst_Q, lst_v_f,lst_K_cr, lst_K_j,lst_lambda,n = 0,r = False,r_index = 0,s = False,s_index = 0,B_cell = False, E_cell = False, RM = False, K_r = 0, VSL = False)
cell_9 = Cell( 9,9,   lst_delta_l,q_data,lst_Q, lst_v_f,lst_K_cr, lst_K_j,lst_lambda,n = 0,r = False,r_index = 0,s = False,s_index = 0,B_cell = False, E_cell = False, RM = False, K_r = 0, VSL = False)
cell_10 = Cell(10,10, lst_delta_l,q_data,lst_Q, lst_v_f,lst_K_cr, lst_K_j,lst_lambda,n = 0,r = False,r_index = 0,s = False,s_index = 0,B_cell = False, E_cell = True , RM = False, K_r = 0, VSL = False)
cell_11 = Cell(11,11, lst_delta_l,q_data,lst_Q, lst_v_f,lst_K_cr, lst_K_j,lst_lambda,n = 0,r = False,r_index = 0,s = False,s_index = 0,B_cell = False, E_cell = False, RM = False, K_r = 0, VSL = False)
cell_12 = Cell(12,12, lst_delta_l,q_data,lst_Q, lst_v_f,lst_K_cr, lst_K_j,lst_lambda,n = 0,r = False,r_index = 0,s = False,s_index = 0,B_cell = False, E_cell = False, RM = False, K_r = 0, VSL = False)
cell_13 = Cell(13,13, lst_delta_l,q_data,lst_Q, lst_v_f,lst_K_cr, lst_K_j,lst_lambda,n = 0,r = False,r_index = 0,s = False,s_index = 0,B_cell = False, E_cell = False, RM = False, K_r = 0, VSL = False)
cell_14 = Cell(14,14, lst_delta_l,q_data,lst_Q, lst_v_f,lst_K_cr, lst_K_j,lst_lambda,n = 0,r = False,r_index = 0,s = False,s_index = 0,B_cell = False, E_cell = False, RM = False, K_r = 0, VSL = False)
cell_15 = Cell(15,15, lst_delta_l,q_data,lst_Q, lst_v_f,lst_K_cr, lst_K_j,lst_lambda,n = 0,r = False,r_index = 0,s = False,s_index = 0,B_cell = False, E_cell = True , RM = False, K_r = 0, VSL = False)


highway.add_cell(cell_1)
highway.add_cell(cell_2)
highway.add_cell(cell_3)
highway.add_cell(cell_4)
highway.add_cell(cell_5)
highway.add_cell(cell_6)
highway.add_cell(cell_7)
highway.add_cell(cell_8)
highway.add_cell(cell_9)
highway.add_cell(cell_10)
highway.add_cell(cell_11)
highway.add_cell(cell_12)
highway.add_cell(cell_13)
highway.add_cell(cell_14)
highway.add_cell(cell_15)


highway.add_link(cell_1, cell_2)
highway.add_link(cell_2, cell_3)
highway.add_link(cell_3, cell_4)
highway.add_link(cell_4, cell_5)
highway.add_link(cell_5, cell_10)
highway.add_link(cell_5, cell_6)
highway.add_link(cell_6, cell_7)
highway.add_link(cell_7, cell_8)
highway.add_link(cell_8, cell_9)
highway.add_link(cell_9, cell_10)
highway.add_link(cell_10, cell_11)
highway.add_link(cell_11, cell_12)
highway.add_link(cell_12, cell_13)
highway.add_link(cell_13, cell_14)
highway.add_link(cell_14, cell_15)

