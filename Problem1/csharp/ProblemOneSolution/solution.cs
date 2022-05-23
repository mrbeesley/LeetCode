namespace ProblemOneSolution.Solve;

public static class Solution 
{
    public static int[] TwoSum(int[] nums, int target)
    {
        for(int x = 0; x < nums.Length; x++)
        {
            var operandOne = nums[x];
            for(int y = 0; y < nums.Length; y++)
            {
                if(x == y) continue;
                var operandTwo = nums[y];
                if(operandOne + operandTwo == target) return new int[] {x, y};
            }
        }
        throw new InvalidDataException("The inputs did not produce a solution");
    }

    public static int[] TwoSumOptimal(int[] nums, int target)
    {
        var values = new Dictionary<int, int>();
        for(int x = 0; x < nums.Length; x++)
        {
            if (!values.ContainsKey(nums[x]))
                values.Add(nums[x], x);
        }
            
        for(int i = 0; i < nums.Length; i++)
        {
            var complement = target - nums[i];
            if (values.ContainsKey(complement) && values[complement] != i) 
                return new int[]{i, values[complement]};
        }
        
        throw new InvalidDataException("The inputs did not produce a solution");
    }
}