# Core Language Libraries

## Data Structures and Utilities

- collections: Advanced container data types for quick problem-solving.
  - Use Cases: Frequency counting (Counter), default values (defaultdict), queues (deque), maintaining order (OrderedDict), and lightweight objects (namedtuple).
  - Counter: Counter(), most_common(), subtract() - defaultdict: defaultdict() - deque: deque(), append(), appendleft(), pop(), popleft(), rotate() - OrderedDict: OrderedDict(), move_to_end() - namedtuple: namedtuple()
- heapq: Priority queues and heaps.
  - Use Cases: Implementing heaps (min-heap/max-heap), solving shortest-path algorithms like Dijkstra.
  - heappush: heappush(heap, item) - heappop: heappop(heap) - heapify: heapify(list) - heappushpop: heappushpop(heap, item) - heapreplace: heapreplace(heap, item) - nlargest: nlargest(n, iterable) - nsmallest: nsmallest(n, iterable)
- bisect: Efficient binary search utilities.
  - Use Cases: Insertions and lookups in sorted lists.
  - bisect_left: bisect_left(list, item) - bisect_right: bisect_right(list, item) - insort_left: insort_left(list, item) - insort_right: insort_right(list, item)
- array: Type-restricted, memory-efficient arrays.
  - Use Cases: Handling large datasets with fixed types.
  - array: array(typecode, [initializer]) - append: array.append() - extend: array.extend() - insert: array.insert() - remove: array.remove() - pop: array.pop() - reverse: array.reverse()
- functools: Higher-order functions and memoization.
  - Use Cases: Efficient recursion (lru_cache), function composition, and accumulators (reduce).
  - lru_cache: lru_cache() - partial: partial() - reduce: reduce() - cmp_to_key: cmp_to_key() - total_ordering: total_ordering() - wraps: wraps() - cache_property: cache_property()

## Algorithmic Problem Solving

### Combinatorics and Iteration

- itertools: Efficient tools for iterations and combinatorics.
  - Use Cases: Generating permutations (✅), combinations, Cartesian products, infinite cycles, and accumulations.

### Math and Optimization

- math: Core math functions.
  - Use Cases: Greatest common divisor (gcd), least common multiple (lcm), power, factorial, and logarithms.
- statistics: Statistical operations.
  - Use Cases: Calculating mean, median, mode, and variance.
- decimal and fractions: Precise decimal and fractional arithmetic.
  - Use Cases: Avoiding floating-point errors in calculations.
- sympy (optional): Symbolic mathematics.
  - Use Cases: Prime checking, algebraic simplifications.

## Graphs and Trees

- collections.defaultdict: Adjacency lists for graph representation.
  - Use Cases: Depth-First Search (DFS) and Breadth-First Search (BFS).
- heapq: Min-heaps for graph algorithms.
  - Use Cases: Dijkstra’s algorithm, Prim’s algorithm.
- Custom classes/namedtuple: Build tree nodes and binary trees.
  - Use Cases: Binary search tree problems, recursive traversals.

## String Manipulation

- re: Regular expressions.
  - Use Cases: Matching, splitting, and finding substrings.
- collections.Counter: Analyze string character frequencies.
  - Use Cases: Anagram detection, palindrome construction.
- difflib: Sequence matching.
  - Use Cases: Finding similarities between strings.

## Input/Output and Parsing

- json: Handling JSON data.
  - Use Cases: Parsing API responses and handling configuration files.
- csv: Work with CSV files.
  - Use Cases: Reading and writing structured data.
- sys.stdin/sys.stdout: Fast I/O for competitive programming.
  - Use Cases: Reading multiple lines of input/output efficiently.

## Advanced Utilities

- time and timeit: Benchmarking code.
  - Use Cases: Measuring execution time of functions.
- dataclasses: Lightweight data structures.
  - Use Cases: Struct-like classes with minimal boilerplate.
- pprint: Pretty-print complex data.
  - Use Cases: Debugging deeply nested data structures.
- logging: Tracking program execution.
  - Use Cases: Monitoring the flow in complex problems.

## Dynamic Programming and Optimization

- functools.lru_cache: Automatic memoization.
  - Use Cases: Speeding up recursive solutions.
- numpy (optional): Numerical computations and matrix operations.
  - Use Cases: Solving DP problems on grids/matrices.
- sortedcontainers: Sorted list, dict, and set.
  - Use Cases: Maintaining order with log-time operations.

## Tests and Debugging

- unittest: Built-in testing framework.
  - Use Cases: Writing and running test cases for algorithms.
- doctest: Test examples in docstrings.
  - Use Cases: Ensuring examples in documentation work as intended.
- trace: Debug execution.
  - Use Cases: Tracking execution paths.

## Miscellaneous

- random: Random number generation.
  - Use Cases: Simulating stochastic processes, shuffling arrays.
- io.StringIO: In-memory string streams.
  - Use Cases: Efficient mock I/O during tests.
- typing: Type hints.
  - Use Cases: Improving code clarity and debugging.

This comprehensive list covers essential Python libraries and their practical use cases, aligned with your objectives. Let me know if you’d like detailed examples for any specific library!
