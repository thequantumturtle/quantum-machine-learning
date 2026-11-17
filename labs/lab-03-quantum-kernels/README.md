# Lab 3 — Quantum Kernels and Classification

**Prepared by Daniel Justice · Carnegie Mellon University · 17-620 Quantum Machine Learning · Fall 2026**  
© 2026 Daniel Justice for original contributions; third-party materials retain their respective rights. Use and reuse are subject to applicable university policies.

**80 minutes · PennyLane · Ungraded practice — no submission required.**

## Our question

**We know how to compare quantum states. Can those similarities help make predictions?**

This guided lab extends Lab 2's quantum encoding and state overlap ideas. You will investigate two one-qubit feature maps on a small binary classification problem, inspect a fidelity kernel matrix, use it with a classical SVM, compare strong classical baselines, and explore how feature-map choices and measurement shots affect the results.

You do not need a quantum cloud account, hardware access, or any additional software beyond the course environment. **There is no graded lab submission.** Quizzes and homework have separate instructions and deadlines.

## Get started

1. Start Docker Desktop or the Docker Engine/Compose plugin.
2. Open a terminal at the **course student repository root** (`thequantumturtle/quantum-machine-learning`).
3. Update your checkout with `git pull` after saving any local work (or download a fresh course ZIP).
4. Run:

   ```bash
   docker compose up --build
   ```

5. Open the **tokenized** JupyterLab URL printed by Docker, commonly at `127.0.0.1:8888`.
6. In JupyterLab open `labs/lab-03-quantum-kernels/lab.ipynb`, and run cells from the top.

If the notebook is not yet in your checkout, it has not been released to students; use the copy your instructor distributes through the course.

## Timing

| Section | Time | Activity |
|---|---:|---|
| A | 10 min | Recall quantum fidelity and inspect a labeled dataset |
| B | 15 min | Feature maps and a six-point similarity heatmap |
| C | 20 min | Exact Gram matrix, quantum-kernel SVM, classical baselines |
| D | 20 min | Change the embedding and watch the decision boundary move |
| E | 10 min | Ideal finite-shot sampling and uncertainty |
| F | 5 min | Reflect and connect to variational classifiers |

The notebook includes optional experiments. If time is short, prioritize the worked examples and group discussion.

## Important scientific distinctions

- The quantum circuits in this lab are **simulated**, not submitted to real hardware.
- The circuit's feature map is fixed; a **classical SVM** learns the decision boundary.
- A successful hand-designed embedding does not demonstrate quantum speedup.
- The classical RBF kernel is an important comparator.
- Our finite-shot examples model ideal sampling, not the full effects of device noise.

## Troubleshooting

- **Module not found:** Use the course's Docker/Jupyter Python kernel, not an unrelated local Python environment.
- **Notebook widgets do not display:** Continue with the static plots and preset experiments; the widgets are optional.
- **The plots look wrong after editing:** Restart the kernel and run cells in order.
- **Docker cannot connect:** Start Docker Desktop or the Docker Engine and try again.
- **Port 8888 already in use:** Stop the competing server or use the alternative port guidance in the course README.

**Assessment:** This is an ungraded lab. You do not need to upload the notebook or written responses to Canvas.

