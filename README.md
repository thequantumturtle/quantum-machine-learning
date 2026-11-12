# Quantum Machine Learning — CMU 17-620

Student-facing quantum machine learning exercises, maintained by The Quantum Turtle.

**Status: instructor preview.** Do not distribute until the Docker image and notebook are executed end-to-end.

## Lab 2: Quantum Encoding and Similarity

Requires Docker with Compose. Start from this repository:

```bash
docker compose up --build
```

Open the tokenized JupyterLab URL printed in the terminal. Work in `labs/lab-02-quantum-encoding/lab.ipynb`; edits persist in this Git checkout.

After a tested versioned image is published, use:

```bash
docker compose -f compose.yaml -f compose.pull.yaml up
```

## Homework 1: Quantum Kernel Classification

The larger coding assignment extends Lab 2. Open `homework/hw-01-quantum-kernel-classification/hw.ipynb` in the same JupyterLab environment. See its `README.md` for the task, scoring rubric, and submission expectations. A due date will be posted in the LMS.

## Source material
Conceptual inspiration: *A Practical Guide to Quantum Machine Learning and Quantum Optimization*, Chapter 9, and the Fall 2026 course lectures. These notebooks are course exercises, not reproductions of the textbook.

Never commit answer keys, private assessments, student work, credentials, or instructor-only materials. Repository is private until publication rights and course readiness are confirmed.
