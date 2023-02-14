## Data types
The type of data can determine how you interact with the data in the StarLifter system. For example, date types allow you to filter and rollup by date. Setting the right data type will ensure you are getting the correct functionatly from your data.

## How to set a data type
How-to video link - 

Define the kind of data in each column by setting the data type.  

To set a data type:
1.  Right click on the field you want to set.

<img src="../assets/datatype.png"  style="width:403px" class="border"></img>

2.  Select **Fields**

<img src="../assets/datatype.png"  style="width:403px" class="border"></img> 

3.  Select the desired type from the **Data type** dropdown

<img src="../assets/datatype.png"  style="width:403px" class="border"></img> 


The data types include:
* **Characters** - A string (e.g. Hourly)
* **Currency** - A monetary value ($) (e.g. $1.99)
* **Date** - 06/01/2022
* **General** - A numeric value without a comma separator (e.g. 1536)
* **Number** - An integer or a decimal (e.g. 1,536 or .129)
* **Percent** - A percentage (e.g. 92%)
* **Suggestion** - 
* **Time** - 
* **True/False** -



<img src="../assets/datatype.png"  style="width:403px" class="border"></img> 

### Date Formatting
To modify the default date formatting, change the `Date Format` value in `Show Dictionary` for the date field.  The string may contain replacements for adding the day of week to the formatted date:

* DDD - day of week (ie, Sun, Mon, ...)
* dddd - the localized date

For example, a date of `2022-04-03` will be formatted as:

```
DDD, dddd -> Sun, 04/03/2022
dddd (DDD) -> 04/03/2022 (Sun)
```
