# В ячейке ниже представлен код генерирующий DataFrame, 
# которая состоит всего из 1 столбца. 
# Ваша задача перевести его в one hot вид. Надо сделать это без get_dummies.

# import random
# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI':lst})
# data.head()

import pandas as pd
import numpy as np
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

unique_values = data['whoAmI'].unique()
value_to_index = {value: i for i, value in enumerate(unique_values)}

one_hot_data = np.zeros((len(data), len(unique_values)), dtype=int)

for i, value in enumerate(data['whoAmI']):
    index = value_to_index[value]
    one_hot_data[i, index] = 1

one_hot_df = pd.DataFrame(one_hot_data, columns=unique_values)
print(one_hot_df)