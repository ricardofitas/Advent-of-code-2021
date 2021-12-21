import numpy as np


def make_reports(inp):
    reports = inp.split('\n\n')
    scanners = []

    for rep in reports:
        values = np.array([[int(i) for i in line.split(',')] for line in rep.splitlines()[1:]])
        scanners.append(values)

    return scanners


def get_dists(scanners):
    all_dists = []
    for scan in scanners:
        dists = []
        for point in scan:
            dists.append(np.sum(np.abs(scan - point), axis=1))
        all_dists.append(dists)
    return all_dists


def find_one_overlap(scan0, scan1):
    for i, d0 in enumerate(all_dists[scan0]):
        for j, d1 in enumerate(all_dists[scan1]):
            overlaps = set(d0) & set(d1)
            if len(overlaps) >= 12:
                return i, j, overlaps


def find_positions(s0, s1, p0, p1, overlaps):
    pairs = []

    for d in overlaps:
        if d == 0: continue
        q0 = np.where(all_dists[s0][p0] == d)[0][0]
        q1 = np.where(all_dists[s1][p1] == d)[0][0]

        diff0 = scanners[s0][p0] - scanners[s0][q0]
        diff1 = scanners[s1][p1] - scanners[s1][q1]

        if len(set(np.abs(diff0))) < 3: continue

        order = []
        sign = []

        try:
            for i in range(3):
                idx = np.where(np.abs(diff1) == abs(diff0[i]))[0][0]
                order.append(idx)
                sign.append(diff1[idx] // diff0[i])
            print(order, sign)

            new_orient = scanners[s1][:, order] * np.array(sign)

        except:
            continue

        break

    scanner_pos = scanners[s0][p0] - new_orient[p1]
    new_coords = new_orient + scanner_pos

    return scanner_pos, new_coords


def find_all_scanners():
    found = {0}
    count = 1

    while count < len(scanners):
        s0 = found.pop()

        for i in range(len(scanners)):
            if scanner_positions[i] is not None: continue
            overlaps = find_one_overlap(s0, i)
            if not overlaps: continue
            print(s0, i)
            pos, coords = find_positions(s0, i, *overlaps)
            scanner_positions[i] = pos
            scanners[i] = coords
            found.add(i)
            count += 1


def find_all_beacons():
    beacons = set()

    for blist in scanners:
        beacons.update([tuple(pos) for pos in blist])

    return beacons

inp = open("__21_d19.txt").read()

scanners = make_reports(inp)

all_dists = get_dists(scanners)

scanner_positions = [None] * len(scanners)
scanner_positions[0] = np.array([0, 0, 0])

find_all_scanners()
beacons = find_all_beacons()

print(len(beacons))

maxi = 0

for s1 in scanner_positions:
    for s2 in scanner_positions:
        maxi = max(maxi, np.sum(np.abs(s1 - s2)))

print(maxi)