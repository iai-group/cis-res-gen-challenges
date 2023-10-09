import argparse

import pandas as pd
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm


def effect_size(aov_table, data_df):
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


def one_way_anova(data_df, answer_feature, independent_variable):
    dataframe = pd.DataFrame(
        {
            independent_variable: list(data_df[independent_variable]),
            answer_feature: list(data_df[answer_feature]),
        }
    )

    formula = answer_feature + " ~ C(" + independent_variable + ") "
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
                    + answer_feature
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
                    answer_feature
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


def two_way_anova(data_df, answer_feature, second_independent_variable):
    dataframe = pd.DataFrame(
        {
            "answers_ids": list(data_df["answers_ids"]),
            second_independent_variable: list(
                data_df[second_independent_variable]
            ),
            answer_feature: list(data_df[answer_feature]),
        }
    )

    formula = (
        answer_feature
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
                    + answer_feature
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
                    answer_feature
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
        "data/results/answerability/processed/aggregated_output.csv"
    )
    viewpoint_data_df = pd.read_csv(
        "data/results/viewpoint/processed/aggregated_output.csv"
    )

    # Sampling data for manual analysis
    # answerability_data_df_sample = answerability_data_df.groupby("questions_ids").sample(3)
    # answerability_data_df_sample.to_csv("answerablity_sample.csv")
    # viewpoint_data_df_sample = viewpoint_data_df.groupby("questions_ids").sample(3)
    # viewpoint_data_df_sample.to_csv("viewpoint_sample.csv")

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--type",
        help="Argument type is required and must be either 'one-way' or 'two-way'.",
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
                    answer_features = [
                        "diversity",
                        "transparency",
                        "bias",
                        "satisfaction",
                    ]
                else:
                    answer_features = [
                        "factuality",
                        "confidence",
                        "satisfaction",
                    ]
                if independent_var == "questions_ids":
                    answer_features = ["familiarity"] + answer_features
                for feature in answer_features:
                    one_way_anova(data_df, feature, independent_var)

    elif args.type == "two-way":
        for data_df in [answerability_data_df, viewpoint_data_df]:
            print("\hline")
            for independent_var in [
                "familiarity",
                "questions_ids",
            ]:
                if "diversity" in list(data_df.columns):
                    answer_features = [
                        "diversity",
                        "transparency",
                        "bias",
                        "satisfaction",
                    ]
                else:
                    answer_features = [
                        "factuality",
                        "confidence",
                        "satisfaction",
                    ]

                print("\hline")
                for answer_feature in answer_features:
                    two_way_anova(data_df, answer_feature, independent_var)
                    print("\hline")

    else:
        raise ValueError(
            "Argument type is required and must be either 'one-way' or 'two-way'"
        )
