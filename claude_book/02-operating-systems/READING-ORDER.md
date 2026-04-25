# Operating Systems — Reading Order

## Path: Beginner → Advanced

1. **Operating Systems: Three Easy Pieces (OSTEP)** — Arpaci-Dusseau
   The canonical free OS textbook. Read it cover to cover.
   Order within: Virtualization (CPU + Memory) → Concurrency → Persistence → Distributed.

2. **xv6 Book (MIT)** — read alongside the xv6 source code
   Tiny teaching kernel; pairs with OSTEP — you actually see kernel code.
   Get the source: `git clone https://github.com/mit-pdos/xv6-riscv`

3. **The Little Book About OS Development** — Helin
   Build your own minimal x86 kernel from scratch — for hands-on learners.

4. **Linux Kernel Module Programming Guide** — Salzman et al.
   When you're ready to write Linux kernel modules; production-relevant.

## What this covers and what's missing

OSTEP + xv6 cover ~80% of an undergraduate OS course. For going deeper:
- **Modern Linux internals** → *Linux Kernel Development* (Love, paid) or kernel source
- **Distributed systems** → MIT 6.824 lectures (free YouTube) + papers (Lamport, Paxos, Raft)
- **Systems research** → OSDI, SOSP conference proceedings (free online)

## Implementation milestones
- [ ] Finish all OSTEP homework (free on the OSTEP site)
- [ ] Add a syscall to xv6
- [ ] Write a simple shell that supports pipes
- [ ] Build a small concurrent allocator
