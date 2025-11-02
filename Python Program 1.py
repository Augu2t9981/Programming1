#10/28/2025

#Weather Severity Project
#In hurricane season, we would like to keep track of the severity of the weather. We will invent a measure of weather
#severity that combines the wind speed, and rain fall. Ask the user to enter data on the wind and rain for several days
#ending with -1.0 (sentinel value). The program will use a sentinel controlled loop. The program will count the number
#of days entered, and that count is included in the output.

#The weather severity will be calculated by adding:
    #Average rain multiplied by 10,the average wind.

#For example, if the  average rain is 0.55 inches, and the average wind is 30 mph, the weather severity will be ( 0.55 x
#10 ) + 30.0 = 35.5 The program will output the average rain, and average wind.  It will also output the number of days
#for which data were entered, and the weather severity.

#This is the output that must be produced from you input
#Output
#The average rain is 1.9 inches
#The average wind is 35.0 mph
#The weather severity for these 3 readings is: 54.0

#We can use an object-oriented program or a function used by prior assignments this week.
#This code must continuously produce data sets until -1.0.

#How would I create a program without a break statement

def main():
    print("How is the weather outside:")

    total_rain = 0.0
    total_wind = 0.0
    count = 0

    weather = True
    while weather:
        rain, wind = map(float, input("Enter the val for rain and wind: ").split())
        if rain == -1.0:
            weather = False
        else:
            total_rain += rain
            total_wind += wind
            count += 1

    avg_rain = total_rain / count
    avg_wind = total_wind / count
    avg_severity = (avg_rain * 10) + avg_wind

    print("\n=== Weather Report Summary ===")
    print(f"Average rain: {avg_rain} inches")
    print(f"Average wind: {avg_wind} mph")
    print(f"Weather severity for these 3 readings is: {avg_severity}")

print(main())