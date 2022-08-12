import pandas as pd
import random,os
import numpy as np

test=pd.read_csv('test_plates.csv')

seed=42
def seed_everything(seed=0):
    random.seed(seed)
    os.environ['PYTHONHASHSEED'] = str(seed)
    np.random.seed(seed)

seed_everything(seed)

append_vals=[]
append_vals=[['img_1889.jpg',1682,1705,2093,1781,1,0],
                   ['img_2703.jpg',1704,1832,2228,1928,1,0],
                    ['img_2515.jpg',1626,1671,2201,1774,1,0],
                    ['img_1888.jpg',1967,1262,2205,1319,1,0],
                    ['img_2674.heic',1492,1688,2338,1859,1,0]]

temp_df=pd.DataFrame(append_vals,columns=test.columns)

test=pd.concat((test,temp_df))

test.to_csv('test_plates.csv',index=False)
