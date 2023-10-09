import ast

import pandas as pd

if __name__ == "__main__":
    for output_id in range(1, 10):
        output = pd.read_csv(
            "data/results/viewpoint/mturk_output/QS"
            + str(output_id)
            + "_output.csv"
        )

        summary = [[] for _ in range(10)]
        familiarity = [[] for _ in range(10)]
        diversity = [[] for _ in range(10)]
        transparency = [[] for _ in range(10)]
        bias = [[] for _ in range(10)]
        satisfaction = [[] for _ in range(10)]
        explanation = [[] for _ in range(10)]

        age = []
        education = []
        gender = []

        for row_id, row in output.iterrows():
            for option in ["option_" + str(i) for i in range(1, 6)]:
                if row["Answer.education." + option] == True:
                    education.append(option)
                if row["Answer.age." + option] == True:
                    age.append(option)

            for option in ["option_" + str(i) for i in range(1, 5)]:
                if row["Answer.gender." + option] == True:
                    gender.append(option)

        demographic_info_df = pd.DataFrame(
            {"age": age, "gender": gender, "education": education}
        )
        demographic_info_df

        metrics = [
            "familiarity",
            "diversity",
            "transparency",
            "bias",
            "satisfaction",
        ]

        for row_id, row in output.iterrows():
            questions = ast.literal_eval(row["Input.questions"])
            question_ids = ast.literal_eval(row["Input.questions_ids"])
            for question, question_id in zip(questions, question_ids):
                for option in ["option_" + str(i) for i in range(1, 5)]:
                    if (
                        row[
                            "Answer.familiarity_"
                            + str(question_id)
                            + "."
                            + option
                        ]
                        == True
                    ):
                        familiarity[question_id - 1].append(
                            option.replace("option_", "")
                        )
                    if (
                        row[
                            "Answer.diversity_"
                            + str(question_id)
                            + "."
                            + option
                        ]
                        == True
                    ):
                        diversity[question_id - 1].append(
                            option.replace("option_", "")
                        )
                    if (
                        row[
                            "Answer.transparency_"
                            + str(question_id)
                            + "."
                            + option
                        ]
                        == True
                    ):
                        transparency[question_id - 1].append(
                            option.replace("option_", "")
                        )
                    if (
                        row["Answer.bias_" + str(question_id) + "." + option]
                        == True
                    ):
                        bias[question_id - 1].append(
                            option.replace("option_", "")
                        )
                    if (
                        row[
                            "Answer.satisfaction_"
                            + str(question_id)
                            + "."
                            + option
                        ]
                        == True
                    ):
                        satisfaction[question_id - 1].append(
                            option.replace("option_", "")
                        )
                for option in ["s_" + str(i) for i in range(1, 4)]:
                    if (
                        row["Answer.summary_" + str(question_id) + "." + option]
                        == True
                    ):
                        summary[question_id - 1].append(
                            option.replace("s_", "")
                        )

                explanation[question_id - 1].append(
                    row["Answer.explanation_" + str(question_id)]
                )

        questions = ast.literal_eval(output["Input.questions"][0])

        results_df = pd.DataFrame(
            {
                "questions_ids": question_ids,
                "questions": questions,
                "answers": ast.literal_eval(output["Input.answers"][0]),
                "answers_ids": ast.literal_eval(output["Input.answers_ids"][0]),
                "summaries": ast.literal_eval(output["Input.summaries"][0]),
                "summaries_scores": ast.literal_eval(
                    output["Input.summaries_scores"][0]
                ),
                "summary_result": summary,
                "familiarity": familiarity,
                "diversity": diversity,
                "transparency": transparency,
                "bias": bias,
                "satisfaction": satisfaction,
                "explanation": explanation,
                "age": [list(demographic_info_df["age"])] * len(summary),
                "gender": [list(demographic_info_df["gender"])] * len(summary),
                "education": [list(demographic_info_df["education"])]
                * len(summary),
            }
        )

        results_df = results_df.sort_values("questions_ids")
        results_df.to_csv(
            "data/results/viewpoint/processed/QS"
            + str(output_id)
            + "_output_processed.csv"
        )
