# Natural Language Processing — Reading Order

## Path: Beginner → Advanced

1. **A Primer on Neural Network Models for NLP** — Yoav Goldberg
   Concise bridge from classical NLP to neural methods. ~80 pages, dense but readable.

2. **Speech and Language Processing (SLP3)** — Jurafsky & Martin
   *(Note: download from web.stanford.edu/~jurafsky/slp3/ to this folder if not present)*
   THE NLP textbook. Free draft. Cover to cover, takes months.

3. **Introduction to Information Retrieval** — Manning/Raghavan/Schütze
   Search foundations. Critical for understanding RAG, embeddings, vector search.

## Going beyond books — required for modern NLP

NLP changed enormously after 2018 (BERT) and 2022 (ChatGPT). Books lag by 2+ years.

1. **Stanford CS224n** — free YouTube lectures, the standard NLP course
2. **HuggingFace NLP Course** — huggingface.co/learn/nlp-course (free, hands-on)
3. **Karpathy "Zero to Hero"** — implements GPT from scratch (also referenced in 09-deep-learning)
4. **Read these landmark papers:**
   - Word2Vec (Mikolov 2013)
   - Transformer / Attention Is All You Need (Vaswani 2017)
   - BERT (Devlin 2018)
   - GPT-2/3 (Radford/Brown)
   - T5 (Raffel)
   - InstructGPT (Ouyang) — RLHF
   - LLaMA series

## Implementation milestones
- [ ] Build a bigram language model from text (no neural)
- [ ] Implement Word2Vec from scratch
- [ ] Implement a transformer encoder for classification
- [ ] Fine-tune BERT on a downstream task
- [ ] Build a RAG system with a vector DB (HuggingFace + FAISS or ChromaDB)

## Related folders
- LLM-specific engineering → `22-llm-engineering/`
- DL fundamentals → `09-deep-learning/`
