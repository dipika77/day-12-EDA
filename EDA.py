#Exploratory Data Analysis
#instructions
'''Use a pandas function to print the first five rows of the unemployment DataFrame.
Use a pandas function to print a summary of column non-missing values and data types from the unemployment DataFrame.
Print the summary statistics (count, mean, standard deviation, min, max, and quartile values) of each numerical column in unemployment.'''

# Print the first five rows of unemployment
print(unemployment.head())

# Print a summary of non-missing values and data types in the unemployment DataFrame
print(unemployment.info())

# Print summary statistics for numerical columns in unemployment
print(unemployment.describe())



#instructions
'''Use a method to count the values associated with each continent in the unemployment DataFrame.'''

# Count the values associated with each continent in unemployment
print(unemployment.value_counts("continent"))


#instructions
'''Import the required visualization libraries.
Create a histogram of the distribution of 2021 unemployment percentages across all countries in unemployment; show a full percentage point in each bin.'''

# Import the required visualization libraries
import seaborn as sns
import matplotlib.pyplot as plt

# Create a histogram of 2021 unemployment; show a full percent in each bin
sns.histplot(data = unemployment, x = "2021", binwidth = 1)
plt.show()



#Data Validation
#instructions
'''Update the data type of the 2019 column of unemployment to float.
Print the dtypes of the unemployment DataFrame again to check that the data type has been updated!'''

# Update the data type of the 2019 column to a float
unemployment["2019"] = unemployment["2019"].astype("float")
# Print the dtypes to check your work
print(unemployment.dtypes)


#instructions
'''Define a Series of Booleans describing whether or not each continent is outside of Oceania; call this Series not_oceania.'''

# Define a Series describing whether each continent is outside of Oceania
not_oceania = ~unemployment["continent"].isin(["Oceania"])

# Print unemployment without records related to countries in Oceania
print(unemployment[not_oceania])


#instructions
'''Print the minimum and maximum unemployment rates, in that order, during 2021.
Create a boxplot of 2021 unemployment rates (on the x-axis), broken down by continent (on the y-axis).'''

# Print the minimum and maximum unemployment rates during 2021
print(unemployment["2021"].min(), unemployment["2021"].max())

# Create a boxplot of 2021 unemployment rates, broken down by continent
sns.boxplot(data = unemployment, x = "2021", y = "continent")
plt.show()



#Data summarization
#instructions
'''Print the mean and standard deviation of the unemployment rates for each year (in that order).
Print the mean and standard deviation (in that order) of the unemployment rates for each year, grouped by continent.'''
# Print the mean and standard deviation of rates by year
print(unemployment.agg(["mean", "std"]))

# Print yearly mean and standard deviation grouped by continent
print(unemployment.groupby("continent").agg(["mean", "std"]))


#instructions
'''Create a column called mean_rate_2021 which shows the mean 2021 unemployment rate for each continent.
Create a column called std_rate_2021 which shows the standard deviation of the 2021 unemployment rate for each continent.'''

continent_summary = unemployment.groupby("continent").agg(
    # Create the mean_rate_2021 column
    mean_rate_2021 = ("2021", "mean"),
    # Create the std_rate_2021 column
    std_rate_2021 = ("2021", "std")
)
print(continent_summary)


#instructions
'''Create a bar plot showing continents on the x-axis and their respective average 2021 unemployment rates on the y-axis.'''

# Create a bar plot of continents and their average unemployment
sns.barplot(data = unemployment, x = "continent", y = "2021")
plt.show()



#Addressing missing values
#instructions
'''Print the number of missing values in each column of the DataFrame.
Calculate how many observations five percent of the planes DataFrame is equal to.
Create cols_to_drop by applying boolean indexing to columns of the DataFrame with missing values less than or equal to the threshold.
Use this filter to remove missing values and save the updated DataFrame.'''

# Count the number of missing values in each column
print(planes.isna().sum())

# Find the five percent threshold
threshold = len(planes) * 0.05

# Create a filter
cols_to_drop = planes.columns[planes.isna().sum() <= threshold]

# Drop missing values for columns below the threshold
planes.dropna(subset=cols_to_drop, inplace=True)

print(planes.isna().sum())



#instructions
'''Print the values and frequencies of "Additional_Info".
Create a boxplot of "Price" versus "Airline".'''

# Check the values of the Additional_Info column
print(planes["Additional_Info"].value_counts())

# Create a box plot of Price by Airline
sns.boxplot(data=planes, y= "Price", x= "Airline")

plt.show()


#instructions
'''Group planes by airline and calculate the median price.
Convert the grouped median prices to a dictionary.
Conditionally impute missing values for "Price" by mapping values in the "Airline" column based on prices_dict.
Check for remaining missing values.'''

# Calculate median plane ticket prices by Airline
airline_prices = planes.groupby("Airline")["Price"].median()

print(airline_prices)

# Convert to a dictionary
prices_dict = airline_prices.to_dict()

# Map the dictionary to missing values of Price by Airline
planes["Price"] = planes["Price"].fillna(planes["Airline"].map(prices_dict))

# Check for missing values
print(planes.isna().sum())


#Converting and analyzing categorical data

#instructions
'''Filter planes for columns that are of "object" data type.
Loop through the columns in the dataset.
Add the column iterator to the print statement, then call the function to return the number of unique values in the column.'''

# Filter the DataFrame for object columns
non_numeric = planes.select_dtypes('object')

# Loop through columns
for col in non_numeric.columns:
   
 # Print the number of unique values
  print(f"Number of unique values in {col} column: ", non_numeric[col].nunique())
  
  
#instructions
'''Create a list of categories containing "Short-haul", "Medium", and "Long-haul".
Create short_flights, a string to capture values of "0h", "1h", "2h", "3h", or "4h" taking care to avoid values such as "10h".
Create medium_flights to capture any values between five and nine hours.
Create long_flights to capture any values from 10 hours to 16 hours inclusive.'''

# Create a list of categories
flight_categories = ["Short-haul", "Medium", "Long-haul"]

# Create short_flights
short_flights = "^0h|^1h|^2h|^3h|^4h"

# Create medium_flights
medium_flights = "^5h|^6h|^7h|^8h|^9h"

# Create long_flights
long_flights = "10h|11h|12h|13h|14h|15h|16h"


#instructions
'''Create conditions, a list containing subsets of planes["Duration"] based on short_flights, medium_flights, and long_flights.
Create the "Duration_Category" column by calling a function that accepts your conditions list and flight_categories, setting values not found to "Extreme duration".
Create a plot showing the count of each category.'''

# Create conditions for values in flight_categories to be created


plt.show()
conditions = [
    (planes["Duration"].str.contains(short_flights)),
    (planes["Duration"].str.contains(medium_flights)),
    (planes["Duration"].str.contains(long_flights))
]


# Apply the conditions list to the flight_categories
planes["Duration_Category"] = np.select(conditions, 
                                        flight_categories,
                                        default="Extreme duration")

# Plot the counts of each category
sns.countplot(data=planes, x="Duration_Category")




#working with numeric data
#instructions
'''Print the first five values of the "Duration" column.'''

# Preview the column
print(planes["Duration"].head())

'''Remove 'h' from the column.'''
# Remove the string character
planes["Duration"] = planes["Duration"].str.replace("h", "")


'''Convert the column to float data type.'''
#Convert to float data type.
planes["Duration"] = planes["Duration"].str.replace("h", "").astype(float)


'''Plot a histogram of "Duration" values.'''
# Plot a histogram
plt.hist(planes['Duration'])
plt.show()



#instructions
'''Add a column to planes containing the standard deviation of "Price" based on "Airline".'''
# Price standard deviation by Airline
planes["airline_price_st_dev"] = planes.groupby("Airline")["Price"].transform(lambda x: x.std())

print(planes[["Airline", "airline_price_st_dev"]].value_counts())


'''Calculate the median for "Duration" by "Airline", storing it as a column called "airline_median_duration".'''
# Median Duration by Airline
planes["airline_median_duration"] = planes.groupby("Airline")["Duration"].transform(lambda x: x.median())

print(planes[["Airline","airline_median_duration"]].value_counts())


'''Find the mean "Price" by "Destination", saving it as a column called "price_destination_mean".'''
# Mean Price by Destination
planes["price_destination_mean"] = planes.groupby("Destination")["Price"].transform(lambda x: x.mean())

print(planes[["Destination","price_destination_mean"]].value_counts())



#Heading outliers
#instructions

'''Plot the distribution of "Price" column from planes.'''
# Plot a histogram of flight prices
sns.histplot(data= planes, x= "Price")
plt.show()

'''Display the descriptive statistics for flight duration.'''
# Plot a histogram of flight prices
sns.histplot(data=planes, x="Price")
plt.show()

# Display descriptive statistics for flight duration
print(planes["Duration"].describe())


#instructions
'''Find the 75th and 25th percentiles, saving as price_seventy_fifth and price_twenty_fifth respectively.
Calculate the IQR, storing it as prices_iqr.
Calculate the upper and lower outlier thresholds.
Remove the outliers from planes.'''

# Find the 75th and 25th percentiles
price_seventy_fifth = planes["Price"].quantile(0.75)
price_twenty_fifth = planes["Price"].quantile(0.25)

# Calculate iqr
prices_iqr = price_seventy_fifth - price_twenty_fifth

# Calculate the thresholds
upper = price_seventy_fifth + (1.5 * prices_iqr)
lower = price_twenty_fifth - (1.5 * prices_iqr)

# Subset the data
planes = planes[(planes["Price"] > lower) & (planes["Price"] < upper)]

print(planes["Price"].describe())