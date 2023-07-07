import glob
import pandas as pd

class importData:

    def fetch(index=0, folder=None, cycle=True):
        if folder is None:
            if cycle:
                folder = './BLM_R5IM_Data/cycle/'
            else:
                folder = './BLM_R5IM_Data/R5IM_loss/'
    
        if folder[-1] != '/': folder += '/'        
        
        input_data = pd.read_csv(glob.glob(folder + '*.csv')[index])
        return input_data.drop(columns = input_data.columns[0]).to_numpy()