from typing import List, Dict
from bisect import bisect_left

from tqdm import tqdm


class SegmentTree:
    """
    Segment Tree that can do insert and query a timestamp into/in interval tree [start, end]
    """

    def __init__(self, list_dict_items: List[Dict[str, str | int]]):
        """
        Args:
            list_dict_items: List of Dict
                for each Dict form with {id: name, start: start time, end: end time}

        """

        _points = []
        _points += [_item['start'] for _item in list_dict_items]
        _points += [_item['end'] for _item in list_dict_items]

        self.points = sorted(set(_points))
        self.n_points = len(self.points)

        self.tree = [[] for _ in range(2 * self.n_points)]

        for _item in tqdm(list_dict_items):
            self.insert(_item['id'], _item['start'], _item['end'])
        return

    def insert(self, item_id, start, end):
        start_idx = self.points.index(start)
        end_idx = self.points.index(end)

        start_idx += self.n_points
        end_idx += self.n_points + 1

        while start_idx < end_idx:
            if start_idx % 2 == 1:
                # right tree
                self.tree[start_idx].append(item_id)
                start_idx += 1

            if end_idx % 2 == 1:
                # left tree
                end_idx -= 1
                self.tree[end_idx].append(item_id)

            start_idx //= 2
            end_idx //= 2
        return

    def query(self, timestamp):
        if timestamp < self.points[0] or self.points[-1] < timestamp:
            # no hit (out of range)
            return set()

        idx = bisect_left(self.points, timestamp)
        # idx will in range [0, self.n_points)
        #   the case that idx equals to self.n_points was eleminate on above if-case

        if self.points[idx] == timestamp:
            # direct hit
            return self._query(idx)

        # idx will in range (0, self.n_points)
        #   the case that idx equals to 0 was eleminate on above two if-case

        s_left = self._query(idx - 1)
        s_right = self._query(idx)
        return s_left.intersection(s_right)

    def _query(self, idx):
        idx += self.n_points

        result = []
        while idx > 0:
            result.extend(self.tree[idx])
            idx //= 2
        return set(result)
