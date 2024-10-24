# Results of Qualitative Analysis

The following sections provides details about the qualitative analysis of the comments provided by crowd workers in both user studies.

## Semantic Analysis

The first step in our qualitative analysis was sentiment analysis using LLMs. We used [SiEBERT - English-Language Sentiment Classification](https://huggingface.co/siebert/sentiment-roberta-large-english) model available at HuggingFace to generate semantic labels for the comments collected in both user studies. 

Data collected in both user studies along with sentiment labels can be found [here](../user_study_output/answerability/processed/first_run/aggregated_output_sentiment_labels.csv) for the *answerability study* and [here](../user_study_output/viewpoints/processed/aggregated_output_sentiment_labels.csv) for the *viewpoints study*.

Sentiment labels can be obtained by running [this script](../../scripts/data_analysis/sentiment_analysis.py) using the following command:

`` python -m scripts.data_analysis.sentiment_analysis ``

## Manual Annotation of Comments

In an attempt to explain the overall satisfaction with the response using natural language comments provided by the crowd workers, we manually label 360 user comments in the answerability study and 270 in the viewpoints study. The manual labels can be found [here](answerability_study_first_run.csv) for the first run and [here](answerability_study_second_run.csv) for the second run for the *answerability study* and [here](viewpoints_study.csv) for the *viewpoints study*.

We count the appearance of every label used in our annotation process for every combination of the experimental condition and satisfaction score. The results can be found [here](answerability_study_first_run-qualitative_analysis_stats.csv) for the first run and [here](answerability_study_second_run-qualitative_analysis_stats.csv) for the second run for the *answerability study* and [here](viewpoints_study-qualitative_analysis_stats.csv) for the *viewpoints study*.

### Analysis of the results

We now analyze the open text field comments from Part II of the user studies. To validate our findings, we characterize workers' user experience by analyzing their natural language comments. We manually inspect all the 960 worker comments in the *answerability study* and 270 in the *viewpoints study*. We followed an inductive approach[^1] to identify themes in the comments. After consensus among the authors, one of the authors labeled all comments. Next, we counted how many workers mentioned a particular aspect. While adhering to an established qualitative analysis approach, the authors acknowledge that personal interpretation may introduce some degree of subjectivity in the interpretation and categorization of the data.

*Note: In the reporting below, numbers in parentheses indicate the proportion of high (when the aspect mentioned in the comments is positive) or low (when the aspect is negative) satisfaction ratings corresponding to specific aspects mentioned in the comments. For instance, if three workers mention a positive aspect like "factual correctness" in the open text field, but only two assign high satisfaction scores on the four-point Likert scale, this is reported as 2/3. Conversely, if a negative aspect like "bias" is identified by five workers and four of them express low satisfaction, it is recorded as 4/5.*

Coherence, fluency, naturalness, details, and logic of the response mentioned in the comments are almost always accompanied by high satisfaction ratings (178/185 in the *answerability study* and 23/23 in the *viewpoints study*).

In the *answerability study*, comments mentioning positive aspects such as factual correctness (126/133), information completeness (99/100), agreement with the response (59/60), presence (53/64), and credibility (18/23) of the source are accompanied by high satisfaction ratings (3 or 4 on the Likert scale). However, high satisfaction ratings are not always paired with positive comments. Some comments associated with high satisfaction ratings indicate negative aspects, such as lack of source (4/21) or invalid source (2/11). Additionally, highlighting missing or incomplete information (60/156) does not always cause a decrease in the satisfaction rating. 

In the *viewpoints study*, positive comments indicating high diversity (55/58), balance (6/6), lack of bias (12/13), completeness of the provided response (22/22), or agreement with the answer (8/9) are accompanied by high satisfaction ratings. However, some responses describing negative aspects such as bias (14/25) or lack of diversity (43/64) are still given high satisfaction ratings. Most of the responses described as not diverse (43/64) or imbalanced (12/22) are accompanied by low satisfaction ratings (1 or 2 on the Likert scale).

Additional aspects mentioned in the comments include the usefulness (33/35 comments accompanied by high satisfaction rating) and subjectivity (10/24 comments accompanied by low satisfaction rating) of the response in the *answerability study*, and lack of source (4/12 comments accompanied by low satisfaction rating) in the *viewpoints study*. It is worth pointing out that while usefulness is a common indicator of successful completion of the search task[^2,^3], it is only mentioned in 2.8% of the comments. 

Although satisfaction ratings are skewed (see Data distribution section in [Quantitative Analysis](../quantitative_analysis/README.md)) and other scales such as magnitude estimation[^4] may give us more informative ratings, they are roughly aligned with the dimensions we aim to capture. It implies that the dimensions we use to differentiate between response variants impact user satisfaction. 

Comments from the *answerability study* suggest that satisfaction is associated with both factual correctness and source validity. The frequent user references to factual correctness in comments imply a significant focus on this aspect when evaluating responses. Even though we observe a high correlation between user-reported response dimensions and overall satisfaction, we do not observe a statistically significant effect of the controlled factual correctness on user ratings for this response dimension. This implies that users find these response dimensions important and associate them with their satisfaction, but they are not able to identify factuality correctly in the responses.

Additionally, one-way ANOVA for the *answerability study* revealed that the overall satisfaction is affected by the query and topic familiarity, not the controlled response dimensions. This also explains why the response dimensions mentioned in the comments do not completely align with the actual flaws in the responses. The study's small scale and results sensitivity to the topics may suggest that more queries might reveal the effect of factual correctness and source validity on overall satisfaction.

In the *viewpoints study*, our qualitative analysis shows that user satisfaction is more linked to viewpoint diversity and response completeness than information balance, differing from quantitative findings. It can follow from the fact that the concept of response diversity is better understood by users and is easier to identify. Nevertheless, the qualitative analysis shows that selected response dimensions are indeed common indicators of user satisfaction.

[^1] Williams, J. Patrick. 2008. *Emergent themes, The Sage encyclopedia of qualitative research methods*. Sage Publications. 248-249

[^2] B. Barla Cambazoglu, Valeriia Baranova, Falk Scholer, Mark Sanderson, Leila Tavakoli, and Bruce Croft. 2021. *Quantifying Human-Perceived Answer Utility in Non-factoid Question Answering*. In Proceedings of the 2021 Conference on Human Information Interaction and Retrieval (CHIIR ’21). 75–84

[^3] Jiqun Liu. 2023. *Toward A Two-Sided Fairness Framework in Search and Recommendation*. In Proceedings of the 2023 Conference on Human Information Interaction and Retrieval (CHIIR ’23). 236–246.

[^4] Andrew Turpin, Falk Scholer, Stefano Mizzaro, and Eddy Maddalena. 2015. *The Benefits of Magnitude Estimation Relevance Assessments for Information Retrieval Evaluation*. In Proceedings of the 38th International ACM SIGIR Conference on Research and Development in Information Retrieval (SIGIR ’15). 565–574.