import argparse
import ast

import pandas as pd

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--user_study", help="Argument user_study is required and must be either 'answerability' or 'viewpoint'.")
    args = parser.parse_args()

    if args.user_study == "answerability":
        directory = "data/results/answerability/processed/"
        number_of_files = 12
        metrics = [
            "summary_result",
            "familiarity",
            "factuality",
            "confidence",
            "satisfaction",
        ]
    elif args.user_study == "viewpoint":
        directory = "data/results/viewpoint/processed/"
        number_of_files = 9
        metrics = [
            "summary_result",
            "familiarity",
            "diversity",
            "transparency",
            "bias",
            "satisfaction",
        ]
    else:
        raise ValueError(
            "Argument user_study is required and must be either 'answerability' or 'viewpoint'"
        )

    output = pd.read_csv(directory + "QS1_output_processed.csv")

    aggregated_data = pd.DataFrame(columns=list(output.columns)[1:])

    for output_id in range(1, number_of_files + 1):
        output = pd.read_csv(
            directory + "QS" + str(output_id) + "_output_processed.csv"
        )
        for id, row in output.iterrows():
            for annotation_id in range(0, 3):
                new_row = row.copy(deep=True)
                for metric in metrics + [
                    "explanation",
                    "age",
                    "gender",
                    "education",
                ]:
                    new_row[metric] = list(ast.literal_eval(row[metric]))[
                        annotation_id
                    ]
                aggregated_data = aggregated_data.append(
                    new_row, ignore_index=True
                )

    aggregated_data = aggregated_data.sort_values(
        ["questions_ids", "answers_ids"], ascending=[True, True]
    )

    for metric in metrics:
        aggregated_data[metric] = aggregated_data[metric].apply(
            lambda xn: int(xn)
        )

    aggregated_data.to_csv(directory + "aggregated_output.csv", index=False)
