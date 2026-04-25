# DevOps / Cloud — Reading Order

## Currently sparse

Most DevOps knowledge lives in **vendor docs** (Docker, Kubernetes, AWS, Terraform). Books help with the principles; daily work is docs + practice.

## What you have

1. **Bash Guide for Beginners** — Garrels — basic shell scripting
2. **Advanced Bash-Scripting Guide** — Cooper — comprehensive shell reference

## What to grab next (FREE)

- **Site Reliability Engineering** + **The SRE Workbook** + **Building Secure & Reliable Systems** — Google — sre.google/books (HTML; check for PDF)
- **The Linux Command Line** — already in `05-software-engineering/`
- **Kubernetes Handbook** — Jimmy Song — jimmysong.io
- **Docker Get Started** — official docs
- **Terraform Tutorials** — developer.hashicorp.com/terraform/tutorials

## What's missing (PAID — worth buying)

- **The DevOps Handbook (2e)** — Kim/Humble/Debois ⭐ (DevOps philosophy + practice)
- **The Phoenix Project** — Kim (DevOps as a novel — surprisingly good)
- **Continuous Delivery** — Humble/Farley
- **Kubernetes Up and Running (3e)** — Burns/Beda/Hightower ⭐
- **Kubernetes in Action (2e)** — Marko Luksa
- **Terraform: Up and Running (3e)** — Brikman ⭐
- **Infrastructure as Code (2e)** — Kief Morris
- **Docker Deep Dive** — Nigel Poulton

## Path: Beginner → Advanced

### Linux + shell (week 1-2)
1. The Linux Command Line (in `05-swe/`)
2. Bash Guide for Beginners

### Containers (week 3-5)
3. Docker official tutorial → build images for 3 services
4. Docker Compose → multi-container apps

### Orchestration (week 6-12)
5. Kubernetes official tutorial (kubernetes.io/docs/tutorials)
6. Run a real app on k3s/minikube
7. Helm charts
8. (Buy Kubernetes Up & Running for systematic coverage)

### Infrastructure as Code (week 13-16)
9. Terraform tutorials
10. Build a real AWS/GCP environment with Terraform
11. CI/CD: GitHub Actions or GitLab CI

### SRE / production (ongoing)
12. SRE book chapters 1-6 (incidents, SLOs)
13. Observability: Prometheus + Grafana, OpenTelemetry
14. Cloud cost management

## Implementation milestones
- [ ] Containerize a real app (Dockerfile from scratch, multi-stage)
- [ ] Deploy on Kubernetes with proper manifests, secrets, configmaps
- [ ] Write Terraform for a real AWS VPC + EKS cluster
- [ ] Set up Prometheus + Grafana + alerting
- [ ] Build a CI/CD pipeline that tests, builds, deploys
- [ ] Run a chaos engineering experiment

## Cert path (optional, useful for jobs)
- AWS Certified Solutions Architect Associate
- CKA (Certified Kubernetes Administrator)
- HashiCorp Certified: Terraform Associate
