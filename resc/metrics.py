import pandas as pd

def cm_to_df(cm, normalize = True):
    """
    Converts a binary classfication raw confusion matrix to a DataFrame.
    """
    cm_df = pd.DataFrame(data = cm,
                 index = ["Truth: 0", "Truth: 1"],
                 columns = ["Predicted: 0", "Predicted: 1"])
    
    if normalize:
        down_sum = cm_df["Predicted: 0"].sum()
        up_sum = cm_df["Predicted: 1"].sum()
        
        if down_sum > 0:            
            cm_df["Predicted: 0"] = cm_df["Predicted: 0"] / cm_df["Predicted: 0"].sum()
            
        if up_sum > 0:
            cm_df["Predicted: 1"] = cm_df["Predicted: 1"] / cm_df["Predicted: 1"].sum()
        
    return cm_df