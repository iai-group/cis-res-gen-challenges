import random

import pandas as pd

if __name__ == "__main__":
    input = pd.read_csv("data/input_data/answerability_input_data.csv")
    question_sets = pd.read_csv(
        "data/user_study_setup/answerability_question_sets.csv"
    )
    question_sets_ids = list(question_sets.columns)[1:]

    for question_set_id in question_sets_ids:
        answers_ids_to_add = dict(
            zip(list(input["Question"]), list(question_sets[question_set_id]))
        )

        answers_to_add = []
        sources_to_add = []
        summaries_to_add = []
        summaries_scores_to_add = []

        for question, answer_id in answers_ids_to_add.items():
            input_row = input[input["Question"] == question]

            answer_column = (
                "A1/A2" if answer_id == "A1" or answer_id == "A2" else "A3/A4"
            )
            answers_to_add.append(list(input_row[answer_column])[0])

            if answer_id == "A1":
                sources_to_add.append(list(input_row["S1"])[0])
            elif answer_id == "A3":
                sources_to_add.append(list(input_row["S3"])[0])
            else:
                sources_to_add.append("")

            summaries = {}
            summaries_columns = [
                "summary correct " + answer_column,
                "summary incorrect " + answer_column,
                "summary incorrect " + answer_column + ".1",
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
                "questions": list(input["Question"]),
                "answers": answers_to_add,
                "answers_ids": list(answers_ids_to_add.values()),
                "sources": sources_to_add,
                "summaries": summaries_to_add,
                "summaries_scores": summaries_scores_to_add,
            }
        )

        question_set_data = question_set_data.sample(frac=1)
        question_set_data.to_csv(
            "data/input_data/question_sets/answerability/QS"
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
        question_set_data_mturk.to_csv(
            "data/input_data/question_sets/answerability/QS"
            + question_set_id
            + "_input.csv",
            index=False,
        )
