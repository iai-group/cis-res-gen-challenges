# Results of Quantitative Analysis

The following sections provides the results reported in the paper along with the scripts used to generate the numbers.

## One-way ANOVA

### One-way ANOVA for experimental condition

Answerability Study: 

| Dependent Variable | Independent Variable(s) | F | p-value | Unbalanced Estimator | Effect Size |
| --- | --- | --- | --- | --- | --- |
|Factual Correctness | Experimental Condition | 2.5 | 0.058 | 0.005 | -- |
|Confidence in Answer Accuracy | Experimental Condition | 0.588 | 0.623 | -0.001 | -- |
|Overall Satisfaction | Experimental Condition | 1.003 | 0.391 | 0.0 | -- |

Viewpoints Study:

| Dependent Variable | Independent Variable(s) | F | p-value | Unbalanced Estimator | Effect Size |
| --- | --- | --- | --- | --- | --- |
|Diversity | Experimental Condition |  31.774 | 0.0 | 0.186 | L |
|Transparency | Experimental Condition | 21.751 | 0.0 | 0.133 | M |
|Balance | Experimental Condition |  17.514 | 0.0 | 0.109 | M |
|Overall Satisfaction | Experimental Condition | 17.687 | 0.0 | 0.11 | M |

### One-way ANOVA for query

Answerability Study:

| Dependent Variable | Independent Variable(s) | F | p-value | Unbalanced Estimator | Effect Size |
| --- | --- | --- | --- | --- | --- |
| Familiarity | Query |  9.022 | 0.0 | 0.07 | M |
|Factual Correctness | Query | 3.538 | 0.0 | 0.023 | S |
|Confidence in Answer Accuracy | Query | 2.223 | 0.019 | 0.011 | S |
|Overall Satisfaction | Query | 5.051 | 0.0 | 0.037 | S |

Viewpoints Study:

| Dependent Variable | Independent Variable(s) | F | p-value | Unbalanced Estimator | Effect Size |
| --- | --- | --- | --- | --- | --- |
|Familiarity | Query | 10.186 | 0.0 | 0.234 | L |
|Diversity | Query | 1.135 | 0.338 | 0.004 | - |
|Transparency | Query | 0.979 | 0.458 | -0.001 | - |
|Balance | Query |  2.136 | 0.027 | 0.036 | S |
|Overall Satisfaction | Query | 2.698 | 0.005 | 0.054 | S |

### One-way ANOVA for the background knowledge

Answerability Study:

| Dependent Variable | Independent Variable(s) | F | p-value | Unbalanced Estimator | Effect Size |
| --- | --- | --- | --- | --- | --- |
|Factual Correctness | Familiarity | 4.326 | 0.005 | 0.01 | S |
|Confidence in Answer Accuracy | Familiarity | 16.374 | 0.0 | 0.046 | S |
|Overall Satisfaction | Familiarity | 23.738 | 0.0 | 0.066 | M |

Viewpoints Study:

| Dependent Variable | Independent Variable(s) | F | p-value | Unbalanced Estimator | Effect Size |
| --- | --- | --- | --- | --- | --- |
|Diversity | Familiarity | 1.041 | 0.375 | 0.0 | - |
|Transparency | Familiarity | 0.831 | 0.478 | -0.002 | - |
|Balance | Familiarity | 0.565 | 0.639 | -0.005 | -  |
|Overall Satisfaction | Familiarity | 1.034 | 0.378 | 0.0 | - |

The results are generated using [this script](../../scripts/data_analysis/anova.py) and the following command:

`` python -m scripts.data_analysis.anova --type one-way ``

### Power Analysis

The power analysis, employing results of one-way ANOVA with the experimental condition as an independent variable and the user-reported values for the main response dimension (factual correctness for the *answerability study* and diversity for the *viewpoints study*) as a dependent variable, was conducted using data collected in the first run. We used the script *future.sample.1wayanova* available [here](https://waseda.app.box.com/v/SIGIR2016PACK) to calculate the power with the following parameters: *F* equal to the corresponding value from the tables above, *m* equal to the number of variants/experimental conditions in user study, and *n* equal to number of workers looking at each variant per topic (9 in the first run).

For the *answerability study*:
- Cohen's f effect size of experimental condition on factuality: 0.11
- Number of workers as a result of power analysis for small effect size (0.1): 1094.17
- Number of workers as a result of power analysis for large effect size (0.4): 72.17

For the *viewpoints study*:
- Cohen's f effect size of experimental condition on diversity: 0.49
- Number of workers as a result of power analysis for small effect size (0.1): 966.47
- Number of workers as a result of power analysis for large effect size (0.4): 63.31

The results indicate that an additional five workers per HIT are required to observe a statistically significant effect of experimental condition on the factual correctness in the *answerability study*, while the 3 workers we initially used in the *viewpoints study* are shown to be sufficient. Additional data for the *answerability study* is collected in the second run with the same worker requirements and rewards. 

The results of the power analysis can be generated using [this script](../../scripts/data_analysis/anova.py) and the following command:

`` python -m scripts.data_analysis.anova --type power-analysis ``

## Two-way ANOVA

### Two-way ANOVA for the interactions between experimental condition and familiarity

Answerability Study:

| Dependent Variable | Independent Variable(s) | F | p-value | Unbalanced Estimator | Effect Size |
| --- | --- | --- | --- | --- | --- |
| Factual Correctness | Experimental Condition | 2.387 | 0.068 | 0.004 | - |
| Factual Correctness | Familiarity | 4.202 | 0.006 | 0.01 | S |
| Factual Correctness | Experimental Condition * Familiarity | 0.69 | 0.718 | -0.003 | - |
| Confidence in Answer Accuracy | Experimental Condition | 0.532 | 0.66 | -0.001 | - |
| Confidence in Answer Accuracy | Familiarity | 16.216 | 0.0 | 0.045 | S |
| Confidence in Answer Accuracy | Experimental Condition * Familiarity | 0.662 | 0.743 | -0.003 | - |
| Overall Satisfaction | Experimental Condition | 0.943 | 0.419 | -0.0 | - |
| Overall Satisfaction | Familiarity | 23.538 | 0.0 | 0.066 | M |
| Overall Satisfaction | Experimental Condition * Familiarity | 0.699 | 0.71 | -0.003 | - |

Viewpoints Study:

| Dependent Variable | Independent Variable(s) | F | p-value | Unbalanced Estimator | Effect Size |
| --- | --- | --- | --- | --- | --- |
| Diversity | Experimental Condition | 30.474 | 0.0 | 0.179 | L |
| Diversity | Familiarity | 0.312 | 0.816 | -0.008 | - |
| Diversity | Experimental Condition * Familiarity | 1.565 | 0.158 | 0.012 | S |
| Transparency | Experimental Condition | 20.813 | 0.0 | 0.128 | M |
| Transparency | Familiarity | 0.352 | 0.788 | -0.007 | - |
| Transparency | Experimental Condition * Familiarity | 1.269 | 0.272 | 0.006 | - |
| Balance | Experimental Condition | 16.83 | 0.0 | 0.105 | M |
| Balance | Familiarity | 0.209 | 0.89 | -0.009 | - |
| Balance | Experimental Condition * Familiarity | 1.282 | 0.266 | 0.006 | - |
| Overall Satisfaction | Experimental Condition | 17.693 | 0.0 | 0.11 | M |
| Overall Satisfaction | Familiarity | 1.08 | 0.358 | 0.001 | - |
| Overall Satisfaction | Experimental Condition * Familiarity | 1.322 | 0.247 | 0.007 | - |

### Two-way ANOVA for the interactions between experimental condition and query

Answerability Study:

| Dependent Variable | Independent Variable(s) | F | p-value | Unbalanced Estimator | Effect Size |
| --- | --- | --- | --- | --- | --- |
| Factual Correctness | Experimental Condition | 2.629 | 0.049 | 0.005 | - |
| Factual Correctness | Query | 3.652 | 0.0 | 0.024 | S |
| Factual Correctness | Experimental Condition * Query | 1.951 | 0.003 | 0.026 | S |
| Confidence in Answer Accuracy | Experimental Condition | 0.613 | 0.607 | -0.001 | - |
| Confidence in Answer Accuracy | Query | 2.288 | 0.015 | 0.012 | S |
| Confidence in Answer Accuracy | Experimental Condition * Query | 2.07 | 0.001 | 0.029 | S |
| Overall Satisfaction | Experimental Condition | 1.068 | 0.362 | 0.0 | - |
| Overall Satisfaction | Query | 5.181 | 0.0 | 0.038 | S |
| Overall Satisfaction | Experimental Condition * Query | 1.898 | 0.004 | 0.025 | S |
Viewpoints Study:

| Dependent Variable | Independent Variable(s) | F | p-value | Unbalanced Estimator | Effect Size |
| --- | --- | --- | --- | --- | --- |
| Diversity | Experimental Condition | 34.433 | 0.0 | 0.198 | L |
| Diversity | Query | 1.505 | 0.147 | 0.017 | S |
| Diversity | Experimental Condition * Query | 1.989 | 0.011 | 0.062 | M |
| Transparency | Experimental Condition | 21.514 | 0.0 | 0.132 | M |
| Transparency | Query | 1.118 | 0.35 | 0.004 | - |
| Transparency | Experimental Condition * Query | 0.779 | 0.724 | -0.015 | - |
| Balance | Experimental Condition | 18.373 | 0.0 | 0.114 | M |
| Balance | Query | 2.423 | 0.012 | 0.045 | S |
| Balance | Experimental Condition * Query | 1.015 | 0.443 | 0.001 | - |
| Overall Satisfaction | Experimental Condition | 19.503 | 0.0 | 0.121 | M |
| Overall Satisfaction | Query | 3.165 | 0.001 | 0.067 | M |
| Overall Satisfaction | Experimental Condition * Query | 1.441 | 0.113 | 0.029 | S |

The results are generated using [this script](../../scripts/data_analysis/anova.py) and the following command:

`` python -m scripts.data_analysis.anova --type two-way ``

## Generalized Linear Models

Answerability Study:

| Dependent Variable | Explanatory Variables | p-value |
| --- | --- | --- |
| Familiarity | Factual Correctness | 0.465 | 
| Familiarity | Confidence in Answer Accuracy | 0.136 | 
| Familiarity | Overall Satisfaction | 0.062 | 
| Overall Satisfaction | Familiarity | 0.388 |
| Overall Satisfaction | Factual Correctness | 0.001 |
| Overall Satisfaction | Confidence in Answer Accuracy | 0.000 | 

Viewpoints Study:

| Dependent Variable | Explanatory Variables | p-value |
| --- | --- | --- |
| Familiarity | Diversity | 0.567 | 
| Familiarity | Transparency | 0.886 | 
| Familiarity | Balance | 0.683 | 
| Familiarity | Overall Satisfaction | 0.848 | 
| Overall Satisfaction | Familiarity | 0.972 |
| Overall Satisfaction | Diversity | 0.209 | 
| Overall Satisfaction | Transparency | 0.436 | 
| Overall Satisfaction | Balance | 0.003 | 

The results are generated using [this script](../../scripts/data_analysis/glm.py) and the following command:

`` python -m scripts.data_analysis.glm ``

## Data distribution

The distribution of user-judged response dimensions per query for both user studies can be generated using [this script](../../scripts/data_analysis/data_distribution.py) and the following command:

`` python -m scripts.data_analysis.data_distribution ``

![](data_distribution.png)

## Demographic information

Demographic information from both user studies can be obtained by running [this script](../../scripts/data_analysis/demographic_information.py) using the following command:

`` python -m scripts.data_analysis.demographic_information ``

| Demographic Information | Option |Answerability User study | Viewpoint User study |
| --- | --- | --- | --- |
| age | 18-30 | 34 | 3 |
| age | 31-45 | 35 | 12 |
| age | 46-60 | 19 | 10 |
| age | 60+ | 7 | 2 |
| age | Prefer not to say | 1 | 0 |
| education | High School | 19 | 8 |
| education | Bachelor's Degree | 59 | 16 |
| education | Master's Degree | 15 | 2 |
| education | Ph.D. or higher | 2 | 0 |
| education | Prefer not to say | 1 | 1 |
| gender | Male | 44 | 15 |
| gender | Female | 52 | 12 |
| gender | Other | 0 | 0 |
| gender | Prefer not to say | 0 | 0 |