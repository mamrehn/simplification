# this tests numpy array simplification using RDP
# 216804 --> 3061 points (98.5% reduction)
# 50ms per VW operation on MBA Core i7

from simplification.cutil import simplify_coords
import json
import numpy as np

if __name__ == "__main__":
    with open("simplification/test/coords_complex.json", 'r') as f:
        coords = np.array(json.load(f))
    for x in xrange(50):
        simplify_coords(coords, 14.)
