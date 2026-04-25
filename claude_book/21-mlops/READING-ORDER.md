# MLOps — Reading Order

## What you have

1. **Rules of Machine Learning** — Martin Zinkevich (Google)
   ~40 short rules. Best ML-system-design starting point. Read in 2 hours.

2. **Practitioners Guide to MLOps** — Google Cloud
   Whitepaper covering the MLOps lifecycle. Practical.

## What to grab (FREE)

- **Machine Learning Engineering** — Andriy Burkov — mlebook.com (read free online; PDF requires email)
- **Made With ML** — Goku Mohandas — madewithml.com (HTML; comprehensive MLOps course)
- **The Big Book of MLOps** — Databricks (free PDF after email signup)
- **Hidden Technical Debt in ML Systems** — Sculley et al. (NeurIPS paper — required reading)

## What's missing (PAID — must buy)

- **Designing Machine Learning Systems** — Chip Huyen ⭐⭐ (THE MLOps book — every AI engineer should read this)
- **Building Machine Learning Pipelines** — Hapke/Nelson (TFX-focused)
- **Practical MLOps** — Gift/Deza
- **Reliable Machine Learning** — Chen/Murphy et al.
- **Introducing MLOps** — Treveil/Omont
- **Machine Learning Design Patterns** — Lakshmanan/Robinson/Munn ⭐
- **Kubeflow for Machine Learning** — Grant/Karau

## Path: Beginner → Advanced

### Foundations (you have some ML, want to deploy it)
1. **Rules of ML** (already here) — read first
2. **Hidden Technical Debt** paper (already on the to-grab list)
3. **Made With ML** (free) — work through end-to-end

### Tooling (pick what your job uses)
4. **MLflow** — experiment tracking + model registry (mlflow.org docs)
5. **Weights & Biases** — wandb.ai (alternative to MLflow)
6. **DVC** — data versioning (dvc.org)
7. **Kubeflow** OR **Vertex AI** OR **SageMaker** — pipeline orchestration

### Production (when serving real traffic)
8. **Buy Designing ML Systems** (Huyen)
9. **Model serving**: TorchServe, BentoML, Triton
10. **Monitoring**: drift detection, performance tracking
11. **A/B testing infrastructure** for models

### Advanced
12. **Feature stores**: Feast, Tecton
13. **Reproducible training**: container images, locked deps, deterministic seeds
14. **Cost optimization**: spot instances, model distillation, quantization
15. **Compliance**: lineage, audit trails, GDPR-style "right to explanation"

## Implementation milestones
- [ ] Track an experiment with MLflow + push best model to a registry
- [ ] Build a Docker image that serves a model behind FastAPI
- [ ] Set up automated retraining on new data
- [ ] Detect data drift in production traffic
- [ ] Run shadow mode + canary for a model rollout
- [ ] Build an end-to-end pipeline: data → train → eval → register → deploy

## Reality check
MLOps is 70% data engineering + DevOps + 30% ML. If you don't have those foundations, this folder won't make sense. See `19-devops-cloud/` and `23-data-engineering/` first.
