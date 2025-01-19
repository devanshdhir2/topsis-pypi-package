import numpy as np
import pandas as pd

def topsis_analysis(data, weights, impacts):
    """
    Perform TOPSIS analysis on a given dataset.
    :param data: Input dataframe with alternatives and criteria
    :param weights: List of weights corresponding to each criterion
    :param impacts: List of impacts ('maximise' or 'minimise') for each criterion
    :return: Dataframe with TOPSIS scores and rankings
    """
    # All the functions from your code embedded here
    def convert_categorical_to_numerical(df):
        for column in df.select_dtypes(include=['object']).columns:
            df[column] = df[column].astype('category').cat.codes
        return df

    def vector_normalisation(column):
        return column / np.sqrt(np.sum(column ** 2))

    def create_normalised_decision_matrix(df):
        return df.apply(vector_normalisation, axis=0)

    def assign_weights(matrix, weights):
        return matrix * weights

    def find_ideal_best_and_worst(matrix, impacts):
        ideal_best = []
        ideal_worst = []
        for i, impact in enumerate(impacts):
            if impact == 'maximise':
                ideal_best.append(matrix.iloc[:, i].max())
                ideal_worst.append(matrix.iloc[:, i].min())
            elif impact == 'minimise':
                ideal_best.append(matrix.iloc[:, i].min())
                ideal_worst.append(matrix.iloc[:, i].max())
            else:
                raise ValueError("Impact must be 'maximise' or 'minimise'")
        return np.array(ideal_best), np.array(ideal_worst)

    def calculate_euclidean_distance(matrix, ideal):
        return np.sqrt(np.sum((matrix - ideal) ** 2, axis=1))

    def calculate_performance_score(distance_to_best, distance_to_worst):
        return distance_to_worst / (distance_to_best + distance_to_worst)

    # Main TOPSIS implementation
    data = convert_categorical_to_numerical(data)
    normalised_matrix = create_normalised_decision_matrix(data)
    weighted_matrix = assign_weights(normalised_matrix, weights)
    ideal_best, ideal_worst = find_ideal_best_and_worst(weighted_matrix, impacts)
    distance_to_best = calculate_euclidean_distance(weighted_matrix.values, ideal_best)
    distance_to_worst = calculate_euclidean_distance(weighted_matrix.values, ideal_worst)
    performance_scores = calculate_performance_score(distance_to_best, distance_to_worst)

    result = data.copy()
    result['TOPSIS Score'] = performance_scores
    result['Rank'] = performance_scores.argsort()[::-1] + 1

    return result