import collections
from typing import List

import matplotlib.pyplot as plt
import pandas as pd


def process_data_for_distribution_plot(response_dimensions: List[str], data_df: pd.DataFrame):
    """Processes the data for the distribution plot.

    Args:
        response_dimensions: The response dimensions used in a user study.
        data_df: Dataframe containing the results from a user study.

    Returns:
        A dictionary containing the data for the distribution plot.
    """
    values_per_query = collections.defaultdict(dict)

    for query_id in range(1, 11):
        for response_dimension in response_dimensions:
            query_sub_df = data_df[data_df["questions_ids"] == query_id]
            query_response_dimension_values = list(query_sub_df[response_dimension])
            values_per_query[query_id][
                response_dimension
            ] = query_response_dimension_values

    return values_per_query


if __name__ == "__main__":
    answerability_data_df = pd.read_csv(
        "results/user_study_output/answerability/processed/aggregated_output_both_runs.csv"
    )
    viewpoint_data_df = pd.read_csv(
        "results/user_study_output/viewpoints/processed/aggregated_output.csv"
    )
    response_dimensions_answerability = [
        "familiarity",
        "factuality",
        "confidence",
        "satisfaction",
    ]
    answer_ids_answerability = ["A1", "A2", "A3", "A4"]
    values_per_query_answerability = process_data_for_distribution_plot(
        response_dimensions_answerability, answerability_data_df
    )

    response_dimensions_viewpoints = [
        "familiarity",
        "diversity",
        "transparency",
        "bias",
        "satisfaction",
    ]
    answer_ids_viewpoints = ["A1", "A2", "A3"]
    values_per_query_viewpoints = process_data_for_distribution_plot(
        response_dimensions_viewpoints, viewpoint_data_df
    )

    n_col = 5
    fig, axs = plt.subplots(2, n_col, figsize=(15, 6))
    for id, response_dimension in enumerate(response_dimensions_answerability):
        boxplot_data = []

        for query_id in range(1, 11):
            boxplot_data.append(
                values_per_query_answerability[query_id][response_dimension]
            )

        axs[int(id / n_col)][id % n_col].boxplot(boxplot_data)
        axs[int(id / n_col)][id % n_col].set_xlabel("Query ID")
        axs[int(id / n_col)][id % n_col].set_ylabel(
            "Worker Self-Reported Rating"
        )
        axs[int(id / n_col)][id % n_col].set_title(
            response_dimension.replace("bias", "balance")
            .replace("factuality", "Factual Correctness")
            .replace("satisfaction", "Overall Satisfaction")
            .replace("confidence", "Confidence in Answer Accuracy")
            .title()
        )

    for i, response_dimension in enumerate(response_dimensions_viewpoints):
        id = i + 5
        boxplot_data = []

        for query_id in range(1, 11):
            boxplot_data.append(
                values_per_query_viewpoints[query_id][response_dimension]
            )

        axs[int(id / n_col)][id % n_col].boxplot(boxplot_data)
        axs[int(id / n_col)][id % n_col].set_xlabel("Query ID")
        axs[int(id / n_col)][id % n_col].set_ylabel(
            "Worker Self-Reported Rating"
        )
        axs[int(id / n_col)][id % n_col].set_title(
            response_dimension.replace("bias", "balance")
            .replace("factuality", "Factual Correctness")
            .replace("satisfaction", "Overall Satisfaction")
            .replace("confidence", "Confidence in Answer Accuracy")
            .title()
        )
    fig.tight_layout(pad=1.0)
    plt.figure(dpi=2000)
    fig.savefig("results/quantitative_analysis/data_distribution.png")
