import os
import sys from dataclass
from catboost import CatBoostRegressor
from sklearn.ensemble import (
    AdaBoostRegressor,
    GradientBoostingClassifier,
    RandomForestClassifier
)
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.tree import DecisionTreeClassifier
from xgboost import XGBRegressor

from src.exception import CustomException
from src.logger import logging