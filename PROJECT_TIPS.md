2018-09-24

[ipython-notebook_kernel_creation]
python -m ipykernel install --user --name tensorflow-kernel --display-name "tf-kernel"
/Users/qizhu/anaconda/envs/tensorflow/bin/python: No module named ipykernel

[Papers Links]
1. https://www.kaggle.com/kimy07/eurusd-15-minute-interval-price-prediction
2. Algorithmic financial trading with deep convolutional neural networks: Time series to image conversion approach

[Adds submodule]

git submodule add [GIT-LINK-FOR-SUBMODULE] [LOCAL-SUBMODULE-LOCATION]

e.g. git submodule add https://github.com/z33pX/mpl_finance_ext.git tools/mpl_finance_ext

[For Visualization Tools]

Seems like pyalgotrader is better than mfe for the support and full documentation
But mfe looks more beautiful

Trying to encapsulates or wraps mfe and using pyalgotrader's architecture
