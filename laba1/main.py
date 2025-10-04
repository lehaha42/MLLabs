import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class Main:
    def __init__(self, filepath: str):
        pd.options.display.max_columns = 999
        pd.options.display.width = 999  # для отображения всех столбцов
        self.df = pd.read_csv(filepath)

    def main(self):
        print(self.df)  # вывести начало и конец файла
        self.df.info()  # вывод инфо о датасете
        print(self.df.describe())  # анализ столбцов
        print(self.df.columns)  # вывод столбцов
        # Количество уникальных значений
        for column in self.df.columns:
            print(f'{column}: {self.df[column].nunique()} уникальных значений')
        # Графики
        if input('show?(Y/N):') != 'N':
            for column in self.df.columns[1:]:
                sns.histplot(self.df[column], kde=True)
                plt.title(f'Распределение {column}')
                plt.xlabel(column)
                plt.ylabel('Частота')
                plt.show()
        # Boxplit всех столбцов
        if input('show?(Y/N):') != 'N':
            for column in self.df.columns[1:]:
                sns.boxplot(x=self.df[column])
                plt.title(f'Boxplot {column}')
                plt.xlabel(column)
                plt.show()
                """
                id:
                Gender:
                Age: 
                City: 
                Profession: 
                Academic Pressure:
                Work Pressure:
                CGPA:
                Study Satisfaction:
                Job Satisfaction:
                Sleep Duration:
                Dietary Habits:
                Degree: 
                Have you ever had suicidal thoughts ?:
                Work/Study Hours: 
                Financial Stress:
                Family History of Mental Illness:
                Depression:
                """
        # Визуализация тепловой карты
        if input('show?(Y/N):') != 'N':
            self.df = self.df.drop('Gender', axis=1)
            self.df = self.df.drop('City', axis=1)
            self.df = self.df.drop('Profession', axis=1)
            self.df = self.df.drop('Sleep Duration', axis=1)
            self.df = self.df.drop('Dietary Habits', axis=1)
            self.df = self.df.drop('Degree', axis=1)
            self.df = self.df.drop('Have you ever had suicidal thoughts ?', axis=1)
            self.df = self.df.drop('Financial Stress', axis=1)
            self.df = self.df.drop('Family History of Mental Illness', axis=1)
            correlation_matrix = self.df.corr()
            sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
            plt.title('Корреляционная матрица')
            plt.show()
            """сильная корреляция: job satisfaction - Pressure;
               средняя корреляция: depression - pressure; 
                слабая корреляция: depression - age, depression - study satisfaction, depression - study hours"""


if __name__ == '__main__':
    Main("../dataset/student_depression_dataset.csv").main()
