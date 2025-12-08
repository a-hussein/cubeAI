

class CrossSetupForSolverMixin:
    """
    This class provides functions used as set up for the CrossSolverMixin class.
    """

    def combo(self):
        cross_dict = self.identify_cross_edge_type()

        _combo = []
        _combos = [[]] * 4
        for i, _type in enumerate(cross_dict):
            for face_with_white_edge in list(
                cross_dict[i][list(cross_dict[i].keys())[0]].keys()
            ):
                _combo.append(list(cross_dict[i].keys())[0])
                _combo.append(face_with_white_edge)
                _combo.append(
                    list(cross_dict[i].values())[0].get(face_with_white_edge)[0]
                )
                _combo.append(
                    list(cross_dict[i].values())[0].get(face_with_white_edge)[1]
                )

        _combos[0] = _combo[0:4]
        _combos[1] = _combo[4:8]
        _combos[2] = _combo[8:12]
        _combos[3] = _combo[12:16]

        return _combos

    def seven_three_orientation_delta(self, i, j):
        g, r, b, o = 0, 1, 2, 3
        color_mapping = {"g": g, "r": r, "b": b, "o": o}

        bottum_mapping = {0: ["I"], 1: ["Dp"], 2: ["D2"], 3: ["D"]}
        top_mapping = {0: ["I"], 1: ["U"], 2: ["U2"], 3: ["Up"]}

        _combo = self.combo()

        # this is an edge case when we are doing U_delta for one_type/five_type for seven/three
        if _combo[j][2] == "y" or _combo[j][2] == "w":
            layer_delta = (
                color_mapping[_combo[i][2]] - color_mapping[_combo[j][1][0]]
            )  # need face of one_type/five_type
        else:
            layer_delta = color_mapping[_combo[i][2]] - color_mapping[_combo[j][2]]

        sticker_delta = (
            color_mapping[_combo[i][3]] - color_mapping[_combo[j][3]]
        )  # an edge type for y/w edge case is not needed because sticker will not be yellow or white for this release on sticker_delta

        tops = ["_top_type", "_one_type"]
        bottums = ["_five_type", "bottum_type"]

        # D delta
        if _combo[j][0] in bottums:
            new_delta = 0
            # for seven/three to bottum
            if _combo[j][0] == "bottum_type":
                if layer_delta != sticker_delta:
                    new_delta = (layer_delta - sticker_delta) % 4
                    return bottum_mapping[new_delta]
                else:
                    return [
                        "I"
                    ]  # added for case when delta are the same and thus no move needed
            # for seven and three for five
            elif _combo[j][0] == "_five_type":
                new_delta = (layer_delta) % 4
                return bottum_mapping[new_delta]
        # U delta
        # for seven/three to top/one
        elif _combo[j][0] in tops:
            new_delta = (layer_delta) % 4
            return top_mapping[new_delta]

    def combine_seven_three_orientation_delta(self, i, j, k):
        if (
            self.seven_three_orientation_delta(i, j) is not None
            and self.seven_three_orientation_delta(i, k) is not None
        ):
            return self.seven_three_orientation_delta(
                i, j
            ) + self.seven_three_orientation_delta(i, k)
        elif self.seven_three_orientation_delta(i, j) is not None:
            return self.seven_three_orientation_delta(i, j)
        elif self.seven_three_orientation_delta(i, k) is not None:
            return self.seven_three_orientation_delta(i, k)
        else:
            return ["I"]
        # this way we can give one type/top/bottum scenario and return combined top/bottum set up moves

    def one_orientation_delta(self, i, j):
        # anywhere it says "either, not both... it should be in the form of [[alpha], [beta]]... not [alpha, beta]"
        g, r, b, o = 0, 1, 2, 3
        color_mapping = {"g": g, "r": r, "b": b, "o": o}

        bottum_mapping = {0: ["I"], 1: ["Dp"], 2: ["D2"], 3: ["D"]}

        _combo = self.combo()

        # this is an edge case when we are doing D_delta for five_type for top/one
        if (_combo[i][2] == "y" or _combo[i][2] == "w") and (
            _combo[j][2] == "y" or _combo[j][2] == "w"
        ):  # one to five case
            layer_delta = (
                color_mapping[_combo[i][1][0]] - color_mapping[_combo[j][1][0]]
            )  # need face because that will tell me layer of one_type/five_type
        elif _combo[j][2] == "y" or _combo[j][2] == "w":
            layer_delta = (
                color_mapping[_combo[i][2]] - color_mapping[_combo[j][1][0]]
            )  # need face because that will tell me layer of one_type/five_type

        elif _combo[i][2] == "y" or _combo[i][2] == "w":
            layer_delta = (
                color_mapping[_combo[i][1][0]] - color_mapping[_combo[j][2]]
            )  # need face because that will tell me layer of one_type/five_type
        else:
            layer_delta = color_mapping[_combo[i][2]] - color_mapping[_combo[j][2]]

        # an edge type for y/w edge case is not needed because sticker will not be yellow or white for this release on sticker_delta
        # sticker_delta = (
        #     color_mapping[_combo[i][3]] - color_mapping[_combo[j][3]]
        # )

        # tops = ["_top_type", "_one_type"]
        bottums = ["_five_type", "bottum_type"]

        # D delta
        res = ["I"]
        if _combo[j][0] in bottums:
            new_delta = 0
            # for one to bottum (the logic here will be to clear the bottum (provide both one move away if already there, else do nothing, and then do F or Fp, provide both and let tree decide))
            if _combo[j][0] == "bottum_type":
                if layer_delta == 0:
                    #                 new_delta = (layer_delta - sticker_delta)%4
                    #                 return bottum_mapping[new_delta]
                    res = ["D", "Dp"]  # either, not both
                else:
                    res = [
                        "I"
                    ]  # added for case when delta are the same and thus no move needed; dont need to do anything becuase it will happen in seven/three
            # just bring to right location
            # for top and one to five (bring under when doing F swing)
            elif _combo[j][0] == "_five_type":
                new_delta = (layer_delta) % 4
                res = bottum_mapping[new_delta]
            # just bring it under it, the solver will do both moves aand add to trie and see what is better
        return res
        # no U delta

    def top_orientation_delta(self, i, j):
        g, r, b, o = 0, 1, 2, 3
        color_mapping = {"g": g, "r": r, "b": b, "o": o}

        bottum_mapping = {0: ["I"], 1: ["Dp"], 2: ["D2"], 3: ["D"]}

        _combo = self.combo()

        # this is an edge case when we are doing D_delta for five_type for top/one
        if _combo[j][2] == "y" or _combo[j][2] == "w":
            layer_delta = (
                color_mapping[_combo[i][2]] - color_mapping[_combo[j][1][0]]
            )  # need face because that will tell me layer of one_type/five_type
        else:
            layer_delta = color_mapping[_combo[i][2]] - color_mapping[_combo[j][2]]

        sticker_delta = (
            color_mapping[_combo[i][3]] - color_mapping[_combo[j][3]]
        )  # an edge type for y/w edge case is not needed because sticker will not be yellow or white for this release on sticker_delta

        # tops = ["_top_type", "_one_type"]
        bottums = ["_five_type", "bottum_type"]

        # D delta
        res = ["I"]
        if _combo[j][0] in bottums:
            new_delta = 0
            # for top to bottum
            if _combo[j][0] == "bottum_type":
                if layer_delta != sticker_delta:
                    new_delta = (
                        layer_delta - sticker_delta
                    ) % 4  # for now, keeping same logic of seven/three and moving to corrrect orientation, and not following one_type logic and just moving to either side... might revist if need be?
                    res = bottum_mapping[new_delta]
                else:
                    res = [
                        "I"
                    ]  # added for case when delta are the same and thus no move needed
            # just bring to right location
            # for top and one to five
            elif _combo[j][0] == "_five_type":
                new_delta = (layer_delta) % 4
                res = bottum_mapping[new_delta]
            # just bring it under it, the solver will do both moves aand add to trie and see what is better
        return res
        # no U delta

    def five_orientation_delta(self, i, j):
        # anywhere it says "either, not both... it should be in the form of [[alpha], [beta]]... not [alpha, beta]"
        g, r, b, o = 0, 1, 2, 3
        color_mapping = {"g": g, "r": r, "b": b, "o": o}

        # bottum_mapping = {0: ["I"], 1: ["Dp"], 2: ["D2"], 3: ["D"]}
        top_mapping = {0: ["I"], 1: ["U"], 2: ["U2"], 3: ["Up"]}

        _combo = self.combo()

        # this is an edge case when we are doing D_delta for five_type for top/one
        if (_combo[i][2] == "y" or _combo[i][2] == "w") and (
            _combo[j][2] == "y" or _combo[j][2] == "w"
        ):  # one to five case
            layer_delta = (
                color_mapping[_combo[i][1][0]] - color_mapping[_combo[j][1][0]]
            )  # need face because that will tell me layer of one_type/five_type
        elif _combo[j][2] == "y" or _combo[j][2] == "w":
            layer_delta = (
                color_mapping[_combo[i][2]] - color_mapping[_combo[j][1][0]]
            )  # need face because that will tell me layer of one_type/five_type

        elif _combo[i][2] == "y" or _combo[i][2] == "w":
            layer_delta = (
                color_mapping[_combo[i][1][0]] - color_mapping[_combo[j][2]]
            )  # need face because that will tell me layer of one_type/five_type
        else:
            layer_delta = color_mapping[_combo[i][2]] - color_mapping[_combo[j][2]]

        # an edge type for y/w edge case is not needed because sticker will not be yellow or white for this release on sticker_delta
        # sticker_delta = (
        #     color_mapping[_combo[i][3]] - color_mapping[_combo[j][3]]
        # )

        tops = ["_top_type", "_one_type"]
        # bottums = ["_five_type", "bottum_type"]

        # no D delta
        res = ["I"]
        # U delta
        if _combo[j][0] in tops:
            new_delta = (layer_delta) % 4
            res = top_mapping[new_delta]

        return res

    def bottum_orientation_delta(self):
        # only use this function when cross is oriented

        if self.cross_oriented():
            g, r, b, o = 0, 1, 2, 3
            color_mapping = {"g": g, "r": r, "b": b, "o": o}

            bottum_mapping = {0: ["I"], 1: ["Dp"], 2: ["D2"], 3: ["D"]}

            _combo = self.combo()

            sticker_delta = (
                color_mapping[self.cube_state["green"][5]]
                - color_mapping[self.cube_state["green"][8]]
            )  # an edge type for y/w edge case is not needed because sticker will not be yellow or white for this release on sticker_delta

            return bottum_mapping[sticker_delta]

        else:
            return None


class TreeNode:
    """
    This class is used to support the CrossSolver class.
    """

    def __init__(self, val):
        self.val = val
        self.children = []
