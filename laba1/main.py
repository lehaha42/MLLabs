import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class Main:
    def __init__(self, filepath: str):
        pd.options.display.max_columns = 999
        pd.options.display.width = 999  # для отображения всех колонок
        self.df = pd.read_csv(filepath)

    def main(self):
        print(self.df)  # вывести начало и конец файла
        self.df.info()  # вывод инфо о датасете
        print(self.df.describe())  # анализ столбцов


if __name__ == '__main__':
    Main("../dataset/student_depression_dataset.csv").main()
