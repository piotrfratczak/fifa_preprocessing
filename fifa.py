import preprocessing
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import tree
from sklearn import metrics
from sklearn.model_selection import train_test_split

test_size = 0.4
min_impurity_decrease = 1.5


data = preprocessing.preprocess('data.csv')

# print first few rows of the pre-processed data
print(data.head().to_string())


X = data.drop('Wage', axis=1)  # features
y = data['Wage']               # target
# randomly split the data to the training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size)


# get the best pruning option for the decision tree
y_pred = None
dt = None
best = (0.0, 0, dt, y_pred)
for depth in range(3, 20):
    dt = tree.DecisionTreeRegressor(max_depth=depth, min_impurity_decrease=min_impurity_decrease)
    dt.fit(X_train, y_train)
    y_pred = dt.predict(X_test)
    s = (metrics.r2_score(y_test, y_pred), depth, dt, y_pred)
    best = max(best, s)
print('\nR2: ', best[0], '\nMaximal depth of the decision tree: ', best[1], '\n')
dt = best[2]
y_pred = best[3]


# decision tree plot
#plt.figure(figsize=(64, 32))
#tree.plot_tree(dt)
#plt.show()

# Relation Between Jersey Number and Wage of a Player
fig = data.plot(kind='scatter', x='Wage', y='Jersey Number', color='blue')
fig.set_title("Relation Between Jersey Number and Wage of a Player")
fig.set_xlabel('Wage [k€]')
fig = plt.gcf()
plt.show()

# Plot actual target against features
plt.scatter(X_train['Overall'], y_train, c='steelblue', edgecolor='white', s=70)
# Sort X and y by ascending values of Value
plot_x = X_test.loc[:, 'Overall'].values
sort_idx = plot_x.flatten().argsort()
plot_x = plot_x[sort_idx]
plot_y = y_pred[sort_idx]
# Plot predicted target against features
plt.plot(plot_x, plot_y, color='black', lw=2)
plt.xlabel('Overall')
plt.ylabel('Wage [k€]')
plt.show()

df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
print(df)

print('R2 score:', best[0])
print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))
