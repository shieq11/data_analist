# # with open("weather_data.csv") as data_file:
# #     data = data_file.readlines()
#
# # import csv
# #
# # with open("weather_data.csv") as data_file:
# #     data = csv.reader(data_file)
# #     temperature = []
# #     for row in data:
# #         if row[1] != "temp":
# #             temperature.append(int(row[1]))
# #     print(temperature)
#
# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# # print(type(data))
# # print(data["temp"])
#
# # data_dict = data.to_dict()
# # print((data_dict))
# #
# #
# # temp_list = data["temp"].to_list()
# # print(temp_list)
#
# # average = round(sum(temp_list)/ len(temp_list),2)
# # print(average)
# # print(data["temp"].mean())
# #
# # print(data["temp"].max())
#
# # print(data["condition"])
# # print(data.condition)
#
# # Czytanie wybranej linijki z pliku
# # print(data[data.day == "Monday"])
# # print(data[data.temp == data.temp.max()])
#
# # monday = data[data.day == "Monday"]
# # monday_temp_F = monday.temp * 1.8 + 32
# # print(monday_temp_F)
#
# #  Create dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")
import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
black = len(data[data["Primary Fur Color"] == "Black"])
gray = len(data[data["Primary Fur Color"] == "Gray"])
red = len(data[data["Primary Fur Color"] == "Cinnamon"])

data_dict ={
    "color": ["black", "gray", "red"],
    "count": [black, gray, red ]
}

squirrel = pandas.DataFrame(data_dict)
squirrel.to_csv("squirrel_count.csv")