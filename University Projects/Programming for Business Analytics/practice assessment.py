#######################################################################################################################################################
# 
# Name: Mateusz Paw
# SID: 730068016
# Exam Date: 13/12/2024
# Module: BEMM458_A_1_202425
# Github link for this assignment: https://github.com/UniversityExeterBusinessSchool/bemm458-2425-practice-assessment-8-35am-MateuszPawlaczyk1
#
# ######################################################################################################################################################
# Instruction 1. Read the questions and instructions carefully and complete scripts.

# Instruction 2. Only ethical and mininal use of AI is allowed. You might use AI to give advice on how to use a tool or programming language.  
#                You must not use AI to create the code. You might make use of AI to aid debugging of the code.  
#                You must indicate clearly how and where you have used AI.

# Instruction 3. Copy the output of the code and insert it as a comment below your code e.g # OUTPUT (23,45)

# Instruction 4. Ensure you provide comments for the code and the output to show contexual understanding.

# Instruction 5. Upon completing this test, commit to Git, copy and paste your code into the word file and upload the saved file to ELE.
#                There is a leeway on when you need to upload to ELE, however, you must commit to Git at 
#                the end of your session.


# ######################################################################################################################################################
# Question 1 - Loops
# Create a list and use a for loop to answer the following question:
# You are given a dictionary called key_comments. Your allocated keys are the first and last digit of your SID.
# Find the start and end position of each of the items in the sentence using the find command.
# Create and populate a list called my_list with a tuple of (start location, end location) for each value in comments 
 

customer_feedback = """I would like to provide comprehensive feedback on my recent experience with your service. While there are several positives 
I would like to highlight, I also want to offer a few constructive points that I believe could help improve the overall customer experience.

1. Initial Interaction and User-Friendliness
When I first interacted with your platform, I was impressed by the clean design and overall simplicity of the interface. The website’s layout
is intuitive, making it easy to navigate and find relevant information without too much effort. However, I did encounter a few usability 
challenges, particularly in terms of finding specific product details. For example, while browsing through your product catalog, I found 
that some of the product descriptions were not as detailed as I would have liked. Including more comprehensive product specs, usage instructions, 
and perhaps even customer reviews directly on the product page would add immense value and streamline the decision-making process for potential buyers.

2. Product/Service Quality
The quality of the product/service I received was mostly satisfactory. I noticed a high level of attention to detail, which I greatly appreciate. 
The product itself performed as expected, and I found it to be reliable and well-built. That being said, there are a few areas where quality 
control could be slightly improved. In my case, one of the items had a minor defect, and although it did not significantly impact its 
functionality, it did affect the overall impression of the product’s durability. It would be great if additional quality checks were conducted 
before dispatching orders, ensuring that customers receive items in perfect condition every time.
"""

# List of words to search for
key_comments = {
    6: 'defect',
    7: 'durability'}

# Write your search code here and provide comments. 

defect = ((customer_feedback.find('defect'), customer_feedback.find('defect')+len('defect')))
durability = ((customer_feedback.find('durability'), customer_feedback.find('durability')+len('durability')))


# Initialize an empty list to store (start, end) positions

my_list = []

for key, word in key_comments.items():
    first_pos = customer_feedback.find(word)
    end_pos = first_pos + len(word)
    my_list.append((first_pos, end_pos))

print(' The list of first and end positions of the two words is:', my_list)


# This code helps business analysts find key words in customer feedback. Future improvements can be made to also count how many times a certain word
# has been mentioned. This helps businesses better analyse text and gain a better understanding of customer sentiments


##########################################################################################################################################################

# Question 2 - Functions
# Scenario - You are working in an SME as a business analyst and your manager has tasked you to generate weekly reports on metrics like 
# Profit Margin (Net profit margin), Customer Acquisition Cost (CAC), Net Promoter Score (NPS) and Return on Investment (ROI). Use python functions 
# that will take the values and return the metric needed. use the first two and last two digits of your ID number as the input values

# Insert first two digits of ID number here: 73
# Insert last two digits of ID number here: 16

# Write your code for Profit Margin (Net profit margin) 
def net_profit_margin(net_profit, revenue):
    return ((net_profit / revenue) * 100)

# Write your code for Customer Acquisition Cost (CAC)
def CAC(total_marketing_cost, new_customers_aquired):
    return (total_marketing_cost / new_customers_aquired)

# Write your code for Net Promoter Score (NPS)
def NPS(promoters, defectors, total_respondents):
    return (((promoters - defectors) / total_respondents) * 100)

# Write your code for Return on Investment (ROI)
def ROI(net_investment_gain, investment_cost):
    return ((net_investment_gain / investment_cost) * 100)

# Call your designed functions here
print('The Net Profit Margin is:', net_profit_margin(73, 16))

print('The Customer Acquisition Cost is:', CAC(73, 16))

print('The Net Promoter Score is:', NPS(73, 16, 16))

print('The Return on Investment is', ROI(73, 16))

# From the business analytics perspective, these function allow businesses to extract specific pieces of data from datasets, which are often large
# and difficult to make sense out of. This allows companies to save time on crucial analysis and planning, which helps them grow and be more responsive.

##########################################################################################################################################################

# Question 3 - Forecast
# A furniture shop has recently acquired a pair of table and chairs and the data below shows the different prices considered and the corresponding demand.
# Develop a linear regression model and determine
# 1 the optimal price 
# 2 The demand when the company sets the price at £33
"""
Price (£)    Demand (Units)
---------------------------
10           120
12           115
14           105
16           100
18           90
20           85
22           80
24           75
26           68
28           60
30           55
"""

# Write your code here

import statsmodels.api as sma


# Part 2
price = [10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30] # independent
demand = [120, 115, 105, 100, 90, 85, 80, 75, 68, 60, 55] # dependent

model = sma.OLS(demand, sma.add_constant(price)) 
result = model.fit()
#print(result.summary()) # in case we would like to dig deeper and learn more details about the data


predicted_demand = result.predict([1,33])
print('The predicted demaned at $33 is:', predicted_demand[0])


# The significance of using forecasting code is that it helps business analysts create strategies that are optimised and backed by data.
# As such, companies can maximise their revenue, sales, or other metrics.
# Using code in analysis helps business analysts justify their decisions and influence senior management more  effectively.

##########################################################################################################################################################

# Question 4 - Debugging; Plotting and data visualisation chart

import random
import matplotlib.pyplot as plt # error found using AI

# Generate 100 random numbers between 1 and student id number
max_value = int(input("Enter your Student ID: "))
random_numbers = [random.randint(1, max_value) for _ in range(100)]

# Plotting the numbers in a line chart
plt.plot(random_numbers, marker='o', linestyle='-', color='b', label='Random Numbers')
plt.title('Line Chart of 100 Random Numbers') 
plt.xlabel('Index')
plt.ylabel('Random Number')
plt.legend()
plt.grid(True)
plt.show() # error found using AI

# Title not in commas
# fixed import matplotlib.pyplot as plt
# fixed parentheses after plt.show()

# The bug that prevents the code from running is the title 'Line Chart of 100 Random Numbers' not being in commas, which means that python treated it
# not as a string (text), but as variable names, which is incorrect as no such variables exist.

# The second bug could prevent the graph from appearing on other computers, as the library is not defined as plt, but all the codes use plt. syntax.

# The final fix is largely cosmetical but it's good practice to write code in 100% correct syntax

# Debugging and double checking is an important part of business analytics as it ensures that companies do not generate misleading data, or 
# data that cannot be generated on other computers. 

##########################################################################################################################################################
