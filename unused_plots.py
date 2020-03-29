
# sns.lineplot(x="Date", y="Close", data=sp)
# plt.ylabel('S&P Close Price')
# plt.xlabel('Date')
# plt.show()
# plt.clf()
# #
# sns.lineplot(x="Date", y="Daily_Cases", data=result_us)
# plt.ylabel('Daily Corona Cases in the U.S.')
# plt.xlabel('Date')
# plt.show()
# plt.clf()
#
# sns.lineplot(x="Date", y="Daily_Cases", data=result_world)
# plt.ylabel('Daily Corona Cases Worldwide')
# plt.xlabel('Date')
# plt.show()
# plt.clf()
#
# result_us_sortedbycase = result_us.sort_values(['Daily_Cases']).reset_index(drop=True)
# sns.scatterplot('Daily_Cases', 'Close', data=result_us)
# plt.show()
# plt.clf()
#
# result_world_sortedbycase = result_world.sort_values(['Daily_Cases']).reset_index(drop=True)
# sns.scatterplot('Daily_Cases', 'Close', data=result_world)
# plt.show()
# plt.clf()


result_us_sortedbycase = result_us.sort_values(['Total_Cases']).reset_index(drop=True)
# sns.scatterplot('Total_Cases', 'Close', data=result_us)
# plt.title('COVID-19 cases (USA) vs. S&P500 price')
# plt.xlabel('COVID-19 cases (USA)')
# plt.ylabel('Close price')
# plt.show()
# plt.clf()

# sns.scatterplot('Total_Cases', 'Close', data=result_world)
# plt.title('COVID-19 cases worldwide vs. S&P500 close price')
# plt.xlabel('COVID-19 cases')
# plt.ylabel('Close price')
# plt.show()
# plt.clf()
#

## sns.lineplot(x="Date", y="Total_Cases", data=result_us)
# plt.ylabel('Total COVID-19 Cases in the U.S.')
# plt.xlabel('Date')
# plt.show()
# plt.clf()
#
# sns.lineplot(x="Date", y="Total_Cases", data=result_world)
# plt.ylabel('Total COVID-19 Cases Worldwide')
# plt.xlabel('Date')
# plt.show()
# plt.clf()
#

# # a very ugly plot to delete which is the list of daily cases by country
# # sns.lineplot(x="Date", y="Daily_Cases", hue="Country", data=cd)
# # plt.ylabel('Total Corona Cases in the U.S.')
# # plt.xlabel('Date')
# # plt.show()
# # plt.clf()
#
# # Double Plot ! First: Worldwide
# fig, (ax1, ax2) = plt.subplots(2)
# fig.suptitle('COVID-19 Cofirmed Cases and S&P Close Price Value')
# ax1.plot(result_world['Date'], result_world['Total_Cases'],'tab:green')
# ax1.set_ylabel('between y1 and 0')
# ax2.plot(result_world['Date'], result_world['Close'],'tab:red')
# plt.show()
# plt.clf()
#
# # Wanted to color under the graph but in the end it didn't make sense to.
# # ax1.fill_between(result_world['Date'], result_world['Total_Cases'], 0).set_color('g')
# # ax2.fill_between(result_world['Date'], result_world['Close'], 0).set_color('r')
#
#
# # Double Plot ! Second: USA
# fig, (ax1, ax2) = plt.subplots(2)
# fig.suptitle('COVID-19 Cofirmed Cases and S&P Close Price Value')
# ax1.plot(result_us['Date'], result_us['Total_Cases_Cases'],'tab:green')
# ax1.fill_between(result_us['Date'], result_us['Total_Cases_Cases'], 0).set_color('g')
# ax1.set_ylabel('between y1 and 0')
# ax2.plot(result_world['Date'], result_world['Close'],'tab:red')
# plt.show()
# plt.clf()
