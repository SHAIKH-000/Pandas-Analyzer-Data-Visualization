import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class SalesDataAnalyzer:
    def __init__(self, file_path=None):
        self.data = None
        self.last_figure = None
        if file_path is not None:
            self.load_data(file_path)

    def __del__(self):
        print("Object deleted, cleanup done.")

    def load_data(self, file_path):
        try:
            self.data = pd.read_csv(file_path)
            print("Dataset loaded successfully!")
        except FileNotFoundError:
            print("File not found!")
        except Exception as e:
            print("Error while loading file:", e)

    def explore_data(self):
        if self.data is None:
            print("Please load the dataset first!")
            return

        print("== Explore Data ==")
        print("1. Display the first 5 rows")
        print("2. Display the last 5 rows")
        print("3. Display column names")
        print("4. Display data types")
        print("5. Display basic info")
        choice = input("Enter your choice: ")

        if choice == "1":
            print(self.data.head())
        elif choice == "2":
            print(self.data.tail())
        elif choice == "3":
            print(self.data.columns)
        elif choice == "4":
            print(self.data.dtypes)
        elif choice == "5":
            self.data.info()
        else:
            print("Invalid choice!")

    def clean_data(self):
        if self.data is None:
            print("Please load the dataset first!")
            return

        print("== Handle Missing Data ==")
        print("1. Display rows with missing values")
        print("2. Fill missing values with mean")
        print("3. Drop rows with missing values")
        print("4. Replace missing values with a specific value")
        choice = input("Enter your choice: ")

        if choice == "1":
            missing_rows = self.data[self.data.isnull().any(axis=1)]
            if missing_rows.empty:
                print("No missing values found in the dataset!")
            else:
                print(missing_rows)

        elif choice == "2":
            self.data.fillna(self.data.mean(numeric_only=True), inplace=True)
            print("Missing values filled with mean.")

        elif choice == "3":
            self.data.dropna(inplace=True)
            print("Rows with missing values dropped.")

        elif choice == "4":
            value = input("Enter the value to replace missing values with: ")
            self.data.fillna(value, inplace=True)
            print("Missing values replaced with the specified value.")

        else:
            print("Invalid choice!")

    def numpy_operations(self):
        if self.data is None:
            print("Please load the dataset first!")
            return

        sales_array = self.data["Sales"].to_numpy()
        print("Sales Array:", sales_array)

        print("== NumPy Array Operations ==")
        print("1. Indexing")
        print("2. Slicing")
        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                index = int(input("Enter the index: "))
                print("Element:", sales_array[index])
            except IndexError:
                print("Index out of range!")

        elif choice == "2":
            start = int(input("Enter start index: "))
            end = int(input("Enter end index: "))
            print("Sliced Array:", sales_array[start:end])
        else:
            print("Invalid choice!")

    def mathematical_operations(self):
        if self.data is None:
            print("Please load the dataset first!")
            return

        print("== Mathematical Operations ==")
        print("1. Add a value to Sales")
        print("2. Multiply Sales by a value")
        print("3. Sales minus Profit")
        print("4. Profit margin (Profit / Sales)")
        choice = input("Enter your choice: ")

        if choice == "1":
            value = float(input("Enter the value to add: "))
            print(self.data["Sales"] + value)

        elif choice == "2":
            value = float(input("Enter the value to multiply by: "))
            print(self.data["Sales"] * value)

        elif choice == "3":
            print(self.data["Sales"] - self.data["Profit"])

        elif choice == "4":
            print(self.data["Profit"] / self.data["Sales"])

        else:
            print("Invalid choice!")

    def combine_data(self):
        if self.data is None:
            print("Please load the dataset first!")
            return

        path = input("Enter the path of the second CSV file: ")
        try:
            other = pd.read_csv(path)
            self.data = pd.concat([self.data, other], ignore_index=True)
            print("DataFrames combined successfully!")
            print("Total rows now:", len(self.data))
        except FileNotFoundError:
            print("File not found!")

    def split_data(self):
        if self.data is None:
            print("Please load the dataset first!")
            return

        print("== Split Data ==")
        print("1. Split by Region")
        print("2. Split by Product")
        choice = input("Enter your choice: ")

        if choice == "1":
            region = input("Enter region name (North/East/West Coast/South/Central): ")
            result = self.data[self.data["Region"] == region]
            if result.empty:
                print("No data found for this region!")
            else:
                print(result)

        elif choice == "2":
            product = input("Enter product name (e.g. Product A): ")
            result = self.data[self.data["Product"] == product]
            if result.empty:
                print("No data found for this product!")
            else:
                print(result)

        else:
            print("Invalid choice!")

    def search_sort_filter(self):
        if self.data is None:
            print("Please load the dataset first!")
            return

        print("== Search, Sort, Filter ==")
        print("1. Search by Product")
        print("2. Sort by Sales (Ascending)")
        print("3. Sort by Sales (Descending)")
        print("4. Filter Sales greater than a value")
        choice = input("Enter your choice: ")

        if choice == "1":
            product = input("Enter product name: ")
            result = self.data[self.data["Product"] == product]
            if result.empty:
                print("No records found!")
            else:
                print(result)

        elif choice == "2":
            print(self.data.sort_values(by="Sales", ascending=True))

        elif choice == "3":
            print(self.data.sort_values(by="Sales", ascending=False))

        elif choice == "4":
            value = float(input("Show rows where Sales is greater than: "))
            result = self.data[self.data["Sales"] > value]
            if result.empty:
                print("No records found!")
            else:
                print(result)

        else:
            print("Invalid choice!")

    def aggregate_functions(self):
        if self.data is None:
            print("Please load the dataset first!")
            return

        print("== Aggregate Functions ==")
        print("1. Sum of Sales")
        print("2. Mean of Sales")
        print("3. Count of records")
        choice = input("Enter your choice: ")

        if choice == "1":
            print("Total Sales:", self.data["Sales"].sum())

        elif choice == "2":
            print("Average Sales:", self.data["Sales"].mean())

        elif choice == "3":
            print("Total records:", self.data["Sales"].count())

        else:
            print("Invalid choice!")

    def statistical_analysis(self):
        if self.data is None:
            print("Please load the dataset first!")
            return

        print("== Descriptive Statistics ==")
        print("1. Describe")
        print("2. Standard Deviation")
        print("3. Variance")
        print("4. Quantile (percentile)")
        choice = input("Enter your choice: ")

        if choice == "1":
            print(self.data.describe())

        elif choice == "2":
            print("Standard Deviation of Sales:", self.data["Sales"].std())

        elif choice == "3":
            print("Variance of Sales:", self.data["Sales"].var())

        elif choice == "4":
            q = float(input("Enter quantile between 0 and 1 (e.g. 0.5): "))
            print("Quantile:", self.data["Sales"].quantile(q))

        else:
            print("Invalid choice!")

    def create_pivot_table(self):
        if self.data is None:
            print("Please load the dataset first!")
            return

        print("== Advanced Operations ==")
        print("1. Pivot Table (Region-wise Sales)")
        print("2. Groupby (Product-wise total Sales)")
        print("3. Transform (add Region Total column)")
        print("4. Re-index (set SalesID as index)")
        choice = input("Enter your choice: ")

        if choice == "1":
            pivot = pd.pivot_table(self.data, values="Sales", index="Region", aggfunc="sum")
            print(pivot)

        elif choice == "2":
            print(self.data.groupby("Product")["Sales"].sum())

        elif choice == "3":
            self.data["Region_Total"] = self.data.groupby("Region")["Sales"].transform("sum")
            print(self.data[["Region", "Sales", "Region_Total"]])

        elif choice == "4":
            print(self.data.set_index("SalesID"))

        else:
            print("Invalid choice!")

    def convert_types(self):
        if self.data is None:
            print("Please load the dataset first!")
            return

        print("== Data Type Conversion ==")
        print("Before:")
        print(self.data.dtypes)

        self.data["Date"] = pd.to_datetime(self.data["Date"])
        self.data["Sales"] = self.data["Sales"].astype(float)

        print("After:")
        print(self.data.dtypes)

    def visualize_data(self):
        if self.data is None:
            print("Please load the dataset first!")
            return

        print("== Data Visualization ==")
        print("1. Bar Plot")
        print("2. Line Plot")
        print("3. Scatter Plot")
        print("4. Pie Chart")
        print("5. Histogram")
        print("6. Stack Plot")
        print("7. Heatmap (Seaborn)")
        print("8. Box Plot (Seaborn)")
        print("9. Subplots (Bar + Line)")
        choice = input("Enter your choice: ")

        plt.figure()

        if choice == "1":
            plt.bar(self.data["Product"], self.data["Sales"])
            plt.title("Sales by Product")
            plt.xlabel("Product")
            plt.ylabel("Sales")

        elif choice == "2":
            plt.plot(self.data["SalesID"], self.data["Sales"], label="Sales")
            plt.title("Sales Trend")
            plt.xlabel("SalesID")
            plt.ylabel("Sales")
            plt.legend()

        elif choice == "3":
            x_col = input("Enter x-axis column name: ")
            y_col = input("Enter y-axis column name: ")
            plt.scatter(self.data[x_col], self.data[y_col])
            plt.title(f"{y_col} vs {x_col}")
            plt.xlabel(x_col)
            plt.ylabel(y_col)

        elif choice == "4":
            region_sales = self.data.groupby("Region")["Sales"].sum()
            plt.pie(region_sales, labels=region_sales.index, autopct="%1.1f%%")
            plt.title("Sales Share by Region")

        elif choice == "5":
            plt.hist(self.data["Sales"], bins=5)
            plt.title("Sales Distribution")
            plt.xlabel("Sales")
            plt.ylabel("Frequency")

        elif choice == "6":
            plt.stackplot(self.data["SalesID"], self.data["Sales"], self.data["Profit"],
                          labels=["Sales", "Profit"])
            plt.title("Sales and Profit")
            plt.xlabel("SalesID")
            plt.ylabel("Amount")
            plt.legend(loc="upper left")

        elif choice == "7":
            corr = self.data[["Sales", "Profit", "Year"]].corr()
            sns.heatmap(corr, annot=True, cmap="coolwarm")
            plt.title("Correlation Heatmap")

        elif choice == "8":
            sns.boxplot(x="Region", y="Sales", data=self.data)
            plt.title("Sales Distribution by Region")

        elif choice == "9":
            plt.close()
            fig, axes = plt.subplots(1, 2, figsize=(12, 5))
            axes[0].bar(self.data["Product"], self.data["Sales"])
            axes[0].set_title("Sales by Product")
            axes[1].plot(self.data["SalesID"], self.data["Profit"], label="Profit")
            axes[1].set_title("Profit Trend")
            axes[1].set_xlabel("SalesID")
            axes[1].legend()

        else:
            print("Invalid choice!")
            plt.close()
            return

        self.last_figure = plt.gcf()
        plt.show()

    def save_visualization(self):
        if self.last_figure is None:
            print("No plot to save! Generate a plot first (option 6).")
            return

        file_name = input("Enter file name to save the plot (e.g., scatter_plot.png): ")
        try:
            self.last_figure.savefig(file_name)
            print(f"Visualization saved as {file_name} successfully!")
        except Exception as e:
            print("Error while saving:", e)


analyzer = SalesDataAnalyzer()

while True:
    print("========== Data Analysis & Visualization Program ==========")
    print("Please select an option:")
    print("1. Load Dataset")
    print("2. Explore Data")
    print("3. Perform DataFrame Operations")
    print("4. Handle Missing Data")
    print("5. Generate Descriptive Statistics")
    print("6. Data Visualization")
    print("7. Save Visualization")
    print("8. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        path = input("Enter the path of the dataset (CSV file): ")
        analyzer.load_data(path)

    elif choice == "2":
        analyzer.explore_data()

    elif choice == "3":
        print("== Perform DataFrame Operations ==")
        print("1. NumPy Array Operations")
        print("2. Mathematical Operations")
        print("3. Split Data")
        print("4. Combine Data")
        print("5. Search, Sort, Filter")
        print("6. Aggregate Functions")
        print("7. Advanced Operations (Pivot, Groupby)")
        print("8. Convert Data Types")
        sub = input("Enter your choice: ")

        if sub == "1":
            analyzer.numpy_operations()

        elif sub == "2":
            analyzer.mathematical_operations()

        elif sub == "3":
            analyzer.split_data()

        elif sub == "4":
            analyzer.combine_data()

        elif sub == "5":
            analyzer.search_sort_filter()

        elif sub == "6":
            analyzer.aggregate_functions()

        elif sub == "7":
            analyzer.create_pivot_table()

        elif sub == "8":
            analyzer.convert_types()

        else:
            print("Invalid choice!")

    elif choice == "4":
        analyzer.clean_data()

    elif choice == "5":
        analyzer.statistical_analysis()

    elif choice == "6":
        analyzer.visualize_data()

    elif choice == "7":
        analyzer.save_visualization()

    elif choice == "8":
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice!")