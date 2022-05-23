using ProblemOneSolution.Solve;

// See https://aka.ms/new-console-template for more information
Console.WriteLine("Running test set for problem 1");

Console.WriteLine("Test 1: ");
var answer = Solution.TwoSum(new int[]{2,7,11,15}, 9);
Console.WriteLine($"Answer for nums = [2,7,11,15] and target = 9 is [{answer[0]}, {answer[1]}]");

Console.WriteLine("Test 2: ");
answer = Solution.TwoSum(new int[]{3, 2, 4}, 6);
Console.WriteLine($"Answer for nums = [3,2,4] and target = 6 is [{answer[0]}, {answer[1]}]");

Console.WriteLine("Test 3: ");
answer = Solution.TwoSum(new int[]{3, 3}, 6);
Console.WriteLine($"Answer for nums = [3,3] and target = 6 is [{answer[0]}, {answer[1]}]");