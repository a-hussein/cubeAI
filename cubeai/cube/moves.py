from typing import Dict, List
from itertools import product
import random


class Cube:
    def __init__(self, cube_state: Dict[str, List[str]]):
        self.cube_state = cube_state
        self.moves = 0
    
    def rotation(self, arr: List[str]):
        r"""
        Perform single rotation on one face of the cube.
        
        Args:
        -----
            arr (List[str]): a 2-dimensional representation of any face of the cube. 
            Example:[0,1,2]
                    [7,8,3]
                    [6,5,4]   -->  [0,1,2,3,4,5,6,7,8]
        """
        arr[2],arr[3],arr[4],arr[5],arr[6],arr[7],arr[0],arr[1] = arr[0],arr[1],arr[2],arr[3],arr[4],arr[5],arr[6],arr[7]
        return arr      
 
    def I(self):
        pass

    def R(self):
        self.cube_state['yellow'][2], self.cube_state['yellow'][3], self.cube_state['yellow'][4], \
        self.cube_state['blue'][6], self.cube_state['blue'][7], self.cube_state['blue'][0], \
        self.cube_state['white'][2], self.cube_state['white'][3], self.cube_state['white'][4], \
        self.cube_state['green'][2], self.cube_state['green'][3], self.cube_state['green'][4] = self.cube_state['green'][2], self.cube_state['green'][3], self.cube_state['green'][4], self.cube_state['yellow'][2], self.cube_state['yellow'][3], self.cube_state['yellow'][4], self.cube_state['blue'][6], self.cube_state['blue'][7], self.cube_state['blue'][0], self.cube_state['white'][2], self.cube_state['white'][3], self.cube_state['white'][4]
        
        self.cube_state['orange'] = self.rotation(self.cube_state['orange'])
        self.moves += 1

    def U(self):
        self.cube_state['blue'][0], self.cube_state['blue'][1], self.cube_state['blue'][2], \
        self.cube_state['orange'][0], self.cube_state['orange'][1], self.cube_state['orange'][2], \
        self.cube_state['green'][0], self.cube_state['green'][1], self.cube_state['green'][2], \
        self.cube_state['red'][0], self.cube_state['red'][1], self.cube_state['red'][2] = self.cube_state['red'][0], self.cube_state['red'][1], self.cube_state['red'][2], self.cube_state['blue'][0], self.cube_state['blue'][1], self.cube_state['blue'][2], self.cube_state['orange'][0], self.cube_state['orange'][1], self.cube_state['orange'][2], self.cube_state['green'][0], self.cube_state['green'][1], self.cube_state['green'][2]

        self.cube_state['yellow'] = self.rotation(self.cube_state['yellow'])
        self.moves += 1


    def L(self):
        self.cube_state['yellow'][6], self.cube_state['yellow'][7], self.cube_state['yellow'][0], \
        self.cube_state['green'][6], self.cube_state['green'][7], self.cube_state['green'][0], \
        self.cube_state['white'][6], self.cube_state['white'][7], self.cube_state['white'][0], \
        self.cube_state['blue'][2], self.cube_state['blue'][3], self.cube_state['blue'][4] = self.cube_state['blue'][2], self.cube_state['blue'][3], self.cube_state['blue'][4], self.cube_state['yellow'][6], self.cube_state['yellow'][7], self.cube_state['yellow'][0], self.cube_state['green'][6], self.cube_state['green'][7], self.cube_state['green'][0], self.cube_state['white'][6], self.cube_state['white'][7], self.cube_state['white'][0]

        self.cube_state['red'] = self.rotation(self.cube_state['red'])
        self.moves += 1
  
    def D(self):
        self.cube_state['green'][4], self.cube_state['green'][5], self.cube_state['green'][6], \
        self.cube_state['orange'][4], self.cube_state['orange'][5], self.cube_state['orange'][6], \
        self.cube_state['blue'][4], self.cube_state['blue'][5], self.cube_state['blue'][6], \
        self.cube_state['red'][4], self.cube_state['red'][5], self.cube_state['red'][6] = self.cube_state['red'][4], self.cube_state['red'][5], self.cube_state['red'][6], self.cube_state['green'][4], self.cube_state['green'][5], self.cube_state['green'][6], self.cube_state['orange'][4], self.cube_state['orange'][5], self.cube_state['orange'][6], self.cube_state['blue'][4], self.cube_state['blue'][5], self.cube_state['blue'][6]

        self.cube_state['white'] = self.rotation(self.cube_state['white'])
        self.moves += 1

        
    def F(self):
        self.cube_state['yellow'][4], self.cube_state['yellow'][5], self.cube_state['yellow'][6], \
        self.cube_state['orange'][6], self.cube_state['orange'][7], self.cube_state['orange'][0], \
        self.cube_state['white'][0], self.cube_state['white'][1], self.cube_state['white'][2], \
        self.cube_state['red'][2], self.cube_state['red'][3], self.cube_state['red'][4] = self.cube_state['red'][2], self.cube_state['red'][3], self.cube_state['red'][4], self.cube_state['yellow'][4], self.cube_state['yellow'][5], self.cube_state['yellow'][6], self.cube_state['orange'][6], self.cube_state['orange'][7], self.cube_state['orange'][0], self.cube_state['white'][0], self.cube_state['white'][1], self.cube_state['white'][2]

        self.cube_state['green'] = self.rotation(self.cube_state['green'])
        self.moves += 1

    def B(self):
        self.cube_state['yellow'][0], self.cube_state['yellow'][1], self.cube_state['yellow'][2], \
        self.cube_state['red'][6], self.cube_state['red'][7], self.cube_state['red'][0], \
        self.cube_state['white'][4], self.cube_state['white'][5], self.cube_state['white'][6], \
        self.cube_state['orange'][2], self.cube_state['orange'][3], self.cube_state['orange'][4] = self.cube_state['orange'][2], self.cube_state['orange'][3], self.cube_state['orange'][4], self.cube_state['yellow'][0], self.cube_state['yellow'][1], self.cube_state['yellow'][2], self.cube_state['red'][6], self.cube_state['red'][7], self.cube_state['red'][0], self.cube_state['white'][4], self.cube_state['white'][5], self.cube_state['white'][6]
    
        self.cube_state['blue'] = self.rotation(self.cube_state['blue'])
        self.moves += 1

    def Rp(self):
        for _ in range(3):
            self.R()
            self.moves -= 1
        self.moves += 1

    def Up(self):
        for _ in range(3):
            self.U()
            self.moves -= 1
        self.moves += 1
 
    def Lp(self):
        for _ in range(3):
            self.L()
            self.moves -= 1
        self.moves += 1
        
    def Dp(self):
        for _ in range(3):
            self.D()
            self.moves -= 1
        self.moves += 1
        
    def Fp(self):
        for _ in range(3):
            self.F()
            self.moves -= 1
        self.moves += 1
        
    def Bp(self):
        for _ in range(3):
            self.B()
            self.moves -= 1
        self.moves += 1

    def R2(self):
        for _ in range(2):
            self.R()
            self.moves -= 1
        self.moves += 2

    def U2(self):
        for _ in range(2):
            self.U()
            self.moves -= 1
        self.moves += 2

    def L2(self):
        for _ in range(2):
            self.L()
            self.moves -= 1
        self.moves += 2

    def D2(self):
        for _ in range(2):
            self.D()
            self.moves -= 1
        self.moves += 2

    def F2(self):
        for _ in range(2):
            self.F()
            self.moves -= 1
        self.moves += 2

    def B2(self):
        for _ in range(2):
            self.B()
            self.moves -= 1
        self.moves += 2
       
    def get_state(self):
        return self.cube_state
    
    def get_moves(self):
        return self.moves

    def get_edge_count(self) -> Dict[str, int]:
        edge_counts = {}
        edge_values = {1,3,5,7}
        
        for face in self.cube_state:
            edge_counts[face] = 0
            for i, sticker in enumerate(self.cube_state[face]):
                if sticker == face[0] and i in edge_values:
                    edge_counts[face] +=1
        return edge_counts

    def cross_oriented(self, face='white'):
        r"""
        insert
        """

        orientation = ['green', 'red', 'blue', 'orange']
        
        oriented = [
            ['g', 'r', 'b', 'o'], 
            ['r', 'b', 'o', 'g'],
            ['b', 'o', 'g', 'r'],
            ['o','g', 'r', 'b']
        ]
        
        _oriented = []
                
        if self.get_edge_count()[face] != 4:
            return False
        else:
            for i in range(len(oriented[0])):
                _oriented.append(self.cube_state[orientation[i]][5])
        if _oriented in oriented:
            return True
        return False
    
    # making a function to identify what type of white cross edge (in this case, white) do i have
    def identify_cross_edge_type(self, face='white'):    
        _edge_count = 0
        orientation = ['green', 'red', 'blue', 'orange', 'green'] # including green second time so that list not out of index
        orientation_adjust = ['green', 'red', 'blue', 'orange'] # including green above was a dangerous way to handle this...smh, coming back months later to find out why some three_type combo cases yielding "y".. and this is was the reason why. adding this "adjust" variable for now, but this needs to be fixed. includeing an update unit test asap to include three type for orange layer

        _seven_type, _three_type, _one_type, _top_type, _five_type, _bottum_type = {}, {}, {}, {}, {}, {}

        _edges = {1,3,5,7}

        # easy type, ie in the 7 slot of non-yelloow face
        if self.get_edge_count()[face] < 4:
            for i in range(4):
                if self.cube_state[orientation[i]][7] == 'w':
                    _seven_type[orientation[i]] = [self.cube_state[orientation[i+1]][8], self.cube_state[orientation[i+1]][3]]
        
        # easy type, ie in the 7 slot of non-yelloow face
        if self.get_edge_count()[face] < 4:
            for i in range(4):
                if self.cube_state[orientation_adjust[i]][3] == 'w':
                    _three_type[orientation_adjust[i]] = [self.cube_state[orientation_adjust[i-1]][8], self.cube_state[orientation_adjust[i-1]][7]]
        
        # one move away from easy type, ie in the one/five slot of non-yellow face
        if self.get_edge_count()[face] < 4:
            if self.cube_state['green'][1] == 'w':
                _one_type['green'] = [self.cube_state['yellow'][8], self.cube_state['yellow'][5]]
            if self.cube_state['red'][1] == 'w':
                _one_type['red'] = [self.cube_state['yellow'][8], self.cube_state['yellow'][7]]
            if self.cube_state['blue'][1] == 'w':
                _one_type['blue'] = [self.cube_state['yellow'][8], self.cube_state['yellow'][1]]
            if self.cube_state['orange'][1] == 'w':
                _one_type['orange'] = [self.cube_state['yellow'][8], self.cube_state['yellow'][3]]
        
        # one move away from easy type, ie in the one/five slot of non-yellow face
        if self.get_edge_count()[face] < 4:
            if self.cube_state['green'][5] == 'w':
                _five_type['green'] = [self.cube_state['white'][8], self.cube_state['white'][1]]
            if self.cube_state['red'][5] == 'w':
                _five_type['red'] = [self.cube_state['white'][8], self.cube_state['white'][7]]
            if self.cube_state['blue'][5] == 'w':
                _five_type['blue'] = [self.cube_state['white'][8], self.cube_state['white'][5]]
            if self.cube_state['orange'][5] == 'w':
                _five_type['orange'] = [self.cube_state['white'][8], self.cube_state['white'][3]]
        
        # top faced white edges - notice that this returns the face that has the color of the white edge, not the face containing the white edge, which will be yellow in this case
        if self.get_edge_count()[face] < 4:
            for i, color in enumerate(self.cube_state['yellow']):
                if i in _edges and color == 'w':
                    if i == 1:
                        _top_type['yellow_b'] = [self.cube_state['blue'][8], self.cube_state['blue'][1]]
                    if i == 3:
                        _top_type['yellow_o'] = [self.cube_state['orange'][8], self.cube_state['orange'][1]]
                    if i == 5:
                        _top_type['yellow_g'] = [self.cube_state['green'][8], self.cube_state['green'][1]]
                    if i == 7:
                        _top_type['yellow_r'] = [self.cube_state['red'][8], self.cube_state['red'][1]]
                        
        # bottum faced white edges - notice that this returns the face that has the color of the white edge, not the face containing the white edge, which will be white in this case
        # if self.get_edge_count()[face] < 4: # need to check oriented instead
        # if not self.cross_oriented(): # actually, i need combo to show even when oriented, but not permuted
        for i, color in enumerate(self.cube_state['white']):
            if i in _edges and color == 'w':
                if i == 1:
                    _bottum_type['white_g'] = [self.cube_state['green'][8], self.cube_state['green'][5]]
                if i == 3:
                    _bottum_type['white_o'] = [self.cube_state['orange'][8], self.cube_state['orange'][5]]
                if i == 5:
                    _bottum_type['white_b'] = [self.cube_state['blue'][8], self.cube_state['blue'][5]]
                if i == 7:
                    _bottum_type['white_r'] = [self.cube_state['red'][8], self.cube_state['red'][5]]   
    
        cross_edge_types = [
            {'_seven_type': _seven_type}, 
            {'_three_type': _three_type}, 
            {'_one_type': _one_type}, 
            {'_top_type': _top_type},
            {'_five_type': _five_type},
            {'bottum_type': _bottum_type}
        ]
        return cross_edge_types 

    def combo(self):
        cross_dict = self.identify_cross_edge_type()

        _combo = []
        _combos = [[]]*4
        for i, _type in enumerate(cross_dict):
            for face_with_white_edge in list(cross_dict[i][list(cross_dict[i].keys())[0]].keys()):
                _combo.append(list(cross_dict[i].keys())[0])
                _combo.append(face_with_white_edge)
                _combo.append(list(cross_dict[i].values())[0].get(face_with_white_edge)[0])
                _combo.append(list(cross_dict[i].values())[0].get(face_with_white_edge)[1])

        _combos[0] = (_combo[0:4])
        _combos[1] = (_combo[4:8])
        _combos[2] = (_combo[8:12])
        _combos[3] = (_combo[12:16])

        return _combos
        
    def seven_three_orientation_delta(self, i, j):
        g,r,b,o = 0,1,2,3
        color_mapping = {'g': g, 'r': r, 'b': b, 'o':o}

        bottum_mapping = {0: ['I'], 1: ['Dp'], 2: ['D2'], 3:['D']}
        top_mapping = {0: ['I'], 1: ['U'], 2: ['U2'], 3:['Up']}

        _combo = self.combo()
        
        # this is an edge case when we are doing U_delta for one_type/five_type for seven/three
        if _combo[j][2] == 'y' or _combo[j][2] == 'w':
            layer_delta = (color_mapping[_combo[i][2]] - color_mapping[_combo[j][1][0]]) # need face of one_type/five_type
        else:
            layer_delta = (color_mapping[_combo[i][2]] - color_mapping[_combo[j][2]])
            
        sticker_delta = (color_mapping[_combo[i][3]] - color_mapping[_combo[j][3]]) # an edge type for y/w edge case is not needed because sticker will not be yellow or white for this release on sticker_delta
        
        tops = ['_top_type', '_one_type']
        bottums = ['_five_type', 'bottum_type']

        # D delta
        if _combo[j][0] in bottums:
            new_delta=0
            # for seven/three to bottum
            if _combo[j][0] == 'bottum_type':
                if layer_delta != sticker_delta:
                    new_delta = (layer_delta - sticker_delta)%4
                    return bottum_mapping[new_delta]
                else:
                    return ['I'] # added for case when delta are the same and thus no move needed
            # for seven and three for five
            elif _combo[j][0] == '_five_type':
                new_delta = (layer_delta)%4
                return bottum_mapping[new_delta]
        # U delta
        # for seven/three to top/one
        elif _combo[j][0] in tops:
            new_delta = (layer_delta)%4
            return top_mapping[new_delta]
        
    def combine_seven_three_orientation_delta(self, i, j, k):
        if self.seven_three_orientation_delta(i,j) != None and self.seven_three_orientation_delta(i,k) != None:
            return self.seven_three_orientation_delta(i,j) + self.seven_three_orientation_delta(i,k)
        elif self.seven_three_orientation_delta(i,j) != None:
            return self.seven_three_orientation_delta(i,j)
        elif self.seven_three_orientation_delta(i,k) != None:
            return self.seven_three_orientation_delta(i,k)
        else:
            return ['I']
        # this way we can give one type/top/bottum scenario and return combined top/bottum set up moves

    def seven_type_cross_solver(self):
        _cross_dict = self.identify_cross_edge_type()
        # change number here
        if list(_cross_dict[0]['_seven_type'].keys()) == []: # edge case if no seven types
            return

        _faces = ['green', 'red', 'blue', 'orange']

        _combo = self.combo()

        _move = []
        _orientation_move_D = []
        _orientation_move_U = []

        _combo_plus_move = []

        if self.cross_oriented() == False:
            for i, edge in enumerate(_combo): 
                if edge[0] == '_seven_type':
                    if edge[1] == 'green':
                        _move.append('L')
                    elif edge[1] == 'red':
                        _move.append('B')                    
                    elif edge[1] == 'blue':
                        _move.append('R')    
                    elif edge[1] == 'orange':
                        _move.append('F')  

        ####################################
        tops = ['_top_type', '_one_type']
        bottums = ['_five_type', 'bottum_type']

        # check how many sevens
        sevens_counter = 0
        for types in _combo:
            if types[0] == '_seven_type':
                sevens_counter +=1
                
        threes_counter = 0
        for types in _combo:
            if types[0] == '_three_type':
                threes_counter +=1

        tops_that_seven_will_interact_with_counter = 0
        bottums_that_seven_will_interact_with_counter = 0
        for types in _combo:
            if types[0] in tops:
                tops_that_seven_will_interact_with_counter +=1
            elif types[0] in bottums:
                bottums_that_seven_will_interact_with_counter +=1

        # the amount of moves to do will be sevens and their corresponding valid downstreams
        # nums = max(tops_that_seven_will_interact_with_counter, bottums_that_seven_will_interact_with_counter, 1)
        # number_of_orientation_deltas = sevens_counter*nums

        ####new
        # 2: [0,1]
        # 1: [2]
        # 1: [3]
        x,y,z = [],[],[]
        for i in range(sevens_counter):
            x.append(i)
        for i in range(sevens_counter+threes_counter, sevens_counter+threes_counter+tops_that_seven_will_interact_with_counter):
            y.append(i)
        for i in range(sevens_counter+threes_counter+tops_that_seven_will_interact_with_counter, sevens_counter+threes_counter+tops_that_seven_will_interact_with_counter+bottums_that_seven_will_interact_with_counter):
            z.append(i)
            
        if len(x) == 0:
            x = [0]
        if len(y) == 0:
            y = [0]
        if len(z) == 0:
            z = [0]
        a = [x,y,z]
        b=list(product(*a))
        c=[list(i) for i in b]
        
        result_new = [[] for _ in range(len(c))]
        counter=0
        for (i,j,k) in c:
            result_new[counter].extend(self.combine_seven_three_orientation_delta(i,j,k)) # not needed to add as list since no or_moves
            result_new[counter].append(_move[i])
            counter+=1
        
        
        return result_new

    def three_type_cross_solver(self):
        _cross_dict = self.identify_cross_edge_type()
        # change number here
        if list(_cross_dict[1]['_three_type'].keys()) == []: # edge case if no three types
            return

        _faces = ['green', 'red', 'blue', 'orange']

        _combo = self.combo()

        _move = []
        _orientation_move_D = []
        _orientation_move_U = []

        _combo_plus_move = []

        if self.cross_oriented() == False:
            for i, edge in enumerate(_combo): 
                if edge[0] == '_three_type':
                    if edge[1] == 'green':
                        _move.append('Rp')
                    elif edge[1] == 'red':
                        _move.append('Fp')                    
                    elif edge[1] == 'blue':
                        _move.append('Lp')    
                    elif edge[1] == 'orange':
                        _move.append('Bp')  

        ####################################
        tops = ['_top_type', '_one_type']
        bottums = ['_five_type', 'bottum_type']

        # check how many sevens
        sevens_counter = 0
        for types in _combo:
            if types[0] == '_seven_type':
                sevens_counter +=1

        threes_counter = 0
        for types in _combo:
            if types[0] == '_three_type':
                threes_counter +=1

        tops_that_three_will_interact_with_counter = 0
        bottums_that_three_will_interact_with_counter = 0
        for types in _combo:
            if types[0] in tops:
                tops_that_three_will_interact_with_counter +=1
            elif types[0] in bottums:
                bottums_that_three_will_interact_with_counter +=1
        ####new
        # 2: [0,1] threes
        # 1: [2] tops
        # 1: [3] bottums
        x,y,z = [],[],[]
        for i in range(threes_counter):
            x.append(i)
        for i in range(sevens_counter+threes_counter, sevens_counter+threes_counter+tops_that_three_will_interact_with_counter):
            y.append(i)
        for i in range(sevens_counter+threes_counter+tops_that_three_will_interact_with_counter, sevens_counter+threes_counter+tops_that_three_will_interact_with_counter+bottums_that_three_will_interact_with_counter):
            z.append(i)

        if len(x) == 0:
            x = [0]
        if len(y) == 0:
            y = [0]
        if len(z) == 0:
            z = [0]
        a = [x,y,z]
        b=list(product(*a))
        c=[list(i) for i in b]

        result_new = [[] for _ in range(len(c))]
        counter=0
        for (i,j,k) in c:
            # include edge case for sevens_counter, since if this is > 1, the counters for _move will work, but not for orietnatoin delta, thus needs to offset by seven_counters amount 
            if sevens_counter == 0:
                result_new[counter].extend(self.combine_seven_three_orientation_delta(i,j,k)) # not needed to add as list since no or_moves...
                result_new[counter].append(_move[i])
                counter+=1
            elif sevens_counter > 0:
                result_new[counter].extend(self.combine_seven_three_orientation_delta(i+sevens_counter,j,k)) # need to offest by sevens due to combo order
                result_new[counter].append(_move[i])
                counter+=1


        return result_new
            
    def one_orientation_delta(self, i, j):
        # anywhere it says "either, not both... it should be in the form of [[alpha], [beta]]... not [alpha, beta]"
        g,r,b,o = 0,1,2,3
        color_mapping = {'g': g, 'r': r, 'b': b, 'o':o}

        bottum_mapping = {0: ['I'], 1: ['Dp'], 2: ['D2'], 3:['D']}

        _combo = self.combo()

        # this is an edge case when we are doing D_delta for five_type for top/one
        if (_combo[i][2] == 'y' or _combo[i][2] == 'w') and (_combo[j][2] == 'y' or _combo[j][2] == 'w'): # one to five case
            layer_delta = (color_mapping[_combo[i][1][0]] - color_mapping[_combo[j][1][0]]) # need face because that will tell me layer of one_type/five_type
        elif _combo[j][2] == 'y' or _combo[j][2] == 'w':
            layer_delta = (color_mapping[_combo[i][2]] - color_mapping[_combo[j][1][0]]) # need face because that will tell me layer of one_type/five_type
        
        elif _combo[i][2] == 'y' or _combo[i][2] == 'w':
            layer_delta = (color_mapping[_combo[i][1][0]] - color_mapping[_combo[j][2]]) # need face because that will tell me layer of one_type/five_type
        else:
            layer_delta = (color_mapping[_combo[i][2]] - color_mapping[_combo[j][2]])

        sticker_delta = (color_mapping[_combo[i][3]] - color_mapping[_combo[j][3]]) # an edge type for y/w edge case is not needed because sticker will not be yellow or white for this release on sticker_delta

        tops = ['_top_type', '_one_type']
        bottums = ['_five_type', 'bottum_type']

        # D delta
        res = ['I']
        if _combo[j][0] in bottums:
            new_delta=0
            # for one to bottum (the logic here will be to clear the bottum (provide both one move away if already there, else do nothing, and then do F or Fp, provide both and let tree decide))
            if _combo[j][0] == 'bottum_type':
                if layer_delta == 0:
    #                 new_delta = (layer_delta - sticker_delta)%4
    #                 return bottum_mapping[new_delta]
                    res = ['D', 'Dp'] # either, not both
                else:
                    res = ['I'] # added for case when delta are the same and thus no move needed; dont need to do anything becuase it will happen in seven/three
            # just bring to right location
            # for top and one to five (bring under when doing F swing)
            elif _combo[j][0] == '_five_type':
                new_delta = (layer_delta)%4
                res = bottum_mapping[new_delta]
            # just bring it under it, the solver will do both moves aand add to trie and see what is better
        return res
        # no U delta
    
    def top_orientation_delta(self, i, j):
        g,r,b,o = 0,1,2,3
        color_mapping = {'g': g, 'r': r, 'b': b, 'o':o}

        bottum_mapping = {0: ['I'], 1: ['Dp'], 2: ['D2'], 3:['D']}

        _combo = self.combo()

        # this is an edge case when we are doing D_delta for five_type for top/one
        if _combo[j][2] == 'y' or _combo[j][2] == 'w':
            layer_delta = (color_mapping[_combo[i][2]] - color_mapping[_combo[j][1][0]]) # need face because that will tell me layer of one_type/five_type
        else:
            layer_delta = (color_mapping[_combo[i][2]] - color_mapping[_combo[j][2]])

        sticker_delta = (color_mapping[_combo[i][3]] - color_mapping[_combo[j][3]]) # an edge type for y/w edge case is not needed because sticker will not be yellow or white for this release on sticker_delta

        tops = ['_top_type', '_one_type']
        bottums = ['_five_type', 'bottum_type']

        # D delta
        res = ['I']
        if _combo[j][0] in bottums:
            new_delta=0
            # for top to bottum
            if _combo[j][0] == 'bottum_type':
                if layer_delta != sticker_delta:
                    new_delta = (layer_delta - sticker_delta)%4 # for now, keeping same logic of seven/three and moving to corrrect orientation, and not following one_type logic and just moving to either side... might revist if need be?
                    res = bottum_mapping[new_delta]
                else:
                    res = ['I'] # added for case when delta are the same and thus no move needed
            # just bring to right location
            # for top and one to five
            elif _combo[j][0] == '_five_type':
                new_delta = (layer_delta)%4
                res = bottum_mapping[new_delta]
            # just bring it under it, the solver will do both moves aand add to trie and see what is better
        return res
        # no U delta

    def one_type_cross_solver(self):
        # anywhere it says "either, not both... it should be in the form of [[alpha], [beta]]... not [alpha, beta]"

        _cross_dict = self.identify_cross_edge_type()
        # change number here
        if list(_cross_dict[2]['_one_type'].keys()) == []: # edge case if no three types
            return

        _faces = ['green', 'red', 'blue', 'orange']

        _combo = self.combo()

        _move = []
        _orientation_move_D = []
    #     _orientation_move_U = []

        _combo_plus_move = []

        if self.cross_oriented() == False:
            for i, edge in enumerate(_combo): 
                if edge[0] == '_one_type':
                    if edge[1] == 'green':
                        _move.append(['F', 'Fp']) # either , not both
                    elif edge[1] == 'red':
                        _move.append(['L', 'Lp']) # either , not both               
                    elif edge[1] == 'blue':
                        _move.append(['B', 'Bp']) # either , not both
                    elif edge[1] == 'orange':
                        _move.append(['R', 'Rp']) # either , not both

        ####################################
        tops = ['_top_type', '_one_type']
        bottums = ['_five_type', 'bottum_type']

        # needed to offset below
        sevens_threes_counter = 0
        for types in _combo:
            if types[0] == '_seven_type' or types[0] == '_three_type':
                sevens_threes_counter +=1
        
        
        # check how many tops/ones
        ones_counter = 0
        for types in _combo:
            if types[0] == '_one_type':
                ones_counter +=1

        tops_counter = 0
        for types in _combo:
            if types[0] == '_top_type':
                tops_counter +=1

    #     tops_that_three_will_interact_with_counter = 0
        bottums_that_one_will_interact_with_counter = 0
        for types in _combo:
    #         if types[0] in tops:
    #             tops_that_three_will_interact_with_counter +=1
            if types[0] in bottums:
                bottums_that_one_will_interact_with_counter +=1
        ####new
        # 2: [0,1] threes
        # 1: [2] tops
        # 1: [3] bottums
        x,y,z = [],[],[]
        for i in range(ones_counter):
            x.append(i)
        # current catgeory plus prior to previos + things it will interact with
        # plus since it will check prior
        for i in range(sevens_threes_counter+ones_counter+tops_counter, sevens_threes_counter+ones_counter+tops_counter+bottums_that_one_will_interact_with_counter):
            y.append(i)
    #     for i in range(sevens_counter+threes_counter+tops_that_three_will_interact_with_counter, sevens_counter+threes_counter+tops_that_three_will_interact_with_counter+bottums_that_three_will_interact_with_counter):
    #         z.append(i)

        if len(x) == 0:
            x = [0]
        if len(y) == 0:
            y = [0]
    #     if len(z) == 0:
    #         z = [0]
    #     a = [x,y,z]
        a = [x,y]
        b=list(product(*a))
        c=[list(i) for i in b]

        result_new = [[] for _ in range(len(c))]
        counter=0
        for (i,j) in c:
            # include edge case for sevens_counter, since if this is > 1, the counters for _move will work, but not for orietnatoin delta, thus needs to offset by seven_counters amount 
            if sevens_threes_counter == 0: # offset due to order of combo
                result_new[counter].extend([self.one_orientation_delta(i,j)]) # added as a list so that the itertool distributive property works per list; this is especitlaly needed since we have or_moves
                result_new[counter].append(_move[i])
                counter+=1
            elif sevens_threes_counter > 0:
                result_new[counter].extend([self.one_orientation_delta(i+sevens_threes_counter,j)]) # need to offset by sevens_threes due to combo order
                result_new[counter].append(_move[i])
                counter+=1
        
        # print(result_new)

        # this part is to take distrubutive property of set up and solve part now there can be multipe options
        result_new_iterate = []
        for (setup, solver) in result_new:
            if len(setup) > 1 or len(solver) > 1:
                _x = [setup, solver]
                _y = list(product(*_x))
                _z = [list(i) for i in _y]
                result_new_iterate.append(_z)
        final = [item for sublist in result_new_iterate for item in sublist]

        return final

    def top_type_cross_solver(self):
        # anywhere it says "either, not both... it should be in the form of [[alpha], [beta]]... not [alpha, beta]"

        _cross_dict = self.identify_cross_edge_type()
        # change number here
        if list(_cross_dict[3]['_top_type'].keys()) == []: # edge case if no three types
            return

        _faces = ['green', 'red', 'blue', 'orange']

        _combo = self.combo()

        _move = []
        _orientation_move_D = []
    #     _orientation_move_U = []

        _combo_plus_move = []

        if self.cross_oriented() == False:
            for i, edge in enumerate(_combo): 
                if edge[0] == '_top_type':
                    if edge[1] == 'yellow_g':
                        _move.append(['F', 'Fp']) # either , not both
                    elif edge[1] == 'yellow_r':
                        _move.append(['L', 'Lp']) # either , not both                  
                    elif edge[1] == 'yellow_b':
                        _move.append(['B', 'Bp']) # either , not both   
                    elif edge[1] == 'yellow_o':
                        _move.append(['R', 'Rp']) # either , not both 

        ####################################
        tops = ['_top_type', '_one_type']
        bottums = ['_five_type', 'bottum_type']

        # needed to offset below
        sevens_threes_counter = 0
        for types in _combo:
            if types[0] == '_seven_type' or types[0] == '_three_type':
                sevens_threes_counter +=1


        # check how many tops/ones
        ones_counter = 0
        for types in _combo:
            if types[0] == '_one_type':
                ones_counter +=1

        tops_counter = 0
        for types in _combo:
            if types[0] == '_top_type':
                tops_counter +=1

    #     tops_that_three_will_interact_with_counter = 0
        bottums_that_top_will_interact_with_counter = 0
        for types in _combo:
    #         if types[0] in tops:
    #             tops_that_three_will_interact_with_counter +=1
            if types[0] in bottums:
                bottums_that_top_will_interact_with_counter +=1
        ####new
        # 2: [0,1] threes
        # 1: [2] tops
        # 1: [3] bottums
        x,y,z = [],[],[]
        for i in range(tops_counter):
            x.append(i)
        for i in range(sevens_threes_counter+ones_counter+tops_counter, sevens_threes_counter+ones_counter+tops_counter+bottums_that_top_will_interact_with_counter):
            y.append(i)
    #     for i in range(sevens_counter+threes_counter+tops_that_three_will_interact_with_counter, sevens_counter+threes_counter+tops_that_three_will_interact_with_counter+bottums_that_three_will_interact_with_counter):
    #         z.append(i)

        if len(x) == 0:
            x = [0]
        if len(y) == 0:
            y = [0]
    #     if len(z) == 0:
    #         z = [0]
    #     a = [x,y,z]
        a = [x,y]
        b=list(product(*a))
        c=[list(i) for i in b]

        result_new = [[] for _ in range(len(c))]
        counter=0
        for (i,j) in c:
            # include edge case for sevens_counter, since if this is > 1, the counters for _move will work, but not for orietnatoin delta, thus needs to offset by seven_counters amount 
            if sevens_threes_counter == 0:
                result_new[counter].extend([self.top_orientation_delta(i+ones_counter,j)]) # need to offset by ones_counter due to combo order
                result_new[counter].append(_move[i])
                counter+=1
            elif sevens_threes_counter > 0:
                result_new[counter].extend([self.top_orientation_delta(i+sevens_threes_counter+ones_counter,j)]) # need to offset by sevens_tthree and ones due to combo order
                result_new[counter].append(_move[i])
                counter+=1

        # print(result_new)

        # this part is to take distrubutive property of set up and solve part now there can be multipe options
        result_new_iterate = []
        for (setup, solver) in result_new:
            if len(setup) > 1 or len(solver) > 1:
                _x = [setup, solver]
                _y = list(product(*_x))
                _z = [list(i) for i in _y]
                result_new_iterate.append(_z)
        final = [item for sublist in result_new_iterate for item in sublist]

        return final
    
    def five_orientation_delta(self, i, j):
        # anywhere it says "either, not both... it should be in the form of [[alpha], [beta]]... not [alpha, beta]"
        g,r,b,o = 0,1,2,3
        color_mapping = {'g': g, 'r': r, 'b': b, 'o':o}

        bottum_mapping = {0: ['I'], 1: ['Dp'], 2: ['D2'], 3:['D']}
        top_mapping = {0: ['I'], 1: ['U'], 2: ['U2'], 3:['Up']}

        _combo = self.combo()

        # this is an edge case when we are doing D_delta for five_type for top/one
        if (_combo[i][2] == 'y' or _combo[i][2] == 'w') and (_combo[j][2] == 'y' or _combo[j][2] == 'w'): # one to five case
            layer_delta = (color_mapping[_combo[i][1][0]] - color_mapping[_combo[j][1][0]]) # need face because that will tell me layer of one_type/five_type
        elif _combo[j][2] == 'y' or _combo[j][2] == 'w':
            layer_delta = (color_mapping[_combo[i][2]] - color_mapping[_combo[j][1][0]]) # need face because that will tell me layer of one_type/five_type

        elif _combo[i][2] == 'y' or _combo[i][2] == 'w':
            layer_delta = (color_mapping[_combo[i][1][0]] - color_mapping[_combo[j][2]]) # need face because that will tell me layer of one_type/five_type
        else:
            layer_delta = (color_mapping[_combo[i][2]] - color_mapping[_combo[j][2]])

        sticker_delta = (color_mapping[_combo[i][3]] - color_mapping[_combo[j][3]]) # an edge type for y/w edge case is not needed because sticker will not be yellow or white for this release on sticker_delta

        tops = ['_top_type', '_one_type']
        bottums = ['_five_type', 'bottum_type']

        # no D delta
        res = ['I']
        # U delta
        if _combo[j][0] in tops:
            new_delta = (layer_delta)%4
            res = top_mapping[new_delta]
        
        return res
        
    def five_type_cross_solver(self):
        # anywhere it says "either, not both... it should be in the form of [[alpha], [beta]]... not [alpha, beta]"

        _cross_dict = self.identify_cross_edge_type()
        # change number here
        if list(_cross_dict[4]['_five_type'].keys()) == []: # edge case if no three types
            return

        _faces = ['green', 'red', 'blue', 'orange']

        _combo = self.combo()

        _move = []
        _orientation_move_D = []
    #     _orientation_move_U = []

        _combo_plus_move = []

        if self.cross_oriented() == False:
            for i, edge in enumerate(_combo): 
                if edge[0] == '_five_type':
                    if edge[1] == 'green':
                        _move.append(['F', 'Fp']) # either , not both
                    elif edge[1] == 'red':
                        _move.append(['L', 'Lp']) # either , not both                  
                    elif edge[1] == 'blue':
                        _move.append(['B', 'Bp']) # either , not both   
                    elif edge[1] == 'orange':
                        _move.append(['R', 'Rp']) # either , not both 

        ####################################
        tops = ['_top_type', '_one_type']
        bottums = ['_five_type', 'bottum_type']

        # needed to offset below
        sevens_threes_counter = 0
        for types in _combo:
            if types[0] == '_seven_type' or types[0] == '_three_type':
                sevens_threes_counter +=1
        
        ones_tops_counter = 0
        for types in _combo:
            if types[0] == '_one_type' or types[0] == '_top_type':
                ones_tops_counter +=1
        

        # check how many fives/bottums
        fives_counter = 0
        for types in _combo:
            if types[0] == '_five_type':
                fives_counter +=1
                
        bottums_counter = 0
        for types in _combo:
            if types[0] == 'bottum_type':
                bottums_counter +=1

        tops_that_five_will_interact_with_counter = 0
        for types in _combo:
            if types[0] in tops:
                tops_that_five_will_interact_with_counter +=1
    #         if types[0] in bottums:
    #             bottums_that_top_will_interact_with_counter +=1
        ####new
        # 2: [0,1] threes
        # 1: [2] tops
        # 1: [3] bottums
        x,y,z = [],[],[]
        for i in range(fives_counter): #itself
            x.append(i)
        # current catgeory minus prior to previos + things interacting with
        # minus since it will check prior; take mod 4 - 
        for i in range((sevens_threes_counter), (sevens_threes_counter+ones_tops_counter)):
            y.append(i)
    #     for i in range((fives_counter+bottums_counter)-(sevens_threes_counter+ones_tops_counter), (fives_counter+bottums_counter)-(sevens_threes_counter+ones_tops_counter)+tops_that_five_will_interact_with_counter):

    #     for i in range(sevens_counter+threes_counter+tops_that_three_will_interact_with_counter, sevens_counter+threes_counter+tops_that_three_will_interact_with_counter+bottums_that_three_will_interact_with_counter):
    #         z.append(i)

        if len(x) == 0:
            x = [0]
        if len(y) == 0:
            y = [0]
    #     if len(z) == 0:
    #         z = [0]
    #     a = [x,y,z]
        a = [x,y]
        b=list(product(*a))
        c=[list(i) for i in b]
        
        result_new = [[] for _ in range(len(c))]
        counter=0
        for (i,j) in c:
            # include edge case for sevens_counter, since if this is > 1, the counters for _move will work, but not for orietnatoin delta, thus needs to offset by seven_counters amount 
            if (sevens_threes_counter+ones_tops_counter) == 0:
                result_new[counter].extend([self.five_orientation_delta(i,j)])
                result_new[counter].append(_move[i])
                counter+=1
            elif (sevens_threes_counter+ones_tops_counter) > 0:
    #             result_new[counter].extend([self.five_orientation_delta(i+(sevens_threes_counter+ones_tops_counter),(j%(4-(fives_counter+bottums_counter))))]) # offset by everyrthing prior
                result_new[counter].extend([self.five_orientation_delta(i+(sevens_threes_counter+ones_tops_counter),j)]) # offset by everyrthing prior
                result_new[counter].append(_move[i])
                counter+=1


        # this part is to take distrubutive property of set up and solve part now there can be multipe options
        result_new_iterate = []
        for (setup, solver) in result_new:
            if len(setup) > 1 or len(solver) > 1:
                _x = [setup, solver]
                _y = list(product(*_x))
                _z = [list(i) for i in _y]
                result_new_iterate.append(_z)
        final = [item for sublist in result_new_iterate for item in sublist]

        return final

    def bottum_orientation_delta(self):
        # only use this function when cross is oriented
        
        if self.cross_oriented():
            g,r,b,o = 0,1,2,3
            color_mapping = {'g': g, 'r': r, 'b': b, 'o':o}

            bottum_mapping = {0: ['I'], 1: ['Dp'], 2: ['D2'], 3:['D']}

            _combo = self.combo()

            sticker_delta = (color_mapping[self.cube_state['green'][5]] - color_mapping[self.cube_state['green'][8]]) # an edge type for y/w edge case is not needed because sticker will not be yellow or white for this release on sticker_delta

            return bottum_mapping[sticker_delta]
        
        else:
            return None

    def cross_permuted(self):
        # this function is used so that we can identify which bottum algo to use
        # we want to orient the bottum layer before applying the algo, so we must first know how many are permuted
        # this is a shortcut becuase knowing how many are permuted when not oriented lets us know which bottum algo to use
        # usually we would not permute and then orient, but will do for bottum type
        # thus function will let us know how many bottum pieces are permuted and is useful when assuming NOT oriented AND 4 white edges in bottum layers
        _combo = self.combo()
        
        _permuted = []
        for i in range(4):
            if _combo[i][2] == _combo[i][3]:
                _permuted.append(i)
            
        return _permuted

    def bottum_type_cross_solver(self):
        from cubeai.test.testing_functions import do_scramble

        _cross_dict = self.identify_cross_edge_type()
        # change number here
    #     if list(_cross_dict[5]['bottum_type'].keys()) == []: # edge case if no three types
    #         return

        _faces = ['green', 'red', 'blue', 'orange']

        _combo = self.combo()

        _set_up_move = []
        _move = []
        
        # case for for white edges in white face, they are oriented, but there remains D moves, ie, not permuted
        if self.get_edge_count()['white'] == 4 and self.cross_oriented() and (self.combo()[0][2] != self.combo()[0][3]):
            return [self.bottum_orientation_delta()]
            # evetnually can use this on top layer for AUF
        
        # case that the cross does not have 4 bottum types left or oriented, but because above condition, thus solved 
        elif self.get_edge_count()['white'] != 4 or self.cross_oriented():
            # print('not a bottum solver case')
            pass
        
        
        # if not all 4 oriented and 1 permuted:
        if self.get_edge_count()['white'] == 4 and not self.cross_oriented() and (len(self.cross_permuted()) == 1):
            # do D:
            _cube_ = do_scramble(['D'], self)
            # if we now have 2 permuted next to each other:
                # go to ALPHA with D as set up move
            # check if the two permuted are next to each other
            if (len(_cube_.cross_permuted()) == 2) and ((_cube_.cross_permuted()[1]-_cube_.cross_permuted()[0] == 1)%2):
                _move.append(['D'])
                ####ALPHA####
    #             if self.get_edge_count()['white'] == 4 and not self.cross_oriented() and (len(self.cross_permuted()) == 2) and ((cross_permuted(self)[1]-cross_permuted(self)[0] == 1)%2):
                    # do R,D,Rp,Dp,R with one of the non-permuted faces in right layer 
                    # green front
                if _cube_.cross_permuted() == [2,3]:
                    _move.append(['R', 'D', 'Rp', 'Dp', 'R'])
                # orange front
                elif _cube_.cross_permuted() == [0,3]:
                    _move.append(['B', 'D', 'Bp', 'Dp', 'B'])                 
                # blue front
                elif _cube_.cross_permuted() == [0,1]:
                    _move.append(['L', 'D', 'Lp', 'Dp', 'L'])     
                # red front
                elif _cube_.cross_permuted() == [1,2]:
                    _move.append(['F', 'D', 'Fp', 'Dp', 'F'])  
            ####ALPHA####
                return [[item for sublist in _move for item in sublist]]

        
            # elif we now have 2 permuted across each other:
                # go to beta with D as set up move
            elif (len(_cube_.cross_permuted()) == 2) and ((_cube_.cross_permuted()[1]-_cube_.cross_permuted()[0] == 2)%2):
                _move.append(['D'])
                ####BETA####
                # green front
                if _cube_.cube_state['orange'][5] !=  _cube_.cube_state['orange'][8]:
                    _move.append(['F', 'B', 'D2', 'Fp', 'Bp'])
                # red front
                elif _cube_.cube_state['green'][5] !=  _cube_.cube_state['green'][8]:
                    _move.append(['L', 'R', 'D2', 'Lp', 'Rp'])    
                ####BETA####
                return [[item for sublist in _move for item in sublist]]

        
            # elif now we have exactly 4 un-permuted
                # go to gamma (may need to reduce count of moves later)
            elif (len(_cube_.cross_permuted()) == 0):
                _cube_ = do_scramble(['D2'], _cube_)
                _move.append(['Dp'])

                ####ALPHA####
                    # do R,D,Rp,Dp,R with one of the non-permuted faces in right layer 
                    # green front
                if _cube_.cross_permuted() == [2,3]:
                    _move.append(['R', 'D', 'Rp', 'Dp', 'R'])
                # orange front
                elif _cube_.cross_permuted() == [0,3]:
                    _move.append(['B', 'D', 'Bp', 'Dp', 'B'])                 
                # blue front
                elif _cube_.cross_permuted() == [0,1]:
                    _move.append(['L', 'D', 'Lp', 'Dp', 'L'])     
                # red front
                elif _cube_.cross_permuted() == [1,2]:
                    _move.append(['F', 'D', 'Fp', 'Dp', 'F'])  
                ####ALPHA####
                return [[item for sublist in _move for item in sublist]]

            
            
            
            
        # GAMMA
        # if not all 4 oriented and 0 permuted:
        if self.get_edge_count()['white'] == 4 and not self.cross_oriented() and (len(self.cross_permuted()) == 0):# and ((cross_permuted(self)[1]-cross_permuted(self)[0] != 1)%2):
            # can have either alpha or beta case. if alpha, must do D2. if beta, can do either D or Dp
            either_move = random.choice(['D', 'Dp'])
            _cube_ = do_scramble([either_move], self)
            if (len(_cube_.cross_permuted()) == 2) and ((_cube_.cross_permuted()[1]-_cube_.cross_permuted()[0] == 2)%2):
                
                _move.append([either_move])
                ####BETA####
                # green front
                if _cube_.cube_state['orange'][5] !=  _cube_.cube_state['orange'][8]:
                    _move.append(['F', 'B', 'D2', 'Fp', 'Bp'])
                # red front
                elif _cube_.cube_state['green'][5] !=  _cube_.cube_state['green'][8]:
                    _move.append(['L', 'R', 'D2', 'Lp', 'Rp'])    
                ####BETA####
                return [[item for sublist in _move for item in sublist]]

            

            
            # do D2
                # should now have 2 permuted next to each other:
                    # go to alpha with D2 as set up move

            else:
                __cube__ = do_scramble(['D2'], self)
                _move.append(['D2'])
            ####ALPHA####
                # do R,D,Rp,Dp,R with one of the non-permuted faces in right layer 
                # green front
                if __cube__.cross_permuted() == [2,3]:
                    _move.append(['R', 'D', 'Rp', 'Dp', 'R'])
                # orange front
                elif __cube__.cross_permuted() == [0,3]:
                    _move.append(['B', 'D', 'Bp', 'Dp', 'B'])                 
                # blue front
                elif __cube__.cross_permuted() == [0,1]:
                    _move.append(['L', 'D', 'Lp', 'Dp', 'L'])     
                # red front
                elif __cube__.cross_permuted() == [1,2]:
                    _move.append(['F', 'D', 'Fp', 'Dp', 'F'])  
            ####ALPHA####insert
                return [[item for sublist in _move for item in sublist]]

            
        
        # ALPHA
        # if not all 4 oriented and 2 permuted next to each other:
        if self.get_edge_count()['white'] == 4 and not self.cross_oriented() and (len(self.cross_permuted()) == 2) and ((self.cross_permuted()[1]-self.cross_permuted()[0] == 1)%2):
            # do R,D,Rp,Dp,R with one of the non-permuted faces in right layer 
            # green front
            if self.cross_permuted() == [2,3]:
                _move.append(['R', 'D', 'Rp', 'Dp', 'R'])
            # orange front
            elif self.cross_permuted() == [0,3]:
                _move.append(['B', 'D', 'Bp', 'Dp', 'B'])                 
            # blue front
            elif self.cross_permuted() == [0,1]:
                _move.append(['L', 'D', 'Lp', 'Dp', 'L'])     
            # red front
            elif self.cross_permuted() == [1,2]:
                _move.append(['F', 'D', 'Fp', 'Dp', 'F'])     
            return _move
            
        
        # BETA
        # if not all 4 oriented and 2 permuted across each other:
        if self.get_edge_count()['white'] == 4 and not self.cross_oriented() and (len(self.cross_permuted()) == 2) and ((self.cross_permuted()[1]-self.cross_permuted()[0] == 2)%2):
            # do F,B,D2, Fp, Bp with one of the non-permuted faces in right layer 
            # green front
            if self.cube_state['orange'][5] !=  self.cube_state['orange'][8]:
                _move.append(['F', 'B', 'D2', 'Fp', 'Bp'])
        
            # red front
            elif self.cube_state['green'][5] !=  self.cube_state['green'][8]:
                _move.append(['L', 'R', 'D2', 'Lp', 'Rp'])  
            return _move

                    
        # in all of these cases, how do i translate the algo to othe rfaces, i think just hard code lol for the 4 cases
            # idealy would do "x"/"y"/"z", do algo, then un "x"/"y"/"z"
                # R --> B --> L --> F
                # F --> R --> B --> L
            # or i do F on layer and thrrow into my solver from prior cross types
        
        # could have determed if any oriented next to each other and then applied algo then D moves
        
        # i guess i could have gotten edges in white layer and then did one of the above, but it would be less efficient, but i thought of this in beginning with 3-cycle

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.children = [] 

class CrossSolver:
    def __init__(self):
        self.solutions = []

    def treeify(self, cube, cur_moves):
        from cubeai.test.testing_functions import do_scramble, sanitize

        _combo_dict = {
        '_seven_type' : 'seven_type_cross_solver',
        '_three_type' : 'three_type_cross_solver',
        '_one_type' : 'one_type_cross_solver',
        '_top_type' : 'top_type_cross_solver',
        '_five_type' : 'five_type_cross_solver'
        }
        
        _combo = cube.combo()
        _combo_list = []
        for i in _combo:
            _combo_list.append(i[0])

        level = []
        for _combo_type in _combo_list:
            if _combo_type != 'bottum_type':
                level.append(TreeNode(_combo_type))

        # print('combo types:', [[l.val, l.children] for l in level])
        for node in level:
            node.children = getattr(cube, _combo_dict[node.val])()
            node.children = sanitize(node.children)
            node.children = [TreeNode(tuple(c)) for c in node.children]

        _new_cubes = []
        for node in level:
            for c in node.children:
                _new_cube = do_scramble(c.val, cube)
                c.children = [TreeNode(_new_cube)]
                _new_cube_combo = _new_cube.combo()
                _new_cube_combo_list = []
                for i in _new_cube_combo:
                    _new_cube_combo_list.append(i[0])
                if _new_cube_combo_list.count('bottum_type') == 4:
                    _all_moves = []
                    for move_set in (cur_moves + [c.val]):
                        for sub_move in move_set:
                            _all_moves.append(sub_move)
                    final_set_of_moves = _new_cube.bottum_type_cross_solver()
                    if final_set_of_moves == None: # invesitage this
                        final_set_of_moves = [['I']]
                        pass
                    self.solutions.append(_all_moves+final_set_of_moves[0])
                    self.solutions = sanitize(self.solutions) 
                else:
                    _all_moves = []
                    for move_set in (cur_moves + [c.val]):
                        for sub_move in move_set:
                            _all_moves.append(sub_move)
                    if len(_all_moves) <= 5: 
                        self.treeify(_new_cube, cur_moves + [c.val])  # should we return solutions?

        # case for just cross solver only
        if _combo_list.count('bottum_type') == 4:
            final_set_of_moves = cube.bottum_type_cross_solver()
            if final_set_of_moves == None: # invesitage this
                final_set_of_moves = [['I']]
                pass
            self.solutions.append(final_set_of_moves[0]) # should we return solutions?
            self.solutions = sanitize(self.solutions)
