Tools:

* Lag (`resc/lag.py`): Contains two functions, one lags `DataFrame` a given n time, the other lags a whole dataset n times (the independent variables have the first n rows removed). `lag_demonstration.ipynb` demonstrates its use.

* Smooth plot (`resc/smooth_plot.py`): Contains a function that uses `bokeh` to visualize the effect of an averaging a series at some frequency (using `pandas.Grouper`).

* Metrics (`resc/metrics.py`): Contains a function to make a pretty `DataFrame` from a binary classification confusion matrix. Also, allows for normalizing the confusion matrix values to probabilities.

Examples:

* Cross validation example (`linear_reg_with_cv_example.ipynb`): Shows a few `sklearn` cross validators and how to use them both for cross validation and cross validation grid search models (e.x. ` sklearn.linear_model.LassoCV`).