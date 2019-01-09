import java.util.Scanner;
public class ValidateSudoku
{
    public static void main(String[] args)
    {
        int[][] grid = readASolution();
        System.out.println(isValid(grid) ? "Valid Solution ": "Invalid Solution");

    }

    public static int[][] readASolution()
    {
        Scanner input = new Scanner(System.in);
        int[][] solution = new int[9][9];
        System.out.println("Enter your solution  row by row.");
        for(int i=0; i < 9; i++)
        {
            for(int j=0; j < 9; j++)
            {
                solution[i][j] = input.nextInt();
            }
        }
        return solution;
    }

    public static boolean isValid(int[][] grid)
    {
        for(int i=0; i<9; i++)
        {
            for(int j= 0; j < 9; j++)
            {
                if(grid[i][j] < 0 || grid[i][j] > 9 || !isValid(i, j, grid))
                {
                    return false;
                }
            }
        }
        return true;
    }

    public static boolean isValid(int i, int j, int[][] grid )
    {
        for(int col = 0; col < 9; col++)
        {
            if(col != j && grid[i][j] == grid[i][col])
            {
                return false;
            }
        }

        for(int row = 0; row < 9; row++)
        {
            if(row != i && grid[i][j] == grid[row][j] )
            {
                return false;
            }
        }

        for(int row = (i / 3) * 3; row < (i/3) * 3 + 3; row++)
        {
            for(int col= (j/3) * 3; row < (j/3)* 3 + 3; col++)
            {
                if (row != i && col != j && grid[row][col] == grid[i][j])
                {
                    return false;
                }
            }
        }
        return true;
    }



}