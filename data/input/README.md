# Input Data

The distribution of query-response pairs between questions sets in the user studies can be found [here](answerability_question_sets.csv) for the *answerability study* and [here](viewpoints_question_sets.csv) for the *viewpoints study*. Each column corresponds the question set (one HIT) and each row corresponds to the query in the user study. Cells represent the variant of the response for a given query in a specific question set.

Question sets used as input for the *answerability study* can be found [here](answerability/) (and [here](answerability/mturk_input_format/) in the MTurk input format). Question sets fused as input for the *viewpoints study* can be found [here](viewpoints/) (and [here](viewpoints/mturk_input_format/) in the MTurk input format).

[This script](../../scripts/input_preprocessing/answerability.py) has been used for preparing input for the *answerability study* and [this script](../../scripts/input_preprocessing/viewpoints.py) has been used for preparing input for the *viewpoints study*.
