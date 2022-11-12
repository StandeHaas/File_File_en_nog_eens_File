#A28-A1
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('HS6_data_A1_A28.csv')
q_data = {} # v/h
lst_Q = [] # v/hr_index
for i in range(1, 41):
    q_data[i] = [float(df.iloc[j][i]) for j in range(0,24)]
lst_lambda = [df.iloc[27][i] for i in range(1,41)] # number of lanes
lst_delta_l = [int(df.iloc[55][i])/1000 for i in range(1,41)] # km 
for i in range(1,41):
    q_data[i] = [float(q_data[i][j]) / int(lst_lambda[i - 1]) for j in range(0,24)]
    lst_Q.append(max(q_data[i])) #

v_data = {} # km/h
lst_v_f = []
for i in range(1, 41):
    v_data[i] = [float(df.iloc[j][i]) for j in range(30,54)]
    lst_v_f.append(max(v_data[i]))

K_data = {} # v/km
lst_K_cr = [] # v/km
lst_K_j = [] #v/km
for i in range(len(q_data)):
    i += 1
    K_data[i] = [q_data[i][j] / v_data[i][j] for j in range(0,24)]
for i in range(len(lst_Q)):
    j = q_data[i + 1].index(lst_Q[i]) #
    lst_K_cr.append(K_data[i + 1][j] * 2.35)
lst_Q = [i*1 for i in lst_Q]

for i in range(len(lst_K_cr)):
    lst_K_j.append(lst_K_cr[i] * 4) #

for i in range(1,41):
    q_data[i] = [q_data[i][j] * 1.0 for j in range(0,24)]

highway = Highway(5)

cell_10 = Cell(10,  1, lst_delta_l,q_data,lst_Q, lst_v_f,lst_K_cr, lst_K_j,lst_lambda,n = 0,ramp = False,r_index = 0,s = False,s_index = 0,B_cell = True , E_cell = False, RM = False, K_r = 0, VSL = False)
cell_11 = Cell(11,  2, lst_delta_l,q_data,lst_Q, lst_v_f,lst_K_cr, lst_K_j,lst_lambda,n = 0,ramp = False,r_index = 0,s = False,s_index = 0,B_cell = False, E_cell = False, RM = False, K_r = 0, VSL = False)
cell_12 = Cell(12,  3, lst_delta_l,q_data,lst_Q, lst_v_f,lst_K_cr, lst_K_j,lst_lambda,n = 0,ramp = False,r_index = 0,s = False,s_index = 0,B_cell = False, E_cell = False, RM = False, K_r = 0, VSL = False)
cell_13 = Cell(13,  4, lst_delta_l,q_data,lst_Q, lst_v_f,lst_K_cr, lst_K_j,lst_lambda,n = 0,ramp = False,r_index = 0,s = False,s_index = 0,B_cell = False, E_cell = False, RM = False, K_r = 0, VSL = False)
cell_14 = Cell(14,  5, lst_delta_l,q_data,lst_Q, lst_v_f,lst_K_cr, lst_K_j,lst_lambda,n = 0,ramp = False,r_index = 0,s = False,s_index = 0,B_cell = False, E_cell = False, RM = False, K_r = 0, VSL = False)
cell_15 = Cell(15,  6, lst_delta_l,q_data,lst_Q, lst_v_f,lst_K_cr, lst_K_j,lst_lambda,n = 0,ramp = False,r_index = 0,s = False,s_index = 0,B_cell = False, E_cell = False, RM = False, K_r = 0, VSL = False)
cell_200= Cell(200, 7, lst_delta_l,q_data,lst_Q, lst_v_f,lst_K_cr, lst_K_j,lst_lambda,n = 0,ramp = False,r_index = 0,s = False,s_index = 0,B_cell = False, E_cell = False, RM = False, K_r = 0, VSL = False)
cell_201= Cell(201, 8, lst_delta_l,q_data,lst_Q, lst_v_f,lst_K_cr, lst_K_j,lst_lambda,n = 0,ramp = True,r_index = 16,s = False,s_index = 0,B_cell = False, E_cell = False, RM = False, K_r = 0.8, VSL = False, RM_start = 25200, RM_end = 72000)
cell_202= Cell(202, 9, lst_delta_l,q_data,lst_Q, lst_v_f,lst_K_cr, lst_K_j,lst_lambda,n = 0,ramp = False,r_index = 0,s = False,s_index = 0,B_cell = False, E_cell = False, RM = False, K_r = 0, VSL = False)
cell_203= Cell(203,10, lst_delta_l,q_data,lst_Q, lst_v_f,lst_K_cr, lst_K_j,lst_lambda,n = 0,ramp = False,r_index = 0,s = False,s_index = 0,B_cell = False, E_cell = False, RM = False, K_r = 0, VSL = False)
cell_204= Cell(204,11, lst_delta_l,q_data,lst_Q, lst_v_f,lst_K_cr, lst_K_j,lst_lambda,n = 0,ramp = False,r_index = 0,s = True,s_index = 15,B_cell = False, E_cell = False, RM = False, K_r = 0, VSL = False)
cell_205= Cell(205,12, lst_delta_l,q_data,lst_Q, lst_v_f,lst_K_cr, lst_K_j,lst_lambda,n = 0,ramp = True,r_index = 14,s = False,s_index = 0,B_cell = False, E_cell = False, RM = False, K_r = 0, VSL = False)
cell_206= Cell(206,13, lst_delta_l,q_data,lst_Q, lst_v_f,lst_K_cr, lst_K_j,lst_lambda,n = 0,ramp = False,r_index = 0,s = False,s_index = 0,B_cell = False, E_cell = True , RM = False, K_r = 0, VSL = False)
cell_1  = Cell(1,  17, lst_delta_l,q_data,lst_Q, lst_v_f,lst_K_cr, lst_K_j,lst_lambda,n = 0,ramp = False,r_index = 0,s = False,s_index = 0,B_cell = True , E_cell = False, RM = False, K_r = 0, VSL = False)
cell_2  = Cell(2,  18, lst_delta_l,q_data,lst_Q, lst_v_f,lst_K_cr, lst_K_j,lst_lambda,n = 0,ramp = False,r_index = 0,s = False,s_index = 0,B_cell = False, E_cell = False, RM = False, K_r = 0, VSL = False)
cell_3  = Cell(3,  19, lst_delta_l,q_data,lst_Q, lst_v_f,lst_K_cr, lst_K_j,lst_lambda,n = 0,ramp = False,r_index = 0,s = False,s_index = 0,B_cell = False, E_cell = False, RM = False, K_r = 0, VSL = False)
cell_4  = Cell(4,  20, lst_delta_l,q_data,lst_Q, lst_v_f,lst_K_cr, lst_K_j,lst_lambda,n = 0,ramp = False,r_index = 0,s = False,s_index = 0,B_cell = False, E_cell = False, RM = False, K_r = 0, VSL = False)
cell_5  = Cell(5,  21, lst_delta_l,q_data,lst_Q, lst_v_f,lst_K_cr, lst_K_j,lst_lambda,n = 0,ramp = False,r_index = 0,s = False,s_index = 0,B_cell = False, E_cell = False, RM = False, K_r = 0, VSL = False)
cell_100= Cell(100,22, lst_delta_l,q_data,lst_Q, lst_v_f,lst_K_cr, lst_K_j,lst_lambda,n = 0,ramp = False,r_index = 0,s = False,s_index = 0,B_cell = False, E_cell = False, RM = False, K_r = 0, VSL = False)
cell_101= Cell(101,23, lst_delta_l,q_data,lst_Q, lst_v_f,lst_K_cr, lst_K_j,lst_lambda,n = 0,ramp = False,r_index = 0,s = False,s_index = 0,B_cell = False, E_cell = True , RM = False, K_r = 0, VSL = False)
cell_20 = Cell(20 ,24, lst_delta_l,q_data,lst_Q, lst_v_f,lst_K_cr, lst_K_j,lst_lambda,n = 0,ramp = False,r_index = 0,s = False,s_index = 0,B_cell = False, E_cell = False, RM = False, K_r = 0, VSL = False)
cell_30 = Cell(30 ,25, lst_delta_l,q_data,lst_Q, lst_v_f,lst_K_cr, lst_K_j,lst_lambda,n = 0,ramp = False,r_index = 0,s = False,s_index = 0,B_cell = False, E_cell = False, RM = False, K_r = 0, VSL = False)
cell_31 = Cell(31 ,26, lst_delta_l,q_data,lst_Q, lst_v_f,lst_K_cr, lst_K_j,lst_lambda,n = 0,ramp = False,r_index = 0,s = False,s_index = 0,B_cell = False, E_cell = False, RM = False, K_r = 0, VSL = False)
cell_61 = Cell(61 ,27, lst_delta_l,q_data,lst_Q, lst_v_f,lst_K_cr, lst_K_j,lst_lambda,n = 0,ramp = True,r_index = 28,s = False,s_index = 0,B_cell = False, E_cell = False, RM = False, K_r = 0, VSL = False)
cell_62  = Cell(62 ,29,lst_delta_l,q_data,lst_Q, lst_v_f,lst_K_cr, lst_K_j,lst_lambda,n = 0,ramp = False,r_index = 0,s = False,s_index = 0,B_cell = False, E_cell = False, RM = False, K_r = 0, VSL = False)
cell_40 = Cell(40 ,30, lst_delta_l,q_data,lst_Q, lst_v_f,lst_K_cr, lst_K_j,lst_lambda,n = 0,ramp = False,r_index = 0,s = True,s_index = 31,B_cell = False, E_cell = False, RM = False, K_r = 0, VSL = False)
cell_41 = Cell(41 ,32, lst_delta_l,q_data,lst_Q, lst_v_f,lst_K_cr, lst_K_j,lst_lambda,n = 0,ramp = False,r_index = 0,s = False,s_index = 0,B_cell = False, E_cell = False, RM = False, K_r = 0, VSL = False)
cell_42 = Cell(42 ,33, lst_delta_l,q_data,lst_Q, lst_v_f,lst_K_cr, lst_K_j,lst_lambda,n = 0,ramp = True,r_index = 34,s = True,s_index = 35,B_cell = False, E_cell = False, RM = False, K_r = 0, VSL = False)
cell_43 = Cell(43 ,36, lst_delta_l,q_data,lst_Q, lst_v_f,lst_K_cr, lst_K_j,lst_lambda,n = 0,ramp = True,r_index = 37,s = False,s_index = 0,B_cell = False, E_cell = False, RM = False, K_r = 0, VSL = False)
cell_50 = Cell(50 ,38, lst_delta_l,q_data,lst_Q, lst_v_f,lst_K_cr, lst_K_j,lst_lambda,n = 0,ramp = False,r_index = 0,s = False,s_index = 0,B_cell = False, E_cell = False, RM = False, K_r = 0, VSL = False)
cell_44 = Cell(44 ,39, lst_delta_l,q_data,lst_Q, lst_v_f,lst_K_cr, lst_K_j,lst_lambda,n = 0,ramp = False,r_index = 0,s = False,s_index = 0,B_cell = False, E_cell = False, RM = False, K_r = 0, VSL = False)
cell_45 = Cell(45 ,40, lst_delta_l,q_data,lst_Q, lst_v_f,lst_K_cr, lst_K_j,lst_lambda,n = 0,ramp = False,r_index = 0,s = False,s_index = 0,B_cell = False, E_cell = False, RM = False, K_r = 0, VSL = False)

highway.add_cell(cell_10)
highway.add_cell(cell_11)
highway.add_cell(cell_12)
highway.add_cell(cell_13)
highway.add_cell(cell_14)
highway.add_cell(cell_15)
highway.add_cell(cell_200)
highway.add_cell(cell_201)
highway.add_cell(cell_202)
highway.add_cell(cell_203)
highway.add_cell(cell_204)
highway.add_cell(cell_205)
highway.add_cell(cell_206)
highway.add_cell(cell_1)
highway.add_cell(cell_2)
highway.add_cell(cell_3)
highway.add_cell(cell_4)
highway.add_cell(cell_5)
highway.add_cell(cell_100)
highway.add_cell(cell_101)
highway.add_cell(cell_20)
highway.add_cell(cell_30)
highway.add_cell(cell_31)
highway.add_cell(cell_61)
highway.add_cell(cell_62)
highway.add_cell(cell_40)
highway.add_cell(cell_41)
highway.add_cell(cell_42)
highway.add_cell(cell_43)
highway.add_cell(cell_50)
highway.add_cell(cell_44)
highway.add_cell(cell_45)

highway.add_link(cell_10, cell_11)
highway.add_link(cell_11, cell_12)
highway.add_link(cell_12, cell_13)
highway.add_link(cell_13, cell_14)
highway.add_link(cell_14, cell_15)
highway.add_link(cell_15, cell_200)
highway.add_link(cell_200, cell_201)
highway.add_link(cell_201, cell_202)
highway.add_link(cell_202, cell_203)
highway.add_link(cell_203, cell_204)
highway.add_link(cell_204, cell_205)
highway.add_link(cell_205, cell_206)
highway.add_link(cell_1, cell_2)
highway.add_link(cell_2, cell_3)
highway.add_link(cell_3, cell_4)
highway.add_link(cell_4, cell_5)
highway.add_link(cell_5, cell_100)
highway.add_link(cell_100, cell_101)
highway.add_link(cell_2, cell_40)
highway.add_link(cell_40, cell_41)
highway.add_link(cell_41, cell_42)
highway.add_link(cell_42, cell_43)
highway.add_link(cell_43, cell_44)
highway.add_link(cell_44, cell_45)
highway.add_link(cell_45, cell_100)
highway.add_link(cell_13, cell_20)
highway.add_link(cell_20, cell_61)
highway.add_link(cell_61, cell_62)
highway.add_link(cell_62, cell_200)
highway.add_link(cell_20, cell_30)
highway.add_link(cell_30, cell_31)
highway.add_link(cell_31, cell_45)
highway.add_link(cell_43, cell_50)
highway.add_link(cell_50, cell_61)

TTS, results, n_tot, results_v = run(highway, 0*3600, 24*3600)
#TTS, results, n_tot = increase_lanes(highway, [11,12,13,14], 1, 0*3600, 24*3600)
print('V_f:       ',lst_v_f)
print('K_cr:      ',lst_K_cr)
print('K_j:       ',lst_K_j)
print('Q:         ',lst_Q)
print('TTS:       ',TTS)
print('N_tot:     ',n_tot)
print('TTS/N_tot: ',TTS / n_tot)
visualiser(highway, results, [10,11,12,13,14,15,200,201,202,203,204,205], 0, 86400, 24)
visualiser(highway, results, [1,2,40,41,42,43,44,45,100], 0, 86400, 24)
results_1A = visualiser_v_data(highway, v_data, [10,11,12,13,14,15,200,201,202,203,204,205])
results_1B = visualiser_v(highway, results_v, [10,11,12,13,14,15,200,201,202,203,204,205], 0,  86400, 24)
results_2A = visualiser_v_data(highway, v_data, [1,2,40,41,42,43,44,45,100])
results_2B = visualiser_v(highway, results_v, [1,2,40,41,42,43,44,45,100], 0,  86400, 24)
results_3A = visualiser_v_data(highway, v_data, [10,11,12,13,14,15,200,201,202,203,204,205,1,2,3,4,5,40,41,42,43,44,45,100,20,30,31,61,62,50])
results_3B = visualiser_v(highway, results_v, [10,11,12,13,14,15,200,201,202,203,204,205,1,2,3,4,5,40,41,42,43,44,45,100,20,30,31,61,62,50], 0,  86400, 24)

average_difference(results_1A, results_1B)
average_difference(results_2A, results_2B)
average_difference(results_3A, results_3B)