# Economic_Algo_Matala6_Ques1

A function in Python, which receives a collection of possible results, and the values that each player attributes to each result,
And runs the VCG algorithm.
The function uses the following class:

class Agent:
def value (option: int) -> float: ...
Returns the value of the current player to the input option

And the following function responsible for the algorithm:

def vcg (agents: List [Agent], num_options: int)

Sample output:
The chosen option is 4.
Agent # 0 pays 5.
Agent # 1 pays -4.

In addition there is a test file with the two of the
following examples and the expected results.:

example one:

options    1  2  3
agent 1    8, 4, 3
agent 2    5, 8, 1
agent 3    3, 5, 3

expected result:
The chosen option is 2 .
Agent # 1 pays 0 .
Agent # 2 pays 2 .
Agent # 3 pays 1 .

example two:

options    1  2  3  4
agent 1    7, 7, 0, 0
agent 2    0, 8, 0, 0
agent 3    0, 0, 4, 0

expected result:
The chosen option is 2 .
Agent # 1 pays 0 .
Agent # 2 pays 7 .
Agent # 3 pays 0 .



