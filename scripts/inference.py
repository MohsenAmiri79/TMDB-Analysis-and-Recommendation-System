import pandas as pd

from joblib import load
from os.path import join as joinpath

# Constants
from scripts.configs import NON_GENRE_COLS, GENRE_COLS
from scripts.configs import NUMERICAL_COLS, LABEL_ENC_COLS


MODEL_PATH = "./models/"


class ModelInference:
    def __init__(self, model_path=MODEL_PATH):
        self.models = {
            'lr': load(joinpath(model_path,
                                'logistic_regression_model.joblib')),
            'dt': load(joinpath(model_path,
                                'decision_tree_model.joblib')),
            'rf': load(joinpath(model_path,
                                'random_forest_model.joblib')),
            'xgb': load(joinpath(model_path,
                                 'xgboost_model.joblib')),
        }

        self.preps = {
            'genrePCA': load(joinpath(model_path,
                                      'genre_pca.joblib')),
            'label_scale': load(joinpath(model_path,
                                         'label_scaler.joblib')),
            'numeric_norm': load(joinpath(model_path,
                                          'numerical_scaler.joblib')),
            'feature_selector': load(joinpath(model_path,
                                              'feature_selector.joblib')),
        }

    def clean_sample(self, sample):
        numeric_cols = ['revenue'] + NUMERICAL_COLS
        sample[numeric_cols] = \
            self.preps['numeric_norm'].transform(sample[numeric_cols])

        sample[LABEL_ENC_COLS] = \
            self.preps['label_scale'].transform(sample[LABEL_ENC_COLS])

        principal_components = \
            self.preps['genrePCA'].transform(sample[GENRE_COLS])
        principalDf = pd.DataFrame(data=principal_components,
                                   columns=[f'genrePC{i+1}' for i in range(5)])

        x = sample[NON_GENRE_COLS]
        x = self.preps['feature_selector'].transform(x)
        cols = self.preps['feature_selector'].get_support(indices=True)
        selected_features_df = x.iloc[:, cols]

        return pd.concat([selected_features_df, principalDf], axis=1)

    def predict(self, sample, model_name):
        model = self.models[model_name]

        sample = self.clean_sample(sample).values

        if len(sample.shape) == 1:
            sample = sample.reshape(1, -1)

        prediction = model.predict(sample)
        print('eeeee')
        print(model.classes_)
        return prediction
