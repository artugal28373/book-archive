# C / C++ — Reading Order

## Path: Beginner → Advanced

1. **Beej's Guide to C Programming** — Brian Hall
   Friendly C intro. Modern, free, well-written. Start here for C.

2. **Modern C** — Jens Gustedt
   Moves from C basics to advanced (atomics, threads, memory model).

3. **What Every Programmer Should Know About Memory** — Ulrich Drepper
   Long paper, not a book. The ONE document on memory hierarchies, caches, NUMA. Read it after you've written enough C/C++ to care about performance.

## What's missing (PAID — must buy)

C++:
- **A Tour of C++ (3e)** — Bjarne Stroustrup ⭐ (concise modern C++ overview)
- **C++ Primer (5e)** — Lippman/Lajoie/Moo (comprehensive intro)
- **Effective Modern C++** — Scott Meyers ⭐ (idiomatic C++11/14)
- **C++ Concurrency in Action (2e)** — Anthony Williams (concurrency)
- **The C++ Programming Language (4e)** — Stroustrup (reference)

C:
- **The C Programming Language (K&R, 2e)** — Kernighan/Ritchie (classic)
- **C Programming: A Modern Approach (2e)** — K.N. King

## External free resources
- **cppreference.com** — best free C++ reference
- **learncpp.com** — comprehensive free C++ tutorial
- **CppCon talks** — YouTube (Stroustrup, Meyers, Sutter, etc.)

## Implementation milestones
- [ ] Write a small allocator (free list, slab, bump)
- [ ] Build a tiny lexer + parser in C
- [ ] Write a thread pool using `std::thread` + `std::condition_variable`
- [ ] Profile a real workload with `perf` or VTune
- [ ] Use sanitizers: `-fsanitize=address,undefined` on every build

## Use case
C/C++ is used for: systems (kernels, drivers, allocators), embedded, game engines, HPC, real-time, performance-critical libraries (PyTorch, TensorFlow internals). If your career is ML systems / infrastructure, C++ matters. If it's web/AI engineering on top of frameworks, C++ is optional.
