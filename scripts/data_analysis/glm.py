import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf


def glm(formula: str, data_df: pd.DataFrame) -> str:
    """Builds GLM model and returns the summary.

    Args:
        formula: The formula used for building GLM model.
        data_df: Dataframe containing the data.

    Returns:
        The summary of the built GLM model.
    """
    model = smf.glm(formula=formula, data=data_df, family=sm.families.Poisson())

    result = model.fit()
    return result.summary()


if __name__ == "__main__":
    answerability_data_df = pd.read_csv(
        "results/user_study_output/answerability/processed/aggregated_output.csv"
    )
    viewpoint_data_df = pd.read_csv(
        "results/user_study_output/viewpoints/processed/aggregated_output.csv"
    )

    print("*** Answerability user study ***")

    print("Familiarity as an dependent variable")
    print(glm(
        "familiarity ~ factuality + confidence + satisfaction",
        answerability_data_df,
    ))

    print("Satisfaction as an dependent variable")
    print(glm(
        "satisfaction ~ familiarity + factuality + confidence",
        answerability_data_df,
    ))

    print("*** Viewpoint user study ***")

    print("Familiarity as an dependent variable")
    print(glm(
        "familiarity ~ diversity + transparency + bias + satisfaction",
        viewpoint_data_df,
    ))

    print("Satisfaction as an dependent variable")
    print(glm(
        "satisfaction ~ familiarity + diversity + transparency + bias",
        viewpoint_data_df,
    ))
