# LLM Engineering — Reading Order

## Important: this field is mostly papers + docs, not books

The LLM ecosystem moves so fast that most "books" are out of date by publication. Real practitioners read arXiv weekly + ship code.

## What you have

1. **The Little Book of Deep Learning** — François Fleuret
   ~150 pages. Best fast overview of modern DL including transformers.

## What to grab (FREE — courses + docs are king)

### Courses
- **Karpathy "Zero to Hero"** — YouTube — implements GPT from scratch (best single resource for understanding transformers)
- **HuggingFace LLM Course** — huggingface.co/learn (free, hands-on)
- **DeepLearning.AI short courses** — deeplearning.ai (LangChain, RAG, evals — free)
- **Stanford CS336: Language Modeling from Scratch** — stanford-cs336.github.io (free recordings)

### Reference docs
- **HuggingFace Transformers docs** — huggingface.co/docs/transformers
- **LangChain docs** — python.langchain.com
- **LlamaIndex docs** — docs.llamaindex.ai
- **Anthropic API docs** — docs.anthropic.com (prompt engineering, tool use, agentic patterns)

### Required reading (papers — not books)
1. **Attention Is All You Need** (Vaswani 2017) — arXiv 1706.03762 — the transformer
2. **GPT-3 / Language Models are Few-Shot Learners** (Brown 2020) — arXiv 2005.14165
3. **Scaling Laws for Neural Language Models** (Kaplan 2020) — arXiv 2001.08361
4. **Chinchilla / Compute-Optimal LLMs** (Hoffmann 2022) — arXiv 2203.15556
5. **InstructGPT** (Ouyang 2022) — arXiv 2203.02155 — RLHF
6. **Constitutional AI** (Bai 2022) — arXiv 2212.08073
7. **LLaMA 2** (Touvron 2023) — arXiv 2307.09288
8. **DPO** (Rafailov 2023) — arXiv 2305.18290
9. **RAG** (Lewis 2020) — arXiv 2005.11401
10. **A Survey of Large Language Models** (Zhao 2023) — arXiv 2303.18223

## What's missing (PAID — actually worth buying despite the field changing fast)

- **Build a Large Language Model from Scratch** — Sebastian Raschka ⭐⭐ (most practical book — implement GPT step by step)
- **Hands-On Large Language Models** — Alammar/Grootendorst ⭐ (recently published, applied focus)
- **Natural Language Processing with Transformers** — Tunstall/Werra/Wolf (HuggingFace book)
- **Generative Deep Learning (2e)** — David Foster
- **Building LLM Applications for Production** — Chip Huyen

## Path: Beginner → Advanced

### Phase 1 — Understand transformers (4-6 weeks)
1. Karpathy "Zero to Hero" (YouTube)
2. The Annotated Transformer (nlp.seas.harvard.edu/annotated-transformer)
3. Read "Attention Is All You Need"
4. Implement a small GPT yourself

### Phase 2 — Use existing models (2-4 weeks)
5. HuggingFace LLM course
6. Fine-tune a small model (Llama 3 8B with LoRA)
7. Build a basic RAG system (HuggingFace + ChromaDB or FAISS)

### Phase 3 — Production patterns (4-8 weeks)
8. **Prompt engineering** — Anthropic prompt library, OpenAI cookbook
9. **Tool use / function calling** — model-specific docs
10. **Agentic patterns** — ReAct, plan-and-execute, multi-step reasoning
11. **Evaluation** — LLM-as-judge, BLEU/ROUGE for some tasks, human eval, eval harnesses

### Phase 4 — Advanced
12. **Distillation / quantization** for inference cost
13. **vLLM, TensorRT-LLM** for serving
14. **Continuous pretraining** on domain data
15. **Multi-modal** (vision-language models)

## Implementation milestones
- [ ] Implement a transformer block from scratch (no nn.Transformer)
- [ ] Train a tiny LM on TinyStories or TinyShakespeare
- [ ] Fine-tune Llama 3 8B with LoRA on a task-specific dataset
- [ ] Build a RAG system end-to-end (embeddings + vector DB + LLM + reranker)
- [ ] Build an agent that uses tools (calls APIs, executes code)
- [ ] Set up an eval harness with at least 3 metrics
- [ ] Deploy a model behind vLLM with proper rate limiting + monitoring

## Reality check
This is the highest-paid, most-overhyped, most-changing field in tech right now. The half-life of frameworks is ~6 months. Focus on **fundamentals (transformers, attention, training dynamics)** and **shipping things**. Don't waste time learning every new framework that drops.
