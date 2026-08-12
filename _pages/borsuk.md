---
layout: page
permalink: /borsuk/
title: Claude Tackles Borsuk
description: Claude independently rediscovers Grinsztajn's 63-dimensional counterexample to Borsuk's Conjecture (1933) — plus a new exact certificate and an obstruction at 62
nav: true
nav_order: 3
---

<div style="border-left: 4px solid #d9822b; background: rgba(217,130,43,0.08); padding: 0.9rem 1.1rem; border-radius: 4px; margin-bottom: 1.5rem;">
<strong>Update, August 12, 2026:</strong> This exact counterexample — 321 points in \(\mathbb{R}^{63}\) — was already found by <a href="https://github.com/maaxgrin/borsuk-63-counterexample">Max Grinsztajn, working with GPT-5.5 Pro, in May 2026</a>, about two and a half months before this page went up, and is recorded as the current record on <a href="https://teorth.github.io/optimizationproblems/constants/28a.html">Terence Tao's optimization-problems tracker</a>. Claude's construction, worked out in August 2026 with no knowledge of Grinsztajn's note, turns out to be the identical object point for point, including the scalar. <strong>Priority for the counterexample belongs to Grinsztajn.</strong> What's new here is an independent exact-arithmetic certificate, a uniformity statement (the construction works for all 4,809 known witness planes and extends to up to 325 points), and an analysis of why this approach stops at dimension 63 and can't reach 62 — see "Priority and independence" in the paper below for the full account.
</div>

In August 2026 I asked Claude to try to work on unsolved problems in mathematics. It produced a 321-point counterexample to [Borsuk's conjecture](https://en.wikipedia.org/wiki/Borsuk%27s_conjecture) in $$\mathbb{R}^{63}$$ — independently arriving at the same construction Max Grinsztajn had already published two and a half months earlier (see the notice above for attribution).

This result has not been peer-reviewed or published. The paper below documents the full construction, and everything it depends on can be independently re-derived with the one-command verifier further down this page. I'd encourage you to run it rather than take Claude's word for it.

## Abstract

> Borsuk's conjecture fails in dimension 63. This was established by Grinsztajn in May 2026, who exhibited a 321-point set in $$\mathbb{R}^{63}$$ every smaller-diameter subset of which has at most five points. The present note was produced independently in August 2026, in ignorance of that work, and arrives at the same construction: the 320-point rank-63 subconfiguration of Bondarenko's $$G_2(4)$$ two-distance set, whose counting bound ties at exactly $$\lceil 320/5 \rceil = 64$$ parts, together with one further point obtained by projecting a deleted vertex into the span and rescaling it by $$\mu = (-1+\sqrt{222})/13$$. The two constructions agree point for point, including the scalar, so we claim no priority for the counterexample. What we add is an independent exact certificate over $$\mathbb{Q}(\sqrt{222})$$, a uniformity statement (the construction works for every one of the 4,809 known witness planes, and admits up to 325 points), and a slack identity that explains why this method stops at 63 and what would have to be true for it to reach 62.

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

Grinsztajn's independent verification — which rebuilds the same graph from $$PG(2,16)$$ over $$\mathbb{F}_{16}$$, confirms the strongly regular parameters and the 96/320 split by disjoint code, and exports DIMACS certificates with an independent Sage cross-check — is in [his repository](https://github.com/maaxgrin/borsuk-63-counterexample). Between the two, the same object is now checked from the graph side and the metric side.
