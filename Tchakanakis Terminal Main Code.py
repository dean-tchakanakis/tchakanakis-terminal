###################################################################

# Tchakanakis Terminal

# Dean Tchakanakis

# A program that mimics a Bloomberg Terminal. The user is able to 
# be shown a statistical analysis or a graph comparing up to three
# different stock indexes, for a chosen year range. This program
# also features extensive error handling.

# Run the program and follow the instructions on the screen
# carefully.

###################################################################


import turtle
import math
import statistics
import matplotlib.pyplot as plt

def bounce_image(image, starty):
    for i in range(40):
        image.sety(starty + 1)
        starty += 1

    for i in range(40):
        image.sety(starty - 1)
        starty -= 1

def welcome_screen():
    screen.bgcolor("grey10")
    screen.title("")

    header = turtle.Turtle()
    header.speed(0)
    header.color("orange")
    header.penup()
    header.hideturtle()
    header.goto(0,250)
    header.write("Welcome to the Tchakanakis Terminal!", align="center", font=("Courier New", 40, "bold"))

    text1 = turtle.Turtle()
    text1.speed(0)
    text1.color("orange")
    text1.penup()
    text1.hideturtle()
    text1.goto(0,200)
    text1.write("This terminal allows you to analyze and compare", align="center", font=("Courier New", 18, "normal"))

    text2 = turtle.Turtle()
    text2.speed(0)
    text2.color("orange")
    text2.penup()
    text2.hideturtle()
    text2.goto(0,170)
    text2.write("financial data for the three stock indexex below.", align="center", font=("Courier New", 18, "normal"))

    subheader = turtle.Turtle()
    subheader.speed(0)
    subheader.color("orange")
    subheader.penup()
    subheader.hideturtle()
    subheader.goto(0,40)
    subheader.write("Please enter one of the following files into the terminal to conintue.", align="center", font=("Courier New", 18, "normal"))

    turtle.addshape("dowjones.gif")
    turtle.addshape("nasdaq.gif")
    turtle.addshape("sp500.gif")

    dowjones = turtle.Turtle()
    dowjones.hideturtle()
    dowjones.penup()
    dowjones.shape("dowjones.gif")
    dowjones.goto(-450,-150)
    dowjones.showturtle()

    nasdaq = turtle.Turtle()
    nasdaq.hideturtle()
    nasdaq.penup()
    nasdaq.shape("nasdaq.gif")
    nasdaq.goto(0,-150)
    nasdaq.showturtle()

    sp500 = turtle.Turtle()
    sp500.hideturtle()
    sp500.penup()
    sp500.shape("sp500.gif")
    sp500.goto(450, -150)
    sp500.showturtle()

    index_list = [dowjones, nasdaq, sp500]
    for i in range(3):
            bounce_image(index_list[i], -150)

def space_to_begin_screen():
    screen.bgcolor("grey10")
    screen.title("")

    header = turtle.Turtle()
    header.speed(0)
    header.color("orange")
    header.penup()
    header.hideturtle()
    header.goto(0,100)
    header.write("Loading Terminal...", align="center", font=("Courier New", 40, "bold"))

    subheader = turtle.Turtle()
    subheader.speed(0)
    subheader.color("orange")
    subheader.penup()
    subheader.hideturtle()
    subheader.goto(0,40)
    subheader.write("Press space to coninute.", align="center", font=("Courier New", 18, "normal"))

def values_into_list(stock_index, beg_yr, end_yr):
    data_list = []
    with open(stock_index) as index_opened:
        index_read = index_opened.readlines()
    for line in index_read[1:]: 
        if int(line[:4]) >= beg_yr and int(line[:4]) <= end_yr: #If the date is within the year range
            data_list.append(line[11:len(line) - 1]) #Add the value corresponding with the date to the list
    for i in range(len(data_list)): 
        data_list[i] = float(data_list[i]) #Convert every number in the list form a string to a float
    
    return data_list

def goodbye_screen():
    plt.close()
    screen.clear()
    screen.bgcolor("grey10")
    screen.title("")

    header = turtle.Turtle()
    header.speed(0)
    header.color("orange")
    header.penup()
    header.hideturtle()
    header.goto(0,100)
    header.write("Thank you for using the", align="center", font=("Courier New", 40, "bold"))

    header1 = turtle.Turtle()
    header1.speed(0)
    header1.color("orange")
    header1.penup()
    header1.hideturtle()
    header1.goto(0,40)
    header1.write("Tchakanakis Terminal!", align="center", font=("Courier New", 40, "bold"))

    subheader = turtle.Turtle()
    subheader.speed(0)
    subheader.color("orange")
    subheader.penup()
    subheader.hideturtle()
    subheader.goto(0,-20)
    subheader.write("Run the program again to reset the terminal.", align="center", font=("Courier New", 18, "normal"))

def statistical_analysis(stock_index, beg_yr, end_yr):

    data_list = values_into_list(stock_index, beg_yr, end_yr) # Gets data list from the stock index and beginging and ending years

    maximum = max(data_list)
    minimum = min(data_list)
    mean = sum(data_list) / len(data_list)
    median = statistics.median(data_list)
    mode = statistics.mode(data_list)
    variance = statistics.variance(data_list)
    standard_deviation = statistics.stdev(data_list)
    net_change = data_list[len(data_list) - 1] - data_list[0]

    return maximum, minimum, mean, median, mode, variance, standard_deviation, net_change

def statistical_analysis_screen(stock_index, beg_yr, end_yr):

    maximum, minimum, mean, median, mode, variance, standard_deviation, net_change = statistical_analysis(stock_index, beg_yr, end_yr)

    screen = turtle.Screen()
    screen.bgcolor("grey10")
    screen.title("Statistical Analysis")

    header = turtle.Turtle()
    header.speed(0)
    header.color("orange")
    header.penup()
    header.hideturtle()
    header.goto(0,200)
    header.write("Statistical Analysis for " + stock_index.title() + " for the year range " + str(beg_yr) + " to " + str(end_yr), align="center", font=("Courier New", 25, "bold"))

    maximum_turtle = turtle.Turtle()
    maximum_turtle.speed(0)
    maximum_turtle.color("orange")
    maximum_turtle.penup()
    maximum_turtle.hideturtle()
    maximum_turtle.goto(-600,0)
    maximum_turtle.write("Maximum: " + "{:.2f}".format(maximum), align="left", font=("Courier New", 28, "bold"))

    minimum_turtle = turtle.Turtle()
    minimum_turtle.speed(0)
    minimum_turtle.color("orange")
    minimum_turtle.penup()
    minimum_turtle.hideturtle()
    minimum_turtle.goto(-600,-50)
    minimum_turtle.write("Minimum: " + "{:.2f}".format(minimum), align="left", font=("Courier New", 28, "bold"))

    mean_turtle = turtle.Turtle()
    mean_turtle.speed(0)
    mean_turtle.color("orange")
    mean_turtle.penup()
    mean_turtle.hideturtle()
    mean_turtle.goto(-600,-100)
    mean_turtle.write("Mean: " + "{:.2f}".format(mean), align="left", font=("Courier New", 28, "bold"))

    median_turtle = turtle.Turtle()
    median_turtle.speed(0)
    median_turtle.color("orange")
    median_turtle.penup()
    median_turtle.hideturtle()
    median_turtle.goto(-600,-150)
    median_turtle.write("Medain: " + "{:.2f}".format(median), align="left", font=("Courier New", 28, "bold"))

    mode_turtle = turtle.Turtle()
    mode_turtle.speed(0)
    mode_turtle.color("orange")
    mode_turtle.penup()
    mode_turtle.hideturtle()
    mode_turtle.goto(0, 0)
    mode_turtle.write("Mode: " + "{:.2f}".format(mode), align="left", font=("Courier New", 28, "bold"))

    variance_turtle = turtle.Turtle()
    variance_turtle.speed(0)
    variance_turtle.color("orange")
    variance_turtle.penup()
    variance_turtle.hideturtle()
    variance_turtle.goto(0, -50)
    variance_turtle.write("Variance: " + "{:.2f}".format(variance), align="left", font=("Courier New", 28, "bold"))

    standard_deviation_turtle = turtle.Turtle()
    standard_deviation_turtle.speed(0)
    standard_deviation_turtle.color("orange")
    standard_deviation_turtle.penup()
    standard_deviation_turtle.hideturtle()
    standard_deviation_turtle.goto(0, -100)
    standard_deviation_turtle.write("Standard Deviation: " + "{:.2f}".format(standard_deviation), align="left", font=("Courier New", 28, "bold"))

    net_change_turtle = turtle.Turtle()
    net_change_turtle.speed(0)
    if net_change > 0:
        net_change_turtle.color("lime")
    else:
        net_change_turtle.color("red")
    net_change_turtle.penup()
    net_change_turtle.hideturtle()
    net_change_turtle.goto(0, -150)
    net_change_turtle.write("Net Change: " + "{:.2f}".format(net_change), align="left", font=("Courier New", 28, "bold"))

    exit_turtle = turtle.Turtle()
    exit_turtle.speed(0)
    exit_turtle.color("orange")
    exit_turtle.penup()
    exit_turtle.hideturtle()
    exit_turtle.goto(0, -250)
    exit_turtle.write("Press 'x' when you are ready to exit the program.", align="center", font=("Courier New", 18, "normal"))

def select_beg_year_screen(stock_index):
    screen = turtle.Screen()
    screen.bgcolor("grey10")
    screen.title("")

    text1 = turtle.Turtle()
    text1.speed(0)
    text1.color("orange")
    text1.penup()
    text1.hideturtle()
    text1.goto(0,250)
    text1.write("This terminal works by first selecting the year range that", align="center", font=("Courier New", 18, "bold"))

    text2 = turtle.Turtle()
    text2.speed(0)
    text2.color("orange")
    text2.penup()
    text2.hideturtle()
    text2.goto(0,220)
    text2.write("you would like to analyize financial data for.", align="center", font=("Courier New", 18, "bold"))

    header = turtle.Turtle()
    header.speed(0)
    header.color("orange")
    header.penup()
    header.hideturtle()
    header.goto(0,100)
    header.write("Enter the starting year that you would like to analyze for " + stock_index.title() + ".", align="center", font=("Courier New", 18, "normal"))


    text3 = turtle.Turtle()
    text3.speed(0)
    text3.color("orange")
    text3.penup()
    text3.hideturtle()
    text3.goto(0,70)
    text3.write("Ex: '1989'", align="center", font=("Courier New", 14, "normal"))

    turtle.addshape(stock_index + '.gif')

    index_selected = turtle.Turtle()
    index_selected.hideturtle()
    index_selected.penup()
    index_selected.shape(stock_index + ".gif")
    index_selected.goto(0,-150)
    index_selected.showturtle()

def select_end_year_screen(stock_index, beg_yr):
    screen = turtle.Screen()
    screen.bgcolor("grey10")
    screen.title("")

    text1 = turtle.Turtle()
    text1.speed(0)
    text1.color("orange")
    text1.penup()
    text1.hideturtle()
    text1.goto(0,250)
    text1.write("Now that you have selected " + str(beg_yr) + " as your begining year,", align="center", font=("Courier New", 18, "bold"))

    text2 = turtle.Turtle()
    text2.speed(0)
    text2.color("orange")
    text2.penup()
    text2.hideturtle()
    text2.goto(0,220)
    text2.write("enter the ending year that you would like to analyze for.", align="center", font=("Courier New", 18, "bold"))

    turtle.addshape(stock_index + '.gif')

    index_selected = turtle.Turtle()
    index_selected.hideturtle()
    index_selected.penup()
    index_selected.shape(stock_index + ".gif")
    index_selected.goto(0,-150)
    index_selected.showturtle()

def select_stat_or_plot_screen(stock_index):
    screen = turtle.Screen()
    screen.bgcolor("grey10")
    screen.title("")

    header = turtle.Turtle()
    header.speed(0)
    header.color("orange")
    header.penup()
    header.hideturtle()
    header.goto(0,250)
    header.write("This teminal provides two different functions for analyzing stock value data.", align="center", font=("Courier New", 18, "bold"))

    text1 = turtle.Turtle()
    text1.speed(0)
    text1.color("orange")
    text1.penup()
    text1.hideturtle()
    text1.goto(-650,220)
    text1.write("- The 'graph' function graphs the stock values in the given range, and provides a visualization of the data", align="left", font=("Courier New", 14, "normal"))

    text2 = turtle.Turtle()
    text2.speed(0)
    text2.color("orange")
    text2.penup()
    text2.hideturtle()
    text2.goto(-650,200)
    text2.write("- The 'graph' function also allows you to choose 1-2 additional indexes, providing a way to directly compare", align="left", font=("Courier New", 14, "normal"))

    text3 = turtle.Turtle()
    text3.speed(0)
    text3.color("orange")
    text3.penup()
    text3.hideturtle()
    text3.goto(-650,180)
    text3.write("  the values of different indexes", align="left", font=("Courier New", 14, "normal"))

    text4 = turtle.Turtle()
    text4.speed(0)
    text4.color("orange")
    text4.penup()
    text4.hideturtle()
    text4.goto(-650,150)
    text4.write("- The 'stat' function provides a statistical analysis for the chosen stock index, including data points such", align="left", font=("Courier New", 14, "normal"))

    text5 = turtle.Turtle()
    text5.speed(0)
    text5.color("orange")
    text5.penup()
    text5.hideturtle()
    text5.goto(-650,130)
    text5.write("  as mean, median, and net change", align="left", font=("Courier New", 14, "normal"))


    turtle.addshape(stock_index + '.gif')

    index_selected = turtle.Turtle()
    index_selected.hideturtle()
    index_selected.penup()
    index_selected.shape(stock_index + ".gif")
    index_selected.goto(0,-150)
    index_selected.showturtle()

def one_graph(stock_index, beg_yr, end_yr):
    yr_range = end_yr - beg_yr # The number of years
    
    weeks = []
    num = 1
    for i in range(yr_range): # Makes a list of numbers for every year
        weeks.append(num)
        num += 1

    for i in range(len(weeks)): # Multiplies the numbers by 52 to represent weeks
        weeks[i] = weeks[i] * 52

    years = []
    num = beg_yr
    for i in range(yr_range): # List for year range
        years.append(str(num + 1))
        num += 1
    
    plt.figure(figsize=(15, 20))
    plt.title(stock_index.title() + " from " + str(beg_yr) + " to " + str(end_yr))
    plt.xlabel("Years")
    plt.ylabel("Value (USD)")
    if yr_range <= 20:
        plt.xticks(weeks, years)
    elif yr_range <= 25:
        plt.xticks(weeks, years, rotation=20)
    elif yr_range <= 30:
        plt.xticks(weeks, years, rotation=30)
    else:
        plt.xticks(weeks, years, rotation=40)
    plt.plot(values_into_list(stock_index, beg_yr, end_yr), label=stock_index)
    plt.legend()
    plt.figtext(0.5, 0.01, "Click the X on the top right of the screen then press the 'x' key to exit the terminal.", horizontalalignment='center', fontsize=12, color="red")
    plt.show()

def two_graphs(stock_index1, stock_index2, beg_yr, end_yr):
    yr_range = end_yr - beg_yr
    
    weeks = []
    num = 1
    for i in range(yr_range):
        weeks.append(num)
        num += 1

    for i in range(len(weeks)):
        weeks[i] = weeks[i] * 52
  
    years = []
    num = beg_yr
    for i in range(yr_range):
        years.append(str(num + 1))
        num += 1

    plt.figure(figsize=(15, 20))
    plt.title(stock_index1.title() + " and " + stock_index2.title() + " from " + str(beg_yr) + " to " + str(end_yr))
    plt.xlabel("Years")
    plt.ylabel("Value (USD)")
    if yr_range <= 20:
        plt.xticks(weeks, years)
    elif yr_range <= 25:
        plt.xticks(weeks, years, rotation=20)
    elif yr_range <= 30:
        plt.xticks(weeks, years, rotation=30)
    else:
        plt.xticks(weeks, years, rotation=40)
    plt.plot(values_into_list(stock_index1, beg_yr, end_yr), label=stock_index1)
    plt.plot(values_into_list(stock_index2, beg_yr, end_yr), label=stock_index2)
    plt.legend()
    plt.figtext(0.5, 0.01, "Click the X on the top right of the screen then press the 'x' key to exit the terminal.", horizontalalignment='center', fontsize=12, color="red")
    plt.show()
    
def three_graphs(stock_index1, stock_index2, stock_index3, beg_yr, end_yr):
    yr_range = end_yr - beg_yr
    
    weeks = []
    num = 1
    for i in range(yr_range):
        weeks.append(num)
        num += 1

    for i in range(len(weeks)):
        weeks[i] = weeks[i] * 52
  
    years = []
    num = beg_yr
    for i in range(yr_range):
        years.append(str(num + 1))
        num += 1

    plt.figure(figsize=(15, 20))
    plt.title(stock_index1.title() + ", " + stock_index2.title() + ", and " + stock_index3.title() + " from " + str(beg_yr) + " to " + str(end_yr))
    plt.xlabel("Years")
    plt.ylabel("Value (USD)")
    if yr_range <= 20:
        plt.xticks(weeks, years)
    elif yr_range <= 25:
        plt.xticks(weeks, years, rotation=20)
    elif yr_range <= 30:
        plt.xticks(weeks, years, rotation=30)
    else:
        plt.xticks(weeks, years, rotation=40)
    plt.plot(values_into_list(stock_index1, beg_yr, end_yr), label=stock_index1)
    plt.plot(values_into_list(stock_index2, beg_yr, end_yr), label=stock_index2)
    plt.plot(values_into_list(stock_index3, beg_yr, end_yr), label=stock_index3)
    plt.legend()
    plt.figtext(0.5, 0.01, "Click the X on the top right of the screen then press the 'x' key to exit the terminal.", horizontalalignment='center', fontsize=12, color="red")
    plt.show()

def additional_graphs_screen(stock_index):
    screen = turtle.Screen()
    screen.bgcolor("grey10")
    screen.title("")

    header = turtle.Turtle()
    header.speed(0)
    header.color("orange")
    header.penup()
    header.hideturtle()
    header.goto(0,250)
    header.write("You currently have " + stock_index.title() + " selected, you have the option", align="center", font=("Courier New", 18, "bold"))

    header1 = turtle.Turtle()
    header1.speed(0)
    header1.color("orange")
    header1.penup()
    header1.hideturtle()
    header1.goto(0,220)
    header1.write("to overlay up to two more indexes to the graph.", align="center", font=("Courier New", 18, "bold"))

    text1 = turtle.Turtle()
    text1.speed(0)
    text1.color("orange")
    text1.penup()
    text1.hideturtle()
    text1.goto(-650,180)
    text1.write("- Enter '0' into the terminal to graph " + stock_index.title() + " by itself", align="left", font=("Courier New", 14, "normal"))

    text2 = turtle.Turtle()
    text2.speed(0)
    text2.color("orange")
    text2.penup()
    text2.hideturtle()
    text2.goto(-650, 160)
    text2.write("- Enter '1' into the terminal to select an additional index to add to the graph", align="left", font=("Courier New", 14, "normal"))

    text3 = turtle.Turtle()
    text3.speed(0)
    text3.color("orange")
    text3.penup()
    text3.hideturtle()
    text3.goto(-650, 140)
    text3.write("- Enter '2' into the terminal to see all three indexes on the graph", align="left", font=("Courier New", 14, "normal"))

    subheader = turtle.Turtle()
    subheader.speed(0)
    subheader.color("orange")
    subheader.penup()
    subheader.hideturtle()
    subheader.goto(0, 80)
    subheader.write("Please enter a number 0-2 in the terminal.", align="center", font=("Courier New", 14, "normal"))

    turtle.addshape(stock_index + '.gif')

    index_selected = turtle.Turtle()
    index_selected.hideturtle()
    index_selected.penup()
    index_selected.shape(stock_index + ".gif")
    index_selected.goto(0,-150)
    index_selected.showturtle()

def select_additional_index_screen(stock_index):
    screen = turtle.Screen()
    screen.bgcolor("grey10")
    screen.title("")

    header = turtle.Turtle()
    header.speed(0)
    header.color("orange")
    header.penup()
    header.hideturtle()
    header.goto(0,150)
    header.write("You are currently using " + stock_index.title() + ".", align="center", font=("Courier New", 18, "bold"))
    header.goto(0,100)
    header.write("Enter the additional index that you would like to use into the teminal.", align="center", font=("Courier New", 18, "normal"))

    turtle.addshape(stock_index + '.gif')

    index_selected = turtle.Turtle()
    index_selected.hideturtle()
    index_selected.penup()
    index_selected.shape(stock_index + ".gif")
    index_selected.goto(0,-150)
    index_selected.showturtle()

def program():

    screen = turtle.Screen()

    screen.clear()

    all_index_list = ["dowjones", "nasdaq", "sp500"]
    all_years = ['1975', '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023']
    choices = ['0', '1', '2']
    
    welcome_screen()

    stock_index = turtle.textinput('', "Enter 'DowJones', 'Nasdaq', or 'SP500' into the terminal: ")
    stock_index = stock_index.lower().strip()
    while stock_index not in all_index_list:
        stock_index = turtle.textinput('', "INVALID ENTRY: Please enter 'DowJones', 'Nasdaq', or 'SP500' into the terminal: ")
        stock_index = stock_index.lower().strip()

    screen.clear()
    select_beg_year_screen(stock_index)
    beg_yr = turtle.textinput('Begining Year', 'Enter begining year (1975-2023): ')
    while beg_yr not in all_years:
        beg_yr = turtle.textinput('Begining Year', 'INVALID ENTRY: Please enter a valid year (1975-2023): ')
    beg_yr = int(beg_yr)

    del all_years[0:all_years.index(str(beg_yr))] # Deletes all the years before the begining year from all_years

    screen.clear()
    select_end_year_screen(stock_index, beg_yr)
    end_yr = turtle.textinput('Ending Year', 'Enter ending year' + ' (' + str(beg_yr) + '-2023): ')
    while end_yr not in all_years:
        end_yr = turtle.textinput('Ending Year', 'INVALID ENTRY: Please enter a valid year' + ' (' + str(beg_yr) + '-2023): ')
    end_yr = int(end_yr)

    screen.clear()
    select_stat_or_plot_screen(stock_index)
    graph_or_stat = turtle.textinput('Select Graph or Stat', "Enter 'Graph' or 'Stat' into the terminal: ")
    graph_or_stat = graph_or_stat.lower().strip()
    while graph_or_stat != "graph" and graph_or_stat != "stat":
        graph_or_stat = turtle.textinput('', "INVLAID ENTRY: Please enter 'Graph' or 'Stat' into the terminal: ")
        graph_or_stat = graph_or_stat.lower().strip()

    if graph_or_stat == "graph":
        screen.clear()
        additional_graphs_screen(stock_index)
        num_of_additional_graphs = turtle.textinput('Additional Indexes', "You are currently using " + stock_index.title() + ", how many more indexes would you like to use?")
        while num_of_additional_graphs not in choices:
            num_of_additional_graphs = turtle.textinput('Additional Indexes', "INVALID ENTRY: You are currently using " + stock_index.title() + ", how many more indexes would you like to use?")
        num_of_additional_graphs = int(num_of_additional_graphs)
        if num_of_additional_graphs == 0:
            screen.clear()
            one_graph(stock_index, beg_yr, end_yr)
        elif num_of_additional_graphs == 1:
            all_index_list.remove(stock_index)
            screen.clear()
            select_additional_index_screen(stock_index)
            additional_index = turtle.textinput('', "Enter '" + all_index_list[0].title() + "' or '" + all_index_list[1].title() + "' into the terminal: ")
            while additional_index not in all_index_list:
                additional_index = turtle.textinput('', "INVALID ENTRY: Enter " + all_index_list[0].title() + " or " + all_index_list[1].title() + " into the terminal: ")
            screen.clear()
            two_graphs(stock_index, additional_index, beg_yr, end_yr)
        else:
            screen.clear()
            three_graphs("dowjones", "sp500", "nasdaq", beg_yr, end_yr)

    else:
        screen.clear()
        statistical_analysis_screen(stock_index, beg_yr, end_yr)

    
    screen.listen()
    screen.onkey(goodbye_screen, "x")

if __name__ == "__main__":

    screen = turtle.Screen()
    
    space_to_begin_screen()
    screen.listen()

    screen.onkey(program, "space")

    turtle.mainloop()
