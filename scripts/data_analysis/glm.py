import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf

if __name__ == "__main__":
    answerability_data_df = pd.read_csv(
        "data/results/answerability/processed/aggregated_output.csv"
    )
    viewpoint_data_df = pd.read_csv(
        "data/results/viewpoint/processed/aggregated_output.csv"
    )
    
    print('*** Answerability user study ***')
    print('Familiarity as an dependent variable')
    formula = 'familiarity ~ factuality + confidence + satisfaction'
    data_df = answerability_data_df
    model = smf.glm(formula = formula, 
                    data = data_df, 
                    family = sm.families.Poisson())

    result = model.fit()
    print(result.summary())

    print('Satisfaction as an dependent variable')
    formula = 'satisfaction ~ familiarity + factuality + confidence'
    model = smf.glm(formula = formula, 
                    data = data_df, 
                    family = sm.families.Poisson())

    result = model.fit()
    print(result.summary())


    print('*** Viewpoint user study ***')
    print('Familiarity as an dependent variable')
    formula = 'familiarity ~ diversity + transparency + bias + satisfaction'
    data_df = viewpoint_data_df
    model = smf.glm(formula = formula, 
                    data = data_df, 
                    family = sm.families.Poisson())

    result = model.fit()
    print(result.summary())

    print('Satisfaction as an dependent variable')
    formula = 'satisfaction ~ familiarity + diversity + transparency + bias'
    model = smf.glm(formula = formula, 
                    data = data_df, 
                    family = sm.families.Poisson())

    result = model.fit()
    print(result.summary())
    