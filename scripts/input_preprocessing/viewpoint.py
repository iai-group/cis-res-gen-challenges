import random

import pandas as pd

if __name__ == "__main__":
    input = pd.read_csv("data/input_data/viewpoint_input_data.csv")
    question_sets = pd.read_csv(
        "data/user_study_setup/viewpoint_question_sets.csv"
    )
    question_sets_ids = list(question_sets.columns)[1:]

    for question_set_id in question_sets_ids:
        answers_ids_to_add = dict(
            zip(list(input["Query"]), list(question_sets[question_set_id]))
        )

        answers_to_add = []
        summaries_to_add = []
        summaries_scores_to_add = []

        for question, answer_id in answers_ids_to_add.items():
            input_row = input[input["Query"] == question]

            answers_to_add.append(list(input_row[answer_id])[0])

            summaries = {}
            summaries_columns = [
                "Summary " + answer_id,
                "Summary incorrect 1",
                "Summary incorrect 2",
            ]
            summaries_scores = [1, 0, 0]
            for summary_score, summary_column in zip(
                summaries_scores, summaries_columns
            ):
                summaries[list(input_row[summary_column])[0]] = summary_score

            summaries_keys = list(summaries.keys())
            random.shuffle(summaries_keys)
            summaries_shuffled = [
                (key, summaries[key]) for key in summaries_keys
            ]

            summaries_to_add.append(summaries_keys)
            summaries_scores_to_add.append(
                [summaries[key] for key in summaries_keys]
            )

        question_set_data = pd.DataFrame(
            {
                "questions_ids": list(range(1, 11)),
                "questions": list(input["Query"]),
                "answers": answers_to_add,
                "answers_ids": list(answers_ids_to_add.values()),
                "summaries": summaries_to_add,
                "summaries_scores": summaries_scores_to_add,
            }
        )

        question_set_data = question_set_data.sample(frac=1)
        question_set_data.to_csv(
            "data/input_data/question_sets/viewpoint/QS"
            + question_set_id
            + ".csv",
            index=False,
        )

        question_set_data_mturk_dict = {}

        for column in question_set_data.columns:
            question_set_data_mturk_dict[column] = [
                str(list(question_set_data[column]))
            ]

        question_set_data_mturk = pd.DataFrame(question_set_data_mturk_dict)
        question_set_data_mturk

        question_set_data_mturk.to_csv(
            "data/input_data/question_sets/viewpoint/QS"
            + question_set_id
            + "_input.csv",
            index=False,
        )
