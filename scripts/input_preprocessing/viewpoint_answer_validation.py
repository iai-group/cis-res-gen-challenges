import math

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

if __name__ == "__main__":
    answer_evaluation = pd.read_csv(
        "data/input_data/question_selection/viewpoint/answer_validation.csv"
    )
    answer_evaluation = answer_evaluation.fillna("")
    answer_evaluation = answer_evaluation.iloc[2:].set_axis(
        answer_evaluation.columns
        + " "
        + answer_evaluation.iloc[0]
        + " "
        + answer_evaluation.iloc[1],
        axis=1,
    )

    diversity = {
        "A1": [
            float(n.replace(",", "."))
            for n in answer_evaluation["A1.4 Diversity AVG"][:12]
        ],
        "A2": [
            float(n.replace(",", "."))
            for n in answer_evaluation["A2.4 Diversity AVG"][:12]
        ],
        "A3": [
            float(n.replace(",", "."))
            for n in answer_evaluation["A3.4 Diversity AVG"][:12]
        ],
    }
    balance = {
        "A1": [
            float(n.replace(",", "."))
            for n in answer_evaluation["A1.8 Balance AVG"][:12]
        ],
        "A2": [
            float(n.replace(",", "."))
            for n in answer_evaluation["A2.8 Balance AVG"][:12]
        ],
        "A3": [
            float(n.replace(",", "."))
            for n in answer_evaluation["A3.8 Balance AVG"][:12]
        ],
    }

    diversity_values = list(diversity.values())
    whis_div = 0.5
    plt.figure(0, figsize=(10, 7))
    plt.boxplot(diversity_values, whis=whis_div)
    plt.title("Diversity")
    plt.savefig(
        "data/input_data/question_selection/viewpoint/answer_validation_diversity_boxplot.png"
    )

    answer_with_diversity_outliers = np.array(diversity_values[0])

    print("Diversity:")
    q1 = np.quantile(answer_with_diversity_outliers, 0.25)
    print("1st quantile: " + str(q1))
    q3 = np.quantile(answer_with_diversity_outliers, 0.75)
    print("3rd quantile: " + str(q3))
    med = np.median(answer_with_diversity_outliers)
    print("Median: " + str(med))
    iqr = q3 - q1
    upper_bound = q3 + (whis_div * iqr)
    lower_bound = q1 - (whis_div * iqr)
    # print(iqr, upper_bound, lower_bound)
    outliers = answer_with_diversity_outliers[
        answer_with_diversity_outliers <= lower_bound
    ]
    print("The following are the outliers in the boxplot: {}".format(outliers))

    balance_values = list(balance.values())
    whis_bal = 1.5
    plt.figure(1, figsize=(10, 7))
    plt.boxplot(balance_values, whis=whis_bal)
    plt.title("Balance")
    plt.savefig(
        "data/input_data/question_selection/viewpoint/answer_validation_balance_boxplot.png"
    )

    print("Balance:")
    answer_with_balance_outliers = np.array(balance_values[2])
    q1 = np.quantile(answer_with_balance_outliers, 0.25)
    print("1st quantile: " + str(q1))
    q3 = np.quantile(answer_with_balance_outliers, 0.75)
    print("3rd quantile: " + str(q3))
    med = np.median(answer_with_balance_outliers)
    print("Median: " + str(med))
    iqr = q3 - q1
    upper_bound = q3 + (whis_bal * iqr)
    lower_bound = q1 - (whis_bal * iqr)
    # print(iqr, upper_bound, lower_bound)
    outliers = answer_with_balance_outliers[
        (answer_with_balance_outliers >= upper_bound)
    ]
    print("The following are the outliers in the boxplot:{}".format(outliers))
