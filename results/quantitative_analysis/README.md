# Results of Quantitative Analysis

The following sections provides the results reported in the paper along with the scripts used to generate the numbers.

## One-way ANOVA

### One-way ANOVA for experimental condition

Answerability Study: 

| Dependent Variable | Independent Variable(s) | F | p-value | Unbalanced Estimator | Effect Size |
| --- | --- | --- | --- | --- | --- |
|Factual Correctness | Experimental Condition | 1.33 | 0.264 | 0.003 | -- |
|Confidence in Answer Accuracy | Experimental Condition | 0.721 | 0.54 | -0.002 | -- |
|Overall Satisfaction | Experimental Condition | 1.19 | 0.313 | 0.002 | -- |

Viewpoints Study:

| Dependent Variable | Independent Variable(s) | F | p-value | Unbalanced Estimator | Effect Size |
| --- | --- | --- | --- | --- | --- |
|Diversity | Experimental Condition |  31.774 |  0.0 |  0.186 | L |
|Transparency | Experimental Condition |  21.751 |  0.0 |  0.133 | M |
|Balance | Experimental Condition |  17.514 |  0.0 |  0.109 | M |
|Overall Satisfaction | Experimental Condition |  17.687 |  0.0 |  0.11 | M |

### One-way ANOVA for query

Answerability Study:

| Dependent Variable | Independent Variable(s) | F | p-value | Unbalanced Estimator | Effect Size |
| --- | --- | --- | --- | --- | --- |
| Familiarity | Query |  19.067 |  0.0 |  0.311 | L |
|Factual Correctness | Query | 1.858 | 0.057 | 0.021 | S |
|Confidence in Answer Accuracy | Query | 1.4 | 0.187 | 0.01 | S |
|Overall Satisfaction | Query |  3.44 |  0.0 |  0.057 | S |

Viewpoints Study:

| Dependent Variable | Independent Variable(s) | F | p-value | Unbalanced Estimator | Effect Size |
| --- | --- | --- | --- | --- | --- |
|Familiarity | Query |  10.186 |  0.0 |  0.234 | L |
|Diversity | Query | 1.135 | 0.338 | 0.004 | -- |
|Transparency | Query | 0.979 | 0.458 | -0.001 | -- |
|Balance | Query |  2.136 |  0.027 |  0.036 | S |
|Overall Satisfaction | Query |  2.698 |  0.005 |  0.054 | S |

### One-way ANOVA for the background knowledge

Answerability Study:

| Dependent Variable | Independent Variable(s) | F | p-value | Unbalanced Estimator | Effect Size |
| --- | --- | --- | --- | --- | --- |
|Factual Correctness | Familiarity | 0.828 | 0.479 | -0.001 | -- |
|Confidence in Answer Accuracy | Familiarity | 0.466 | 0.706 | -0.004 | -- |
|Overall Satisfaction | Familiarity | 1.564 | 0.198 | 0.005 | -- |

Viewpoints Study:

| Dependent Variable | Independent Variable(s) | F | p-value | Unbalanced Estimator | Effect Size |
| --- | --- | --- | --- | --- | --- |
|Diversity | Familiarity | 1.041 | 0.375 | 0.0 | -- |
|Transparency | Familiarity | 0.831 | 0.478 | -0.002 | -- |
|Balance | Familiarity | 0.565 | 0.639 | -0.005 | -- |
|Overall Satisfaction | Familiarity | 1.034 | 0.378 | 0.0 | -- |

The results are generated using [this script](../../scripts/data_analysis/anova.py) and the following command:

`` python -m scripts.data_analysis.anova --type one-way ``

## Two-way ANOVA

### Two-way ANOVA for the interactions between experimental condition and familiarity

Answerability Study:

| Dependent Variable | Independent Variable(s) | F | p-value | Unbalanced Estimator | Effect Size |
| --- | --- | --- | --- | --- | --- |
| Factual Correctness | Experimental Condition | 1.475 | 0.221 | 0.004 | - |
| Factual Correctness | Familiarity | 0.983 | 0.401 | -0.0 | - |
| Factual Correctness | Experimental Condition:Familiarity | 0.51 | 0.867 | -0.012 | - |
| Confidence in Answer Accuracy | Experimental Condition | 0.77 | 0.512 | -0.002 | - |
| Confidence in Answer Accuracy | Familiarity | 0.522 | 0.668 | -0.004 | - |
| Confidence in Answer Accuracy | Experimental Condition:Familiarity | 0.282 | 0.98 | -0.018 | - |
| Overall Satisfaction | Experimental Condition | 1.205 | 0.308 | 0.002 | - |
| Overall Satisfaction | Familiarity | 1.573 | 0.196 | 0.005 | - |
| Overall Satisfaction | Experimental Condition:Familiarity | 0.732 | 0.679 | -0.007 | - |

Viewpoints Study:

| Dependent Variable | Independent Variable(s) | F | p-value | Unbalanced Estimator | Effect Size |
| --- | --- | --- | --- | --- | --- |
|  Diversity |  Experimental Condition |  30.474 |  0.0 |  0.179 |  L |
| Diversity | Familiarity | 0.312 | 0.816 | -0.008 | - |
| Diversity | Experimental Condition:Familiarity | 1.565 | 0.158 | 0.012 | S |
|  Transparency |  Experimental Condition |  20.813 |  0.0 |  0.128 |  M |
| Transparency | Familiarity | 0.352 | 0.788 | -0.007 | - |
| Transparency | Experimental Condition:Familiarity | 1.269 | 0.272 | 0.006 | - |
|  Balance |  Experimental Condition |  16.83 |  0.0 |  0.105 |  M |
| Balance | Familiarity | 0.209 | 0.89 | -0.009 | - |
| Balance | Experimental Condition:Familiarity | 1.282 | 0.266 | 0.006 | - |
|  Overall Satisfaction |  Experimental Condition |  17.693 |  0.0 |  0.11 |  M |
| Overall Satisfaction | Familiarity | 1.08 | 0.358 | 0.001 | - |
| Overall Satisfaction | Experimental Condition:Familiarity | 1.322 | 0.247 | 0.007 | - |

### Two-way ANOVA for the interactions between experimental condition and query

Answerability Study:

| Dependent Variable | Independent Variable(s) | F | p-value | Unbalanced Estimator | Effect Size |
| --- | --- | --- | --- | --- | --- |
| Factual Correctness | Experimental Condition | 1.466 | 0.224 | 0.004 | -- |
| Factual Correctness | Query | 2.011 | 0.038 | 0.025 |  S |
| Factual Correctness | Experimental Condition * Query  | 2.017 | 0.003 | 0.071 |  M |
| Confidence in Answer Accuracy | Experimental Condition | 0.772 | 0.51 | -0.002 | -- |
| Confidence in Answer Accuracy | Query | 1.481 | 0.154 | 0.012 | S |
| Confidence in Answer Accuracy |  Experimental Condition * Query  | 1.775 | 0.012 | 0.055 |  S |
| Overall Satisfaction | Experimental Condition | 1.341 | 0.261 | 0.003 | -- |
| Overall Satisfaction |  Query | 3.659 | 0.0 | 0.062 |  M |
| Overall Satisfaction |  Experimental Condition * Query  | 1.786 | 0.011 | 0.056 |  S |

Viewpoints Study:

| Dependent Variable | Independent Variable(s) | F | p-value | Unbalanced Estimator | Effect Size |
| --- | --- | --- | --- | --- | --- |
| Diversity |  Experimental Condition | 34.433 | 0.0 | 0.198 |  L |  
| Diversity | Query | 1.505 | 0.147 | 0.017 | S |
| Diversity |  Experimental Condition * Query | 1.989 | 0.011 | 0.062 |  M |
| Transparency |  Experimental Condition | 21.514 | 0.0 | 0.132 |  M |
|Transparency | Query | 1.118 | 0.35 | 0.004 | -- |
|Transparency | Experimental Condition * Query  | 0.779 | 0.724 | -0.015 | -- |
| Balance  |  Experimental Condition | 18.373 | 0.0 | 0.114 |  M |
| Balance |  Query | 2.423 | 0.012 | 0.045 |  S |
| Balance | Experimental Condition * Query  | 1.015 | 0.443 | 0.001 | -- |
| Overall Satisfaction |  Experimental Condition | 19.503 | 0.0 | 0.121 |  M |
| Overall Satisfaction | Query | 3.165 | 0.001 | 0.067 |  M |
|Overall Satisfaction | Experimental Condition * Query  | 1.441 | 0.113 | 0.029 |  S |

The results are generated using [this script](../../scripts/data_analysis/anova.py) and the following command:

`` python -m scripts.data_analysis.anova --type two-way ``

## Generalized Linear Models

Answerability Study:

| Dependent Variable | Explanatory Variables | p-value |
| --- | --- | --- |
| Familiarity | Factual Correctness | 0.117 | 
| Familiarity | Confidence in Answer Accuracy | 0.412 | 
| Familiarity | Overall Satisfaction | 0.007 | 
| Overall Satisfaction | Familiarity | 0.248 |
| Overall Satisfaction | Factual Correctness | 0.069 |
| Overall Satisfaction | Confidence in Answer Accuracy | 0.012 | 

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
| age | 18-30 | 3 | 3 |
| age | 31-45 | 17 | 12 |
| age | 46-60 | 12 | 10 |
| age | 60+ | 3 | 2 |
| age | Prefer not to say | 1 | 0 |
| education | High School | 11 | 8 |
| education | Bachelor's Degree | 21 | 16 |
| education | Master's Degree | 3 | 2 |
| education | Ph.D. or higher | 1 | 0 |
| education | Prefer not to say | 0 | 1 |
| gender | Male | 20 | 15 |
| gender | Female | 16 | 12 |
| gender | Other | 0 | 0 |
| gender | Prefer not to say | 0 | 0 |