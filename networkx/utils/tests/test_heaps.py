from nose.tools import *
import networkx as nx
from networkx.utils import *

data = [('min', nx.NetworkXError),
        ('get', 20, None),
        ('get', 4, None),
        ('insert', 8, 45, True),
        ('insert', 10, 26, True),
        ('min', (10, 26)),
        ('insert', 7, 56, True),
        ('insert', 13, 62, True),
        ('min', (10, 26)),
        ('get', 7, 56),
        ('pop', (10, 26)),
        ('pop', (8, 45)),
        ('min', (7, 56)),
        ('insert', 19, 28, True),
        ('pop', (19, 28)),
        ('insert', 3, 13, True),
        ('min', (3, 13)),
        ('min', (3, 13)),
        ('min', (3, 13)),
        ('get', 17, None),
        ('insert', 4, 33, True),
        ('pop', (3, 13)),
        ('insert', 13, 79, False),
        ('get', 5, None),
        ('min', (4, 33)),
        ('insert', 16, 91, True),
        ('pop', (4, 33)),
        ('get', 11, None),
        ('min', (7, 56)),
        ('pop', (7, 56)),
        ('insert', 6, 55, True),
        ('min', (6, 55)),
        ('get', 16, 91),
        ('pop', (6, 55)),
        ('pop', (13, 79)),
        ('insert', 13, 94, True),
        ('insert', 7, 36, True),
        ('pop', (7, 36)),
        ('insert', 3, 82, True),
        ('min', (3, 82)),
        ('pop', (3, 82)),
        ('pop', (16, 91)),
        ('insert', 5, 54, True),
        ('insert', 14, 45, True),
        ('insert', 20, 89, True),
        ('min', (14, 45)),
        ('min', (14, 45)),
        ('pop', (14, 45)),
        ('min', (5, 54)),
        ('min', (5, 54)),
        ('min', (5, 54)),
        ('min', (5, 54)),
        ('insert', 2, 35, True),
        ('insert', 3, 71, True),
        ('get', 17, None),
        ('min', (2, 35)),
        ('pop', (2, 35)),
        ('get', 8, None),
        ('insert', 11, 98, True),
        ('insert', 9, 52, True),
        ('insert', 10, 45, True),
        ('insert', 4, 9, True),
        ('pop', (4, 9)),
        ('get', 9, 52),
        ('min', (10, 45)),
        ('get', 7, None),
        ('min', (10, 45)),
        ('insert', 16, 42, True),
        ('min', (16, 42)),
        ('insert', 6, 90, True),
        ('insert', 15, 16, True),
        ('insert', 11, 36, True),
        ('pop', (15, 16)),
        ('insert', 8, 91, True),
        ('insert', 10, 75, False),
        ('insert', 5, 77, False),
        ('pop', (11, 36)),
        ('insert', 20, 83, True),
        ('min', (16, 42)),
        ('insert', 15, 79, True),
        ('insert', 11, 55, True),
        ('min', (16, 42)),
        ('get', 19, None),
        ('min', (16, 42)),
        ('insert', 20, 42, True),
        ('min', (16, 42)),
        ('insert', 9, 34, True),
        ('pop', (9, 34)),
        ('get', 3, 71),
        ('get', 8, 91),
        ('min', (16, 42)),
        ('insert', 6, 4, True),
        ('pop', (6, 4)),
        ('min', (16, 42)),
        ('min', (16, 42)),
        ('get', 18, None),
        ('insert', 9, 74, True),
        ('pop', (16, 42)),
        ('insert', 15, 10, True),
        ('insert', 9, 100, False),
        ('pop', (15, 10)),
        ('pop', (20, 42)),
        ('insert', 20, 38, True),
        ('pop', (20, 38)),
        ('insert', 2, 78, True),
        ('insert', 14, 62, True),
        ('get', 8, 91),
        ('insert', 14, 12, True),
        ('insert', 18, 8, True),
        ('min', (18, 8)),
        ('pop', (18, 8)),
        ('get', 7, None),
        ('get', 17, None),
        ('pop', (14, 12)),
        ('insert', 2, 30, True),
        ('insert', 20, 53, True),
        ('min', (2, 30)),
        ('insert', 15, 71, True),
        ('insert', 13, 79, True),
        ('insert', 7, 23, True),
        ('insert', 7, 43, False),
        ('pop', (2, 30)),
        ('insert', 8, 65, True),
        ('min', (7, 43)),
        ('min', (7, 43)),
        ('min', (7, 43)),
        ('get', 20, 53),
        ('insert', 19, 41, True),
        ('get', 16, None),
        ('get', 14, None),
        ('pop', (19, 41)),
        ('pop', (7, 43)),
        ('pop', (20, 53)),
        ('insert', 10, 32, True),
        ('get', 16, None),
        ('insert', 6, 75, True),
        ('get', 5, 77),
        ('get', 13, 79),
        ('insert', 3, 91, False),
        ('min', (10, 32)),
        ('get', 8, 65),
        ('pop', (10, 32)),
        ('pop', (11, 55)),
        ('min', (8, 65)),
        ('pop', (8, 65)),
        ('insert', 11, 26, True),
        ('insert', 12, 30, True),
        ('insert', 13, 88, False),
        ('pop', (11, 26)),
        ('get', 10, None),
        ('pop', (12, 30)),
        ('pop', (15, 71)),
        ('min', (6, 75)),
        ('insert', 15, 22, True),
        ('min', (15, 22)),
        ('pop', (15, 22)),
        ('insert', 16, 75, True),
        ('insert', 19, 74, True),
        ('insert', 4, 89, True),
        ('insert', 19, 73, True),
        ('get', 1, None),
        ('insert', 6, 78, False),
        ('min', (19, 73)),
        ('pop', (19, 73)),
        ('get', 9, 100),
        ('insert', 16, 63, True),
        ('insert', 3, 70, True),
        ('get', 3, 70),
        ('min', (16, 63)),
        ('min', (16, 63)),
        ('min', (16, 63)),
        ('insert', 8, 43, True),
        ('pop', (8, 43)),
        ('insert', 18, 42, True),
        ('insert', 18, 45, False),
        ('get', 3, 70),
        ('insert', 13, 38, True),
        ('insert', 12, 68, True),
        ('insert', 4, 37, True),
        ('insert', 3, 40, True),
        ('insert', 20, 66, True),
        ('insert', 17, 3, True),
        ('get', 17, 3),
        ('insert', 1, 27, True),
        ('insert', 7, 6, True),
        ('pop', (17, 3)),
        ('pop', (7, 6)),
        ('min', (1, 27)),
        ('insert', 20, 43, True),
        ('insert', 3, 3, True),
        ('min', (3, 3)),
        ('insert', 12, 61, True),
        ('pop', (3, 3)),
        ('insert', 13, 74, False),
        ('pop', (1, 27)),
        ('insert', 4, 27, True),
        ('get', 1, None),
        ('insert', 18, 59, False),
        ('pop', (4, 27)),
        ('insert', 5, 100, False)]


def _test_heap_class(cls, *args, **kwargs):
    heap = cls(*args, **kwargs)
    for op in data:
        if op[-1] is not nx.NetworkXError:
            assert_equal(op[-1], getattr(heap, op[0])(*op[1:-1]))
        else:
            assert_raises(op[-1], getattr(heap, op[0]), *op[1:-1])

def test_PairingHeap():
    _test_heap_class(PairingHeap)


def test_BinaryHeap():
    _test_heap_class(BinaryHeap)