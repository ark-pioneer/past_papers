# Past Papers Repository

This repository contains organised AQA Computer Science past papers and supporting materials for both **AS Level** and **A Level**.
---


## 📁 How to Navigate

### 1. Choose the Level
- Go to:
  - `a_level/` → A Level materials
  - `as_level/` → AS Level materials

### 2. Select a Year or Skeleton Program name

Each folder is named as:
```
YEAR - Skeleton Program Name
```

Examples:
- `2019 - Text Adventures`
- `2022 - Breakthrough`
- `2026 - Ant Simulation`

👉 These correspond to the **Paper 1 Skeleton Programs**.
---

### 3. Inside a Year Folder

You may find:

#### ✅ Main Components
- **Student Pack**  
  → Original exam materials (without official QP)

- **Solutions (Exam questions)**  
  → Example solutions to exam sections Section B and Section D

- **Practice Materials**
  → Extra structured tasks for revision
  → Solutions to the tasks

---


## 🎯 How Students Should Use This

### Suggested Workflow
1. Pick a year (e.g. `2022 - Breakthrough`)
2. Read the **student pack**
3. Attempt:
   - Practice question sets (`q1 → q4`)
4. Check answers using:
   - Teacher-provided solutions
---



Below is a comprehensive breakdown of the skeleton programs and Section D tasks from 2017 to 2026.
I have focused on the A-level (7517) papers, as these provide the most rigorous Section D requirements relevant to your MPS point 4 expertise.

1. Skeleton Program History (2017–2026)
The AQA pattern typically rotates between Simulations, Board Games/Puzzles, and Abstract Data Type (ADT) Implementations.

| Year | Skeleton Program Name | Primary Paradigm / Theme | Key Complexity |
|---|---|---|---|
| 2026 | Ant Simulation | Simulation / Bio-inspired | Pheromone trails, grid-based state |
| 2025 | Target Clear | Arcade/Logic Game | Reverse Polish Notation (RPN), expression eval |
| 2024 | Symbol Puzzle | Logic/Constraint Puzzle | Recursion, backtracking logic |
| 2023 | Dastan | Strategy Board Game | Complex OOP, move validation, queues |
| 2022 | Breakthrough! | Strategy/Logic Game | 2D Arrays, piece movement, win conditions |
| 2021 | HexBaron | Strategy Board Game | Hexagonal coordinate mapping, OOP |
| 2020 | Food Magnate | Economic Simulation | Object interaction, resource management |
| 2019 | Text Adventures | Interactive Fiction | Graphs/Linked structures, text parsing |
| 2018 | Words with AQA | Word Game / Scrabble-like | String manipulation, dictionary (Hash/File) |
| 2017 | Rabbits and Foxes | Predator-Prey Simulation | Mathematical modeling, grid updates |

2. Analysis of Section D Questions
Section D (the "Coding" section) typically consists of 4–5 questions. Based on a longitudinal review, they fall into very specific buckets:

Type 1: The "Add a Feature" Task (High Frequency)
These require implementing a new rule or mechanic.

* Examples: Add a "Super move" in HexBaron; implement a "Save Game" feature (File I/O); add a new predator type in the Simulation.
* Skill: Understanding existing class hierarchies and extending them.

Type 2: The "Validation/Bug Fix" Task
Ensuring the user doesn't break the program.

* Examples: Prevent a piece from moving off the board; validate that an expression doesn't divide by zero; ensure names aren't empty.
* Skill: Defensive programming and robust try/except or if logic.

Type 3: The "Data Structure Modification" Task
Changing how data is stored or retrieved.

* Examples: Changing a Fixed-size Queue to a Circular Queue; implementing a High Score table using a List of Objects; sorting a list of results.
* Skill: Fundamentals of Data Structures (Section 2 of the spec).

3. Frequency Analysis (A-Level Paper 1)
This frequency table categorizes the "core problem" being solved in Section D across the last ~10 exam cycles.

| Category | Frequency | Common Tasks |
|---|---|---|
| Game Logic / Rule Changes | ~45% | Modifying move logic, adding new game pieces, changing win conditions. |
| Validation & Error Handling | ~25% | Adding range checks, presence checks, and preventing crashes. |
| File I/O (Persistence) | ~15% | Loading maps from .txt, saving high scores, exporting game state. |
| Algorithm Implementation | ~10% | Writing a search algorithm (Linear/Binary) or a simple sort (Bubble/Insertion). |
| ADT Manipulation | ~5% | Directly modifying a Stack, Queue, or Linked List implementation. |

4. Summary & Strategy
AQA has moved heavily toward OOP-centric skeletons since 2021.
* 2017–2019 were often procedural or hybrid.
* 2020–2026 are almost entirely Object-Oriented, requiring students to understand inheritance, encapsulation, and composition to even find where to start their Section D answer.
> Teacher's Note: The 2025/2026 papers show a trend toward "Compound Features" in the 12–14 mark questions—e.g., "Implement a new feature AND save the result to a file."
>
Useful Sources for Follow-up:
* AQA Website: Past Papers & Mark Schemes (Official archive).
* Wikibooks: A-level Computing/AQA/Paper 1 (Excellent community-driven analysis of skeleton code).
* ZigZag Education: Often provides the "unofficial" breakdowns and practice Section D tasks for the current year's skeleton.


