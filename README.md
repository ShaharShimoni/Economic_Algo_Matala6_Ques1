# Economic_Algo_Matala6_Ques1

A function in Python, which receives a collection of possible results, and the values that each player attributes to each result, <br />
And runs the VCG algorithm. <br />
The function uses the following class: <br />
<br />
class Agent:<br />
def value (option: int) -> float: ...<br />
Returns the value of the current player to the input option<br />
<br />
And the function vcg for the algorithm:<br />
<br />
def vcg (agents: List [Agent], num_options: int)<br />
<br />
Sample output:<br />
The chosen option is 4.<br />
Agent # 0 pays 5.<br />
Agent # 1 pays -4.<br />
<br />
In addition there is a test file with the two of the<br />
following examples and the expected results.:<br />
<br />
example one:<br />
<br />
options    1  2  3<br />
agent 1    8, 4, 3<br />
agent 2    5, 8, 1<br />
agent 3    3, 5, 3<br />
<br />
expected result:<br />
The chosen option is 2 .<br />
Agent # 1 pays 0 .<br />
Agent # 2 pays 2 .<br />
Agent # 3 pays 1 .<br />
<br />
example two:<br />
<br />
options    1  2  3  4<br />
agent 1    7, 7, 0, 0<br />
agent 2    0, 8, 0, 0<br />
agent 3    0, 0, 4, 0<br />
<br />
expected result:<br />
The chosen option is 2 .<br />
Agent # 1 pays 0 .<br />
Agent # 2 pays 7 .<br />
Agent # 3 pays 0 .<br />



