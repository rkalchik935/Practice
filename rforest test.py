import numpy as np

from decisiontree import DecisionTree


class RandomForestClassifier():

    def __init__(self, n_base_learner=10, max_depth=5, min_samples_leaf=1, min_information_gain=0.0,  
                 numb_of_features_splitting=None, bstrap_size=None) -> None:
        self.n_base_learner = n_base_learner
        self.max_depth = max_depth
        self.min_samples_leaf = min_samples_leaf
        self.min_information_gain = min_information_gain
        self.numb_of_features_splitting = numb_of_features_splitting

        self.bstrap_size = bstrap_size


    def _create_bstrap_samples(self, X, Y) -> tuple:

        # creates bootstrap samples for each base learner
        bstrap_samples_X = []
        bstrap_samples_Y = []


        for i in range(self.n_base_learner):

            if not self.bstrap_size:
                self.bstrap_size = X.shape[0]

            sampled_idx = np.random.choice(X.shape[0], size=self.bstrap_size, replace=True)
            bstrap_samples_X.append(X[sampled_idx])
            bstrap_samples_Y.append(Y[sampled_idx])

        return bstrap_samples_X, bstrap_samples_Y


    def train(self, X_train : np.array, Y_train : np.array) -> None:

        bstrap_samples_X, bstrap_samples_Y = self._create_bstrap_samples(X_train, Y_train)

        self.base_learner_list = []

        for base_learner_idx in range(self.n_base_learner):
            base_learner = DecisionTree(max_depth=self.max_depth, min_samples_leaf=self.min_samples_leaf, 
            min_information_gain=self.min_information_gain, numb_of_features_splitting=self.numb_of_features_splitting)

            base_learner.train(bstrap_samples_X[base_learner_idx], bstrap_samples_Y[base_learner_idx])
            self.base_learner_list.append(base_learner)

        self.feature_importance = self._calculate_rf_feature_importances(self.base_learner_list)


    def create_proba_w_base_learners(self, X_set : np.array) -> list:

        # creates list of predictions for all base learners
        pred_prob_list = []
        for base_learner in self.base_learner_list:
            pred_prob_list.append(base_learner.predict_proba(X_set))

        return pred_prob_list


    def predict_proba(self, X_set : np.array) -> list:

        # returns the predicted probabilities for a given dataset
        pred_probs = []
        base_learners_pred_probs = self.create_proba_w_base_learners(X_set)

        # average the predicted probabilities of the base learners
        for obs in range(X_set.shape[0]):
            base_learner_probs_for_obs = [a[obs] for a in base_learners_pred_probs]

            obs_average_pred_probs = np.mean(base_learner_probs_for_obs, axis=0)
            pred_probs.append(obs_average_pred_probs)

        return pred_probs


    def predict(self, X_set: np.array) -> np.array:

        pred_probs = self.predict_proba(X_set)

        # return indices of max values
        preds = np.argmax(pred_probs, axis=1)

        return preds

    def _calculate_rf_feature_importance(self, base_learners):

        feature_importance_dict_list = []
        for base_learner in base_learners:
            feature_importance_dict_list.append(base_learner.feature_importances)

        feature_importance_list = [list(x.values()) for x in feature_importance_dict_list]
        average_feature_importance = np.mean(feature_importance_list, axis=0)

        return average_feature_importance