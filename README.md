# Modified BlackJack: Achieve 31
## Assignment 1, COL870 @ IIT Delhi

Modified Blackjack [(Achieve 31)](https://docs.google.com/document/d/1X27z_b080tR1UamYVrZKEKYOMewKCnaHXBnJvbxugDY/edit) using Reinforcement Learning: 

We would like to implement and play a Game similar to the Blackjack given in Sutton and Barto (5.3) with some differences in the rules of the game which are mentioned in the Jupyter notebook _Acheive31.ipynb_

Deatils of the implementation can be found out in the document _Report.pdf_

State space is described by a tuple <dealer showing card, agent sum, usable 1, usable 2, usable 3>. Refer the report for seeing what 'usable' means.
The class _Environment_ models the environment and moves to the next state based on the action taken by the agent. The moves of the dealer are simulated as part of the environment model. In the following, a Model-free setting is assumed, i.e., agent does not know the environment model and can act only based on its past experience. In particular, it contains two public APIs as follows (taking example of python for syntax):
* ```reset()```: Resets the environment and returns initial state of the environment.
```
def reset():
	stuff()
	return initial_state
```

* ```step()```: Takes an action and moves to next_state. Returns next_state, reward associated with the transition and done representing end of episode.
```
def step(action):
	action_based_stuff()
	return next_state, reward, done
```
#### Policy Evaluation
Assuming that the agent follows the following strategy: keep on playing until it can reach a sum of 25 or more using its current cards. Once this happens, stick. This policy is identical to the Dealer’s policy.

Following methods are used to evaluate the Q-value function (for each state action pair) using the following methods:
1. Monte Carlo - both first-visit and every visit.
2. k-step TD with values of k going from 1, 3, 5, 10, 100 and 1000. This experiment is repeated after taking averages over 100 runs and 1000 runs in each case.
Diagrams similar to the ones used by Sutton and Barto for plotting the value-function are shown below. X-Y plane is used to denote the current state (dealer showing card and agent sum, with 27 different plots for each value of usuables), and Z-axis to denote the value of each state.
Following plots are shown for usables (0,0,0)
- MC every visit !(https://github.com/navreeetkaur/blackjack/blob/master/all%20plots/MC/10000-0-0-0-every.png) MC first visit !(https://github.com/navreeetkaur/blackjack/blob/master/all%20plots/MC/10000-0-0-0-first.png)
- 1 step TD (V averaged over 1000 runs) !(https://github.com/navreeetkaur/blackjack/blob/master/all%20plots/TD/1TD-num1000-(0-0-0).png) 3 step TD (V averaged over 1000 runs) !(https://github.com/navreeetkaur/blackjack/blob/master/all%20plots/TD/3TD-num1000-(0-0-0).png)
- 5 step TD (V averaged over 1000 runs) !(https://github.com/navreeetkaur/blackjack/blob/master/all%20plots/TD/5TD-num1000-(0-0-0).png) 10 step TD (V averaged over 1000 runs) !(https://github.com/navreeetkaur/blackjack/blob/master/all%20plots/TD/10TD-num1000-(0-0-0).png)
- 100 step TD (V averaged over 1000 runs) !(https://github.com/navreeetkaur/blackjack/blob/master/all%20plots/TD/100TD-num1000-(0-0-0).png) 1000 step TD (V averaged over 1000 runs) !(https://github.com/navreeetkaur/blackjack/blob/master/all%20plots/TD/1000TD-num1000-(0-0-0).png)

#### Policy Control
* Implement the following methods to learn the optimal policy:
	*  k-step lookahead SARSA. Use an epsilon-greedy policy with a fixed value of epsilon = 0.1. Use the values of k=1, 10, 100, 1000. 
	* k-step lookahead SARSA. Use an epsilon-greedy policy. Starting with a value of epsilon = 0.1, gradually decay it inversely proportional to the number of iterations (i.e., one update corresponds to one iteration). Use the values of k=1, 10, 100, 1000 as earlier.
	* Q-learning with a 1-step greedy look-ahead policy for update and epsilon-greedy policy for exploration in the environment with a fixed epsilon value of 0.1.
	* Forward view of the eligibility traces for TD(0.5) using on-policy control. Decay epsilon inversely proportional to the number of iterations starting with a value of 0.1.  
* Run each of your algorithms for 100 episodes. Use alpha (learning rate) = 0.1. For each algorithm, plot the performance (on a single graph) with number of episodes on x-axis and reward (averaged over 10 different runs) on y-axis. Which algorithm is able to learn the fastest? Comment.
* Next train each of your algorithms for 100,000 episodes. For each algorithm, generate a set of 10 new (test) episodes by playing the game using your trained algorithm. Generate a new test set of 10 different episodes by playing with your learned algorithm in each case. Compute the performance of each of the algorithms averaged over this test set. Use alpha (learning rate) = 0.1. Next, repeat the entire experiment by learning the models for alpha values in the set {0.1, 0.2, 0.3, 0.4, 0.5}. Plot the average test performance on y-axis with alpha value on x-axis. What do you observe? Does alpha values have any impact on the final learned model?
* Plot the value function for each actionable state for your optimal policy obtained by algorithm in 1(d) above (i.e., TD(0.5) with decaying epsilon). Use alpha - 0.1. How different is the optimal state value function from the one observed using the fixed policy described earlier in the Policy Evaluation section. Comment on your observations.


