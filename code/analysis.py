import os
import numpy as np
import pandas as pd
import matplotlib
import seaborn as sns
from scipy import stats
import math
import matplotlib.pyplot as plt

def sort_df(df):
    df = df.sort_values(by=['x','y','z','yaw','pitch','roll'])
    return df

def plot(file):
    doplot = 1
    df = pd.read_csv(f'./results/{file}.csv')
    
    df_tmp = df
    ax = sns.lineplot(x=f'{file}', y=f'vmaf', data=df_tmp)
    ax.set(xlabel=f"{file}", ylabel=f"VMAF")
    # plt.xticks(range(0,91,30))
    # plt.xlim((0,90))
    plt.ylim((0,100))
    if doplot:
        plt.savefig(f'./plots/{file}.png', dpi=300)
    plt.show()

def main():
    files = ['x','y','z','yaw','pitch','roll']
    # for file in files:
    #     df = pd.read_csv(f'./results/{file}_old.csv')
    #     df = sort_df(df)
    #     df.to_csv(f'./results/{file}.csv')
    for file in files:
        plot(file)

if __name__ == '__main__':
    main()