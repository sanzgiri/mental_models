# Hick's Law

 **Introduction**

Hick's Law, also known as the Hick-Hyman Law, is a psychological principle that explains how the time it takes for an individual to make a decision increases with the number and complexity of choices available. This mental model has significant implications in various fields such as user experience design, marketing, and cognitive psychology.

**Core Concept**

First proposed by psychologists William Edmund Hick and Ray Hyman in the 1950s, Hick's Law posits that the average reaction time (T) required to choose among n equally probable choices is approximately:

    T = b * log₂(n + 1)

Where 'b' is a constant that can be determined empirically. The logarithmic relationship between decision time and number of options means that increasing the number of choices doesn't necessarily double the decision time; instead, it results in a slower, yet less dramatic increase. If the choices have unequal probabilities, the law can be generalized as:

    T = b * H

Where 'H' is the information-theoretic entropy of the decision, defined as the sum of each alternative's probability multiplied by the logarithm of its inverse plus one.

**Examples**

1. **Menu Design**: A restaurant with a simple menu might have a faster service time compared to one offering hundreds of items, due to the increased complexity and decision-making required for customers. ([Related Model: Fitts's Law](/models/fitts-law))
2. **Election Voting**: In elections with multiple candidates, voters might take longer to decide if there are numerous options. This could potentially impact voter turnout and decision quality.
3. **Product Selection**: Online retailers may experience increased shopping cart abandonment if they present customers with too many product choices, as the customer may struggle to make a decision due to decision paralysis.

**Application**

Understanding Hick's Law can help in making informed decisions about design, product development, and marketing strategies. For example, designers might choose to simplify menus or product offerings to reduce decision fatigue and improve user experience. Similarly, marketers might tailor their messaging to emphasize the most appealing options to guide customer choices.

**Related Models**

1. [Fitts's Law](/models/fitts-law) – another psychological principle that relates the time needed to move a given distance on a target to the size of the target and the accuracy required for the movement.
2. [The Paradox of Choice](/models/paradox-of-choice) - a concept that suggests having too many choices can lead to anxiety, indecision, and dissatisfaction among consumers.

**References**

- [Wikipedia Entry](https://en.wikipedia.org/wiki/Hick%27s_law)
- Cockburn, A., Gutwin, C., & Greenberg, S. (2007). A predictive model of menu performance. Proceedings of the SIGCHI Conference on Human Factors in Computing Systems.
- Hick, W. E. (1952). On the rate of gain of information. Quarterly Journal of Experimental Psychology.
- Hyman, R. (1953). Stimulus information as a determinant of reaction time. Journal of Experimental Psychology.
- Rosati, L. (2013). How to design interfaces for choice: Hick-Hyman law and classification for information architecture. In Slavic, A., Salah, A., & Davies, C. (eds.), Classification and visualization: interfaces to knowledge: proceedings of the International UDC Seminar.
- Seow, S. C. (2005). Information Theoretic Models of HCI: A Comparison of the Hick–Hyman Law and Fitts's Law. Human-Computer Interaction.
- Welford, A. T. (1968). Fundamentals of Skill. Methuen, Massachusetts.