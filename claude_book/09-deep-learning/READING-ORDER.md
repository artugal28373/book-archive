# Deep Learning — Reading Order

## Prerequisites
You need:
- Linear algebra (Hefferon or Mathematics for ML chapters 2–4)
- Calculus + chain rule
- Python + NumPy basic fluency
- Ideally finished a few chapters of a classical ML book first (e.g., Daumé)

## Reading Order

1. **The Little Book of Deep Learning** — François Fleuret
   ~150 pages, dense. Best fastest overview of modern DL (covers transformers).

2. **Dive into Deep Learning (D2L)** — Zhang/Lipton/Li/Smola
   The modern hands-on DL textbook with PyTorch/MXNet/JAX code. Includes transformers, attention, BERT-era NLP. Cover to cover.

## Going beyond books — required for research

Books are 2+ years behind. After D2L:

1. **Karpathy — "Zero to Hero" YouTube series** — implements micrograd, makemore, GPT from scratch. Most efficient learning path for transformers in 2026.

2. **The Annotated Transformer** — http://nlp.seas.harvard.edu/annotated-transformer/

3. **Stanford CS231n** (vision) — videos on YouTube, all assignments online.

4. **Read these papers, in order:**
   - "Attention Is All You Need" (Vaswani 2017)
   - GPT-2, GPT-3 papers
   - LLaMA, LLaMA 2/3 papers
   - "Training Compute-Optimal LLMs" (Chinchilla)
   - "Scaling Laws for Neural Language Models" (Kaplan)
   - InstructGPT / RLHF paper
   - Direct Preference Optimization (DPO)
   - Constitutional AI (Anthropic)
   - Recent: Mamba, Mixtral, etc.

## Implementation milestones
You're not "advanced" until you can:
- [ ] Implement backprop on a 2-layer MLP from scratch (no autograd)
- [ ] Implement a transformer block from scratch (PyTorch, no nn.Transformer)
- [ ] Train a small language model on TinyShakespeare
- [ ] Fine-tune a small open model (e.g., Llama-3-8B) with LoRA
- [ ] Reproduce one arXiv paper end-to-end

## Related folders
- DL math → `07-machine-learning/Mathematics-for-Machine-Learning-Deisenroth.pdf`
- LLM-specific → `22-llm-engineering/`
- DL for NLP → `11-nlp/`
