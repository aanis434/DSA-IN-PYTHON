### Recursion with 3 steps

1. Recusion case - the flow
    ``` n = n * factorial(n-1) ```
2. Base case - the stopping citeria
    ``` if n in [0,1]:
        return 1
    ```
3. Unintentional case - the constraint 
    ``` assert n >= 0 and int(n) == n, 'The number must be positive integer.' ```

### Why Recursion?
1. Recursive thinking is really important in programming and it helps you break down big problems into smaller ones and easier to use
2. The prominent usage of recursion in data structes like trees and graphs. 
3. Interviews
4. It is used in many algorithms (divide and conquer, greedy and dynamic programming)

### Recursive vs Iterative Solutions
**Points**              **Recursion**           **Iteration**           **Notes**
* Space efficient?          No                        Yes              No stack memory require in case of iteration
* Time efficient?           No                        Yes              In case of recursion system needs more time for
                                                                       pop and push elements to stack memory which makes recursion less time efficient
* Easy to code?             Yes                       No               We use recursion especially in the case 
                                                                       we know that is a problem can be divided into similar sub problmes.


### When to use recursion?
- When we can easily breakdown a problem into similar subproblem
- When we are fine with extra overhead (both time and space) that comes with it
- When we need a quick working soulution instead of efficient one
- When we use memorizaiton in recursion
    - preorder tree traversal: 15, 9, 3, 1, 4, 12, 23, 17, 28


### When avoid it?
- If time and space complexity matters for us.
- Recursion uses more memory. If we use embedded memory. For example an application that takes more memory in the phone is not efficient
- Recursion can be slow