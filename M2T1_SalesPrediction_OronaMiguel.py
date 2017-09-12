#CTI-110
#M2T1 - Sales Prediction
#Miguel Orona
#9/7/2017
#A program that predicts sales.

#Get the projected total sales.
total_sales = float (input('Enter the projected sales: '))

#Calculate the profit as 23 percent of total sales.
profit = total_sales * 0.23

#Display the profit.
print ('The profitis $', format (profit, ',.2f'))

