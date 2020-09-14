# Collegiate Advantage
An analysis on salaries with respect to major and college to determine a 
relationship between prestige and monetary success.

This README describes some preliminary findings that will eventually be made into a more presentable format. 

Also check out [the Kaggle notebook](https://www.kaggle.com/dylanpjackson/collegiate-advantage) for some initial analysis.

## Findings / Visualizations
Mid-Career Salaries, displayed with Python:
![alt text](https://github.com/DylanPJackson/collegiate_advantage/blob/master/imgs/all_types.png)

Median Starting Salaries by Major, displayed with R:
![Median Starting Salaries vs Major](https://github.com/DylanPJackson/collegiate_advantage/blob/master/imgs/starting_major_R.png)

### Noteworthy Findings 
* Ivy League has the highest salary, except for 10th Percentile Mid Career which it loses to by Engineering by only about $4,000
* Ivy League salary beats every other type in every group by an increasing margin
* A comparison between Ivy League and second place
  * [category] : [Ivy League's difference] - [type]
  * Starting : +$1417 - Engineering
  * Mid Career : +$16282 - Engineering
  * 25th Mid Career : +$1402 - Engineering
  * 75th Mid Career : +$49256 - Engineering
  * 90th Mid Career : +$78482 - Liberal Arts
* What type of school would be considered 'second best'?
  * Easily Engineering, until 75th percentile for Mid Career when it becomes very close to Liberal Arts, and is eventually succeeded by it in the 90th percentile
* Who has the highest growth potential?
  * Ivy League, easily
  * Then Liberal Arts by a large margin
  * Then Engineering / Party schools about equally
  * Finally State schools
* What is the best school for the 'average graduate'?
  * Decidedly Ivy League
  * Engineering decidedly in second by ~$16,000 less
  * Liberal Arts in third by ~$30,000 less
  * Party and State by ~$55,000 less 
    * Liberal Arts schools have the same distance from Engineering schools as Engineering schools have from Ivy League, so if you were to say Ivy League is the best of all types, then Engineering iis the best of the rest. 

## Why?
A little while ago, I had a conversation with my cousin and my other cousin's
girlfriend. We had differing beliefs on what sort of advantage your college
and major gets you in your career. I wanted to determine which side had more
truth to it, so I decided to find some data to maybe clear up the matter. 

[This data](https://www.kaggle.com/wsj/college-salaries?select=degrees-that-pay-back.csv)
is from a fairly popular Kaggle dataset published three years ago, which was 
taken from a publication by the Wall Street Journal, sourced by PayScale.
It contains various salary data arranged by school and major which reports
Starting Median Salary, Median Starting Salary, and the 10th, 25th, 75th, and 
90th percentiles for Starting Salary.

My goal is to identify what sort of advantage you get based off of your major 
and school, and to what effect 'prestige' plays into that edge. I want to take
a couple different approaches to this, namely in the way I work with the data. 
I'll start by familiarizing myself with the data in Python, then transition to 
R and eventually a database approach. This is mainly for my own practice, and
also because I want to see what limitations / advantages each of these
approaches offers. 


