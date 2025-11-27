# Bell Curve

 **Title:** Understanding Normal Distributions (Gaussian Distribution)

Normal distributions, also known as Gaussian distributions, are a type of continuous probability distribution that are crucial in statistics and various fields such as machine learning, physics, and engineering. They're characterized by their symmetric bell-shaped curve.

**Key Parameters:** The normal distribution has two main parameters: the mean (μ) and variance (σ²).

1. **Mean (μ):** Represents the center or location of the distribution. In a standard normal distribution, μ is 0.
2. **Variance (σ²):** Measures the spread or dispersion of the data around the mean. In a standard normal distribution, σ² is 1.

**Probability Density Function (PDF):** The probability density function (PDF) describes the shape of the normal distribution curve. For a normal distribution with mean μ and variance σ², the PDF is defined as:

f(x) = (1 / (√(2πσ²))) * e^(-(x - μ)² / (2σ²))

**Standard Normal Distribution:** A standard normal distribution has a mean of 0 and variance of 1. It's denoted by N(0, 1). When dealing with a standard normal distribution, we often use z-scores to represent points along the curve in terms of their number of standard deviations from the mean.

**Cumulative Distribution Function (CDF):** The CDF is the integral of the PDF and gives the probability that a random variable will take on a value less than or equal to a specific point. For a standard normal distribution, the CDF is denoted by Φ(z).

The normal distribution has several properties that make it particularly useful:

1. **Symmetry:** The normal distribution is symmetric around its mean. This means that μ = -σ² * (2 * PHI(-z)) for any z.
2. **Standardization:** Any normally distributed variable can be standardized by subtracting the mean and dividing by the standard deviation, resulting in a standard normal distribution.
3. **Sum of Normals is Normal:** If X1 ~ N(μ1, σ1²) and X2 ~ N(μ2, σ2²), then X1 + X2 follows a normal distribution with mean (μ1 + μ2) and variance (σ1² + σ2²).

**Notation:** The probability density of the standard Gaussian distribution is often denoted by φ(z) or ϕ(z), while the cumulative distribution function is denoted by Φ(z). When a random variable X follows a normal distribution with mean μ and variance σ², we may write X ~ N(μ, σ²).

**References:**
- [Wikipedia Entry](https://en.wikipedia.org/wiki/Bell_Curve)