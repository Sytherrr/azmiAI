from sklearn.linear_model import LinearRegression, Lasso
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor, AdaBoostRegressor
from xgboost import XGBRegressor
from catboost import CatBoostRegressor
import numpy as np

def perform_analysis(student):
    gpa = student.gpa
    attendance = student.performance_set.latest('id').attendance
    data = np.array([[gpa, attendance]])
    analysis_result = {}

    models = {
        "Linear Regression": LinearRegression(),
        "Lasso": Lasso(),
        "K-Neighbors Regressor": KNeighborsRegressor(),
        "Decision Tree": DecisionTreeRegressor(),
        "Random Forest Regressor": RandomForestRegressor(),
        "Gradient Boosting": GradientBoostingRegressor(),
        "XGBRegressor": XGBRegressor(),
        "CatBoosting Regressor": CatBoostRegressor(verbose=False),
        "AdaBoost Regressor": AdaBoostRegressor(),
    }

    for model_name, model in models.items():
        model.fit(data, [0])
        prediction = model.predict(data)[0]
        analysis_result[model_name] =  prediction

    return analysis_result