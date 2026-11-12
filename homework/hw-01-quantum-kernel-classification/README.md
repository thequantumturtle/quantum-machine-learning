# Homework 1 — Quantum Kernel Classification

**Prepared by Daniel Justice · Carnegie Mellon University · 17-620 Quantum Machine Learning · Fall 2026**  
© 2026 Daniel Justice for original contributions; third-party materials retain their respective rights. Use and reuse are subject to applicable university policies.

**CMU 17-620 | Fall 2026 mini-2 | Instructor preview**

**Estimated effort:** 5–7 hours, including coding, testing, figures, and analysis.  
**Points:** 100. **Due date:** Assigned separately in the LMS.

## Driving question

**When we change the encoding, how does the resulting similarity change a classifier?**

This assignment extends Lab 2. Implement **two fixed quantum kernels** in PennyLane, train **classical SVMs** with their kernel matrices, compare classical baselines, and study finite-shot measurement error.

### How to work

Run the notebook top to bottom. After completing the code in each section, run the corresponding **checkpoint cell**. Checkpoints test feature-map shapes, known overlaps, kernel-matrix invariants, and SVM result structure. They provide immediate feedback but do not replace the written explanations or ensure every part of your model is scientifically meaningful.

If the notebook fails, read the first failing check before changing later sections. The private instructor notebook has completed solutions; do not assume a particular kernel must have the highest held-out accuracy.

### Submit

1. A completed starter notebook that runs from a clean kernel.
2. Figures and brief written responses embedded in the notebook.
3. A 300–500-word conclusion in the last Markdown cell.

Use the **same train/test split** for all models. Fit preprocessing on the training set only. Use a common SVM regularization setting. The existing Docker environment includes all necessary packages; no Qiskit or quantum hardware account is needed.

### Grading rubric

| Category | Points |
|---|---:|
| A. Explain data preprocessing and avoid leakage | 10 |
| B. Implement angle and amplitude overlap circuits | 25 |
| C. Build and validate kernel matrices | 20 |
| D. Train and evaluate quantum-kernel and classical baselines | 20 |
| E. Analyze finite-shot estimates | 10 |
| F. Interpret the results and limitations | 15 |
| **Total** | **100** |

**Integrity:** Complete your own analysis and follow course rules for citing outside code or AI assistance. Instructor solutions remain private.

**Run:** From the student repository root execute docker compose up --build, then open homework/hw-01-quantum-kernel-classification/hw.ipynb.