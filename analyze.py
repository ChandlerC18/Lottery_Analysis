import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

## frequency of each number
def single_frequency_number(df, filename, add_title=''):
    def count(row):
        # print(row['Mega ball'] - 1)
        mega[row['Mega ball'] - 1] += 1
        for i in range(1, 6):
            arr[row[f'Ball {i}'] - 1] += 1

    max_num = df[['Ball 1', 'Ball 2', 'Ball 3', 'Ball 4', 'Ball 5']].max().max()
    max_mega = max(df['Mega ball'])

    arr = [0 for i in range(max_num)]
    mega = [0 for i in range(max_mega)]
    df.apply(count, axis=1)

    ball_freq_df = pd.DataFrame({'Number' : range(1, len(arr) + 1), 'Frequency' : arr})
    mega_freq_df = pd.DataFrame({'Number' : range(1, len(mega) + 1), 'Frequency' : mega})

    fig, ax = plt.subplots(1, 2, figsize=(15,8))
    sns.barplot(data=ball_freq_df, x='Number', y="Frequency", ax=ax[0], color='lightskyblue')
    ax[0].title.set_text('Frequency of ball numbers' + add_title)
    ax[0].set_xticks(ax[0].get_xticks()[::5])

    sns.barplot(data=mega_freq_df, x='Number', y="Frequency", ax=ax[1], color='orchid')
    ax[1].title.set_text('Frequency of Mega Ball numbers' + add_title)
    ax[1].set_xticks(ax[1].get_xticks()[::5])

    plt.tight_layout() # compresses the layout of the figure
    plt.savefig(os.path.join(save_directory, filename)) # saves the figure
    plt.show()

def single_frequency_number_by_year(year):
    year_df = df.loc[df['Date'].str[-4:] == str(year)]
    single_frequency_number(year_df, f'single_frequency_number_{year}.png', add_title=f' in {year}')

def pair_frequencies(df, filename, add_title=''):
    def count(row):
        balls = [f'Ball {i}' for i in range(1, 6)]

        for i in balls:
            for j in balls:
                if i != j:
                    pairs.iloc[row[i] - 1][row[j]] += 1

    max_num = df[['Ball 1', 'Ball 2', 'Ball 3', 'Ball 4', 'Ball 5']].max().max()
    pairs = pd.DataFrame({i : [0 for j in range(max_num)] for i in range(1, max_num + 1)}, index=range(1, max_num + 1))
    df.apply(count, axis=1)

    fig, ax = plt.subplots(figsize=(8,8))
    sns.heatmap(data=pairs, cmap='PuBu', square=True, annot=False)
    plt.title('Frequency of pairs of numbers' + add_title)

    plt.tight_layout() # compresses the layout of the figure
    plt.savefig(os.path.join(save_directory, filename)) # saves the figure
    plt.show()

def pair_frequencies_by_year(year):
    year_df = df.loc[df['Date'].str[-4:] == str(year)]
    pair_frequencies(year_df, f'pair_frequencies_number_{year}.png', add_title=f' in {year}')

if __name__ == '__main__':
    df = pd.read_csv('lottery_data.csv')

    save_directory = 'Plots'
    if not os.path.exists(os.path.join(save_directory)):
    	os.mkdir(os.path.join(save_directory)) # create directory to save figures if it does not already exist

    # single_frequency_number(df, 'single_frequency_numbers.png')

    pair_frequencies(df, 'pair_frequencies.png')

    for i in range(1996, 2023):
    #     single_frequency_number_by_year(i)

        pair_frequencies_by_year(i)
