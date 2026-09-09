# Phase 0 Diagnostic

## 1. Invert this matrix by hand

```
| 1 2 3 |
| 0 1 4 |
| 5 6 0 |
```

**First attempt:** computed the transpose instead of the inverse.

```
| 1 0 5 |
| 2 1 6 |
| 3 4 0 |
```

**Correct answer (the actual inverse):**

```
| -24  18   5 |
|  20 -15  -4 |
|  -5   4   1 |
```

**Gap identified:** confused transpose (reshuffle rows/columns) with inverse (the matrix A⁻¹ such that A · A⁻¹ = identity). Real gap, not a slip — needs Phase 1's linear algebra work from the start, not as a refresher.

## 2. What does a derivative measure?

**First attempt:** "a way of transforming a function unto its previous state" — this actually describes what an *integral* does, not a derivative.

**Correct intuition:** a derivative measures the rate of change of a function's output relative to a tiny change in its input — the slope of the tangent line at a point.

**Gap identified:** derivative/integral intuition not solid yet.

## 3. Write a function that computes a CSV column's mean, no pandas

Started with zero Python recall — no `open()`, `.split()`, loops, or functions. Built it correctly step by step, with zero wrong outputs along the way, once each piece was introduced. Final result: see `phase0/column_mean.py`.

**Verdict:** no syntax recall going in, but fast, error-free pickup once shown each piece — the gap here is unfamiliarity, not difficulty understanding.

## Overall verdict

Real starting point is beginner in both math and code, not "Python + some math" as first self-reported. That's fine — it's common for rusty knowledge to feel more solid than it is until something actually tests it.

**What this changes:** Phase 1's math is a full first pass, not a quick refresher. Python keeps being learned by building real things step by step — that's what worked here — not a separate course.
