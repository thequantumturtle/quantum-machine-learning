# Quantum Machine Learning — CMU 17-620

Student-facing quantum machine learning exercises, maintained by The Quantum Turtle.

**Lab 2 release checklist:** The course environment and student notebook syntax have passed GitHub Actions. Students need **read access to this repository** (or a copy supplied in Canvas). The student repository is public. The published GHCR image has **not yet been verified**, so use the build-from-source instructions below.

## Lab 2 — Encoding Classical Data and Quantum Similarity

### Before class

Install **Docker Desktop** (Mac or Windows) or Docker Engine with the Compose plugin (Linux). Start Docker and verify the following commands succeed in a terminal:

```bash
docker --version
docker compose version
```

You also need Git to clone the repository, or you can select **Code → Download ZIP** on its GitHub page if you have access.

### Get the course files

If you can access the GitHub repository, use:

```bash
git clone https://github.com/thequantumturtle/quantum-machine-learning.git
cd quantum-machine-learning
```

**Already cloned it?** From inside the directory, run `git pull` instead. Save any unfinished notebook edits first. If you downloaded the repository as a ZIP, extract it, then open a terminal in that folder.

### Start JupyterLab in Docker

From the **repository root** (where `compose.yaml` lives):

```bash
docker compose up --build
```

The first run downloads a Python base image and installs the course dependencies. It can take longer than later runs. Wait for the terminal to display a local JupyterLab URL containing a token, for example `http://127.0.0.1:8888/lab?token=...`.

Open **the tokenized URL printed by your own terminal**, not the example URL above. In JupyterLab, open:

`labs/lab-02-quantum-encoding/lab.ipynb`

Run the imports cell, then work through Lab 2 **in notebook order**. The repository is mounted into the container, so notebook edits are saved to your local course directory. **Lab 2 is ungraded practice. You do not need to submit this notebook or upload anything to Canvas.** Save your progress if you wish; quizzes and homework have separate graded submissions.

To stop JupyterLab, press **Ctrl+C** in the terminal. You can start it again with `docker compose up` (or `docker compose up --build` after changing dependencies).

### Troubleshooting

- **Cannot open the GitHub repository / 404:** The repository is private and your GitHub account does not have access. Ask the instructor for access or a Canvas download. A GitHub URL alone does not grant access.
- **Cannot connect to the Docker daemon:** Start Docker Desktop and wait for it to report that the engine is running.
- **Port 8888 already in use:** Stop another Jupyter/Docker session. Alternatively, change the host-side port in `compose.yaml` from `127.0.0.1:8888:8888` to `127.0.0.1:8889:8888`, then restart and use the URL with port 8889.
- **ModuleNotFoundError:** Make sure you opened JupyterLab from this Docker container and selected its Python 3 kernel, rather than a local Python installation.
- **Missing or broken widget:** Run the notebook in order, check the imports cell, and restart the kernel if you previously ran an outdated cell.
- **Docker rebuild is slow:** The first build installs PennyLane and JupyterLab; subsequent launches normally reuse cached layers.
- **Windows:** Use Docker Desktop's supported Linux-container backend. Open a terminal where the extracted repository is located.

### Instructor verification

The [student CI workflow](https://github.com/thequantumturtle/quantum-machine-learning/actions) builds the core Docker image and checks student notebook syntax. The private instructor workflow separately runs complete Lab 2 and HW1 solutions. Automated verification does not replace a first-day student-access test.

## Optional prebuilt image (only after instructor confirmation)

The repository has a GitHub Actions workflow named **Publish core image to GHCR**. It can publish the multi-platform image `ghcr.io/thequantumturtle/qml-core:fall-2026-v1`. Until the instructor verifies that the image was published and made accessible to students, **do not use the pull-only Compose override**. The supported first-day command is `docker compose up --build`.

## Homework 1 — Quantum Kernel Classification

The longer coding assignment extends Lab 2. Its starter is at `homework/hw-01-quantum-kernel-classification/hw.ipynb`. The instructor will announce when the homework is assigned and its due date; having the starter in the repository does **not** mean it is already due.

## Source material

Conceptual inspiration: *A Practical Guide to Quantum Machine Learning and Quantum Optimization*, Chapter 9, and Fall 2026 course lectures. These notebooks are original course exercises, not reproductions of the textbook.

**Never commit:** instructor answer keys, private assessments, student work, credentials, or instructor-only material to this student repository.
