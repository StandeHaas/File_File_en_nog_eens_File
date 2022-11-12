import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math

class Highway: 
    def __init__(self, delta_t, directed = False): 
        self.directed = directed
        self.delta_t = delta_t
        self.dict = {}

    def add_cell(self, cell):  
        self.dict[cell.value] = cell 
    
    def add_link(self, from_cell, to_cell, weight=0): 
        self.dict[from_cell.value].add_link(to_cell.value, weight)
        if self.directed == False:
            self.dict[to_cell.value].add_link(from_cell.value, weight)
    
    def run_ctm(self, start, end):
        timesteps = int(86400 / self.delta_t)
        start /= self.delta_t
        end /= self.delta_t
        adjust_data(self)
        TTS = 0 
        VSL_check = 0
        VSL_check_2 = 0
        results = {}
        results_v = {}
        n_tot = 0
        for cell in self.dict: 
            for _link in self.dict[cell].links:
                        if _link > cell:
                            link = _link  
            if self.dict[link].r == True:
                self.dict[link].set_input_ratio_onramp(input_ratio_onramp(self, self.dict[link], self.dict[cell]))
        for t in range(timesteps):
            if t >= start and t <= end:
                lst_results = {}
                lst_results_v = {}
                lst_cell_2 = []
                for cell in self.dict:
                    lst_links = []
                    r_in = 0 
                    _r_in = 0
                    cell_2 = 0
                    y_out_all = 0
                    y_out = 0 
                    y_2_out = 0
                    n_1_out = 0
                    n_2_out = 0
                    s = 0
                    s_2 = 0
                    r_in = 0
                    if self.dict[cell].VSL == True:
                        if t > self.dict[cell].VSL_start/self.delta_t and VSL_check == 0:
                            VSL(highway, self.dict[cell].list_cells, self.dict[cell].v_c, self.dict[cell].v_c_max, self.dict[cell].alpha, self.dict[cell].A, self.dict[cell].E)
                            VSL_check = 1
                        if t > self.dict[cell].VSL_end/self.delta_t and VSL_check == 1:
                            for cell in self.dict[cell].list_cells:
                                self.dict[cell].set_K_cr(self.dict[cell].lst_K_cr[self.dict[cell].index - 1])
                                self.dict[cell].set_v_f(self.dict[cell].lst_v_f[self.dict[cell].index - 1])
                                self.dict[cell].set_a(10)
                            VSL_check = 2
                        if t > self.dict[cell].VSL_start_2/self.delta_t and VSL_check_2 == 0:
                            VSL(highway, self.dict[cell].list_cells, self.dict[cell].v_c, self.dict[cell].v_c_max, self.dict[cell].alpha, self.dict[cell].A, self.dict[cell].E)
                            VSL_check_2 = 1
                        if t > self.dict[cell].VSL_end_2/self.delta_t and VSL_check_2 == 1:
                            for cell in self.dict[cell].list_cells:
                                self.dict[cell].set_K_cr(self.dict[cell].lst_K_cr[self.dict[cell].index - 1])
                                self.dict[cell].set_v_f(self.dict[cell].lst_v_f[self.dict[cell].index - 1])
                                self.dict[cell].set_a(10)
                            VSL_check_2 = 2
                    for link in self.dict[cell].links:
                        if link > cell:
                            lst_links.append(link)
                    if cell in lst_cell_2:
                        pass
                    elif self.dict[cell].E_cell == True:
                        pass
                    elif len(lst_links) > 0:
                        if self.dict[lst_links[0]].E_cell == True:
                            y_out = self.dict[cell].n * (self.delta_t / 3600 * self.dict[cell].get_v() / self.dict[cell].delta_l)
                            self.dict[cell].set_output(y_out, s = 0)
                            lst_results[cell] = self.dict[cell].n
                            lst_results_v[cell] = self.dict[cell].get_v()
                        else:
                            if self.dict[cell].B_cell == True:
                                n_1_out = self.dict[cell].get_q(t) * self.dict[cell].lanes
                                Q_N_tot = []
                                for link in lst_links:
                                    Q_out = self.dict[link].Q * self.dict[link].lanes * (1 / 3600 * self.delta_t)
                                    N_out = self.dict[link].w / self.dict[link].v_f * (self.dict[link].N - self.dict[link].n)
                                    Q_N_tot.append(min(Q_out, N_out))
                                y_out = min(n_1_out, sum(Q_N_tot))
                                n_tot += y_out
                                
                                if len(lst_links) == 2:
                                    if y_out == n_1_out:
                                        output_ratio_highway = output_ratio(self, lst_links, t)
                                        link_1_out = n_1_out * output_ratio_highway
                                        link_2_out = n_1_out * (1 - output_ratio_highway)
                                        if link_1_out > Q_N_tot[0]:
                                            link_2_out += link_1_out - Q_N_tot[0]
                                            link_1_out = Q_N_tot[0]
                                        elif link_2_out > Q_N_tot[1]:
                                            link_1_out += link_2_out - Q_N_tot[1]
                                            link_2_out = Q_N_tot[1]
                                    else:
                                        link_1_out = Q_N_tot[0]
                                        link_2_out = Q_N_tot[1]
                                if len(lst_links) == 1:
                                    self.dict[lst_links[0]].set_input(y_out, y_2_out=0, r_in=0)
                                else: 
                                    self.dict[lst_links[0]].set_input(link_1_out, y_2_out=0, r_in=0)
                                    self.dict[lst_links[1]].set_input(link_2_out, y_2_out=0, r_in=0)
                                lst_results[cell] = self.dict[cell].n
                                lst_results_v[cell] = self.dict[cell].get_v()
                            else: 
                                n_1_out = self.dict[cell].n * (self.delta_t / 3600 * self.dict[cell].get_v() / self.dict[cell].delta_l)
                                n_2_out = 0
                                Q_N_tot = []
                                for _cell_2 in self.dict[lst_links[0]].links:
                                    if _cell_2 < lst_links[0] and _cell_2 != cell:
                                        cell_2 = _cell_2
                                        lst_cell_2.append(cell_2)
                                        n_2_out = self.dict[cell_2].n * (self.delta_t / 3600 * self.dict[cell_2].get_v() / self.dict[cell_2].delta_l)
                                        
                                TTS += self.dict[cell].n
                                if cell_2 != 0:
                                    TTS += self.dict[cell_2].n
                                
                                if self.dict[lst_links[0]].ramp == True:
                                    _r_in = self.dict[lst_links[0]].get_r_value(t)
                                    input_ratio_for_onramp = self.dict[lst_links[0]].input_ratio_onramp
                                else:
                                    _r_in = 0 
                                
                                n_out = n_1_out + n_2_out + _r_in
                                for link in lst_links:
                                    Q_out = self.dict[link].Q * self.dict[link].lanes * (1 / 3600 * self.delta_t)
                                    N_out = self.dict[link].w / self.dict[link].v_f * (self.dict[link].N - self.dict[link].n)
                                    Q_N_tot.append(min(Q_out, N_out))
                                y_out_all = min(n_out, sum(Q_N_tot))
                                n_tot += y_out
                                if len(lst_links) == 2:
                                    if y_out_all == n_out:
                                        output_ratio_highway = output_ratio(self, lst_links,t)
                                        link_1_out = n_1_out * output_ratio_highway
                                        link_2_out = n_1_out * (1 - output_ratio_highway)
                                        if link_1_out > Q_N_tot[0]:
                                            link_2_out += link_1_out - Q_N_tot[0]
                                            link_1_out = Q_N_tot[0]
                                        elif link_2_out > Q_N_tot[1]:
                                            link_1_out += link_2_out - Q_N_tot[1]
                                            link_2_out = Q_N_tot[1]
                                    else:
                                        link_1_out = Q_N_tot[0]
                                        link_2_out = Q_N_tot[1]

                                if cell_2 != 0: 
                                    if self.dict[cell].RM == True and t > self.dict[cell].RM_start / self.delta_t and t < self.dict[cell].RM_end / self.delta_t:
                                        y_2_out = min(n_2_out, sum(Q_N_tot))
                                        y_out =  max(0, self.dict[lst_links[0]].r + self.dict[cell].K_r*(self.dict[lst_links[0]].K_cr * self.dict[lst_links[0]].delta_l * self.dict[lst_links[0]].lanes - self.dict[lst_links[0]].n))
                                        self.dict[lst_links[0]].set_r(y_out)
                                        y_out = min(self.dict[cell].n, y_out)
                                    elif self.dict[cell_2].RM == True and t > self.dict[cell_2].RM_start / self.delta_t and t < self.dict[cell_2].RM_end / self.delta_t:  
                                        y_out = min(n_out, sum(Q_N_tot)) 
                                        y_2_out =  max(0, self.dict[lst_links[0]].r + self.dict[cell_2].K_r*(self.dict[lst_links[0]].K_cr * self.dict[lst_links[0]].delta_l * self.dict[lst_links[0]].lanes - self.dict[lst_links[0]].n))
                                        self.dict[lst_links[0]].set_r(y_2_out)
                                        y_2_out = min(self.dict[cell_2].n, y_2_out)
                                    else:
                                        if y_out_all != n_out: 
                                            input_ratio = get_input_ratio(self, cell, cell_2)
                                            y_out = y_out_all * input_ratio
                                            y_2_out = y_out_all * (1 - input_ratio)
                                        else:
                                            y_out = n_1_out
                                            y_2_out = n_2_out
                                        if y_out > n_1_out:
                                            y_2_out += y_out - n_1_out
                                            y_out = n_1_out
                                        if y_2_out > n_2_out:
                                            y_out += y_2_out - n_2_out
                                            y_2_out = n_2_out        
                                else:
                                    y_out = y_out_all
                                    y_2_out = 0
                                
                                if _r_in != 0:
                                    if self.dict[lst_links[0]].RM == True and t > self.dict[lst_links[0]].RM_start / self.delta_t and t < self.dict[lst_links[0]].RM_end / self.delta_t:
                                        y_out = min(n_out, sum(Q_N_tot)) 
                                        r_in = max(0, self.dict[lst_links[0]].r + self.dict[lst_links[0]].K_r*(self.dict[lst_links[0]].K_cr * self.dict[lst_links[0]].delta_l * self.dict[lst_links[0]].lanes - self.dict[lst_links[0]].n))
                                        self.dict[lst_links[0]].set_r(r_in)
                                        if r_in < _r_in: 
                                            self.dict[lst_links[0]].set_input_r(_r_in - r_in, t)
                                        r_in = min(r_in, _r_in)
                                    else:
                                        if y_out_all != n_out:
                                            r_jam = _r_in - y_out_all * (1 - input_ratio_for_onramp)
                                            self.dict[lst_links[0]].set_input_r(r_jam, t)
                                            r_in = y_out_all * (1- input_ratio_for_onramp)
                                            y_out = y_out_all * input_ratio_for_onramp
                                        else: 
                                            r_in = _r_in
                                        if y_out > n_1_out:
                                            r_in += y_out - n_1_out
                                            y_out = n_1_out
                                        if r_in > _r_in:
                                            y_out += r_in - _r_in
                                            r_in = _r_in

                                if self.dict[cell].s == True:
                                    if y_out == n_out: 
                                        s = y_out * self.dict[cell].get_beta(t) 
                                        y_out *= (1 - self.dict[cell].get_beta(t))
                                    else:
                                        s = y_out * self.dict[cell].get_beta(t) 
                                        if s + y_out > n_out:
                                            ratio = n_out / (s + y_out)
                                            s *= ratio
                                            y_out *= ratio         
                                else:
                                    s = 0 
                                if cell_2 != 0:
                                    if self.dict[cell_2].s == True:
                                        if y_2_out == n_2_out:
                                            s_2 = y_out * self.dict[cell_2].get_beta(t) 
                                            y_2_out *= (1 - self.dict[cell_2].get_beta(t))
                                        else:
                                            s_2 = y_2_out * self.dict[cell_2].get_beta(t) 
                                            if s_2 + y_2_out > n_2_out:
                                                ratio = n_2_out / (s_2 + y_2_out)
                                                s_2 *= ratio
                                                y_2_out *= ratio   
                                else:
                                    s_2 = 0 
                                self.dict[cell].set_output(y_out, s)
                                if cell_2 != 0:
                                    self.dict[cell_2].set_output(y_2_out, s_2)
                                if len(lst_links) == 1:
                                    self.dict[lst_links[0]].set_input(y_out, y_2_out, r_in)
                                    self.dict[lst_links[0]].set_q(y_out + y_2_out + r_in)
                                else:
                                    self.dict[lst_links[0]].set_input(link_1_out, y_2_out, r_in)
                                    self.dict[lst_links[0]].set_q(link_1_out + y_2_out + r_in)
                                    self.dict[lst_links[1]].set_input(link_2_out, y_2_out, r_in)
                                    self.dict[lst_links[1]].set_q(link_2_out + y_2_out + r_in)
                                lst_results[cell] = self.dict[cell].n
                                lst_results_v[cell] = self.dict[cell].get_v()
                                if cell_2 != 0:
                                    lst_results[cell_2] = self.dict[cell_2].n
                                    lst_results_v[cell_2] = self.dict[cell_2].get_v()
                    results[t] = lst_results 
                    results_v[t] = lst_results_v        
        return TTS * self.delta_t, results, n_tot, results_v
    
class Cell: 
    def __init__(self, 
               value, 
               index, 
               lst_delta_l,
               q_data,
               lst_Q, 
               lst_v_f,
               lst_K_cr, 
               lst_K_j,
               lst_lambda, 
               ramp, 
               r_index, 
               s, 
               s_index, 
               B_cell, 
               E_cell, 
               RM, 
               K_r,
               VSL,
               n = 0, 
               a = 10,
               RM_start = 0,
               RM_end = 86400,
               VSL_start = 0,
               VSL_end = 86400, 
               VSL_start_2 = 86400,
               VSL_end_2 = 86400,
               list_cells = 0, 
               v_c = 0, 
               v_c_max = 0, 
               alpha = 0, 
               A = 0, 
               E = 0):
        self.index = index
        self.links = {}
        self.value = value
        self.delta_l = lst_delta_l[index - 1]
        self.q = 0 
        self.lst_q = q_data[index]
        self.Q = lst_Q[index - 1]
        self.v_f = lst_v_f[index - 1]
        self.lst_v_f = lst_v_f
        self.K_cr = lst_K_cr[index -1]
        self.lst_K_cr = lst_K_cr
        self.K_j = lst_K_j[index - 1]
        self.lanes = int(lst_lambda[index -1])
        self.n = n
        self.ramp = ramp
        if ramp == True:
            self.lst_r = q_data[r_index] + [0,0,0,0]
            self.input_ratio_onramp = 0
        self.s = s
        if s == True:
            self.lst_s = q_data[s_index]
            self.lst_beta = split_ratio(self)
        self.B_cell = B_cell
        self.E_cell = E_cell
        self.RM = RM
        self.RM_start = RM_start
        self.RM_end = RM_end
        self.K_r = K_r
        self.r = 0
        self.VSL = VSL
        self.VSL_start = VSL_start
        self.VSL_end = VSL_end
        self.VSL_start_2 = VSL_start_2
        self.VSL_end_2 = VSL_end_2
        self.list_cells = list_cells
        self.v_c = v_c
        self.v_c_max = v_c_max
        self.alpha = alpha
        self.A = A
        self.E = E
        self.a = a
        self.N = self.K_j * self.delta_l * self.lanes 
        self.w = -(self.v_f * self.K_cr / (self.K_cr - self.K_j))
    
    def add_link(self, cell, weight=0):
        self.links[cell] = weight
    

    def get_q(self, t):
        return self.lst_q[t]
    def get_v(self):
        return self.v_f * math.exp(-(1/self.a)*(((self.n / (self.lanes * self.delta_l) / self.K_cr) ** self.a)))
    def get_r_value(self, t):
        return self.lst_r[t]
    def get_beta(self, t):
        return self.lst_beta[t]

    def set_lst_q(self, lst_q):
        self.lst_q = lst_q
    def set_lst_r(self, lst_r):
        self.lst_r = lst_r
    def set_lst_s(self, lst_s):
        self.lst_s = lst_s
    def set_lst_beta(self, lst_beta):
        self.lst_beta = lst_beta
    def set_input_ratio_onramp(self, input_ratio_onramp):
        self.input_ratio_onramp = input_ratio_onramp
    def set_lanes(self, lanes):
        self.lanes = lanes
    def set_v_f(self, v_f):
        self.v_f = v_f
    def set_K_cr(self, K_cr):
        self.K_cr = K_cr
    def set_q(self, q):
        self.q = q
    def set_a(self, a):
        self.a = a
    def set_input(self, y_out, y_2_out, r_in):
        self.n += y_out + y_2_out + r_in
    def set_output(self, y_out, s):
        self.n -= y_out + s
    def set_input_r(self, r_extra, t):
        self.lst_r[t + 1] += r_extra
    def set_r(self, r):
        self.r = r 

def get_input_ratio(self, cell_1, cell_2): 
    input_1 = self.dict[cell_1].lanes * self.dict[cell_1].Q
    input_2 = self.dict[cell_2].lanes * self.dict[cell_2].Q
    return input_1 / (input_1 + input_2)

def split_ratio(self):
    beta_lst = []
    for t in range(len(self.lst_q)):
        beta = self.lst_s[t] / (self.lst_s[t] + self.lst_q[t])
        beta_lst.append(beta)
    return beta_lst 

def input_ratio_onramp(self, link, cell):
    input_cell = cell.lanes * cell.Q
    input_r = max(link.lst_r) * 3600 / self.delta_t
    return input_cell / (input_r + input_cell)

def output_ratio(self, lst_links, t):
    return self.dict[lst_links[0]].get_q(t) / (self.dict[lst_links[0]].get_q(t)  + self.dict[lst_links[1]].get_q(t))

def adjust_data(self):
    timesteps_per_hour =  int(3600 / self.delta_t)
    for cell in self.dict:
        lst_q = []
        for q in self.dict[cell].lst_q:
            for _ in range(timesteps_per_hour):
                lst_q.append(q/timesteps_per_hour)
        self.dict[cell].set_lst_q(lst_q)
        if self.dict[cell].ramp == True:
            lst_r = []
            for q in self.dict[cell].lst_r:
                for _ in range(timesteps_per_hour):
                    lst_r.append(q/timesteps_per_hour)
            self.dict[cell].set_lst_r(lst_r)
        if self.dict[cell].s == True:
            lst_s = []
            lst_beta = []
            for q in self.dict[cell].lst_s:
                for _ in range(timesteps_per_hour):
                    lst_s.append(q/timesteps_per_hour)
            self.dict[cell].set_lst_s(lst_s)
            for beta in self.dict[cell].lst_beta: 
                for _ in range(timesteps_per_hour):
                    lst_beta.append(beta)
            self.dict[cell].set_lst_beta(lst_beta)

def visualiser(highway, results, list_lanes, start, end, number_ts):
    fig, ax = plt.subplots(nrows=number_ts, ncols=1)
    start /= highway.delta_t
    end /= highway.delta_t
    delta_t = (end - start) / number_ts
    plt_results = {}
    for number_t in range(number_ts):
        lst = [0 for _ in range(len(list_lanes))]
        for t in results:
            if t > start + number_t*delta_t and t < start + (number_t + 1)*delta_t:
                index = 0
                for value in list_lanes:
                    lst[index] += results[t][value]
                    index += 1
                break

        plt_results[number_t] = lst
    t =  0
    for row in ax:
        row.plot(plt_results[t])
        t += 1
    fig.canvas.set_window_title('Aantal voertuigen in cel van {}h tot {}h met tijdstap {}h.'.format(round(start*highway.delta_t/3600 , 2),round(end*highway.delta_t/3600 , 2), round(delta_t*highway.delta_t/3600 , 2)))
    fig.suptitle('Aantal voertuigen in cel van {}h tot {}h met tijdstap {}h.'.format(round(start*highway.delta_t/3600 , 2), round(end*highway.delta_t/3600 , 2), round(delta_t*highway.delta_t/3600 , 2)))
    fig.supxlabel('Cellen')
    fig.supylabel('Aantal voertuigen per cel')
    plt.xticks(range(len(list_lanes)), list_lanes)
    plt.show()

def visualiser_v(highway, results, list_lanes, start, end, number_ts):
    fig, ax = plt.subplots(nrows=number_ts, ncols=1)
    start /= highway.delta_t
    end /= highway.delta_t
    delta_t = (end - start) / number_ts
    plt_results = {}
    for number_t in range(number_ts):
        lst = [0 for _ in range(len(list_lanes))]
        for t in results:
            if t > start + number_t*delta_t and t < start + (number_t + 1)*delta_t:
                index = 0
                for value in list_lanes:
                    lst[index] += results[t][value]
                    index += 1
                break

        plt_results[number_t] = lst
    t =  0
    for row in ax:
        row.plot(plt_results[t])
        t += 1
    fig.canvas.set_window_title('Snelheid in cel van {}h tot {}h met tijdstap {}h.'.format(round(start*highway.delta_t/3600 , 2),round(end*highway.delta_t/3600 , 2), round(delta_t*highway.delta_t/3600 , 2)))
    fig.suptitle('Snelheid in cel van {}h tot {}h met tijdstap {}h.'.format(round(start*highway.delta_t/3600 , 2), round(end*highway.delta_t/3600 , 2), round(delta_t*highway.delta_t/3600 , 2)))
    fig.supxlabel('Cellen')
    fig.supylabel('Snelheid per cel')
    plt.xticks(range(len(list_lanes)), list_lanes)
    plt.show()

    return plt_results

def visualiser_v_data(highway, results, list_lanes, number_ts=24):
    fig, ax = plt.subplots(nrows=number_ts, ncols=1)
    plt_results = {}
    for t in range(24):
        lst = [0 for _ in range(len(list_lanes))]
        i = 0
        for cell in list_lanes:
            lst[i] += v_data[highway.dict[cell].index][t]
            i += 1
        plt_results[t] = lst
    t =  0
    for row in ax:
        row.plot(plt_results[t])
        t += 1
    fig.canvas.set_window_title('Snelheid afkomstig uit emperische data van 0h tot 24h met tijdstappen van 1h')
    fig.suptitle('Snelheid afkomstig uit emperische data van 0h tot 24h met tijdstappen van 1h')
    fig.supxlabel('Cellen')
    fig.supylabel('Snelheid per cel')
    plt.xticks(range(len(list_lanes)), list_lanes)
    plt.show()
    
    return plt_results

def run(self, start=0, end=86400):
    TTS, results,n_tot,results_v = self.run_ctm(start, end)
    return TTS, results, n_tot, results_v

def VSL(self, list_cells, v_c, v_c_max, alpha, A, E):
    for cell in range(len(list_cells)):
        b = min(v_c[cell] / v_c_max[cell] * (1 + alpha[cell]), 1)
        self.dict[list_cells[cell]].set_v_f(min(v_c_max[cell] * b, self.dict[list_cells[cell]].v_f))
        self.dict[list_cells[cell]].set_K_cr(self.dict[list_cells[cell]].K_cr * (1 + A[cell]*(1 - b)))   
        self.dict[list_cells[cell]].set_a(self.dict[list_cells[cell]].a*(E[cell] - (E[cell] - 1)* b))

def increase_lanes(self, list_cells, increasement = 1, start=0, end=86400):
    for cell in list_cells:
        self.dict[cell].set_lanes(self.dict[cell].lanes + increasement)
    TTS, results, n_tot, results_v = self.run_ctm(start, end)
    return TTS, results, n_tot, results_v

def average_difference(results_1, results_2):
    z = 0 
    for t in range(24):
        for i in range(len(results_1[1])):
            z += abs(results_1[t][i] - results_2[t][i])
    z /= 24 * len(results_1[1])
    print(z)

df = pd.read_csv() #file
q_data = {} # v/h
lst_Q = [] # v/hr_index
for i in range(1, 12):
    q_data[i] = [float(df.iloc[j][i]) for j in range(0,24)]
lst_lambda = [df.iloc[27][i] for i in range(1,12)] # number of lanes
lst_delta_l = [int(df.iloc[55][i])/1000 for i in range(1,12)] # km 
for i in range(1,12):
    q_data[i] = [float(q_data[i][j]) / int(lst_lambda[i - 1]) for j in range(0,24)]
    lst_Q.append(max(q_data[i]) * 1.2) 
v_data = {} # km/h
lst_v_f = []
for i in range(1, 12):
    v_data[i] = [int(df.iloc[j][i]) for j in range(30,54)]
    lst_v_f.append(max(v_data[i]))

K_data = {} # v/km
lst_K_cr = [] # v/km
lst_K_j = [] # v/km
for i in range(len(q_data)):
    i += 1
    K_data[i] = [q_data[i][j] / v_data[i][j] for j in range(0,24)]
for i in range(len(lst_Q)):
    j = q_data[i + 1].index(lst_Q[i] / 1.2)
    lst_K_cr.append(K_data[i + 1][j])

for i in range(len(lst_K_cr)):
    lst_K_j.append(lst_K_cr[i] * 5) 

highway = Highway(2.5)

# input of highway system

TTS, results, n_tot, results_v = run(highway, 0*3600, 24*3600)
print('V_f:       ',lst_v_f)
print('K_cr:      ',lst_K_cr)
print('K_j:       ',lst_K_j)
print('Q:         ',lst_Q)
print('TTS:       ',TTS)
print('N_tot:     ',n_tot)
print('TTS/N_tot: ',TTS / n_tot)
visualiser(highway, results, [], 0, 86400, 24) # requires list of cells to display
