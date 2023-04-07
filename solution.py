import pandas as pd
import numpy as np


chat_id = 460411293 # Ваш chat ID, не меняйте название переменной


def solution(x: np.array) -> float:
# v = a*t
t = 10
v = np.min(x) + 37
return v/t
