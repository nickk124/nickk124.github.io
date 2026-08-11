---
layout: page
permalink: /borsuk/
title: A 63-dimensional counterexample to Borsuk's conjecture
description: A new, smaller counterexample to Borsuk's conjecture, found with Claude
nav: true
nav_order: 3
---

In August 2026 I asked Claude to try to work on unsolved problems in mathematics. It found a new counterexample to [Borsuk's conjecture](https://en.wikipedia.org/wiki/Borsuk%27s_conjecture): 321 points in $$\mathbb{R}^{63}$$ that cannot be partitioned into 64 subsets of smaller diameter. This is the smallest dimension in which the conjecture is now known to fail, beating the previous record of dimension 64 ([Jenrich, 2014](https://arxiv.org/abs/1308.0206)), and closing a gap that had stood open for $$4 \le n \le 63$$.

This result has not been peer-reviewed or published yet. The paper below documents the full construction, and everything it depends on can be independently re-derived with the one-command verifier further down this page. I'd encourage you to run it rather than take Claude's word for it.

## Abstract

> We exhibit a set of 321 points in $$\mathbb{R}^{63}$$ that cannot be partitioned into 64 subsets of smaller diameter, so Borsuk's conjecture fails in dimension 63. The previous smallest counterexample was in dimension 64 (Jenrich, 2014), and the conjecture was open for $$4 \le n \le 63$$. The construction adds a single point to the 320-point rank-63 subconfiguration of Bondarenko's two-distance set, whose counting bound has been stuck at exactly $$\lceil 320/5 \rceil = 64$$ parts. The added point is not a vertex of the underlying strongly regular graph, so the resulting set is a three-distance set; this is precisely why the example was not reachable inside the two-distance framework in which all previous work took place.

<div style="margin: 1.5rem 0;">
  <a href="{{ '/assets/pdf/borsuk63.pdf' | relative_url }}" class="btn btn-sm z-depth-0" role="button">Download PDF</a>
</div>

<div style="border: 1px solid var(--global-divider-color, #ccc); border-radius: 8px; overflow: hidden; margin-bottom: 1.5rem;">
  <object data="{{ '/assets/pdf/borsuk63.pdf' | relative_url }}" type="application/pdf" width="100%" style="height: 80vh; display: block;">
    <p style="padding: 1rem;">
      Your browser can't display the PDF inline.
      <a href="{{ '/assets/pdf/borsuk63.pdf' | relative_url }}">Download it here</a> instead.
    </p>
  </object>
</div>

## Verify it yourself

The point set is 321 &times; 63 coordinates, provided as both a NumPy array and a plain CSV. The verifier below depends on nothing but NumPy, reads only the point set, and re-derives the affine dimension, the distance spectrum, the diameter, the independence number of the diameter graph, and the counting bound:

```bash
python verify63.py
```

Expected output ends with:

```
VERIFIED: Borsuk fails in R^63
```

Files:
- [`verify63.py`]({{ '/assets/borsuk/verify63.py' | relative_url }})
- [`borsuk63_points.npy`]({{ '/assets/borsuk/borsuk63_points.npy' | relative_url }}) (NumPy array, 321 &times; 63)
- [`borsuk63_points.csv`]({{ '/assets/borsuk/borsuk63_points.csv' | relative_url }}) (same data, plain text)

The paper also describes an exact-arithmetic certificate (over $$\mathbb{Q}$$ and $$\mathbb{Q}(\sqrt{222})$$) that re-establishes every load-bearing claim without floating point, cross-checked against an independent CP-SAT solve. That code will be linked here once its repository is public.
