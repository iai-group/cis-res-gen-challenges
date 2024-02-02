"""Script used for generating sentiment labels for the comments provided by
crowd workers in the user study."""

import pandas as pd
from transformers import pipeline

if __name__ == "__main__":
    sentiment_analysis = pipeline(
        "sentiment-analysis", model="siebert/sentiment-roberta-large-english"
    )

    answerability_data_df = pd.read_csv(
        "results/user_study_output/answerability/processed/aggregated_output_both_runs.csv"
    )
    viewpoint_data_df = pd.read_csv(
        "results/user_study_output/viewpoints/processed/aggregated_output.csv"
    )

    for user_study_name, data_df in zip(
        ["answerability", "viewpoint"],
        [answerability_data_df, viewpoint_data_df],
    ):
        sentiment_labels = []
        sentiment_scores = []
        for id, row in data_df.iterrows():
            sentiment_pred = sentiment_analysis(row["explanation"])
            sentiment_labels.append(sentiment_pred[0]["label"])
            sentiment_scores.append(round(sentiment_pred[0]["score"], 2))

        data_df["sentiment_label"] = sentiment_labels
        data_df["sentiment_score"] = sentiment_scores

        data_df.to_csv(
            "results/user_study_output/"
            + user_study_name
            + "/processed/aggregated_output_sentiment_labels.csv"
        )
