"""Stand-alone verifier for the 63-dimensional Borsuk counterexample.

Reads ONLY the saved point set (data/borsuk63_points.npy, 321 x 63 real
coordinates) and re-derives everything from the coordinates themselves:
no graph, no eigenvectors, no construction code.  This is the artifact a
referee runs.

  python -m borsuk.verify63            # verify
  python -m borsuk.verify63 --dump     # (re)build the point file
"""
import json
import os
import sys

import numpy as np

DDIR = os.path.join(os.path.dirname(__file__), "data")
PTS = os.path.join(os.path.dirname(__file__), "borsuk63_points.npy")
CERT = os.path.join(DDIR, "borsuk63_certificate.json")


def dump(plane=0):
    """Rebuild the point set from the construction and save it."""
    pass
    pass
    pass
    A = get_A()
    U = eigen_coords(A)
    W_all, _, _ = unions_96(A)
    W = sorted(W_all[plane])
    S = np.array(sorted(set(range(416)) - set(W)))
    x0 = W[0]
    y, nv2, mu = phantom(U, S, x0)
    X65 = np.vstack([U[S, :], y[None, :]])
    # rotate into the 63 dimensions it actually spans
    Uu, sv, Vt = np.linalg.svd(X65, full_matrices=False)
    k = int((sv > 1e-9).sum())
    X = Uu[:, :k] * sv[:k]
    np.save(PTS, X)
    cert = {
        "claim": "Borsuk's conjecture fails in R^63",
        "graph": "G2(4) graph, SRG(416,100,36,20), data/g24_adj.npy",
        "eigenspace": "r = 20, multiplicity 65, Gram = E_r",
        "gram_values": {"norm2": "5/32", "adjacent": "1/32",
                        "nonadjacent": "-1/96"},
        "witness_plane_index": plane,
        "W_support_96": W,
        "S_zero_set_320": S.tolist(),
        "phantom_source_x0": int(x0),
        "phantom_v_norm2": "13/96",
        "phantom_mu": "(-1 + sqrt(222))/13",
        "distances2": {"phantom_to_neighbours_of_x0": "(53 - sqrt(222))/156",
                       "adjacent_in_S": "1/4", "diameter": "1/3"},
        "npoints": int(X.shape[0]), "dim": int(X.shape[1]),
        "alpha_diameter_graph": 5,
        "parts_needed": 65, "parts_allowed_by_borsuk": 64,
    }
    with open(CERT, "w") as f:
        json.dump(cert, f, indent=1)
    print(f"saved {X.shape} -> {PTS}\nsaved certificate -> {CERT}")


def max_clique_bits(adj_bits, n):
    best = 0

    def expand(R, P, X):
        nonlocal best
        if not P and not X:
            best = max(best, R)
            return
        if R + bin(P).count("1") <= best:
            return
        PX = P | X
        pivot, pbest = -1, -1
        m = PX
        while m:
            v = (m & -m).bit_length() - 1
            m &= m - 1
            c = bin(P & adj_bits[v]).count("1")
            if c > pbest:
                pivot, pbest = v, c
        m = P & ~adj_bits[pivot]
        while m:
            v = (m & -m).bit_length() - 1
            m &= m - 1
            expand(R + 1, P & adj_bits[v], X & adj_bits[v])
            P &= ~(1 << v)
            X |= (1 << v)

    expand(0, (1 << n) - 1, 0)
    return best


def main():
    X = np.load(PTS)
    n, d = X.shape
    print(f"loaded {n} points in R^{d}")
    ok = True

    sv = np.linalg.svd(X - X.mean(0), compute_uv=False)
    adim = int((sv > 1e-9 * sv[0]).sum())
    print(f"  affine dimension: {adim}")
    ok &= (adim == d == 63)

    D2 = (np.sum(X * X, 1)[:, None] + np.sum(X * X, 1)[None, :]
          - 2 * X @ X.T)
    np.fill_diagonal(D2, 0.0)
    iu = np.triu_indices(n, 1)
    vals, cnts = np.unique(np.round(D2[iu], 9), return_counts=True)
    print(f"  squared-distance spectrum: "
          f"{dict(zip(vals.tolist(), cnts.tolist()))}")
    ok &= (D2[iu].min() > 1e-9)                      # points distinct
    b2 = D2[iu].max()
    print(f"  diameter^2 = {b2:.12f}")

    # diameter graph: pairs at (numerically) maximal distance
    far = (D2 > b2 - 1e-7)
    np.fill_diagonal(far, False)
    near = (~far)
    np.fill_diagonal(near, False)
    bits = [int("".join("1" if near[i, j] else "0"
                        for j in range(n - 1, -1, -1)), 2) for i in range(n)]
    alpha = max_clique_bits(bits, n)                 # alpha(far) = omega(near)
    print(f"  independence number of the diameter graph: {alpha}")
    parts = -(-n // alpha)
    print(f"  every smaller-diameter part has <= {alpha} points "
          f"-> at least ceil({n}/{alpha}) = {parts} parts")
    print(f"  Borsuk's conjecture in R^{d} allows {d + 1} parts")
    ok &= (parts > d + 1)
    print(f"\n{'VERIFIED: Borsuk fails in R^%d' % d if ok else 'FAILED'}")
    return 0 if ok else 1


if __name__ == "__main__":
    if "--dump" in sys.argv:
        dump()
        sys.exit(0)
    sys.exit(main())
