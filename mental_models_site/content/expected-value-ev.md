# Expected Value (EV)

 **Expected Value: A Powerful Mental Model for Decision-Making**

The mental model of Expected Value is a fundamental concept in probability theory, serving as a generalization of the weighted average. It provides a mathematical framework for assessing the possible outcomes and their probabilities in uncertain situations, allowing individuals to make informed decisions that maximize potential benefits and minimize risks.

In simple terms, Expected Value calculates the long-term average outcome of an event by multiplying each possible result by its probability and summing them up. If all possible outcomes are equiprobable, the expected value is equivalent to the standard average. However, in more complex scenarios where some outcomes are more likely than others, the expected value takes these probabilities into account.

**Calculating Expected Value for Finite Outcomes:**

Let's consider a concrete example: suppose we roll a fair six-sided die. The possible values for X (the number of pips showing on the top face) are 1, 2, 3, 4, 5, and 6, with each outcome being equally likely with a probability of 1/6. To find the expected value of X, we calculate:

E[X] = 1*1/6 + 2*1/6 + 3*1/6 + 4*1/6 + 5*1/6 + 6*1/6 = 7/2 or approximately 3.5

If we roll the die n times and compute the average, the strong law of large numbers states that as n grows, the average will almost surely converge to E[X].

**Calculating Expected Value for Countably Infinite Outcomes:**

In some cases, a random variable may have countably infinite possible outcomes. To handle these situations, we define the expected value as an infinite sum where each outcome is weighted by its probability:

E[X] = ∑(i=1)^∞ x_i * p_i

However, when dealing with infinite sums, there are potential issues related to ordering and convergence. As a result, many mathematical textbooks only consider the case that the infinite sum converges absolutely, which ensures that the expected value is a finite number independent of the order of the summands. If the infinite sum does not converge absolutely, the random variable does not have a finite expectation.

**Applying Expected Value to Real-World Decisions:**

The concept of Expected Value can be applied to various real-world scenarios, such as betting in games of chance or making investment decisions. By analyzing potential outcomes and their probabilities, individuals can make informed decisions that maximize their potential benefits and minimize their risks.

For example, consider a roulette game with 38 numbered pockets where a $1 bet on a single number yields a payoff of $35 if the ball lands on the chosen number. The expected profit from such a bet is:

E[gain] = -$1 * (37/38) + $35 * (1/38) = -$1 / 19

This means that, in the long run, one would expect to lose approximately $10 for every 19 bets on a single number. Understanding this expected value can help players make informed decisions about their betting strategies.

In conclusion, the Expected Value mental model is a powerful tool for making decisions in uncertain situations. By calculating and analyzing potential outcomes and their probabilities, individuals can make informed decisions that maximize their potential benefits and minimize their risks.