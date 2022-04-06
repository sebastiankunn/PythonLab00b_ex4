import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
if __name__ == '__main__':
    exer=input("insert exercise number\n")
    match exer:
        case '1':
            sales = pd.read_csv("sales_data.csv")
            profit=sales['total_profit'].values
            months=sales['month_number'].values
            plt.plot(months,profit,label = 'Profit data of last year',color='r',marker='o',markerfacecolor='k', linestyle='-', linewidth=3.0)
            plt.xlabel('Months')
            plt.ylabel( 'Profit')
            plt.xticks(months)
            plt.title('Profit for month')
            plt.yticks([100e3, 200e3, 300e3, 400e3, 500e3])
            plt.show()
        case '3':
            sales = pd.read_csv("sales_data.csv")
            fc=sales['facecream'].values
            fw=sales['facewash'].values
            tp=sales['toothpaste'].values
            bs=sales['bathingsoap'].values
            s=sales['shampoo'].values
            m=sales['moisturizer'].values
            months = sales['month_number'].values
            plt.figure()
            plt.plot(months, fc,label='Face cream')
            plt.plot(months, fw, label='Face wash')
            plt.plot(months, tp, label='Toothpaste')
            plt.plot(months, bs, label='Bathing soap')
            plt.plot(months, s, label='Shampoo')
            plt.plot(months, m, label='Moisturizer')
            plt.xlabel('Months')
            plt.ylabel('Sales')
            plt.legend(loc='upper left')
            plt.xticks(months)
            plt.yticks([1e3, 2e3, 4e3, 6e3, 8e3, 10e3, 12e3, 15e3, 18e3])
            plt.title('Sales Data')
            plt.show()
        case '4':
            sales=pd.read_csv("sales_data.csv")
            tp=sales['toothpaste'].values
            months=sales['month_number'].values
            plt.figure()
            plt.scatter(months,tp)
            plt.xlabel('Months')
            plt.ylabel('Toothpaste sales')
            plt.xticks(months)
            plt.title('Toothpaste sales data')
            plt.show()
        case '5':
            sales=pd.read_csv("sales_data.csv")
            bs=sales['bathingsoap'].values
            months=sales['month_number'].values
            plt.figure()
            plt.bar(months,bs)
            plt.xlabel('Months')
            plt.ylabel('Bathing soap sales')
            plt.xticks(months)
            plt.title('Bathing soap sales data')
            plt.show()
        case '6':
            sales = pd.read_csv("sales_data.csv")
            total = sales['total_profit'].values
            months = sales['month_number'].values
            profit_range = [150e3, 175e3, 200e3, 225e3, 250e3, 300e3, 350e3]
            plt.figure()
            plt.hist(total,profit_range)

            plt.xlabel('Months')
            plt.ylabel('Total profit')
            plt.xticks(profit_range)
            plt.title('Total profit data')
            plt.show()
        case '7':
            sales = pd.read_csv("sales_data.csv")
            bs = sales['bathingsoap'].values
            fw = sales['facewash'].values
            months = sales['month_number'].values
            fig, axs = plt.subplots(1, 2, figsize=(5, 5))
            axs[0].plot(months,bs)
            axs[1].plot(months,fw)
            plt.show()
