from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Literal


class EdgeType(str, Enum):
    SEVEN = "_seven_type"
    THREE = "_three_type"
    ONE = "_one_type"
    TOP = "_top_type"
    FIVE = "_five_type"
    BOTTOM = "bottum_type"


@dataclass(frozen=True)
class EdgeCase:
    edge_type: EdgeType
    white_face: str
    adjacent_face_color: str
    sticker_color: str

    def as_legacy(self) -> list[str]:
        return [
            self.edge_type.value,
            self.white_face,
            self.adjacent_face_color,
            self.sticker_color,
        ]


COLOR_INDEX = {"g": 0, "r": 1, "b": 2, "o": 3}
BOTTOM_DELTA_TO_MOVE = {0: ["I"], 1: ["Dp"], 2: ["D2"], 3: ["D"]}
TOP_DELTA_TO_MOVE = {0: ["I"], 1: ["U"], 2: ["U2"], 3: ["Up"]}
TOP_EDGE_TYPES = {EdgeType.TOP, EdgeType.ONE}
BOTTOM_EDGE_TYPES = {EdgeType.FIVE, EdgeType.BOTTOM}


class CrossSetupForSolverMixin:
    """
    Setup helpers used by the cross solver.

    These methods classify white-edge cases and compute orientation setup moves.
    """

    def _combo_cases(self) -> list[EdgeCase]:
        cross_dict = self.identify_cross_edge_type()
        cases: list[EdgeCase] = []
        for item in cross_dict:
            edge_name, by_face = next(iter(item.items()))
            for face_with_white_edge, (adj_color, sticker_color) in by_face.items():
                cases.append(
                    EdgeCase(
                        edge_type=EdgeType(edge_name),
                        white_face=face_with_white_edge,
                        adjacent_face_color=adj_color,
                        sticker_color=sticker_color,
                    )
                )
        return cases

    def combo(self):
        """
        Legacy `combo` shape used by downstream solver code and tests.
        """

        combos = [case.as_legacy() for case in self._combo_cases()]
        while len(combos) < 4:
            combos.append([])
        return combos[:4]

    @staticmethod
    def _is_white_or_yellow(color: str) -> bool:
        return color in {"w", "y"}

    def _compute_layer_delta(
        self,
        source: EdgeCase,
        target: EdgeCase,
        mode: Literal["target_aware", "both_aware"],
    ) -> int:
        if mode == "target_aware":
            if self._is_white_or_yellow(target.adjacent_face_color):
                source_ref = source.adjacent_face_color
                target_ref = target.white_face[0]
            else:
                source_ref = source.adjacent_face_color
                target_ref = target.adjacent_face_color
            return COLOR_INDEX[source_ref] - COLOR_INDEX[target_ref]

        if self._is_white_or_yellow(source.adjacent_face_color) and self._is_white_or_yellow(
            target.adjacent_face_color
        ):
            source_ref = source.white_face[0]
            target_ref = target.white_face[0]
        elif self._is_white_or_yellow(target.adjacent_face_color):
            source_ref = source.adjacent_face_color
            target_ref = target.white_face[0]
        elif self._is_white_or_yellow(source.adjacent_face_color):
            source_ref = source.white_face[0]
            target_ref = target.adjacent_face_color
        else:
            source_ref = source.adjacent_face_color
            target_ref = target.adjacent_face_color
        return COLOR_INDEX[source_ref] - COLOR_INDEX[target_ref]

    @staticmethod
    def _compute_sticker_delta(source: EdgeCase, target: EdgeCase) -> int:
        return COLOR_INDEX[source.sticker_color] - COLOR_INDEX[target.sticker_color]

    @staticmethod
    def _bottom_move(delta: int) -> list[str]:
        return BOTTOM_DELTA_TO_MOVE[delta % 4]

    @staticmethod
    def _top_move(delta: int) -> list[str]:
        return TOP_DELTA_TO_MOVE[delta % 4]

    def seven_three_orientation_delta(self, i, j):
        cases = self._combo_cases()
        source = cases[i]
        target = cases[j]

        layer_delta = self._compute_layer_delta(source, target, mode="target_aware")
        sticker_delta = self._compute_sticker_delta(source, target)

        if target.edge_type in BOTTOM_EDGE_TYPES:
            if target.edge_type == EdgeType.BOTTOM:
                if layer_delta != sticker_delta:
                    return self._bottom_move(layer_delta - sticker_delta)
                return ["I"]
            if target.edge_type == EdgeType.FIVE:
                return self._bottom_move(layer_delta)
            return None

        if target.edge_type in TOP_EDGE_TYPES:
            return self._top_move(layer_delta)
        return None

    def combine_seven_three_orientation_delta(self, i, j, k):
        left = self.seven_three_orientation_delta(i, j)
        right = self.seven_three_orientation_delta(i, k)

        merged: list[str] = []
        if left is not None:
            merged.extend(left)
        if right is not None:
            merged.extend(right)
        return merged if merged else ["I"]

    def one_orientation_delta(self, i, j):
        # "either, not both" is represented as e.g. ["D", "Dp"]
        cases = self._combo_cases()
        source = cases[i]
        target = cases[j]

        layer_delta = self._compute_layer_delta(source, target, mode="both_aware")
        result = ["I"]

        if target.edge_type in BOTTOM_EDGE_TYPES:
            if target.edge_type == EdgeType.BOTTOM:
                if layer_delta == 0:
                    result = ["D", "Dp"]
                else:
                    result = ["I"]
            elif target.edge_type == EdgeType.FIVE:
                result = self._bottom_move(layer_delta)
        return result

    def top_orientation_delta(self, i, j):
        cases = self._combo_cases()
        source = cases[i]
        target = cases[j]

        layer_delta = self._compute_layer_delta(source, target, mode="target_aware")
        sticker_delta = self._compute_sticker_delta(source, target)
        result = ["I"]

        if target.edge_type in BOTTOM_EDGE_TYPES:
            if target.edge_type == EdgeType.BOTTOM:
                if layer_delta != sticker_delta:
                    result = self._bottom_move(layer_delta - sticker_delta)
                else:
                    result = ["I"]
            elif target.edge_type == EdgeType.FIVE:
                result = self._bottom_move(layer_delta)
        return result

    def five_orientation_delta(self, i, j):
        # "either, not both" is represented as e.g. ["F", "Fp"]
        cases = self._combo_cases()
        source = cases[i]
        target = cases[j]

        layer_delta = self._compute_layer_delta(source, target, mode="both_aware")
        result = ["I"]
        if target.edge_type in TOP_EDGE_TYPES:
            result = self._top_move(layer_delta)
        return result

    def bottom_orientation_delta(self):
        # only use this function when cross is oriented
        if not self.cross_oriented():
            return None

        sticker_delta = (
            COLOR_INDEX[self.cube_state["green"][5]]
            - COLOR_INDEX[self.cube_state["green"][8]]
        )
        return BOTTOM_DELTA_TO_MOVE[sticker_delta % 4]

    def bottum_orientation_delta(self):
        # backward-compatible typo alias
        return self.bottom_orientation_delta()


@dataclass
class TreeNode:
    """
    Support node used by the cross-solver search tree.
    """

    val: Any
    children: list["TreeNode"] = field(default_factory=list)
