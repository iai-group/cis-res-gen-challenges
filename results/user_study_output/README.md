# User Study Output

This directory contains data collected in our studies. Raw output from Amazon Mechanical Turk can be found [here](answerability/mturk_output/) for the *answerability study* and [here](viewpoints/mturk_output/) for the *viewpoints study*. 

We used [this script](../../scripts/results_processing/answerability.py) for processing MTurk output for the *answerability study* and [this script](../../scripts/results_processing/viewpoints.py) for processing MTurk output for the *viewpoints study*.

The results aggregated for all the HITs can be found [here](answerability/processed/aggregated_output.csv) for the *answerability study* and [here](viewpoints/processed/aggregated_output.csv) for the *viewpoints study*. The aggregation of the results was done using [this script](../../scripts/results_processing/results_aggregation.py) and the following command:

``python -m scripts.results_processing.results_aggregation --user_study {user_study_name}``

``user_study_name`` in the command above needs to be replace with ``answerability`` or ``viewpoints``.