import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class Main:
    def __init__(self, filepath: str):
        self.df = pd.read_csv(filepath)

    def main(self):
        print(self.df)  # вывести начало и конец файла
        self.df.info()  # вывод инфо о датасете


if __name__ == '__main__':
    Main("../dataset/student_depression_dataset.csv").main()
