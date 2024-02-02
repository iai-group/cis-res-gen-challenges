import argparse
from typing import List, Tuple

import numpy as np
import pandas as pd
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
from statsmodels.stats.oneway import effectsize_oneway
from statsmodels.stats.power import FTestAnovaPower


def effect_size(
    aov_table: pd.DataFrame, data_df: pd.DataFrame
) -> Tuple[List[float], List[str]]:
    """Calculates the effect size for each parameter.

    Args:
        aov_table: Pd.DataFrame containing the ANOVA table.
        data_df: Dataframe containing the data.

    Returns:
        A tuple containing the effect size and the size.
    """
    w2facts = []
    sizes = []
    for id, row in aov_table.iterrows():
        w2fact = round(
            (row["df"] * (row["F"] - 1))
            / (row["df"] * (row["F"] - 1) + len(data_df)),
            3,
        )
        w2facts.append(w2fact)
        if w2fact >= 0.14:
            size = "L"
        elif w2fact >= 0.06 and w2fact < 0.14:
            size = "M"
        elif w2fact >= 0.01 and w2fact < 0.06:
            size = "S"
        else:
            size = "-"
        sizes.append(size)
    return w2facts, sizes


def one_way_anova(
    data_df: pd.DataFrame,
    response_dimension: List[str],
    independent_variable: str,
):
    """Runs a one-way ANOVA test.

    Args:
        data_df: Dataframe containing the data.
        response_dimension: _description_
        independent_variable: _description_
    """
    dataframe = pd.DataFrame(
        {
            independent_variable: list(data_df[independent_variable]),
            response_dimension: list(data_df[response_dimension]),
        }
    )

    formula = response_dimension + " ~ C(" + independent_variable + ") "
    model = ols(formula, dataframe).fit()
    aov_table = anova_lm(model, typ=2)

    w2facts, sizes = effect_size(aov_table, data_df)
    aov_table["w2facts"] = w2facts
    aov_table["sizes"] = sizes

    # print(aov_table.round(3))

    for _, row in aov_table.iterrows():
        if row.name != "Residual":
            param = (
                row.name.replace("C(", "")
                .replace(")", "")
                .replace("answers_ids", "answer condition")
                .replace("questions_ids", "question")
                .lower()
            )
            fvalue = round(row["F"], 3)
            pvalue = round(row["PR(>F)"], 3)
            if pvalue <= 0.05:
                print(
                    "\\textbf{"
                    + response_dimension
                    + "} & \\textbf{"
                    + param
                    + "} & \\textbf{"
                    + str(fvalue)
                    + "} & \\textbf{"
                    + str(pvalue)
                    + "} & \\textbf{"
                    + str(row["w2facts"])
                    + "} & \\textbf{"
                    + row["sizes"]
                    + "} \\\\"
                )
            else:
                print(
                    response_dimension
                    + " & "
                    + param
                    + " & "
                    + str(fvalue)
                    + " & "
                    + str(pvalue)
                    + " & "
                    + str(row["w2facts"])
                    + " & "
                    + row["sizes"]
                    + " \\\\"
                )


def two_way_anova(
    data_df: pd.DataFrame,
    response_dimension: List[str],
    second_independent_variable: str,
):
    """Runs a two-way ANOVA test.

    Args:
        data_df: Dataframe containing the data.
        response_dimension: List of response dimensions.
        second_independent_variable: Second independent variable.
    """

    dataframe = pd.DataFrame(
        {
            "answers_ids": list(data_df["answers_ids"]),
            second_independent_variable: list(
                data_df[second_independent_variable]
            ),
            response_dimension: list(data_df[response_dimension]),
        }
    )

    formula = (
        response_dimension
        + " ~ C(answers_ids) + C("
        + second_independent_variable
        + ") + C(answers_ids):C("
        + second_independent_variable
        + ")"
    )
    model = ols(formula, dataframe).fit()
    aov_table = anova_lm(model, typ=2)

    w2facts, sizes = effect_size(aov_table, data_df)
    aov_table["w2facts"] = w2facts
    aov_table["sizes"] = sizes

    # print(aov_table.round(3))

    for _, row in aov_table.iterrows():
        if row.name != "Residual":
            param = (
                row.name.replace("C(", "")
                .replace(")", "")
                .replace("answers_ids", "answer condition")
                .replace("questions_ids", "question")
                .lower()
            )
            fvalue = round(row["F"], 3)
            pvalue = round(row["PR(>F)"], 3)
            if pvalue <= 0.05:
                print(
                    "\\textbf{"
                    + response_dimension
                    + "} & \\textbf{"
                    + param
                    + "} & \\textbf{"
                    + str(fvalue)
                    + "} & \\textbf{"
                    + str(pvalue)
                    + "} & \\textbf{"
                    + str(row["w2facts"])
                    + "} & \\textbf{"
                    + row["sizes"]
                    + "} \\\\"
                )
            else:
                print(
                    response_dimension
                    + " & "
                    + param
                    + " & "
                    + str(fvalue)
                    + " & "
                    + str(pvalue)
                    + " & "
                    + str(row["w2facts"])
                    + " & "
                    + row["sizes"]
                    + " \\\\"
                )


if __name__ == "__main__":
    answerability_data_df = pd.read_csv(
        "results/user_study_output/answerability/processed/aggregated_output_both_runs.csv"
    )
    viewpoint_data_df = pd.read_csv(
        "results/user_study_output/viewpoints/processed/aggregated_output.csv"
    )

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--type",
        help="Argument type is required. Select 'one-way' or 'two-way'.",
    )
    args = parser.parse_args()

    if args.type == "one-way":
        for data_df in [answerability_data_df, viewpoint_data_df]:
            print("\hline")
            for independent_var in [
                "answers_ids",
                "questions_ids",
                "familiarity",
            ]:
                print("\hline")
                if "diversity" in list(data_df.columns):
                    response_dimensions = [
                        "diversity",
                        "transparency",
                        "bias",
                        "satisfaction",
                    ]
                else:
                    response_dimensions = [
                        "factuality",
                        "confidence",
                        "satisfaction",
                    ]
                if independent_var == "questions_ids":
                    response_dimensions = ["familiarity"] + response_dimensions
                for feature in response_dimensions:
                    print(feature)
                    one_way_anova(data_df, feature, independent_var)

                    if independent_var == "answers_ids" and feature in ["diversity", "factuality"]:
                        means = []
                        standard_deviations = []
                        ns = []

                        for answer_id in list(set(data_df["answers_ids"])):
                            means.append(np.mean(list(data_df[data_df["answers_ids"] == answer_id][feature])))
                            standard_deviations.append(np.std(list(data_df[data_df["answers_ids"] == answer_id][feature])))
                            ns.append(len(list(data_df[data_df["answers_ids"] == answer_id][feature])))

                        assumption = pd.DataFrame({'means': means, 'standard_deviations': standard_deviations, 'n': ns})

                        print(assumption)
                        
                        assumption['variances'] = assumption.standard_deviations**2
                        ese = effectsize_oneway(means = assumption.means,
                                                vars_ = assumption.variances,
                                                nobs = assumption.n, use_var="equal")
                        ese = np.sqrt(ese)
                        print("Cohen's f effect size of experimental condition on " + feature + ": " + str(ese))                    
                        ese = 0.1
                        sample_size = FTestAnovaPower().solve_power(effect_size=ese, nobs=None, 
                                                alpha=0.05, k_groups=len(assumption), power=0.8)
                        print("Sample size as a result of power analysis for large effect size (0.4): " + str(sample_size))

    elif args.type == "two-way":
        for data_df in [answerability_data_df, viewpoint_data_df]:
            print("\hline")
            for independent_var in [
                "familiarity",
                "questions_ids",
            ]:
                if "diversity" in list(data_df.columns):
                    response_dimensions = [
                        "diversity",
                        "transparency",
                        "bias",
                        "satisfaction",
                    ]
                else:
                    response_dimensions = [
                        "factuality",
                        "confidence",
                        "satisfaction",
                    ]

                print("\hline")
                for response_dimension in response_dimensions:
                    two_way_anova(data_df, response_dimension, independent_var)
                    print("\hline")

    else:
        raise ValueError(
            "Argument type is required and must be either 'one-way' or 'two-way'"
        )
