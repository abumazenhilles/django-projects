from django.shortcuts import render
import pandas as pd
import matplotlib.pyplot as plt


def home(request):
    return render(request, 'dashboard.html')


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def article(request):
    return render(request, 'article_list.html')


def forum(request):
    return render(request, 'forum/post_list.html')


def researchG(request):
    # df = pd.read_csv("C:\\projects\\Django\\CPSevents\\mysite\\articlesstatic\\sales_data.csv")
    # profitList = df['total_profit'].tolist()
    # monthList = df['month_number'].tolist()
    # plt.plot(monthList, profitList, label='Month-wise Profit data of last year')
    # plt.xlabel('Month number')
    # plt.ylabel('Profit in dollar')
    # plt.xticks(monthList)
    # plt.title('Company profit per month')
    # plt.yticks([100000, 200000, 300000, 400000, 500000])
    # plt.show()
    covid_data= pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/03-17-2020.csv')
    print(covid_data)
    print("\nDataset information:")
    print(covid_data.info())
    print("\nMissing data information:")
    print(covid_data.isna().sum())
    return render(request, 'researchguide.html')


# class Persptron(object):
#     def __init__(self, eta=0.01, n_iter=50, random_state=1):
#         self.eta = eta
#         self.n_iter = n_iter
#         self.random_state = random_state

#     def fit(self, X, y):
#         rgen = np.random.RandomState(self.random_state)
#         self.w_ = rgen.normal(loc=0.0, scale=0.01, size=1 + X.shape[1])
#         self.error_ = []

#         for _ in range(self.n_iter):
#             errors = 0
#             for xi, target in zip(X, y):
#                 update = self.eta * (target - self.predict(xi))
#                 self.w_[1:] += update * xi
#                 self.w_[0] += update
#                 errors += int(update != 0.0)
#             self.errors_.append(errors)
#         return self

#     def net_input(self, X):
#         return np.dot(X, self.w_[1:]) + self.w_[0]

#     def predict(self, X):
#         return np.where(self.net_input(X) >= 0.0, 1, -1)


# v1 = np.array([1, 2, 3])
# v2 = 0.5 * v1
# np.arccos(v1.dot(v2) / (np.linalg.norm(v1) + np.linalg.norm(v2)))
