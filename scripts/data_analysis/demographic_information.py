from collections import Counter

import pandas as pd

age_mapping = {
    1: "18-30",
    2: "31-45",
    3: "46-60",
    4: "60+",
    5: "Prefer not to say",
}
education_mapping = {
    1: "High School",
    2: "Bachelor's Degree",
    3: "Master's Degree",
    4: "Ph.D. or higher",
    5: "Prefer not to say",
}
gender_mapping = {1: "Male", 2: "Female", 3: "Other", 5: "Prefer not to say"}

if __name__ == "__main__":
    answerability_data_df = pd.read_csv(
        "data/results/answerability/processed/aggregated_output.csv"
    )
    viewpoint_data_df = pd.read_csv(
        "data/results/viewpoint/processed/aggregated_output.csv"
    )

    for user_study_name, data_df in zip(
        ["Answerability", "Viewpoints"],
        [answerability_data_df, viewpoint_data_df],
    ):
        print(
            "Demographic information for the " + user_study_name + " User Study"
        )
        print(
            {
                age_mapping[int(key.replace("option_", ""))]: int(value / 10)
                for (key, value) in dict(Counter(list(data_df["age"]))).items()
            }
        )
        print(
            {
                education_mapping[int(key.replace("option_", ""))]: int(
                    value / 10
                )
                for (key, value) in dict(
                    Counter(list(data_df["education"]))
                ).items()
            }
        )
        print(
            {
                gender_mapping[int(key.replace("option_", ""))]: int(value / 10)
                for (key, value) in dict(
                    Counter(list(data_df["gender"]))
                ).items()
            }
        )
