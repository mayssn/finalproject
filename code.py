import os
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
import seaborn as sns
import numpy as np
import sklearn
from sklearn.model_selection import train_test_split
import warnings
warnings.filterwarnings('ignore')

os.makedirs('plots', exist_ok=True)

os.makedirs('picscreen', exist_ok=True)

# To merge columns, we must standardize the formats of date and convert from string to date datatype.
def to_date(x):
    x = x.split('/')  #
    return dt.datetime(year=int("20" + x[2]), month=int(x[0]), day=int(x[1]))


sp = pd.read_csv('sp.csv', delimiter=r",")
sp = sp[['Date', 'Open', 'Close', 'Volume']]

cd = pd.read_csv('cd.csv', delimiter=r",")
cd = cd.rename(columns={
    "DateRep": "Date",
    "Countries and territories": "Country",
    "Cases": "Daily_Cases"}, errors="raise")
cd['Date'] = cd['Date'].apply(to_date)
sp['Date'] = pd.to_datetime(sp['Date'])

# Creating a table for cases in the U.S. and one worldwide.
cd_us = cd[['Date', 'Daily_Cases', 'Deaths', 'Country', 'GeoId']].query("GeoId == 'US'")
cd_world = cd[['Date', 'Daily_Cases', 'Deaths', 'Country', 'GeoId']].groupby(['Date'])['Daily_Cases'].sum()

result_us = pd.merge(sp, cd_us, on='Date')
result_world = pd.merge(sp, cd_world, on='Date')

result_us = result_us[['Date', 'Close', 'Daily_Cases']]
result_world = result_world[['Date', 'Close', 'Daily_Cases']]

# print (cd_us.dtypes)
# print(cd_world.dtypes)
# print(result_us)
# print(result_world)

# Cumulative Sum:  (we have daily confirmed COVID-19 cases but we need the cumulative sum).
result_world['Total_Cases'] = result_world['Daily_Cases'].cumsum(skipna=False)
result_us['Total_Cases'] = result_us['Daily_Cases'].cumsum(skipna=False)
# print(result_us)

# Testing the correlation
corr_world = result_world.corr()
corr_usa= result_us.corr()
print (corr_world)
print (corr_usa)


##Creating the plots to see both dataframes in a comprehensible manner, starting with COVID
fig, ax = plt.subplots()
ax2= sns.lineplot(x="Date", y="Total_Cases", data=result_world, color='pink', label="World")
ax1= sns.lineplot(x="Date", y="Total_Cases", data=result_us, color='r', label="U.S.A")
plt.ylabel('Cases')
plt.xlabel('Date')
ax1.fill_between(result_us['Date'], result_world['Total_Cases'], 0).set_color('pink')
ax2.fill_between(result_world['Date'], result_us['Total_Cases'], 0).set_color('r')
plt.title('COVID-19 Confirmed Cases ')
plt.savefig(f'plots/COVID', format='png')
plt.show()
plt.clf()

# S&P500 close price place
ax3= sns.lineplot(x="Date", y="Close", data=sp, color='r')
plt.ylabel('Price')
plt.xlabel('Date')
plt.title('S&P500 Close Price ')
plt.savefig(f'plots/SP500', format='png')
plt.show()
plt.clf()

# Given the S&P is in the U.S, I wanted to see which had a stronger impact: Corona cases worldwise vs US.
result_world_sortedbycase = result_world.sort_values(['Total_Cases']).reset_index(drop=True)

fig, (ax1, ax2) = plt.subplots(1,2)
ax1.scatter('Total_Cases', 'Close', data=result_us, s=10, c='indianred', marker="o", label='second')
ax1.set_title('Confirmed COVID-19 Cases U.S.A ')
ax1.set_ylabel('S&P 500 close price')
ax2.scatter('Total_Cases', 'Close', data=result_world, s=10, c='firebrick', marker="s", label='first')
ax2.set_title('Confirmed COVID-19 Cases Worldwide ')
ax2.set_ylabel('S&P 500 close price')
plt.savefig(f'plots/scatter', format='png')
plt.show()
plt.clf()


# Stock market only started being affected after > 58000 cases. For predictive purposes, I cut values below that sum.
result_world50k = result_world[result_world['Total_Cases'] > 58000]
# print(result_world50k)


# Split a dataframe between a train and test dataframe using numpy.
# Note:That after we cut off values <58000, we ended up with even less data. Using 20% for train was insufficient.
msk = np.random.rand(len(result_world50k)) < 0.65
train = result_world50k[msk]
test = result_world50k[~msk]

x_train = np.asanyarray(train[['Total_Cases']])
y_train = np.asanyarray(train[['Close']])

x_test = np.asanyarray(test[['Total_Cases']])
y_test = np.asanyarray(test[['Close']])

# Both Linerar and Logistical regressions didn't work. We have to use Polynomial Features
from sklearn.preprocessing import PolynomialFeatures
from sklearn import linear_model
from sklearn import metrics

# Applying Polynomial features with degree 2 and calculate prediction values.
# Then evaluate through MSE, RMSE and R2 score
poly_1 = PolynomialFeatures(degree=2)
x_train_poly = poly_1.fit_transform(x_train)

clf_1 = linear_model.LinearRegression()
train_y_ = clf_1.fit(x_train_poly, y_train)
predicted_value_clf_1 = clf_1.predict(poly_1.fit_transform(x_test))
error_mse_deg_2 = metrics.mean_squared_error(y_test, predicted_value_clf_1)
error_rmse_deg_2 = np.sqrt(metrics.mean_squared_error(y_test, predicted_value_clf_1))
r2_score_deg_2 = metrics.r2_score(y_test, predicted_value_clf_1)
print("Linear 2 degree")
print(clf_1.intercept_)
print(clf_1.coef_)
print("Mean squared Error for Polynomial with 2 degree:", error_mse_deg_2)
print("Root mean squared error for poly with 2 degree:", error_rmse_deg_2)
print("R2 Score for Poly with 2 degree", r2_score_deg_2)

# Applying Polynomial features with degree 3 and calculate prediction values.
# Then evaluate through MSE, RMSE and R2 score
poly_2 = PolynomialFeatures(degree=3)
x_train_poly = poly_2.fit_transform(x_train)

clf_2 = linear_model.LinearRegression()
train_y_ = clf_2.fit(x_train_poly, y_train)
predicted_value_clf_2 = clf_2.predict(poly_2.fit_transform(x_test))
error_mse_deg_3 = metrics.mean_squared_error(y_test, predicted_value_clf_2)
error_rmse_deg_3 = np.sqrt(metrics.mean_squared_error(y_test, predicted_value_clf_2))
r2_score_deg_3 = metrics.r2_score(y_test, predicted_value_clf_2)
print("Linear 3 degree")
print(clf_2.intercept_)
print(clf_2.coef_)
print("Mean squared Error for Polynomial with 3 degree:", error_mse_deg_3)
print("Root mean squared error for poly with 2 degree:", error_rmse_deg_3)
print("R2 Score for Poly with 3 degree", r2_score_deg_3)


def f_1(x):
    return clf_1.intercept_[0] + clf_1.coef_[0][1] * x + clf_1.coef_[0][2] * x ** 2


def f_2(x):
    return clf_2.intercept_[0] + clf_2.coef_[0][1] * x + clf_2.coef_[0][2] * x ** 2 + clf_2.coef_[0][3] * x ** 3


# Plot the final graph of applied model with legend.
plt.scatter(result_world50k.Total_Cases, result_world50k.Close, color='deepskyblue', label='Train values')
plt.scatter(x_test, predicted_value_clf_1, color="lime", label='Predicted val Quadratic')
plt.scatter(x_test, predicted_value_clf_2, color='orangered', label='Predicted val Cubic')
xx = np.arange(58 * 10 ** 3, 4 * 10 ** 5)
plt.plot(xx, f_1(xx), '-g', label='Quadratic')
plt.plot(xx, f_2(xx), '-r', label='Cubic')
plt.title(' The effect of COVID-19 on the stock value of S&P500 ')
plt.xlabel('Cases')
plt.ylabel('Close Price')
plt.legend(loc='lower right')
plt.savefig(f'plots/prediction4', format='png')
plt.show()
plt.clf()

# I would have liked to do the formula that would regenerate this code various times and save it
# under different names to get the different graphs generated in one code. But my time is too limited
#to figure it out



