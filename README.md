# The effect of COVID-19 on the stock market.

Mayss Naber, March 28, 2020

-----

### Resources
The repository includes: 

* The COVID-19 dataset from  : Python script for your analysis: `code.py`
* Results figure/saved file:  `plots/`
* Folder with graphs for README.md file: 'viz'
* The .gitignore file

-----
### Research Question
What is the impact of the COVID-19 virus on the stock market and can we infer any predictive analyses from existing data?

### Abstract 
This study looks into data of both confirmed COVID-19 cases and the S&P 500 (close) prices to generate descriptive
analysis and to (try to) make a predictive one. The descriptive analysis found different stages with 
different relationships between the two factors. First, a lack of relationship followed by a threshold of panic,
with a strong negative correlation. What happens after has yet to unfold, we are still
in the early stages of the pandemic- and because of that, we were unable to infer predictive results.

### Introduction 
The world is facing a pandemic: COVID-19. Millions have lost their jobs, businesses are closing down,
stock markets are crashing... Are we in for a recession, or is this just a panic that will settle down? 
Inspired by a dataset that connected "Total Coronavirus Cases with Worldwide Pornhub Traffic Changes", 
I decided to analyse the relationship between COVID-19 & the stock market, and see if a predictive model could
be inferred.  

### Hypothesis
I hypothesize a strong negative correlation between the two factors. This hypothesis will be tested in upcoming steps.

### Confirmed COVID-19 cases. 

Let us first look at the numbers of confirmed COVID-19 cases. 
As we can see in the graph below, we had a period of relative stabilization of growth rates
followed by a marked and sudden shift into what we have now, which is exponential growth. 
The latter seems to have taken place somewhere between the 1st and 2nd week of March, 2020.
A quick google search of news, filtered to that time frame, provides a general idea as to what happened.
The latter can be summarized with the following Global News article published on March 5th, 2020: 
"*Fears over COVID-19 mount across the West as outbreak eases in China*".  

![COVID-19 Cases](/viz/covid19.png)

That being said, it is important to distinguish between total cases and total *confirmed* cases.
Total *confirmed* cases is subjective to frequency of testing. It is very likely that the virus was spreading
but countries were not testing for it. Given that countries are increasing their frequency of tests,
we cannot, from this data alone, infer any conclusion regarding the actual speed of contagion of COVID-19. 
Instead, we would need to look at numbers given a constant frequency of tests. 

### The Stock Market 
To capture the general behavior of the stock market, I chose to examine 
the S&P 500 stock which measures the stock performance of 500 large companies
listed on US. stock exchanges. 

###### S&P Stock Price (close) from Jan 1, 2019- March 26, 2020.
![S&P 500](/viz/sp500.png)


We saw earlier that the confirmed cases of COVID-19 took a drastic shift in growth rates
during the 2nd week of March 2020, this graph reveals that stock market actually reacted a little bit earlier - in the 
1st week. Given that tests do need a few days to confirm results, then the tests that confirmed those results
also took place on the first week of march (the same time that stock market started crashing here). 
The fact that the stock market reacted before the exponential growth of confirmed cases is very important for analysis.
It means the stock did not actually react to actual increase in confirmed cases. More likely, it reacted to social factors, to a social panic  that took place on the first week of March- a threshold that reflects the shift in people`s attitudes towards the virus. 
The latter leading to both a panic in the stock market &
more COVID-19 testing which generated results on the 2nd week leading to the growth in confirmed cases. 

### Why the 1st week of March?
Why did the world suddenly react to COVID-19 on the 1st week of March? Can this be explained by geographic spread
of the virus? Meaning, did the world react when it first spread outside of China, or did it only react 
when it reached countries like the EU and/or US? Or was this a media induced panic? 

Many variables may be at play here. Understanding them could provide great insight in predicting the socio-economic 
reactions of future potential pandemics. That being said, the factors that induced the sudden shift 
in people's attitudes may be different from the variables that affect the stock market following this shift. 
Understanding what happened requires an entire study of its own and one that I feel inspired to pursue after 
this assignment. For now, I will keep matters simple and focus on what I need for this study: 
* I do not need to look into variables that induced the behavioral
shift, but I do need to do is ensure that my prediction model does not include data that precedes this shift. 
As mentioned, when the number of cases were first rising, the stock market was rising too. 
This would display itself as a positive correlation and that would be inaccurate. 
* This study assumes that confirmed COVID-19 cases do affect the stock market.
But which number of cases should I use for my prediction model? 
What numbers are most affecting the stock market? Is it the number of cases worldwide? The number of cases in the US?
The number of cases after the virus left Wuhan? There are many possibilities at play and answering this question
requires further analysis. Given the scope of this project and because the S&P 500 is based in the US, I will keep things simple and only compare the impact of cases in the US vs worldwide.


### The impact of confirmed COVID-19 case: US vs Worldwide.

In this step we will both test our hypothesis and compare the impact of numbers in the US vs worldwide:

###### COVID-19 Cases & S&P 500 stock price: Computing a correlation (using pearson parameter):

|   | Total Cases (USA) | Total Cases (World) |
|:-------|:---------------|:---------------|
|Stock Price|      -0.613006 |     -0.853012 |



###### COVID-19 Cases & S&P 500 stock price: Scatterplot:

![COVID-19 Scatter Plot](/viz/scatter.png)

The correlation measure displays a rather moderate negative correlation with cases in the US and yet strong negative one with global
ones. The scatterplot, one the other hand, reveals the following:
* First of all, the low density of markers on the right side can be explained by the exponential increase of confirmed cases that
we saw earlier.
* There is a negative correlation with cases in the US. but we can see that the market reacted before the virus reached the US,
when they were still at zero confirmed cases.As such, for our prediction model, we will use the number of cases worldwide. 
* The scatterplot reconfirms a the strong negative correlation with cases worldwide,but we can also see that the fear & panic only began after around 58k confirmed cases. This is in fact same threshold we saw earlier, but rather than seeing it in terms of date, 
we are seeing it in terms of numbers of confirmed cases worldwide. The latter being the x-axis of our prediction model. 
As such, to prevent inaccuracies of the "denial stage", we will simply filter out data for the first 58k confirmed
cases.

### Predictive analysis
 
The method used to model this data was a linear regression with polynomial terms. The latter allows us to fit curves
into our model. Both cubic and quadratic terms were included. The data was then plotted and finally evaluated through
through MSE, RMSE and R2 scores. Unfortunately, the experiment did not succeed 
because running it generates different results. Here are some of the plots that were generated: 

![Prediction #1 ](/viz/prediction.png)


![Prediction #2 ](/viz/prediction2.png)


![Prediction #3 ](/viz/prediction3.png)


![Prediction #4 ](/viz/prediction4.png)


### (Lack of) Results
The very fact of different plots being generated means the MSE, RMSE and R2 are not even worth discussing. It means
the model failed, at least for now. This failure was because the data used was 
too small and became even smaller after excluding the first 58k cases confirmed cases. 

For the most part, the cubic function seems to predict that market prices will continue to fall 
whereas the quadratic function predicts that the prices will start to rise again. This is more likely because
of the last few days of US. government intervention in the stock market that made prices jump (incl. the printing
of money and Trump's stimulus package).

Despite the failure of the model, an important question does arise: Was the stock market slump an unwarranted panic
that will soon be resolved following US. government intervention (as predicted by the quadratic function) -
OR-  is the recent rising in prices only a temporary hype that will soon go back to crashing figures as predicted by the
cubic function  (..most of the time)? 
 
If I were to guess, I would say the latter. But at this moment in time, I do not know enough.

### Conclusion & Discussion

While the predictive model did fail, we were able to extract some valuable insights: 
* The relationship between COVID-19 and the stock market is not as simple as originally predicted and undergoes 
different stages. 
* We have so far seen two stages. At first, there is no impact of the virus on the stock market. 
Then, a sudden shift in people's attitudes towards the virus. This is when a strong negative correlation 
is formed. 

I do expect that we may see other different stages regarding the socio-econmic impact of the virus.
Perhaps, people will undergo some form of adaption and newer technologies will emerge. 
It is again, too soon to tell. I do however, look forward to using my code in the upcoming days/weeks, 
to replug updated numbers and generate newer and better estimates. 

### Future Research

As mentioned, it would be interesting to study the variables that led to the drastic shift on the first week of March, 2020.
It would also be interesting to undergo this same study, but using the Dow Jones stock instead of the S&P 500, to then analyze 
the impact of the virus across different industries.

-----
### References
Links to the datasets: 
* [COVID-19 Geographic Distribution (03/26/2020) *European Centre for Disease Prevention & Control*_](https://www.ecdc.europa.eu/en/publications-data/download-todays-data-geographic-distribution-covid-19-cases-worldwide)


* [ S&P 500 Historical Data, (03/26/2020) *Yahoo! Finance*](https://finance.yahoo.com/quote/%5EGSPC/history/)

