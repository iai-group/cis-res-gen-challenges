# Queries

In our user studies, we consider only CAsT'20 and CAsT'22 datasets. The 2019 edition has relatively low complexity compared to these two, while the 2021 dataset provides relevance assessments on the level of documents instead of passages. For each user study, we select a set of ten queries from the TREC CAsT’20 and ’22 collections that are susceptible to one of the identified problems.  

## Answerability Study

To identify queries that face the problem of unanswerability (i.e., queries for which answers have not been found), we use the information nugget annotations from **CAsT-snippets dataset**[^1] to indicate whether the answer or part of it has been found in the top retrieved passages. We aim to select queries that are not widely covered in the corpus and for which retrieving the answer was challenging. Based on the annotations provided in the CAsT-snippets dataset, we select queries that contain annotated snippets in some but not all of the top 5 passages according to the relevance scores provided in TREC CAsT datasets.

![alt text](/data/queries/answerability/unanswerability_question_selection.png)

This way, we ensure that the query faces the problem of unanswerability, but some passages contain information that can be used to generate accurate responses. 

In the first step, we exclude from this study the queries that are fully answerable or fully unanswerable given the top 5 passages (queries for which at least 2 out of 3 annotators found snippets in 4 or 5 passages; queries for which at least 2 out of 3 annotators did not find any snippets in 4 or 5 passages). More precisely, we select queries for which at least 2 out of 3 annotators decided that there is no answer present in 2 or 3 passages out of 5 (a list of candidate queries can be found [here](data/queries/answerability/candidate_questions.csv)). In the second step, these queries are sorted with respect to relevance scores of passages without answers provided by TREC organizers. Passages with high relevance scores but with no answer identified are exceptionally challenging because they are highly relevant to the question even though they do not provide the exact answer. The 10 queries from the top of the list are included in our study. After selecting potential candidates, we randomly select only one query per topic to maintain the topical diversity of the study. The queries used in the *answerability study* can be found [here](data/responses/answerability_data.csv).

## Viewpoints Study

Open-ended queries about intricate topics with multiple aspects or contentious topics where multiple viewpoints are possible are specifically prone to incomplete responses. To identify such queries in TREC CAsT collections, we:
1. manually select a subset of potential candidates and 
2. ask users to prioritize the selected queries in terms of their controversy and broadness. 

In step 1) we attempt to identify queries related to politics, society, environment, science, education, and technology. Queries that are strongly dependent on the conversational context or require background knowledge provided in previous responses are not taken into account. A list of candidate queries can be found [here](data/queries/viewpoints/candidate_questions.csv).

In step 2) we run a small crowdsourcing task where users are presented with a question and asked to assess on an ordinal scale of 1-5 its controversy and broadness. Based on the collected judgments, we select the top 12 queries for which we generate different variants of the responses. Specifically, we set a threshold on broadness for 3 on a scale of 1--5, then sort by controversy score and take the top-scoring question per topic. The results of this crwodsourcing task can be found [here](data/queries/viewpoints/crowdsourcing_results.csv) At this stage, we select two additional queries to run an additional validation step. Twelve queries for which we generate responses in the *viewpoints study* can be found [here](data/queries/viewpoints/potential_input_data.csv). The queries used in the *viewpoints study* can be found [here](data/responses/viewpoints_input_data.csv).

[^1]: Reference and link to the GitHub repository are removed to preserve anonymity; it will be added upon paper acceptance.