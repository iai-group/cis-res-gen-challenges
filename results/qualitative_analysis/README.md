# Results of Qualitative Analysis

The following sections provides details about the qualitative analysis of the comments provided by crowd workers in both user studies.

## Semantic Analysis

The first step in our qualitative analysis was sentiment analysis using LLMs. We used [SiEBERT - English-Language Sentiment Classification](https://huggingface.co/siebert/sentiment-roberta-large-english) model available at HuggingFace to generate semantic labels for the comments collected in both user studies. 

Data collected in both user studies along with sentiment labels can be found [here](../user_study_output/answerability/processed/aggregated_output_sentiment_labels.csv) for the *answerability study* and [here](../user_study_output/viewpoints/processed/aggregated_output_sentiment_labels.csv) for the *viewpoints study*.

Sentiment labels can be obtained by running [this script](../../scripts/data_analysis/sentiment_analysis.py) using the following command:

`` python -m scripts.data_analysis.sentiment_analysis ``

## Manual Annotation of Comments

In an attempt to explain the overall satisfaction with the response using natural language comments provided by the crowd workers, we manually label 360 user comments in the answerability study and 270 in the viewpoints study. The manual labels can be found [here](answerability_study.csv) for the *answerability study* and [here](viewpoints_study.csv) for the *viewpoints study*.

We count the appearance of every label used in our annotation process for every combination of the experimental condition and satisfaction score. The results can be found [here](answerability_study-qualitative_analysis.csv) for the *answerability study* and [here](viewpoints_study-qualitative_analysis.csv) for the *viewpoints study*.

### Analysis of the results

*Note: The numbers provided in parentheses in the following analysis indicate the number of comments with high/low satisfaction scores out of all the comments that mention the given feature.*

Coherence, fluency, naturalness, details, and logic of the response mentioned in the comments are always accompanied by high satisfaction scores (71/71 in the *answerability study* and 23/23 in the *viewpoints study*).

In the *answerability study*, comments mentioning factual correctness (68/71), completeness of provided information (55/55), agreement with the response (27/27), presence (32/36), and credibility (10/13) of the source are accompanied by high satisfaction scores (3 or 4). However, high satisfaction scores are not always paired with positive comments. Some of the comments indicating a lack of source (12/14) or invalid source (7/8) are still accompanied by high satisfaction scores. Additionally, pointing out in the comments missing or incomplete information (49/93) does not cause a decrease in the satisfaction score. 

In the *viewpoints study*, comments indicating high diversity (55/58), balance (6/6), lack of bias (12/13), completeness of the provided response (22/22), or agreement with the answer (8/9) are accompanied by high satisfaction scores. However, some of the responses described as biased (11/25) or not diverse (21/64) are still given high satisfaction scores. Most of the responses described as not diverse (43/64) or imbalanced (12/22) are accompanied by low satisfaction scores (1 or 2).

Additional aspects mentioned in the comments include the usefulness (10/11 comments accompanied by high satisfaction score) and subjectivity (8/17 comments accompanied by low satisfaction score) of the response in the *answerability study*, and lack of source (4/12 comments accompanied by low satisfaction score) in the *viewpoints study*.