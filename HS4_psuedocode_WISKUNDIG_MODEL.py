import matplotlib.pyplot as plt
import pandas as pd

# define CLASS highway: (-> graph)
#   DEF __INIT__:
#     TRUE or FALSE directed graph (-> FALSE since has to look back at cells in certain cases)
#     graph_dict = {}
#     define TIMESTEP
#
#   DEF add cell (defined in Cell CLASS):
#      add cell and cell.value to graph_dict
#
#   DEF add link:
#      access from_cell through graph_dict and add link te cell CLASS
#      IF cell is undirected:
#           access to_cell through gprah_dict and add link to cell CLASS
#   
#   DEF RUN_CTM():
#       amount of timesteps = 86400 / TIMESTEP
#       adjust_data(self, timestep) (-> makes sure that we have as many inputs as timesteps)
#       r = 0 (-> ramp metering variable)
#       TTS = 0 
#       FOR t in range(amount of timesteps):
#           lst_cell_2 = []
#           FOR value (of cell (they are in order)) in graph dict:
    #           IF value in lst_cell_2:
    #               pass
    #           ELIF graph_dict.get_e_cell() == TRUE:
    #               pass
    #           ELSE: 
'Update TTS'
#                   TTS += cell.get_n + cell_2.get_n                     
"DEFINE output and make sure it doens't exceed the capacity of the output cell in case it has a r"
    #               IF graph_dict[value].get_b_cell = TRUE:
    #                   n_1_out = graph_dict[value].get_q_lst(t)
    #               ELSE:
    #                   n_1_out = cell.get_n * (self.timestep / (cell.get_delta_l / cell.get_v_f)
    #               n_2_out = 0
    #
    #               FOR link in links cell:
    #                   IF link value > current value cell: (you know that it's a cell to which you output)(it has 1 at max)
    #                       link = link value
        #                   FOR next_link in links link: (checks if output only has one input)
        #                       IF value of next link < link value && value != value of current cell: (has multiple inputs)
        #                           cell_2 = graph_dict.value
        #                           lst_cell_2.append(cell_2)
        #                           n_2_out = next link.get_n * (self.timestep / (next link.get_delta_l / next link.get_v_f)
        #                       ELSE:
        #                           cell_2 = 0 

'extra input r'
#                   IF graph_dict[link].get_onramp == TRUE:
#                       r_in = graph_dict[link].get_onramp_data(t)
#                       input_ratio_onramp = graph_dict[link].get_input_ratio()
#                   ELSE: 
#                       r_in = 0 

'Calculation for y_out'
    #               n_out = n_1_out + n_2_out + r_in 
    #               Q_out = link.get_Q * link.get_lambda
    #               N_out = \frac{w}{v_f}(N_i*lambda-n_i) (for link cell)
    #               y_out_all = min of n,Q,N

'extra input incase an other controlled cell'
    #               IF n_2_out != 0: (update the input if there's input from multiple cells)
    #                   IF y_out_all != n_out (so vehicles are getting in at maximum capacity):    
'since RM requires too many variables just gone do it within the code, bit messy'
'should really be checked prop incorrect'
        #                   IF value.get RM == TRUE:
        #                        y_2_out = Min(n_2_out, Q_out, N_out) 
        #                        y_out = Max(0, K_r(Q/v_f*delta_l - n - y_2_out)) (-> Q,v_f, delta_l and n of link to which we output)
        #                   ELIF cell_2.get RM == TRUE:
        #                       y_out = Min(n_out, Q_out, N_out) 
        #                       y_2_out = Max(0, K_r(Q/v_f*delta_l - n - y_out)) (-> Q, v_f, delta_l en n of link to which we output)
        #                   ELSE: 
            #                   input_ratio = input_ratio(current cell, cell_2)
            #                   IF value cell_2 < value current cell:
            #                       y_2_out = y_out_all * (1 - input_ratio)
            #                       y_out = y_out_all *  input_ratio
            #                   ELSE: 
            #                       y_2_out = y_out_all * input_ratio
            #                       y_out = y_out_all * (1 - input_ratio)             
        #           ELSE:
        #               y_out = y_out_all
        

"update y_out in case of input r"
#                   IF r_in != 0:
#                       IF y_out_all != n_out (so vehicles are getting in at maximum capacity):
    #                       r_jam = r_in - y_out_all * (1- input_onramp_onramp)
    #                       graph_dict[link].set_input_r(r_jam, t + 1)
    #                       r_in = y_out_all * (1- input_onramp_onramp)                       
    #                       y_out = y_out_all *  input_ratio_onramp
           
'DEFINE extra output: offramps'          
        #           IF value has offramps:
            #           s = y_out / (1 - beta)* beta  (-> beta accessed by getter function of current cell with timestep)
            #           y_out *= (1 - beta) 
            #       ELSE:
            #           s = 0 
        #           IF cell_2 has offramps:
            #           s_2 = y_2_out / (1- beta)*beta (beta accessed by getter function of the cell_2 with timestep)
            #           y_2_out *= (1 - beta) 
            #       ELSE: 
            #           s_2 = 0 

'FINAL calculation'
    #               graph_dict[value].set_output(y_out, s)
    #               IF cell_2:
          #               graph_dict[cell_2].set_output(y_2_out, s_2)
    #               graph_dict[link].set_input(y_out, y_2_out, r_in)

'RETURN TTS'
#       return TTS * delta_t


'the CELL'
# define CLASS cell:
#   DEF __INIT__():
#       DICT links 
#       define VALUE of cell (increasing numbers will be connected to each other forming a highway)
#       define LENGHT of cell
#       define all values to form FD (this will always be defined for a single lane, to keep it all aline, calculation will happen in run function): 
#            Q
#            v_f   
#            K_cr
#            K_j
#            lambda (number of lanes)
#            n, number of vehicles (t = 0, n = 0)
#            lst_q
#            lst_s  
#            lst_r
#       calculate other required variables:
#            N (max number of vehicles) = K_j * delta_l
#            w (speed of shockwave) (= (v_f - K_cr)/(K_j - K_cr))
#       TRUE FALSE onramps
#       IF TRUE: 
#           input_ratio_onramp = input_ratio_onramp() 
#       TRUE FALSE offramps
#       IF TRUE (->) split ratio for offramps (beta = 0 normally))
#           beta = split_ratio(lst_q, lst_s)
#       TRUE FALSE E_cell
#           
#       TRUE FALSE B_cell
#       IF TRUE:
#          lst_q list with data per hour
#       
#       RM (-> normally set to FALSE)
#           K_r (-> normally set to 0)
#       VSL (-> normally set to FALSE)
#           alpha (-> 'naveling' normally set to 0)
#           b
#           A
#           lst_v_c
#   
# DEF add link:
#       add cell to links DICT
#
#   DEF GETTERS for all input values of cell (for Highway class)
#   DEF SETTERS for all values X_t (i.e. that change over time and are influenced by highway module)
#   DEF SETTERS INPUT to increase n by the amount of y_in + r 
#   DEF SETTERS OUTPUT to decrease n by the amount of y_out + s
#   DEF SETTER INPUT to increase r by the amount of r_jam on time t in list
#
'some function that compares two cells that are both influenced on maybe lanes and Q to define in which proportion the get allowed on road'
'should look if there is a proper approximation for this but for now this is a good guess'
# DEF input_ratio(cell_1, cell_2):
#   input_1 = graph_dict[cell_1].get_lambda * graph_dict[cell_1].get_Q
#   input_2 = graph_dict[cell_2].get_lambda * graph_dict[cell_2].get_Q
#   IF cell_1.value > cell_2.value:
#     RETURN input_1 / (input_1 + input_2)
#   ELSE:
#     RETURN input_2 / (input_1 + input_2)
#
'Split ratio: that can change every hour'
# DEF split_ratio(cell, s): (-> both lists of q)
#   beta_lst = []
#   FOR t in range(len(cell)):
#       beta = s[t] / (s[t] + cell[t])
#       beta_lst.append(beta)
#   return beta_lst
#
'Input ratio for onramp (-> should look for better solution)'
# DEF inut_ratio(cell, r):
#   input_cell = cell.get_lambda * cell.get_Q
#   input_r = max(r)
#   RETURN input_cell / (input_r + input_cell)
#   
'Adjust data'
# DEF adjust_data(highway, timestep):
#   lst_q = []
#   lst_r = []
#   lst_s = []
#   timestep_per_hour = 3600 / timestep
#   FOR value in highway:
#      IF B_CELL:
#         FOR value in q (of b_cell):
#            FOR _ in range(timestep_per_hour):
#               lst_q.append(value)
#         graph_dict[value of b_cell].set_lst_q(lst_q)
#     IF ONRAMP:
#         FOR value in q (of onramp):
#            FOR _ in range(timestep_per_hour):
#               lst_r.append(value)
#         graph_dict[value of cell].set_lst_r(lst_r)
#     IF OFFRAMP:
#         FOR value in s (of offramp):
#            FOR _ in range(timestep_per_hour):
#               lst_s.append(value)
#         graph_dict[value of cell].set_lst_s(lst_s)
#

"ALREADY PROGAMMED OUT SINCE THIS IS JUST BASIC DATA MANAG"

"TRANSFORM DATA & (semi) automatic cell and highway structure"
" the use of historical doesn't require some API, just read a download CSV file." 
"exact form of data is unclear this is just a simple principle"
'make sure that all units are equal, so veh,h,km'
#   df (pandas dataframe) = read csv file
' each cell will have hour averages of flow and speed'
#  FOR each cell:
#   read q to form a list
#   ? requires manual input for the amount of lanes 
#   FOR q in range(len(lst_q)):
#       lst_q[q] /= lambda
#   read v to form a list
#   v_f = max(v)
#   Q = max(q)
#   create list k = q / v
#   ? read the max and min for K_cr and K_j = 4 * K_cr (-> follows out of some old study really inaccurate) --> this is really inaccurate 
#   ? requires manual input for lenght of celld
# FOR each onramps:
#   read q to form a list lst_r
# FOR each offramp:
#   read q to form a list lst_s

# FOR each cell:
#   create cell CLASS with all the data combined (-> including data for on/offramps)
# create B cell with lst_q
# create E cell with N and Q = infty (k_j = infinty) ()
# 
# create Highway CLASS
# create LINKS between the cells





"FUNCTTIONS FOR VSL, RM and increasing of LANES" "-> since the models are small we will introduce the same VSL speed in all of the cells"
'RM is inplemented within the code, when the decrease in TTS wants to be measured, just run one with and one without and compare'
# DEF VSL(Highway, list_cells): (-> uses the last proposed model out 2018)
#    v_c_max = max(lst_v_c)
#    results = {}
#       TTS = hihgway.run_cmt (-> zero VSL case)
#       results[v_c] = TTS
#    for v_c in lst_v_c
#       b = min(v_c / v_c_max) * (1 + alpha), 1)
#       v_f  = min(v_c_max * b, v_f)
#       k_cr = k_cr(1 + A(1 - b))
#       FOR cell in list_cells:
    #       graph_dict[cell].set_vf(v_f)
    #       graph_dict[cell].set_k_cr(k_cr)
#       TTS = hihgway. run_ctm
#       results[v_c] = TTS
#   get maximum from results to find best VSL speed 
#   return or print best speed, TTS and improvement
#
# DEF increase_lanaes(Highway, list_cells, increasement = ): (-> just simple increase lambda, but inplement optimising)
#   results = {}
#   TTS = highway.run_ctm
#   results[v_c] = TTS
#   for cell in list_cells:
#       graph_dict[cell].set_lambda(graph_dict[cell].get_lambda + increasement)
#   TTS = highwat.run_ctm
#   results[v_c] = TTS
#   return or print improvent 