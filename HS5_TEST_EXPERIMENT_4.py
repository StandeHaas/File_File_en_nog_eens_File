# test with r+
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('HS5_TEST_EXPERIMENT_4.csv')
q_data = {} # v/h
lst_Q = [] # v/hr_index
for i in range(1, 17):
    q_data[i] = [float(df.iloc[j][i]) for j in range(0,24)]
lst_lambda = [df.iloc[27][i] for i in range(1,17)] # number of lanes
lst_delta_l = [int(df.iloc[55][i])/1000 for i in range(1,17)] # km 
for i in range(1,17):
    q_data[i] = [float(q_data[i][j]) / int(lst_lambda[i - 1]) for j in range(0,24)]
    lst_Q.append(max(q_data[i]) * 1.2)  

v_data = {} # km/h
lst_v_f = []
for i in range(1, 17):
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
    lst_K_cr.append(K_data[i + 1][j] * 3.5)

for i in range(len(lst_K_cr)):
    lst_K_j.append(lst_K_cr[i] * 4)
highway = Highway(5)

cell_1 = Cell(  1, 1, lst_delta_l,q_data,lst_Q, lst_v_f,lst_K_cr, lst_K_j,lst_lambda,n = 0,ramp = False,r_index = 0,s = False,s_index = 0,B_cell = True , E_cell = False, RM = False, K_r = 0, VSL = False)
cell_2 = Cell(  2, 2, lst_delta_l,q_data,lst_Q, lst_v_f,lst_K_cr, lst_K_j,lst_lambda,n = 0,ramp = False,r_index = 0,s = False,s_index = 0,B_cell = False, E_cell = False, RM = False, K_r = 0, VSL = False)
cell_3 = Cell(  3, 3, lst_delta_l,q_data,lst_Q, lst_v_f,lst_K_cr, lst_K_j,lst_lambda,n = 0,ramp = False,r_index = 0,s = False,s_index = 0,B_cell = False, E_cell = False, RM = False, K_r = 0, VSL = False)
cell_4 = Cell(  4, 4, lst_delta_l,q_data,lst_Q, lst_v_f,lst_K_cr, lst_K_j,lst_lambda,n = 0,ramp = False,r_index = 0,s = False,s_index = 0,B_cell = False, E_cell = False, RM = False, K_r = 0, VSL = False)
cell_5 = Cell(  5, 5, lst_delta_l,q_data,lst_Q, lst_v_f,lst_K_cr, lst_K_j,lst_lambda,n = 0,ramp = False,r_index = 0,s = False,s_index = 0,B_cell = False, E_cell = False, RM = True, K_r = 5, VSL = False, RM_start = 61200)
cell_10 = Cell( 6,6, lst_delta_l,q_data,lst_Q, lst_v_f,lst_K_cr, lst_K_j,lst_lambda,n = 0,ramp = False,r_index = 0,s = False,s_index = 0,B_cell = True , E_cell = False, RM = False, K_r = 0, VSL = False)
cell_11 = Cell( 7,7, lst_delta_l,q_data,lst_Q, lst_v_f,lst_K_cr, lst_K_j,lst_lambda,n = 0,ramp = False,r_index = 0,s = False,s_index = 0,B_cell = False, E_cell = False, RM = False, K_r = 0, VSL = False)
cell_12 = Cell( 8,8, lst_delta_l,q_data,lst_Q, lst_v_f,lst_K_cr, lst_K_j,lst_lambda,n = 0,ramp = False,r_index = 0,s = False,s_index = 0,B_cell = False, E_cell = False, RM = False, K_r = 0, VSL = False)
cell_13 = Cell( 9,9, lst_delta_l,q_data,lst_Q, lst_v_f,lst_K_cr, lst_K_j,lst_lambda,n = 0,ramp = False,r_index = 0,s = False,s_index = 0,B_cell = False, E_cell = False, RM = False, K_r = 0, VSL = False)
cell_14 = Cell(10,10, lst_delta_l,q_data,lst_Q, lst_v_f,lst_K_cr, lst_K_j,lst_lambda,n = 0,ramp = False,r_index = 0,s = False,s_index = 0,B_cell = False, E_cell = False, RM = False, K_r = 0, VSL = False)
cell_20 = Cell(11,11, lst_delta_l,q_data,lst_Q, lst_v_f,lst_K_cr, lst_K_j,lst_lambda,n = 0,ramp = False,r_index = 0,s = False,s_index = 0,B_cell = False, E_cell = False, RM = False, K_r = 0, VSL = False)
cell_21 = Cell(12,12, lst_delta_l,q_data,lst_Q, lst_v_f,lst_K_cr, lst_K_j,lst_lambda,n = 0,ramp = False,r_index = 0,s = False,s_index = 0,B_cell = False, E_cell = False, RM = False, K_r = 0, VSL = False)
cell_22 = Cell(13,13, lst_delta_l,q_data,lst_Q, lst_v_f,lst_K_cr, lst_K_j,lst_lambda,n = 0,ramp = False,r_index = 0,s = False,s_index = 0,B_cell = False, E_cell = False, RM = False, K_r = 0, VSL = False)
cell_23 = Cell(14,14, lst_delta_l,q_data,lst_Q, lst_v_f,lst_K_cr, lst_K_j,lst_lambda,n = 0,ramp = False,r_index = 0,s = False,s_index = 0,B_cell = False, E_cell = False, RM = False, K_r = 0, VSL = False)
cell_24 = Cell(15,15, lst_delta_l,q_data,lst_Q, lst_v_f,lst_K_cr, lst_K_j,lst_lambda,n = 0,ramp = False,r_index = 0,s = False,s_index = 0,B_cell = False, E_cell = False, RM = False, K_r = 0, VSL = False)
cell_25 = Cell(16,16, lst_delta_l,q_data,lst_Q, lst_v_f,lst_K_cr, lst_K_j,lst_lambda,n = 0,ramp = False,r_index = 0,s = False,s_index = 0,B_cell = False, E_cell = True , RM = False, K_r = 0, VSL = False)


highway.add_cell(cell_10)
highway.add_cell(cell_11)
highway.add_cell(cell_12)
highway.add_cell(cell_13)
highway.add_cell(cell_14)
highway.add_cell(cell_1)
highway.add_cell(cell_2)
highway.add_cell(cell_3)
highway.add_cell(cell_4)
highway.add_cell(cell_5)
highway.add_cell(cell_20)
highway.add_cell(cell_21)
highway.add_cell(cell_22)
highway.add_cell(cell_23)
highway.add_cell(cell_24)
highway.add_cell(cell_25)

highway.add_link(cell_10, cell_11)
highway.add_link(cell_11, cell_12)
highway.add_link(cell_12, cell_13)
highway.add_link(cell_13, cell_14)
highway.add_link(cell_14, cell_20)
highway.add_link(cell_1, cell_2)
highway.add_link(cell_2, cell_3)
highway.add_link(cell_3, cell_4)
highway.add_link(cell_4, cell_5)
highway.add_link(cell_5, cell_20)
highway.add_link(cell_20, cell_21)
highway.add_link(cell_21, cell_22)
highway.add_link(cell_22, cell_23)
highway.add_link(cell_23, cell_24)
highway.add_link(cell_24, cell_25)

TTS, results, n_tot, results_v = run(highway, 0*3600, 24*3600)
print('V_f:       ',lst_v_f)
print('K_cr:      ',lst_K_cr)
print('K_j:       ',lst_K_j)
print('Q:         ',lst_Q)
print('TTS:       ',TTS)
print('N_tot:     ',n_tot)
print('TTS/N_tot: ',TTS / n_tot)
visualiser(highway, results, [1,2,3,4,5,20,21,22,23,24], 0, 86400, 24)
visualiser(highway, results, [10,11,12,13,14,20,21,22,23,24], 0, 86400, 24)
