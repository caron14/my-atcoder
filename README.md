# Overview

This is an AtCoder competitive programming repository containing solutions to various contest problems. Solutions are organized by contest and problem difficulty.

## Repository Structure

- `contest/ABC{number}/` - Contest-specific directories containing solutions
  - Problems are labeled A, B, C, E representing increasing difficulty
  - Solutions written in Python (.py) and Julia (.jl)
  - Some problems have multiple solution attempts (e.g., TLE vs AC functions)

## Language-Specific Patterns

### Python Solutions
- Standard structure: `main()` function with `if __name__ == '__main__': main()`
- Input parsing: `int(input())`, `map(int, input().split())`, `list(map(int, input().split()))`
- Common imports: `collections` for Counter, defaultdict
- Algorithm patterns: greedy, dynamic programming, graph traversal
- Output: Direct `print()` statements

### Julia Solutions
- Input parsing: `parse(Int, readline())`, `parse.(Int, split(readline()))`
- Multiple line input: `readlines(stdin)` for batch processing
- Data structures: `Dict()` for mappings, arrays with 1-based indexing
- Output: `println()` for results

## Problem-Solving Patterns

### Common Algorithmic Approaches
- **Array manipulation**: Sorting, counting, prefix sums
- **String processing**: Character swapping, palindrome detection
- **Mathematical**: Combinatorics, probability calculations
- **Data structures**: Sets for deduplication, counters for frequency

### Code Organization
- Solutions often include example input/output as comments
- Multiple solution approaches in same file (TLE vs optimized)
- Clean separation between input parsing, algorithm logic, and output

## Development Workflow

When working on new problems:
1. Create new file in appropriate `contest/ABC{number}/` directory
2. Follow naming convention: `{problem_letter}.py` or `{problem_letter}.jl`
3. Include sample input/output as comments for testing
4. Implement efficient algorithms considering time/space complexity constraints

## Testing

No automated testing framework - solutions are validated against AtCoder judge system. Include sample test cases as comments in solution files for manual verification.