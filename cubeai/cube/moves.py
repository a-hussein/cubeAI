from typing import Dict, List


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

        _seven_type, _three_type, _one_type, _five_type, _top_type, _bottum_type = {}, {}, {}, {}, {}, {}

        _edges = {1,3,5,7}

        # easy type, ie in the 7 slot of non-yelloow face
        if self.get_edge_count()[face] < 4:
            for i in range(4):
                if self.cube_state[orientation[i]][7] == 'w':
                    _seven_type[orientation[i]] = [self.cube_state[orientation[i+1]][8], self.cube_state[orientation[i+1]][3]]
        
        # easy type, ie in the 7 slot of non-yelloow face
        if self.get_edge_count()[face] < 4:
            for i in range(4):
                if self.cube_state[orientation[i]][3] == 'w':
                    _three_type[orientation[i]] = [self.cube_state[orientation[i-1]][8], self.cube_state[orientation[i-1]][7]]
        
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
        if self.get_edge_count()[face] < 4:
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
            {'_five_type': _five_type},
            {'_top_type': _top_type},
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

    def orientation_delta(self, i, j, which_layer='bottum'):
        g,r,b,o = 0,1,2,3
        color_mapping = {'g': g, 'r': r, 'b': b, 'o':o}

        bottum_mapping = {0: ['I'], 1: ['Dp'], 2: ['D','D'], 3:['D']}
        top_mapping = {0: ['I'], 1: ['Up'], 2: ['U','U'], 3:['U']}

        _combo = self.combo()
            
        layer_delta = (color_mapping[_combo[i][2]] - color_mapping[_combo[j][2]])
        sticker_delta = (color_mapping[_combo[i][3]] - color_mapping[_combo[j][3]])
        
        new_delta = 0
        if layer_delta != sticker_delta:
            new_delta = (layer_delta - sticker_delta)%4
        
        if which_layer == 'bottum':
            return bottum_mapping[new_delta]
        else:
            return top_mapping[new_delta]

    def seven_type_cross_solver(self):
        _cross_dict = self.identify_cross_edge_type()
        if list(_cross_dict[0]['_seven_type'].keys()) == []: # edge case if no seven types
            return
        
        _faces = ['green', 'red', 'blue', 'orange']

        _combo = self.combo()
        
        _move = []
        _orientation_move = []
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
        # this should potentially be its own function
        sevens = []
        for i, edge in enumerate(_combo):
            if edge[0] == '_seven_type':
                sevens.append(i)
            
        bottums = []
        for i, edge in enumerate(_combo):
            if edge[0] == 'bottum_type':
                bottums.append(i)
        
        _i_j = []
        for seven in sevens:
            for bottum in bottums:
                _i_j.append([seven, bottum])
        
        ####################################

        for i, seven_bottums in enumerate(_i_j):
            _orientation_move.append(self.orientation_delta(_i_j[i][0], _i_j[i][1]))
        
        
        for i, move in enumerate(_move):
            for j, (seven, bottum) in enumerate(_i_j):
                if i == seven:
                    _combo_plus_move.append(_orientation_move[j] + [move])
        
        return _combo_plus_move   

    def three_type_cross_solver(self):
        _cross_dict = self.identify_cross_edge_type()
        if list(_cross_dict[1]['_three_type'].keys()) == []:
            return
        
        _faces = ['green', 'red', 'blue', 'orange']

        _combo = self.combo()
        
        _move = []
        _orientation_move = []
        _combo_plus_move = []
        
        
        # one move to solve _three_type
        if self.cross_oriented() == False:
            for face_with_white_edge in list(_cross_dict[1]['_three_type'].keys()):
                if face_with_white_edge == 'green':
                    _move.append('Rp')
                elif face_with_white_edge == 'red':
                    _move.append('Fp')                    
                elif face_with_white_edge == 'blue':
                    _move.append('Lp')    
                elif face_with_white_edge == 'orange':
                    _move.append('Bp')   
        
        ####################################
        # this should potentially be its own function
        threes = []
        for i, edge in enumerate(_combo):
            if edge[0] == '_three_type':
                threes.append(i)
            
        bottums = []
        for i, edge in enumerate(_combo):
            if edge[0] == 'bottum_type':
                bottums.append(i)
        
        _i_j = []
        for three in threes:
            for bottum in bottums:
                _i_j.append([three, bottum])
        
        ####################################

        for i, three_bottums in enumerate(_i_j):
            _orientation_move.append(self.orientation_delta(_i_j[i][0], _i_j[i][1]))
        
        # this takse care of edge case where one three, one seven and one bottum
        if len(_i_j) == 1:
            _combo_plus_move.append(_orientation_move[0] + [_move][0])

        # otherwise take "cross-product"
        else:
            for i, move in enumerate(_move):
                for j, (three, bottum) in enumerate(_i_j):
                    if i == three:
                        _combo_plus_move.append(_orientation_move[j] + [move])
                    

        return _combo_plus_move