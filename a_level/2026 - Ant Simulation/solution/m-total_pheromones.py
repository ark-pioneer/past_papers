# Simulation class
def GetTotalPheromoneStrengthInArea(self, StartRow, StartColumn, EndRow, EndColumn):
    TotalStrength = 0

    for P in self._Pheromones:
        if (P.GetRow() >= StartRow and P.GetRow() <= EndRow and
            P.GetColumn() >= StartColumn and P.GetColumn() <= EndColumn):
            TotalStrength += P.GetStrength()

    return TotalStrength


def DisplayMenu():
    print()
    print("1. Display overall details")
    print("2. Display area details")
    print("3. Inspect cell")
    print("4. Advance one stage")
    print("5. Advance X stages")
    print("6. Display total pheromone strength in an area")
    print("9. Quit")
    print()
    print("> ", end='')

#  inside the while Choice != "9": loop in Main():
# elif Choice == "6":
#     StartRow, StartColumn = GetCellReference()
#     EndRow, EndColumn = GetCellReference()
#     Total = ThisSimulation.GetTotalPheromoneStrengthInArea(
#         StartRow, StartColumn, EndRow, EndColumn
#     )
#     print(f"Total pheromone strength in area: {Total}\n")
