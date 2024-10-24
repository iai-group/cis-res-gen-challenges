import argparse
from typing import List, Tuple

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats
from statsmodels.formula.api import ols
from statsmodels.graphics.factorplots import interaction_plot
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

def anova(
    data_df: pd.DataFrame,
    response_dimension: str,
    first_independent_variable: str,
    second_independent_variable: str = None,
    third_independent_variable: str = None,
):
    """Runs a two-way ANOVA test.

    Args:
        data_df: Dataframe containing the data.
        response_dimension: List of response dimensions.
        second_independent_variable: Second independent variable.
        third_independent_variable: Third independent variable.
    """
    dataframe = pd.DataFrame(
        {
            first_independent_variable: list(data_df[first_independent_variable]),
            response_dimension: list(data_df[response_dimension]),
        }
    )
    if second_independent_variable:
        dataframe[second_independent_variable] = list(
            data_df[second_independent_variable]
        )
    if third_independent_variable:
        dataframe[third_independent_variable] = list(
            data_df[third_independent_variable]
        )

    if third_independent_variable:
        formula = (
            response_dimension + " ~ C(" + first_independent_variable + ") + C(" + second_independent_variable + ") + C(" + third_independent_variable + ") + C(" +
            first_independent_variable + "):C(" + second_independent_variable + ") + C(" + first_independent_variable + "):C(" + third_independent_variable + ") + C(" + second_independent_variable + "):C(" + third_independent_variable + ") + C(" +
            first_independent_variable + "):C(" + second_independent_variable + "):C(" + third_independent_variable + ")"
        )
    elif second_independent_variable:
        formula = (
            response_dimension + " ~ C(" + first_independent_variable + ") + C(" + second_independent_variable + ") + C(" + 
            first_independent_variable + "):C(" + second_independent_variable + ")"
        )
    else:
        formula = (
            response_dimension + " ~ C(" + first_independent_variable + ") "
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
                .replace("questions_ids", "question")
                .lower()
            )
            # fvalue = round(row["F"], 3)
            pvalue = round(row["PR(>F)"], 3)
            if pvalue <= 0.05:
                print(
                    "\\textbf{"
                    + response_dimension
                    + "} & \\textbf{"
                    + param
                    + "} & \\textbf{"
                    # + str(fvalue)
                    # + "} & \\textbf{"
                    + str(pvalue)
                    + "} & \\textbf{"
                    # + str(row["w2facts"])
                    # + "} & \\textbf{"
                    + row["sizes"]
                    + "} \\\\"
                )
            else:
                print(
                    response_dimension
                    + " & "
                    + param
                    + " & "
                    # + str(fvalue)
                    # + " & "
                    + str(pvalue)
                    + " & "
                    # + str(row["w2facts"])
                    # + " & "
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

    controlled_factuality = []
    controlled_source = []
    for index, row in answerability_data_df.iterrows():
        if row["answers_ids"] == "A1" or row["answers_ids"] == "A2":
            controlled_factuality.append(1) # factually correct
        else:
            controlled_factuality.append(0) # hallucinated
        if row["answers_ids"] == "A1" or row["answers_ids"] == "A3":
            controlled_source.append(1) # source present (may be invalid)
        else:
            controlled_source.append(0) # no source
    answerability_data_df["controlled_factuality"] = controlled_factuality
    answerability_data_df["controlled_source"] = controlled_source

    controlled_diversity = []
    controlled_balance = []
    for index, row in viewpoint_data_df.iterrows():
        if row["answers_ids"] == "A1" or row["answers_ids"] == "A2":
            controlled_diversity.append(1) # multiple viewpoints
        else:
            controlled_diversity.append(0) # single viewpoint
        if row["answers_ids"] == "A1":
            controlled_balance.append(1) # balanced
        else:
            controlled_balance.append(0) # unbalanced
    viewpoint_data_df["controlled_diversity"] = controlled_diversity
    viewpoint_data_df["controlled_balance"] = controlled_balance

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--type",
        help="Argument type is required. Select 'two-way' or 'three-way'.",
    )
    args = parser.parse_args()

    if args.type == "one-way":
        for data_df in [answerability_data_df, viewpoint_data_df]:
            print("\hline")
            for independent_var in [
                "questions_ids",
                "familiarity",
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
                if independent_var == "questions_ids":
                    response_dimensions = ["familiarity"] + response_dimensions
                for feature in response_dimensions:
                    anova(data_df, feature, independent_var)

    elif args.type == "two-way":
        for data_df in [answerability_data_df, viewpoint_data_df]:
            print("\hline")
            if "diversity" in list(data_df.columns):
                response_dimensions = [
                    "diversity",
                    "transparency",
                    "bias",
                    "satisfaction",
                ]
                first_independent_variable = "controlled_diversity"
                second_independent_variable = "controlled_balance"
            else:
                response_dimensions = [
                    "factuality",
                    "confidence",
                    "satisfaction",
                ]
                first_independent_variable = "controlled_factuality"
                second_independent_variable = "controlled_source"
            for feature in response_dimensions:
                anova(data_df, feature, first_independent_variable, second_independent_variable)
                fig = interaction_plot(data_df[first_independent_variable],data_df[second_independent_variable],data_df[feature])
                plt.savefig("plots/" + feature + "_" + first_independent_variable + "_"  + second_independent_variable + "_interaction_plot.png")

    elif args.type == "three-way":
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
                    first_independent_variable = "controlled_diversity"
                    second_independent_variable = "controlled_balance"
                else:
                    response_dimensions = [
                        "factuality",
                        "confidence",
                        "satisfaction",
                    ]
                    first_independent_variable = "controlled_factuality"
                    second_independent_variable = "controlled_source"
                for feature in response_dimensions:
                    anova(data_df, feature, first_independent_variable, second_independent_variable, independent_var)

    elif args.type == "pearson":
         for data_df in [answerability_data_df, viewpoint_data_df]:
            print("\hline")
            dependent_var = "satisfaction"
            if "diversity" in list(data_df.columns):
                independent_variables = [
                    "familiarity",
                    "diversity",
                    "transparency",
                    "bias",
                ]
            else:
                independent_variables = [
                    "familiarity",
                    "factuality",
                    "confidence",
                ]
            for independent_var in independent_variables:
                # anova(data_df, dependent_var, independent_var)
                pc = stats.pearsonr(data_df[dependent_var], data_df[independent_var])
                print(independent_var + " & " + str(round(pc[0], 3)) + " & " + str(round(pc[1], 3)) + " \\\\")
    
    elif args.type == "power-analysis":
        answerability_data_df = pd.read_csv(
            "results/user_study_output/answerability/processed/first_run/aggregated_output.csv"
        )
        for study, data_df in zip(["Answerability Study", "Viewpoints Study"], [answerability_data_df, viewpoint_data_df]):
            print("---Power Analysis for " + study + "---")
            independent_var = "answers_ids"
            if "diversity" in list(data_df.columns):
                feature = "diversity"
            else:
                feature = "factuality"

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

    else:
        raise ValueError(
            "Argument type is required and must be selected from 'one-way', 'two-way', 'three-way', or 'pearson'."
        )
