# Skeleton Program for the AQA AS Summer 2022 examination
# Annotated with function purpose, parameters, and return types

import random

EMPTY_STRING = ""
SPACE = ' '
GRID_SIZE = 9 

def ResetDataStructures():
  """
  Overall Purpose: Initializes and returns empty puzzle-related data structures.
  Parameters: None
  Returns:
    PuzzleGrid (list[list[str]])
    Puzzle (list[str])
    Answer (list[str])
    Solution (list[str])
  """
  Puzzle = [EMPTY_STRING for Line in range(GRID_SIZE * GRID_SIZE)]
  PuzzleGrid = [[SPACE for Column in range(GRID_SIZE + 1)] for Row in range(GRID_SIZE + 1)]
  Solution = [EMPTY_STRING for Line in range(GRID_SIZE + 1)]
  Answer = [EMPTY_STRING for Line in range(2 * GRID_SIZE * GRID_SIZE)]
  return PuzzleGrid, Puzzle, Answer, Solution

def LoadPuzzleFile(PuzzleName, Puzzle):
  """
  Overall Purpose: Loads the puzzle from a file into the Puzzle list.
  Parameters:
    PuzzleName (str)
    Puzzle (list[str])
  Returns:
    Puzzle (list[str])
    OK (bool)
  """
  try:
    Line = 0
    FileIn = open(f"{PuzzleName}.txt", 'r')
    CellInfo = FileIn.readline().strip()
    while CellInfo != EMPTY_STRING:
      Puzzle[Line] = CellInfo
      CellInfo = FileIn.readline().strip()
      Line += 1
    FileIn.close()
    OK = Line != 0
    if not OK:
      print("Puzzle file empty")
  except:
    print("Puzzle file does not exist")
    OK = False
  return Puzzle, OK

def LoadSolution(PuzzleName, Solution):
  """
  Overall Purpose: Loads the correct solution grid from a file.
  Parameters:
    PuzzleName (str)
    Solution (list[str])
  Returns:
    Solution (list[str])
    OK (bool)
  """
  OK = True
  try:
    FileIn = open(f"{PuzzleName}S.txt", 'r')
    for Line in range(1, GRID_SIZE + 1):
      Solution[Line] = SPACE + FileIn.readline().strip()
      if len(Solution[Line]) != GRID_SIZE + 1:
        OK = False
        print(Line, Solution, "File data error")
    FileIn.close()
  except:
    print("Solution file does not exist")
    OK = False
  return Solution, OK

def ResetAnswer(PuzzleName, Answer):
  """
  Overall Purpose: Resets the Answer list with the puzzle name and empty entries.
  Parameters:
    PuzzleName (str)
    Answer (list[str])
  Returns:
    Answer (list[str])
  """
  Answer[0] = PuzzleName
  Answer[1] = "0"
  Answer[2] = "0"
  for Line in range(3, 2 * GRID_SIZE * GRID_SIZE):
    Answer[Line] = EMPTY_STRING
  return Answer

def TransferPuzzleIntoGrid(PuzzleName, PuzzleGrid, Puzzle, Answer):
  """
  Overall Purpose: Fills PuzzleGrid with data from Puzzle and resets Answer.
  Parameters:
    PuzzleName (str)
    PuzzleGrid (list[list[str]])
    Puzzle (list[str])
    Answer (list[str])
  Returns:
    PuzzleGrid (list[list[str]])
    Answer (list[str])
    OK (bool)
  """
  OK = True
  try:
    Line = 0
    while Puzzle[Line] != EMPTY_STRING:
      Row = int(Puzzle[Line][0])
      Column = int(Puzzle[Line][1])
      Digit = Puzzle[Line][2]
      PuzzleGrid[Row][Column] = Digit
      Line += 1
    PuzzleGrid[0][0] = 'X'
    Answer = ResetAnswer(PuzzleName, Answer)
  except:
    print("Error in puzzle file")
    OK = False
  return PuzzleGrid, Answer, OK

def LoadPuzzle(PuzzleGrid, Puzzle, Answer, Solution):
  """
  Overall Purpose: Loads a new puzzle and its solution from files.
  Parameters:
    PuzzleGrid, Puzzle, Answer, Solution (list structures)
  Returns:
    PuzzleGrid, Puzzle, Answer, Solution (lists)
  """
  PuzzleGrid, Puzzle, Answer, Solution = ResetDataStructures()
  PuzzleName = input("Enter puzzle name to load: ")
  Puzzle, OK = LoadPuzzleFile(PuzzleName, Puzzle)
  if OK:
    Solution, OK = LoadSolution(PuzzleName, Solution)
  if OK:
    PuzzleGrid, Answer, OK = TransferPuzzleIntoGrid(PuzzleName, PuzzleGrid, Puzzle, Answer)
  if not OK:
    PuzzleGrid, Puzzle, Answer, Solution = ResetDataStructures()
  return PuzzleGrid, Puzzle, Answer, Solution

def TransferAnswerIntoGrid(PuzzleGrid, Answer):
  """
  Overall Purpose: Inserts the answers from Answer into the PuzzleGrid.
  Parameters:
    PuzzleGrid (list[list[str]])
    Answer (list[str])
  Returns:
    PuzzleGrid (list[list[str]])
  """
  for Line in range(3, int(Answer[2]) + 3):
    CellInfo = Answer[Line]
    Row = int(CellInfo[0])
    Column = int(CellInfo[1])
    Digit = CellInfo[2]
    PuzzleGrid[Row][Column] = Digit
  return PuzzleGrid

def LoadPartSolvedPuzzle(PuzzleGrid, Puzzle, Answer, Solution):
  """
  Overall Purpose: Loads a partially solved puzzle from a file.
  Parameters:
    PuzzleGrid, Puzzle, Answer, Solution (list structures)
  Returns:
    PuzzleGrid, Puzzle, Answer, Solution (lists)
  """
  PuzzleGrid, Puzzle, Answer, Solution = LoadPuzzle(PuzzleGrid, Puzzle, Answer, Solution)
  try:
    PuzzleName = Answer[0]
    FileIn = open(f"{PuzzleName}P.txt", 'r')
    CellInfo = FileIn.readline().strip()
    if PuzzleName != CellInfo:
      print("Partial solution file is corrupt")
    else:
      Line = 0
      while CellInfo != EMPTY_STRING:
        Answer[Line] = CellInfo
        Line += 1
        CellInfo = FileIn.readline().strip()
    FileIn.close()
    PuzzleGrid = TransferAnswerIntoGrid(PuzzleGrid, Answer)
  except:
    print("Partial solution file does not exist")
  return PuzzleGrid, Puzzle, Answer, Solution

def DisplayGrid(PuzzleGrid):
  """
  Overall Purpose: Outputs the current state of the puzzle grid.
  Parameters:
    PuzzleGrid (list[list[str]])
  Returns: void
  """
  print()
  print("   1   2   3   4   5   6   7   8   9  ")
  print(" |===.===.===|===.===.===|===.===.===|")
  for Row in range(1, GRID_SIZE + 1):
    print(f"{Row}|", end='')    
    for Column in range(1, GRID_SIZE + 1):
      if Column % 3 == 0:
        print(f"{SPACE}{PuzzleGrid[Row][Column]}{SPACE}|", end='')
      else:
        print(f"{SPACE}{PuzzleGrid[Row][Column]}{SPACE}.", end='')
    print()
    if Row % 3 == 0:
      print(" |===.===.===|===.===.===|===.===.===|") 
    else:
      print(" |...........|...........|...........|")
  print()

def SolvePuzzle(PuzzleGrid, Puzzle, Answer):
  """
  Overall Purpose: Lets the user solve the puzzle via keyboard input.
  Parameters:
    PuzzleGrid (list[list[str]])
    Puzzle (list[str])
    Answer (list[str])
  Returns:
    PuzzleGrid (list[list[str]])
    Answer (list[str])
  """
  DisplayGrid(PuzzleGrid)
  if PuzzleGrid[0][0] != 'X':
    print("No puzzle loaded")
  else:
    print("Enter row column digit: ")
    print("(Press Enter to stop)")
    CellInfo = input()
    while CellInfo != EMPTY_STRING:
      InputError = False
      if len(CellInfo) != 3:
        InputError = True
      else:
        Digit = CellInfo[2]
        try:
          Row = int(CellInfo[0])
        except:
          InputError = True
        try:
          Column = int(CellInfo[1])
        except:
          InputError = True
        if (Digit < '1' or Digit > '9'):
          InputError = True
      if InputError:
        print("Invalid input")
      else:
        PuzzleGrid[Row][Column] = Digit
        Answer[2] = str(int(Answer[2]) + 1)
        Answer[int(Answer[2]) + 2] = CellInfo
        DisplayGrid(PuzzleGrid)
      print("Enter row column digit: ")
      print("(Press Enter to stop)")
      CellInfo = input()
  return PuzzleGrid, Answer

def DisplayMenu():
  """
  Overall Purpose: Displays the main user menu.
  Parameters: None
  Returns: void
  """
  print()
  print("Main Menu")
  print("=========")
  print("L - Load new puzzle")
  print("P - Load partially solved puzzle")
  print("S - Solve puzzle") 
  print("C - Check solution")
  print("K - Keep partially solved puzzle")
  print("X - Exit") 
  print()

def NumberPuzzle():
  """
  Overall Purpose: Main game loop managing menu and puzzle interaction.
  Parameters: None
  Returns: void
  """
  Finished = False
  PuzzleGrid, Puzzle, Answer, Solution = ResetDataStructures()
  while not Finished:
    DisplayMenu()
    MenuOption = input("Enter your choice: ").upper()
    if MenuOption == 'L':
      PuzzleGrid, Puzzle, Answer, Solution = LoadPuzzle(PuzzleGrid, Puzzle, Answer, Solution)
    elif MenuOption == 'P':
      PuzzleGrid, Puzzle, Answer, Solution = LoadPartSolvedPuzzle(PuzzleGrid, Puzzle, Answer, Solution)
    elif MenuOption == 'K':
      KeepPuzzle(PuzzleGrid, Answer)
    elif MenuOption == 'C':
      if PuzzleGrid[0][0] != 'X':
        print("No puzzle loaded")
      else:
        if int(Answer[2]) > 0:
          ErrorCount, Solved = CheckSolution(PuzzleGrid, Answer, Solution)
          Answer = CalculateScore(Answer, ErrorCount)
          if Solved:
            print("You have successfully solved the puzzle")
            Finished = True
          else:
            print(f"Your score so far is {Answer[1]}")
        else:
          print("No answers to check")
    elif MenuOption == 'S':
      PuzzleGrid, Answer = SolvePuzzle(PuzzleGrid, Puzzle, Answer)
    elif MenuOption == 'X':
      Finished = True
    else:
      print("Invalid menu option. Try again")
  if Answer[2] != EMPTY_STRING:
    DisplayResults(Answer)

if __name__ == "__main__":
  NumberPuzzle()
