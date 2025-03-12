### 1. **Faster Approach for CPU-bound Task:**
- **Threading** (0.62741 seconds) was faster than **multiprocessing** (1.13150 seconds) in this case. Multiprocessing typically helps with CPU-bound tasks, but overhead from managing separate processes might have caused slower performance here.

### 2. **Faster Approach for I/O-bound Task:**
- **Threading** (2.00509 seconds) was faster than **multiprocessing** (2.20194 seconds) for I/O-bound tasks. Threads are more efficient for I/O as they share memory and can continue working while waiting for I/O operations.

### 3. **Impact of the GIL:**
- The **GIL** restricts threads from executing bytecode simultaneously, which hurts performance for **CPU-bound tasks** but has minimal effect on **I/O-bound tasks**, where threads can wait without blocking others.

### 4. **When to Prefer Threads or Processes:**
- **Threads** are better for **I/O-bound tasks** (lightweight, less overhead).
- **Processes** are better for **CPU-bound tasks** (parallelism and bypass GIL restrictions).
