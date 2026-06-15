def GetAreaDetails(self, StartRow, StartColumn, EndRow, EndColumn):
    Details = ""
    for Row in range(StartRow, EndRow + 1):
        for Column in range(StartColumn, EndColumn + 1):
            Details += f"{Row}, {Column}: "
            TempCell = self._Grid[self.__GetIndex(Row, Column)]

            if self.GetNestInCell(TempCell) is not None:
                Details += " Nest "

            NumberOfAnts = self.GetNumberOfAntsInCell(TempCell)
            if NumberOfAnts > 0:
                Details += f" Ants: {NumberOfAnts} "

            NumberOfPheromones = self.GetNumberOfPheromonesInCell(TempCell)
            if NumberOfPheromones > 0:
                Details += f" Pheromones: {NumberOfPheromones} "
                Strongest = self.GetStrongestPheromoneInCell(TempCell)
                Details += f"Strongest pheromone: {Strongest} "

            AmountOfFood = TempCell.GetAmountOfFood()
            if AmountOfFood > 0:
                Details += f" {AmountOfFood} food "

            Details += "\n"

    return Details