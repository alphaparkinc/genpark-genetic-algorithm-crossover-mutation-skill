# genpark-genetic-algorithm-crossover-mutation-skill

> Genetic algorithm optimizer with tournament selection, single-point crossover, bit-flip mutation, and elitism.

Part of the **GenPark AI Agent Skills Matrix**. Production-ready, zero external dependencies, native Python 3.9+ standard library.

## Architecture

```mermaid
flowchart TD
    A[Initial Candidate Population] --> B[Evolutionary Selection & Variation]
    B --> C[Metaheuristic Swarm Optimization]
    C --> D[Optimal Global Solution]
    D --> E[MCP Protocol Endpoint]
```

## Features
- **Zero Third-Party Dependencies**: Pure Python standard library (`math`, `random`).
- **Robust Metaheuristics**: Genetic crossover/mutation, PSO swarm velocity, simulated annealing Metropolis criterion, and ACO stigmergy.
- **Native MCP Protocol Support**: Integrated JSON-RPC 2.0 stdio server ready for Claude Desktop, Cursor, and Windsurf.

## Installation

```bash
pip install genpark-genetic-algorithm-crossover-mutation-skill
```

Or clone directly:

```bash
git clone https://github.com/alphaparkinc/genpark-genetic-algorithm-crossover-mutation-skill.git
cd genpark-genetic-algorithm-crossover-mutation-skill
python example_usage.py
```

## Quick Start

```python
from client import *
# Refer to example_usage.py for end-to-end execution
```

## Model Context Protocol (MCP) Setup

Add to your `claude_desktop_config.json` or `cursor.json`:

```json
{
  "mcpServers": {
    "genpark-genetic-algorithm-crossover-mutation-skill": {
      "command": "python",
      "args": ["-m", "genpark-genetic-algorithm-crossover-mutation-skill.mcp_server"]
    }
  }
}
```

## License
MIT License. Copyright (c) 2026 AlphaPark Inc. & Alpha-Park.
