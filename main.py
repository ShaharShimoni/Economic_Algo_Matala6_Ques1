# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List

class Agent:
    worth_for_me=[]
    without_me=[]
    my_max=0;   # max value without the agent
    def value(self,option:int)->float:
        return self.worth_for_me[option];

def vcg(agents:List[Agent],num_options:int):
    max=0;
    # finds the max:
    max_option=0;
    for i in range(0,num_options):
        sum = 0;
        for j in agents:  #pass all the agents
            sum+=j.value(i); # what is the value for this agent
        for j in agents:  #the options without each agent
            j.without_me[i]=sum-j.value(i);
        if sum>max:  #better option
            max=sum;
            max_option=i;  #saves this option

    #print("without each agent");
    #for j in agents:  # the options without each agent
        #print(j.without_me);

    print("The chosen option is",max_option+1,".");
    count=1;
    for j in agents:   #all the agents
         max_2=0;
         for i in range(0, num_options):  # all options
             if j.without_me[i]>max_2:
                 max_2=j.without_me[i];
                 j.my_max=max_2;   # max value without agent j
         print("Agent #",count,"pays",j.my_max-j.without_me[max_option],".");
         count+=1;


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
   #first example from class:
    one=Agent();
    two = Agent();
    three = Agent();

    worth_for_one=[8,4,3];
    worth_for_two = [5,8,1];
    worth_for_three = [3,5,3];

    one.worth_for_me=worth_for_one;
    two.worth_for_me=worth_for_two;
    three.worth_for_me=worth_for_three;

    one.without_me=[0,0,0];
    two.without_me=[0,0,0];
    three.without_me=[0,0,0];


    array_Agent=[one,two,three];

    #for j in array_Agent:  # the options without each agent
        #print(j.worth_for_me);

    vcg(array_Agent, 3);

# second example from class:
    print(" ");
    a=Agent();
    b = Agent();
    c = Agent();
    worth_for_a = [7,0,0,0];
    worth_for_b = [0,8,0,0];
    worth_for_c = [0,0,4,0];

    a.worth_for_me = worth_for_a;
    b.worth_for_me = worth_for_b;
    c.worth_for_me = worth_for_c;

    a.without_me = [0, 0, 0,0];
    b.without_me = [0, 0, 0,0];
    c.without_me = [0, 0, 0,0];

    array_Agent2 = [a, b, c];
    vcg(array_Agent2, 4);




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
