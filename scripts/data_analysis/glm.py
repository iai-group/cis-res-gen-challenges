import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf


def glm(formula, data_df):
    model = smf.glm(formula = formula, 
                    data = data_df, 
                    family = sm.families.Poisson())

    result = model.fit()
    print(result.summary())

if __name__ == "__main__":
    answerability_data_df = pd.read_csv(
        "data/results/answerability/processed/aggregated_output.csv"
    )
    viewpoint_data_df = pd.read_csv(
        "data/results/viewpoint/processed/aggregated_output.csv"
    )
    
    print('*** Answerability user study ***')

    print('Familiarity as an dependent variable')
    glm('familiarity ~ factuality + confidence + satisfaction', answerability_data_df)

    print('Satisfaction as an dependent variable')
    glm('satisfaction ~ familiarity + factuality + confidence', answerability_data_df)


    print('*** Viewpoint user study ***')

    print('Familiarity as an dependent variable')
    glm('familiarity ~ diversity + transparency + bias + satisfaction', viewpoint_data_df)

    print('Satisfaction as an dependent variable')
    glm('satisfaction ~ familiarity + diversity + transparency + bias', viewpoint_data_df)
    