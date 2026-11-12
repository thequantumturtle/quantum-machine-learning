# Lab 2 — Quantum Encoding and Similarity

**Prepared by Daniel Justice · Carnegie Mellon University · 17-620 Quantum Machine Learning · Fall 2026**  
© 2026 Daniel Justice for original contributions; third-party materials retain their respective rights. Use and reuse are subject to applicable university policies.

**Duration:** 80 minutes. **Framework:** PennyLane (not Qiskit). **Ungraded practice — no submission required.**

In this lab you will compare classical cosine similarity with quantum squared-overlap kernels from angle and amplitude encodings. You will also estimate an overlap from finite-shot measurements and explain what a fixed quantum kernel does and does not optimize.

## Getting started

1. Install and start Docker Desktop, or Docker Engine with Compose.
2. Download or clone the **student** course repository.
3. Open a terminal in the repository root and run:

```bash
docker compose up --build
```

4. Open the **tokenized** localhost:8888 link shown in your terminal.
5. In JupyterLab, open `labs/lab-02-quantum-encoding/lab.ipynb` and work through the demonstrations and TODOs in order. The TODOs and discussion prompts are for practice; no completed notebook or written answers are collected.

For troubleshooting and updating your checkout, see the [course README](../../README.md).

**Note:** You need access to this GitHub repository (or the instructor's Canvas distribution). The Docker image is built locally; you do not need access to a private container registry or a quantum hardware account.

**Assessment note:** Lab 2 has no Canvas submission. Quizzes and Homework 1 are separate graded activities with their own instructions and deadlines.

## After-class review

Lab 2 is ungraded practice with no submission requirement. If your instructor releases a completed reference, find it in the **Canvas course**, not in this public repository. The practice notebook remains available here for future classes.
