import collections

import matplotlib.pyplot as plt
import pandas as pd


def generate_data_for_plot(answer_features, data_df):
    values_per_question_hist = collections.defaultdict(dict)

    for question_id in range(1, 11):
        for answer_feature in answer_features:
            question_sub_df = data_df[data_df["questions_ids"] == question_id]
            question_metric_values = list(question_sub_df[answer_feature])
            values_per_question_hist[question_id][
                answer_feature
            ] = question_metric_values

    return values_per_question_hist


if __name__ == "__main__":
    answerability_data_df = pd.read_csv(
        "data/results/answerability/processed/aggregated_output.csv"
    )
    viewpoint_data_df = pd.read_csv(
        "data/results/viewpoint/processed/aggregated_output.csv"
    )
    answer_features_answ = [
        "familiarity",
        "factuality",
        "confidence",
        "satisfaction",
    ]
    answer_ids_answ = ["A1", "A2", "A3", "A4"]
    values_per_question_hist_answ = generate_data_for_plot(
        answer_features_answ, answerability_data_df
    )

    answer_features_view = [
        "familiarity",
        "diversity",
        "transparency",
        "bias",
        "satisfaction",
    ]
    answer_ids_view = ["A1", "A2", "A3"]
    values_per_question_hist_view = generate_data_for_plot(
        answer_features_view, viewpoint_data_df
    )

    n_col = 5
    fig, axs = plt.subplots(2, n_col, figsize=(15, 6))
    for id, answer_feature in enumerate(answer_features_answ):
        boxplot_data = []

        for question_id in range(1, 11):
            boxplot_data.append(
                values_per_question_hist_answ[question_id][answer_feature]
            )

        axs[int(id / n_col)][id % n_col].boxplot(boxplot_data)
        axs[int(id / n_col)][id % n_col].set_xlabel("Query")
        axs[int(id / n_col)][id % n_col].set_ylabel(
            "Worker Self-Reported Score"
        )
        axs[int(id / n_col)][id % n_col].set_title(
            answer_feature.replace("bias", "balance")
            .replace("factuality", "Factual Correctness")
            .replace("satisfaction", "Overall Satisfaction")
            .title()
        )

    for i, answer_feature in enumerate(answer_features_view):
        id = i + 5
        boxplot_data = []

        for question_id in range(1, 11):
            boxplot_data.append(
                values_per_question_hist_view[question_id][answer_feature]
            )

        axs[int(id / n_col)][id % n_col].boxplot(boxplot_data)
        axs[int(id / n_col)][id % n_col].set_xlabel("Query")
        axs[int(id / n_col)][id % n_col].set_ylabel(
            "Worker Self-Reported Score"
        )
        axs[int(id / n_col)][id % n_col].set_title(
            answer_feature.replace("bias", "balance")
            .replace("factuality", "Factual Correctness")
            .replace("satisfaction", "Overall Satisfaction")
            .title()
        )
    fig.tight_layout(pad=1.0)
    plt.figure(dpi=2000)
    fig.savefig("data/results/data_distribution.png")
