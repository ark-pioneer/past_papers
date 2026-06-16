# **Expanded Section D Questions with Detailed Explanations (Based on 2026 Skeleton Program)**

Aligned to AQA 7517 Paper 1 Section D patterns.

***

# **Q1 — Add a new ant type that deposits double‑strength pheromone**

## **Problem Description**

Currently, WorkerAnts drop pheromones equal to `self._NewPheromoneStrength`. The question asks you to add a **new ant subclass** (e.g., *ScoutAnt*) that drops **double-strength pheromones** whenever carrying food.

This tests:

*   OOP inheritance
*   Extension of existing hierarchy
*   Understanding of `UpdateAntsPheromoneInCell()` behaviour

## **Tasks**

### **Task 1 — Create a new subclass**

Create a class:

```python
class ScoutAnt(Ant):
    def __init__(...):
        super().__init__(...)
        self._TypeOfAnt = "scout"
```

### **Task 2 — Override pheromone behaviour**

Inside Simulation → `UpdateAntsPheromoneInCell`, detect scout ants:

```python
if A.GetTypeOfAnt() == "scout":
    new_strength = self._NewPheromoneStrength * 2
else:
    new_strength = self._NewPheromoneStrength
```

### **Task 3 — Add scouts to nests**

Modify `SetUpANestAt` to spawn **one scout per nest**.

### **Task 4 — Ensure movement rules still work**

ScoutAnt inherits movement from WorkerAnt unless changed — acceptable.

***

## **Expected Input/Output**

### **Input**

    Enter simulation number: 1
    4

(Player advances one stage.)

### **Output (example for a cell the scout passed through)**

    PHEROMONES
    Ant 12 with strength of 2000

If default strength = 1000, scout leaves 2000.

***

# **Q2 — Add validation to ensure ants cannot move outside the grid**

## **Problem Description**

Movement currently uses `_ChangeCell()` without *post‑validation*.  
Although neighbour indices prevent invalid picks, worker ants carrying food walk toward nest using raw coordinate increments — meaning **they CAN walk off the grid** in extreme cases.

This tests:

*   Defensive programming
*   Coordinate bounds checking
*   Understanding of ant movement logic (`ChooseCellToMoveTo`)

## **Tasks**

### **Task 1 — Add a grid-boundary check utility**

Inside `Simulation`:

```python
def IsInsideGrid(self, row, col):
    return 1 <= row <= self._NumberOfRows and 1 <= col <= self._NumberOfColumns
```

### **Task 2 — Apply check after movement**

Inside WorkerAnt:

```python
new_r, new_c = self._ChangeCell(...)
if simulation.IsInsideGrid(new_r, new_c):
    self._Row, self._Column = new_r, new_c
```

### **Task 3 — Prevent illegal moves by keeping ant still**

If outside grid → ant simply doesn’t move.

### **Task 4 — Add feedback (optional)**

Teacher version only — not required by exam.

***

## **Expected Input/Output**

### **Input**

    Enter simulation number: 1
    Advance one stage

### **Output**

No visible output change EXCEPT ants will never appear at coordinates like:

    0, x
    x, 0
    11, y  (in a 10x10 grid)

***

# **Q3 — Modify the pheromone list to use a circular queue for decay tracking**

## **Problem Description**

All pheromones are stored in a Python list. Each stage, every pheromone is iterated over, even if many are nearly decayed.  
A circular queue would:

*   Track pheromones in “age buckets”
*   Efficiently remove pheromones that reach zero
*   Reduce repeated scanning

This tests understanding of ADTs.

## **Tasks**

### **Task 1 — Create a circular queue class**

```python
class CircularQueue:
    def __init__(self, size):
        self.data = [None]*size
        self.head = 0
        self.tail = 0
```

### **Task 2 — Replace list storage**

In `Simulation.__init__`:

```python
self._Pheromones = CircularQueue(5000)   # or other size
```

### **Task 3 — Update append and remove**

Instead of:

```python
self._Pheromones.append(Pheromone(...))
```

Use:

```python
self._Pheromones.enqueue(Pheromone(...))
```

### **Task 4 — Update AdvanceStage loop**

Iterate through circular queue instead of the list.

***

## **Expected Input/Output**

No change to external behaviour.  
Performance improves for large simulations.

Example cell output *remains identical*:

    Ant 7 with strength of 850

***

# **Q4 — Implement save/load of pheromone map (File I/O)**

## **Problem Description**

Students must add the ability to export and import:

*   Position (row, col)
*   Strength
*   BelongsTo ant ID

This matches AQA’s persistence pattern (e.g., 2021/2023/2025 papers).

## **Tasks**

### **Task 1 — Add menu options**

Modify `DisplayMenu()` and main loop to add:

    6. Save pheromones
    7. Load pheromones

### **Task 2 — Implement SavePheromones()**

Write a CSV file:

    row,col,ant,strength

Loop through `self._Pheromones`.

### **Task 3 — Implement LoadPheromones()**

Read the file and recreate Pheromone objects.

### **Task 4 — Clear existing pheromones before loading**

To avoid duplication.

***

## **Expected Example Output**

### **Saving**

    Saved pheromone map to pheromones.txt

### **File contents**

    2,4,12,900
    2,5,3,700
    4,1,7,1000

### **Loading**

    Pheromone map loaded (3 entries)

***

# **Q5 — Implement a breadth‑first search (BFS) for an ant to find nearest food**

## **Problem Description**

Worker ants normally follow pheromones or move randomly.  
You are asked to implement BFS so that ants **detect nearest food source**, then move toward it.

This tests:

*   Graph search
*   Grid navigation
*   Using `_GetIndicesOfNeighbours` effectively

## **Tasks**

### **Task 1 — Implement BFS function**

Inside Simulation:

```python
def BFSFindFood(self, start_row, start_col):
    # return (row, col) of nearest food cell
```

### **Task 2 — Use queue of (row, col)**

Track visited cells.

### **Task 3 — Detect first cell where food > 0**

Return coordinates.

### **Task 4 — Modify WorkerAnt movement**

If carrying no food:

*   Call BFS
*   Move one step toward food location
*   Otherwise revert to normal logic

***

## **Expected Input/Output**

### **Input**

    Advance one stage

### **Output change**

Workers will immediately begin moving toward nearest food cluster.

Example:

    3, 4: Ants: 1
    3, 5: Ants: 2

Previously random movement becomes structured.

Complexity Levels of the Five Questions
Q1 — Add a new ant type with double‑strength pheromones
Complexity Level: HIGH
Why?

Requires creating a new subclass
Requires modifying Simulation.UpdateAntsPheromoneInCell
Requires injecting the new ant type into nest creation
Requires understanding how pheromone behaviour emerges during AdvanceStage

This is a classic AQA 10–14 mark feature-addition question because it spans multiple classes and involves understanding behaviour rather than just modifying data.

Q2 — Grid-boundary validation to prevent illegal movement
Complexity Level: MEDIUM
Why?

Involves defensive programming, which is common in 7–9 mark Section D tasks
The logic is isolated to WorkerAnt movement, so it’s not as wide in scope
Requires reading but not drastically altering the program structure

This is typical of AQA’s validation/bug‑fix questions (25% historical frequency).

Q3 — Convert pheromone storage to a circular queue
Complexity Level: HIGH
Why?

Requires designing and implementing a full ADT
Must replace multiple list operations throughout the code
Requires full understanding of the decay loop and pheromone life cycle
Most students find structural changes to ADTs challenging

This is a difficult data structure modification task, typically 12–14 marks.

Q4 — Save/load pheromone map (File I/O)
Complexity Level: MEDIUM–HIGH
Why?

Involves adding new menu interactions
Requires reading and writing structured data
Requires correctly recreating objects
Spans at least 3–4 code areas, but the logic is conceptually straightforward

File I/O questions in AQA scripts usually sit around 8–12 marks, depending on complexity.

Q5 — Implement BFS to locate nearest food source
Complexity Level: HIGH
Why?

Requires algorithm design (BFS)
Must integrate results into movement logic
Needs careful coordination between grid indexing, neighbours, and ant state
Algorithm implementation questions historically score 10% but are usually hard when they appear

This is the most algorithmically challenging of the five and would be marked at the top band (12–14 marks) on Paper 1.

Summary Table (Quick Reference)

| Question | Topic Type                       | AQA Difficulty Category | Mark Band |
|---------|-----------------------------------|--------------------------|-----------|
| **Q1**  | Add a feature / OOP extension     | **High**                 | 10–14     |
| **Q2**  | Validation / bug fix              | **Medium**               | 7–9       |
| **Q3**  | ADT rewrite (Circular Queue)      | **High**                 | 12–14     |
| **Q4**  | File I/O (save/load)              | **Medium–High**          | 8–12      |
| **Q5**  | Algorithm implementation (BFS)    | **High**                 | 12–14     |


Low complexity

Below are **5 low‑tier Section D‑style questions**, each written **in the same structured format** as before:

*   **Problem description**
*   **2–5 subtasks with guidance**
*   **Expected input/output**

These are suitable for **4–6 mark** AQA-style programming tasks (KS5 introductory coding items).

***

# **Low‑Tier Question 1 — Display the Total Number of Ants in the Simulation**

## **Problem Description**

Students must add a simple function to count how many ants exist in total.  
This tests: *basic list traversal* and *simple method creation*.

## **Tasks**

### **Task 1 — Add a method to Simulation**

Create a method such as `GetTotalAnts()` returning `len(self._Ants)`.

### **Task 2 — Add a menu option (e.g., option 6)**

Display the total number of ants to the user.

### **Task 3 — Call the new method inside the main loop**

Print the result.

***

## **Expected Input/Output**

### **Input**

    6

### **Output**

    Total ants in simulation: 18

***

# **Low‑Tier Question 2 — Display Total Food in a Selected Area**

## **Problem Description**

Students add a feature to total the food values from a selected rectangular region.  
This reinforces: *looping*, *cell access*, and *simple accumulation*.

## **Tasks**

### **Task 1 — Add new method: GetAreaFoodTotal(startR, startC, endR, endC)**

Loop over grid cells and sum `GetAmountOfFood()`.

### **Task 2 — Add menu option**

Prompt the user for the start/end coordinates (reuse `GetCellReference()`).

### **Task 3 — Print the result**

Show the total food found in that region.

***

## **Expected Input/Output**

### **Input**

    Enter row number: 2
    Enter column number: 2
    Enter row number: 4
    Enter column number: 4

### **Output**

    Total food in selected area: 850

***

# **Low‑Tier Question 3 — Add a Simple “Ant Counter per Cell” Function**

## **Problem Description**

Students must implement a function that counts and displays how many ants exist in an inspected cell without showing other details.  
This focuses on: *method extraction* and *basic condition checking*.

## **Tasks**

### **Task 1 — Create a new method GetAntCountAt(row, col)**

Reuse `GetNumberOfAntsInCell()` but wrap it in a dedicated method.

### **Task 2 — Add menu option**

Ask the user for a cell and print “Ants at this cell: X”.

### **Task 3 — Ensure correct indexing**

Use `self._Grid[self.__GetIndex(row, col)]`.

***

## **Expected Input/Output**

### **Input**

    Enter row number: 3
    Enter column number: 4

### **Output**

    Ants at this cell: 2

***

# **Low‑Tier Question 4 — Add a Function to Display the Food at a Nest**

## **Problem Description**

Students write a method to check and display the **food level stored inside a nest** at a selected position.  
This tests understanding of: *nest lookup* and simple formatting.

## **Tasks**

### **Task 1 — Add a new method GetNestFood(row, col)**

Use `GetNestInCell()` and return `N.GetFoodLevel()` if a nest exists.

### **Task 2 — Add menu option**

Prompt user to choose a cell.

### **Task 3 — Handle missing nests**

If no nest is found, print:

    No nest at this location.

***

## **Expected Input/Output**

### **Input**

    Enter row number: 2
    Enter column number: 4

### **Output**

    Nest food level: 500

***

# **Low‑Tier Question 5 — Add a “List All Food Cells” Feature**

## **Problem Description**

Students create a feature listing all cells containing food (>0).  
This tests: *simple iteration* and *string formatting*.

## **Tasks**

### **Task 1 — Add a method ListFoodCells()**

Loop through grid cells and print coordinates of those with food.

### **Task 2 — Add a menu option**

Print results when chosen.

### **Task 3 — Format output neatly**

Example format:

    (2,4) – 500 food
    (7,1) – 200 food

***

## **Expected Input/Output**

### **Input**

    7

### **Output**

    Food cells:
    (2,4) – 500 food
    (5,3) – 300 food

