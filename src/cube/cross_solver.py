from .engine_solver import TreeNode
from itertools import product
import random


class CrossSolverMixin:
    """
    This class uses the CrossSetupForSolverMixin class to help solve each sub-type of cross types.
    """

    def seven_type_cross_solver(self):
        _cross_dict = self.identify_cross_edge_type()
        # change number here
        if (
            list(_cross_dict[0]["_seven_type"].keys()) == []
        ):  # edge case if no seven types
            return

        _faces = ["green", "red", "blue", "orange"]

        _combo = self.combo()

        _move = []
        _orientation_move_D = []
        _orientation_move_U = []

        _combo_plus_move = []

        if not self.cross_oriented():
            for i, edge in enumerate(_combo):
                if edge[0] == "_seven_type":
                    if edge[1] == "green":
                        _move.append("L")
                    elif edge[1] == "red":
                        _move.append("B")
                    elif edge[1] == "blue":
                        _move.append("R")
                    elif edge[1] == "orange":
                        _move.append("F")

        ####################################
        tops = ["_top_type", "_one_type"]
        bottums = ["_five_type", "bottum_type"]

        # check how many sevens
        sevens_counter = 0
        for types in _combo:
            if types[0] == "_seven_type":
                sevens_counter += 1

        threes_counter = 0
        for types in _combo:
            if types[0] == "_three_type":
                threes_counter += 1

        tops_that_seven_will_interact_with_counter = 0
        bottums_that_seven_will_interact_with_counter = 0
        for types in _combo:
            if types[0] in tops:
                tops_that_seven_will_interact_with_counter += 1
            elif types[0] in bottums:
                bottums_that_seven_will_interact_with_counter += 1

        # the amount of moves to do will be sevens and their corresponding valid downstreams
        # nums = max(tops_that_seven_will_interact_with_counter, bottums_that_seven_will_interact_with_counter, 1)
        # number_of_orientation_deltas = sevens_counter*nums

        ####new
        # 2: [0,1]
        # 1: [2]
        # 1: [3]
        x, y, z = [], [], []
        for i in range(sevens_counter):
            x.append(i)
        for i in range(
            sevens_counter + threes_counter,
            sevens_counter
            + threes_counter
            + tops_that_seven_will_interact_with_counter,
        ):
            y.append(i)
        for i in range(
            sevens_counter
            + threes_counter
            + tops_that_seven_will_interact_with_counter,
            sevens_counter
            + threes_counter
            + tops_that_seven_will_interact_with_counter
            + bottums_that_seven_will_interact_with_counter,
        ):
            z.append(i)

        if len(x) == 0:
            x = [0]
        if len(y) == 0:
            y = [0]
        if len(z) == 0:
            z = [0]
        a = [x, y, z]
        b = list(product(*a))
        c = [list(i) for i in b]

        result_new = [[] for _ in range(len(c))]
        counter = 0
        for i, j, k in c:
            result_new[counter].extend(
                self.combine_seven_three_orientation_delta(i, j, k)
            )  # not needed to add as list since no or_moves
            result_new[counter].append(_move[i])
            counter += 1

        return result_new

    def three_type_cross_solver(self):
        _cross_dict = self.identify_cross_edge_type()
        # change number here
        if (
            list(_cross_dict[1]["_three_type"].keys()) == []
        ):  # edge case if no three types
            return

        _faces = ["green", "red", "blue", "orange"]

        _combo = self.combo()

        _move = []
        _orientation_move_D = []
        _orientation_move_U = []

        _combo_plus_move = []

        if not self.cross_oriented():
            for i, edge in enumerate(_combo):
                if edge[0] == "_three_type":
                    if edge[1] == "green":
                        _move.append("Rp")
                    elif edge[1] == "red":
                        _move.append("Fp")
                    elif edge[1] == "blue":
                        _move.append("Lp")
                    elif edge[1] == "orange":
                        _move.append("Bp")

        ####################################
        tops = ["_top_type", "_one_type"]
        bottums = ["_five_type", "bottum_type"]

        # check how many sevens
        sevens_counter = 0
        for types in _combo:
            if types[0] == "_seven_type":
                sevens_counter += 1

        threes_counter = 0
        for types in _combo:
            if types[0] == "_three_type":
                threes_counter += 1

        tops_that_three_will_interact_with_counter = 0
        bottums_that_three_will_interact_with_counter = 0
        for types in _combo:
            if types[0] in tops:
                tops_that_three_will_interact_with_counter += 1
            elif types[0] in bottums:
                bottums_that_three_will_interact_with_counter += 1
        ####new
        # 2: [0,1] threes
        # 1: [2] tops
        # 1: [3] bottums
        x, y, z = [], [], []
        for i in range(threes_counter):
            x.append(i)
        for i in range(
            sevens_counter + threes_counter,
            sevens_counter
            + threes_counter
            + tops_that_three_will_interact_with_counter,
        ):
            y.append(i)
        for i in range(
            sevens_counter
            + threes_counter
            + tops_that_three_will_interact_with_counter,
            sevens_counter
            + threes_counter
            + tops_that_three_will_interact_with_counter
            + bottums_that_three_will_interact_with_counter,
        ):
            z.append(i)

        if len(x) == 0:
            x = [0]
        if len(y) == 0:
            y = [0]
        if len(z) == 0:
            z = [0]
        a = [x, y, z]
        b = list(product(*a))
        c = [list(i) for i in b]

        result_new = [[] for _ in range(len(c))]
        counter = 0
        for i, j, k in c:
            # include edge case for sevens_counter, since if this is > 1, the counters for _move will work, but not for orietnatoin delta, thus needs to offset by seven_counters amount
            if sevens_counter == 0:
                result_new[counter].extend(
                    self.combine_seven_three_orientation_delta(i, j, k)
                )  # not needed to add as list since no or_moves...
                result_new[counter].append(_move[i])
                counter += 1
            elif sevens_counter > 0:
                result_new[counter].extend(
                    self.combine_seven_three_orientation_delta(i + sevens_counter, j, k)
                )  # need to offest by sevens due to combo order
                result_new[counter].append(_move[i])
                counter += 1

        return result_new

    def one_type_cross_solver(self):
        # anywhere it says "either, not both... it should be in the form of [[alpha], [beta]]... not [alpha, beta]"

        _cross_dict = self.identify_cross_edge_type()
        # change number here
        if (
            list(_cross_dict[2]["_one_type"].keys()) == []
        ):  # edge case if no three types
            return

        _faces = ["green", "red", "blue", "orange"]

        _combo = self.combo()

        _move = []
        _orientation_move_D = []
        #     _orientation_move_U = []

        _combo_plus_move = []

        if not self.cross_oriented():
            for i, edge in enumerate(_combo):
                if edge[0] == "_one_type":
                    if edge[1] == "green":
                        _move.append(["F", "Fp"])  # either , not both
                    elif edge[1] == "red":
                        _move.append(["L", "Lp"])  # either , not both
                    elif edge[1] == "blue":
                        _move.append(["B", "Bp"])  # either , not both
                    elif edge[1] == "orange":
                        _move.append(["R", "Rp"])  # either , not both

        ####################################
        # tops = ["_top_type", "_one_type"]
        bottums = ["_five_type", "bottum_type"]

        # needed to offset below
        sevens_threes_counter = 0
        for types in _combo:
            if types[0] == "_seven_type" or types[0] == "_three_type":
                sevens_threes_counter += 1

        # check how many tops/ones
        ones_counter = 0
        for types in _combo:
            if types[0] == "_one_type":
                ones_counter += 1

        tops_counter = 0
        for types in _combo:
            if types[0] == "_top_type":
                tops_counter += 1

        #     tops_that_three_will_interact_with_counter = 0
        bottums_that_one_will_interact_with_counter = 0
        for types in _combo:
            #         if types[0] in tops:
            #             tops_that_three_will_interact_with_counter +=1
            if types[0] in bottums:
                bottums_that_one_will_interact_with_counter += 1
        ####new
        # 2: [0,1] threes
        # 1: [2] tops
        # 1: [3] bottums
        x, y = [], []
        # z = []
        for i in range(ones_counter):
            x.append(i)
        # current catgeory plus prior to previos + things it will interact with
        # plus since it will check prior
        for i in range(
            sevens_threes_counter + ones_counter + tops_counter,
            sevens_threes_counter
            + ones_counter
            + tops_counter
            + bottums_that_one_will_interact_with_counter,
        ):
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
        a = [x, y]
        b = list(product(*a))
        c = [list(i) for i in b]

        result_new = [[] for _ in range(len(c))]
        counter = 0
        for i, j in c:
            # include edge case for sevens_counter, since if this is > 1, the counters for _move will work, but not for orietnatoin delta, thus needs to offset by seven_counters amount
            if sevens_threes_counter == 0:  # offset due to order of combo
                result_new[counter].extend(
                    [self.one_orientation_delta(i, j)]
                )  # added as a list so that the itertool distributive property works per list; this is especitlaly needed since we have or_moves
                result_new[counter].append(_move[i])
                counter += 1
            elif sevens_threes_counter > 0:
                result_new[counter].extend(
                    [self.one_orientation_delta(i + sevens_threes_counter, j)]
                )  # need to offset by sevens_threes due to combo order
                result_new[counter].append(_move[i])
                counter += 1

        # print(result_new)

        # this part is to take distrubutive property of set up and solve part now there can be multipe options
        result_new_iterate = []
        for setup, solver in result_new:
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
        if (
            list(_cross_dict[3]["_top_type"].keys()) == []
        ):  # edge case if no three types
            return

        _faces = ["green", "red", "blue", "orange"]

        _combo = self.combo()

        _move = []
        _orientation_move_D = []
        #     _orientation_move_U = []

        _combo_plus_move = []

        if not self.cross_oriented():
            for i, edge in enumerate(_combo):
                if edge[0] == "_top_type":
                    if edge[1] == "yellow_g":
                        _move.append(["F", "Fp"])  # either , not both
                    elif edge[1] == "yellow_r":
                        _move.append(["L", "Lp"])  # either , not both
                    elif edge[1] == "yellow_b":
                        _move.append(["B", "Bp"])  # either , not both
                    elif edge[1] == "yellow_o":
                        _move.append(["R", "Rp"])  # either , not both

        ####################################
        # tops = ["_top_type", "_one_type"]
        bottums = ["_five_type", "bottum_type"]

        # needed to offset below
        sevens_threes_counter = 0
        for types in _combo:
            if types[0] == "_seven_type" or types[0] == "_three_type":
                sevens_threes_counter += 1

        # check how many tops/ones
        ones_counter = 0
        for types in _combo:
            if types[0] == "_one_type":
                ones_counter += 1

        tops_counter = 0
        for types in _combo:
            if types[0] == "_top_type":
                tops_counter += 1

        #     tops_that_three_will_interact_with_counter = 0
        bottums_that_top_will_interact_with_counter = 0
        for types in _combo:
            #         if types[0] in tops:
            #             tops_that_three_will_interact_with_counter +=1
            if types[0] in bottums:
                bottums_that_top_will_interact_with_counter += 1
        ####new
        # 2: [0,1] threes
        # 1: [2] tops
        # 1: [3] bottums
        x, y = [], []
        # z = []
        for i in range(tops_counter):
            x.append(i)
        for i in range(
            sevens_threes_counter + ones_counter + tops_counter,
            sevens_threes_counter
            + ones_counter
            + tops_counter
            + bottums_that_top_will_interact_with_counter,
        ):
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
        a = [x, y]
        b = list(product(*a))
        c = [list(i) for i in b]

        result_new = [[] for _ in range(len(c))]
        counter = 0
        for i, j in c:
            # include edge case for sevens_counter, since if this is > 1, the counters for _move will work, but not for orietnatoin delta, thus needs to offset by seven_counters amount
            if sevens_threes_counter == 0:
                result_new[counter].extend(
                    [self.top_orientation_delta(i + ones_counter, j)]
                )  # need to offset by ones_counter due to combo order
                result_new[counter].append(_move[i])
                counter += 1
            elif sevens_threes_counter > 0:
                result_new[counter].extend(
                    [
                        self.top_orientation_delta(
                            i + sevens_threes_counter + ones_counter, j
                        )
                    ]
                )  # need to offset by sevens_tthree and ones due to combo order
                result_new[counter].append(_move[i])
                counter += 1

        # print(result_new)

        # this part is to take distrubutive property of set up and solve part now there can be multipe options
        result_new_iterate = []
        for setup, solver in result_new:
            if len(setup) > 1 or len(solver) > 1:
                _x = [setup, solver]
                _y = list(product(*_x))
                _z = [list(i) for i in _y]
                result_new_iterate.append(_z)
        final = [item for sublist in result_new_iterate for item in sublist]

        return final

    def five_type_cross_solver(self):
        # anywhere it says "either, not both... it should be in the form of [[alpha], [beta]]... not [alpha, beta]"

        _cross_dict = self.identify_cross_edge_type()
        # change number here
        if (
            list(_cross_dict[4]["_five_type"].keys()) == []
        ):  # edge case if no three types
            return

        _faces = ["green", "red", "blue", "orange"]

        _combo = self.combo()

        _move = []
        _orientation_move_D = []
        #     _orientation_move_U = []

        _combo_plus_move = []

        if not self.cross_oriented():
            for i, edge in enumerate(_combo):
                if edge[0] == "_five_type":
                    if edge[1] == "green":
                        _move.append(["F", "Fp"])  # either , not both
                    elif edge[1] == "red":
                        _move.append(["L", "Lp"])  # either , not both
                    elif edge[1] == "blue":
                        _move.append(["B", "Bp"])  # either , not both
                    elif edge[1] == "orange":
                        _move.append(["R", "Rp"])  # either , not both

        ####################################
        tops = ["_top_type", "_one_type"]
        # bottums = ["_five_type", "bottum_type"]

        # needed to offset below
        sevens_threes_counter = 0
        for types in _combo:
            if types[0] == "_seven_type" or types[0] == "_three_type":
                sevens_threes_counter += 1

        ones_tops_counter = 0
        for types in _combo:
            if types[0] == "_one_type" or types[0] == "_top_type":
                ones_tops_counter += 1

        # check how many fives/bottums
        fives_counter = 0
        for types in _combo:
            if types[0] == "_five_type":
                fives_counter += 1

        bottums_counter = 0
        for types in _combo:
            if types[0] == "bottum_type":
                bottums_counter += 1

        tops_that_five_will_interact_with_counter = 0
        for types in _combo:
            if types[0] in tops:
                tops_that_five_will_interact_with_counter += 1
        #         if types[0] in bottums:
        #             bottums_that_top_will_interact_with_counter +=1
        ####new
        # 2: [0,1] threes
        # 1: [2] tops
        # 1: [3] bottums
        x, y = [], []
        # z = []
        for i in range(fives_counter):  # itself
            x.append(i)
        # current catgeory minus prior to previos + things interacting with
        # minus since it will check prior; take mod 4 -
        for i in range(
            (sevens_threes_counter), (sevens_threes_counter + ones_tops_counter)
        ):
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
        a = [x, y]
        b = list(product(*a))
        c = [list(i) for i in b]

        result_new = [[] for _ in range(len(c))]
        counter = 0
        for i, j in c:
            # include edge case for sevens_counter, since if this is > 1, the counters for _move will work, but not for orietnatoin delta, thus needs to offset by seven_counters amount
            if (sevens_threes_counter + ones_tops_counter) == 0:
                result_new[counter].extend([self.five_orientation_delta(i, j)])
                result_new[counter].append(_move[i])
                counter += 1
            elif (sevens_threes_counter + ones_tops_counter) > 0:
                #             result_new[counter].extend([self.five_orientation_delta(i+(sevens_threes_counter+ones_tops_counter),(j%(4-(fives_counter+bottums_counter))))]) # offset by everyrthing prior
                result_new[counter].extend(
                    [
                        self.five_orientation_delta(
                            i + (sevens_threes_counter + ones_tops_counter), j
                        )
                    ]
                )  # offset by everyrthing prior
                result_new[counter].append(_move[i])
                counter += 1

        # this part is to take distrubutive property of set up and solve part now there can be multipe options
        result_new_iterate = []
        for setup, solver in result_new:
            if len(setup) > 1 or len(solver) > 1:
                _x = [setup, solver]
                _y = list(product(*_x))
                _z = [list(i) for i in _y]
                result_new_iterate.append(_z)
        final = [item for sublist in result_new_iterate for item in sublist]

        return final

    def bottum_type_cross_solver(self):
        from .helpers import do_scramble

        _cross_dict = self.identify_cross_edge_type()
        # change number here
        #     if list(_cross_dict[5]['bottum_type'].keys()) == []: # edge case if no three types
        #         return

        _faces = ["green", "red", "blue", "orange"]

        _combo = self.combo()

        _set_up_move = []
        _move = []

        # case for for white edges in white face, they are oriented, but there remains D moves, ie, not permuted
        if (
            self.get_edge_count()["white"] == 4
            and self.cross_oriented()
            and (self.combo()[0][2] != self.combo()[0][3])
        ):
            return [self.bottum_orientation_delta()]
            # evetnually can use this on top layer for AUF

        # case that the cross does not have 4 bottum types left or oriented, but because above condition, thus solved
        elif self.get_edge_count()["white"] != 4 or self.cross_oriented():
            # print('not a bottum solver case')
            pass

        # if not all 4 oriented and 1 permuted:
        if (
            self.get_edge_count()["white"] == 4
            and not self.cross_oriented()
            and (len(self.cross_permuted()) == 1)
        ):
            # do D:
            _cube_ = do_scramble(["D"], self)
            # if we now have 2 permuted next to each other:
            # go to ALPHA with D as set up move
            # check if the two permuted are next to each other
            if (len(_cube_.cross_permuted()) == 2) and (
                (_cube_.cross_permuted()[1] - _cube_.cross_permuted()[0] == 1) % 2
            ):
                _move.append(["D"])
                ####ALPHA####
                #             if self.get_edge_count()['white'] == 4 and not self.cross_oriented() and (len(self.cross_permuted()) == 2) and ((cross_permuted(self)[1]-cross_permuted(self)[0] == 1)%2):
                # do R,D,Rp,Dp,R with one of the non-permuted faces in right layer
                # green front
                if _cube_.cross_permuted() == [2, 3]:
                    _move.append(["R", "D", "Rp", "Dp", "R"])
                # orange front
                elif _cube_.cross_permuted() == [0, 3]:
                    _move.append(["B", "D", "Bp", "Dp", "B"])
                # blue front
                elif _cube_.cross_permuted() == [0, 1]:
                    _move.append(["L", "D", "Lp", "Dp", "L"])
                # red front
                elif _cube_.cross_permuted() == [1, 2]:
                    _move.append(["F", "D", "Fp", "Dp", "F"])
                ####ALPHA####
                return [[item for sublist in _move for item in sublist]]

            # elif we now have 2 permuted across each other:
            # go to beta with D as set up move
            elif (len(_cube_.cross_permuted()) == 2) and (
                (_cube_.cross_permuted()[1] - _cube_.cross_permuted()[0] == 2) % 2
            ):
                _move.append(["D"])
                ####BETA####
                # green front
                if _cube_.cube_state["orange"][5] != _cube_.cube_state["orange"][8]:
                    _move.append(["F", "B", "D2", "Fp", "Bp"])
                # red front
                elif _cube_.cube_state["green"][5] != _cube_.cube_state["green"][8]:
                    _move.append(["L", "R", "D2", "Lp", "Rp"])
                ####BETA####
                return [[item for sublist in _move for item in sublist]]

            # elif now we have exactly 4 un-permuted
            # go to gamma (may need to reduce count of moves later)
            elif len(_cube_.cross_permuted()) == 0:
                _cube_ = do_scramble(["D2"], _cube_)
                _move.append(["Dp"])

                ####ALPHA####
                # do R,D,Rp,Dp,R with one of the non-permuted faces in right layer
                # green front
                if _cube_.cross_permuted() == [2, 3]:
                    _move.append(["R", "D", "Rp", "Dp", "R"])
                # orange front
                elif _cube_.cross_permuted() == [0, 3]:
                    _move.append(["B", "D", "Bp", "Dp", "B"])
                # blue front
                elif _cube_.cross_permuted() == [0, 1]:
                    _move.append(["L", "D", "Lp", "Dp", "L"])
                # red front
                elif _cube_.cross_permuted() == [1, 2]:
                    _move.append(["F", "D", "Fp", "Dp", "F"])
                ####ALPHA####
                return [[item for sublist in _move for item in sublist]]

        # GAMMA
        # if not all 4 oriented and 0 permuted:
        if (
            self.get_edge_count()["white"] == 4
            and not self.cross_oriented()
            and (len(self.cross_permuted()) == 0)
        ):  # and ((cross_permuted(self)[1]-cross_permuted(self)[0] != 1)%2):
            # can have either alpha or beta case. if alpha, must do D2. if beta, can do either D or Dp
            either_move = random.choice(["D", "Dp"])
            _cube_ = do_scramble([either_move], self)
            if (len(_cube_.cross_permuted()) == 2) and (
                (_cube_.cross_permuted()[1] - _cube_.cross_permuted()[0] == 2) % 2
            ):
                _move.append([either_move])
                ####BETA####
                # green front
                if _cube_.cube_state["orange"][5] != _cube_.cube_state["orange"][8]:
                    _move.append(["F", "B", "D2", "Fp", "Bp"])
                # red front
                elif _cube_.cube_state["green"][5] != _cube_.cube_state["green"][8]:
                    _move.append(["L", "R", "D2", "Lp", "Rp"])
                ####BETA####
                return [[item for sublist in _move for item in sublist]]

            # do D2
            # should now have 2 permuted next to each other:
            # go to alpha with D2 as set up move

            else:
                __cube__ = do_scramble(["D2"], self)
                _move.append(["D2"])
                ####ALPHA####
                # do R,D,Rp,Dp,R with one of the non-permuted faces in right layer
                # green front
                if __cube__.cross_permuted() == [2, 3]:
                    _move.append(["R", "D", "Rp", "Dp", "R"])
                # orange front
                elif __cube__.cross_permuted() == [0, 3]:
                    _move.append(["B", "D", "Bp", "Dp", "B"])
                # blue front
                elif __cube__.cross_permuted() == [0, 1]:
                    _move.append(["L", "D", "Lp", "Dp", "L"])
                # red front
                elif __cube__.cross_permuted() == [1, 2]:
                    _move.append(["F", "D", "Fp", "Dp", "F"])
                ####ALPHA####insert
                return [[item for sublist in _move for item in sublist]]

        # ALPHA
        # if not all 4 oriented and 2 permuted next to each other:
        if (
            self.get_edge_count()["white"] == 4
            and not self.cross_oriented()
            and (len(self.cross_permuted()) == 2)
            and ((self.cross_permuted()[1] - self.cross_permuted()[0] == 1) % 2)
        ):
            # do R,D,Rp,Dp,R with one of the non-permuted faces in right layer
            # green front
            if self.cross_permuted() == [2, 3]:
                _move.append(["R", "D", "Rp", "Dp", "R"])
            # orange front
            elif self.cross_permuted() == [0, 3]:
                _move.append(["B", "D", "Bp", "Dp", "B"])
            # blue front
            elif self.cross_permuted() == [0, 1]:
                _move.append(["L", "D", "Lp", "Dp", "L"])
            # red front
            elif self.cross_permuted() == [1, 2]:
                _move.append(["F", "D", "Fp", "Dp", "F"])
            return _move

        # BETA
        # if not all 4 oriented and 2 permuted across each other:
        if (
            self.get_edge_count()["white"] == 4
            and not self.cross_oriented()
            and (len(self.cross_permuted()) == 2)
            and ((self.cross_permuted()[1] - self.cross_permuted()[0] == 2) % 2)
        ):
            # do F,B,D2, Fp, Bp with one of the non-permuted faces in right layer
            # green front
            if self.cube_state["orange"][5] != self.cube_state["orange"][8]:
                _move.append(["F", "B", "D2", "Fp", "Bp"])

            # red front
            elif self.cube_state["green"][5] != self.cube_state["green"][8]:
                _move.append(["L", "R", "D2", "Lp", "Rp"])
            return _move

        # in all of these cases, how do i translate the algo to othe rfaces, i think just hard code lol for the 4 cases
        # idealy would do "x"/"y"/"z", do algo, then un "x"/"y"/"z"
        # R --> B --> L --> F
        # F --> R --> B --> L
        # or i do F on layer and thrrow into my solver from prior cross types

        # could have determed if any oriented next to each other and then applied algo then D moves

        # i guess i could have gotten edges in white layer and then did one of the above, but it would be less efficient, but i thought of this in beginning with 3-cycle


class CrossSolver:
    """
    This class solves the cross. It relies on the TreeNode class.
    """

    def __init__(self):
        self.solutions = []

    def treeify(self, cube, cur_moves):
        from .helpers import (
            do_scramble,
            sanitize,
        )  # if put at top of file, will create circular import errors, eventually need to restructure

        _combo_dict = {
            "_seven_type": "seven_type_cross_solver",
            "_three_type": "three_type_cross_solver",
            "_one_type": "one_type_cross_solver",
            "_top_type": "top_type_cross_solver",
            "_five_type": "five_type_cross_solver",
        }

        _combo = cube.combo()
        _combo_list = []
        for i in _combo:
            _combo_list.append(i[0])

        level = []
        for _combo_type in _combo_list:
            if _combo_type != "bottum_type":
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
                if _new_cube_combo_list.count("bottum_type") == 4:
                    _all_moves = []
                    for move_set in cur_moves + [c.val]:
                        for sub_move in move_set:
                            _all_moves.append(sub_move)
                    final_set_of_moves = _new_cube.bottum_type_cross_solver()
                    if final_set_of_moves is None:  # invesitage this
                        final_set_of_moves = [["I"]]
                        pass
                    self.solutions.append(_all_moves + final_set_of_moves[0])
                    self.solutions = sanitize(self.solutions)
                else:
                    _all_moves = []
                    for move_set in cur_moves + [c.val]:
                        for sub_move in move_set:
                            _all_moves.append(sub_move)
                    if len(_all_moves) <= 6:
                        self.treeify(
                            _new_cube, cur_moves + [c.val]
                        )  # should we return solutions?

        # case for just cross solver only
        if _combo_list.count("bottum_type") == 4:
            final_set_of_moves = cube.bottum_type_cross_solver()
            if final_set_of_moves is None:  # invesitage this
                final_set_of_moves = [["I"]]
                pass
            self.solutions.append(final_set_of_moves[0])  # should we return solutions?
            self.solutions = sanitize(self.solutions)
