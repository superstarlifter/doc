## Functions
Functions are predefined formulas that are used in [calculated fields.](https://docs.starlifter.io/#/how_to/calculate)

To access the available functions for a calcuated field, click the left icon of the chip and select function.

<p align="center">
<img src="../assets/function_def_1.png"  style="width:800px" class="border"></img>    <img src="../assets/function_def_2.png"  style="width:800px" class="border"></img>
</p>



## List of Functions

### Mid
MID returns a specific number of characters from a text string, starting at the position you specify, based on the number of characters you specify.

<img src="../assets/function_mid_3.png"  style="width:800px" class="border">

Results:
<p align="center">
</img> <img src="../assets/function_mid_4.png"  style="width:400px" class="border"></img> 
</p>


### Min
MIN returns the smallest numeric value in the data provided.

### Max
MAX returns the largest numeric value in the data provided.

### DateDif
DateDif calculates the number of days, months, or years between two dates.

The example below uses an IF Statement to check for a value in the *Departure date* field and the calculates the number of days between *Departure date* and *Start date* 

<img src="../assets/function_datedif_2.png"  style="width:800px" class="border"></img> 

Results:
<p align="center">
<img src="../assets/function_datedif_3.png"  style="width:400px" class="border"></img> 
</p>

### DaysFromNow
DaysFromNow calculates the number of days from a given date until the current date.

<img src="../assets/function_daysfromnow_1.png"  style="width:800px" class="border"></img> 

Results:
<p align="center">
<img src="../assets/function_daysfromnow_2.png"  style="width:400px" class="border"></img> 
</p>

### Concatenate
Concatenate joins values together and returns the result as a string.

<img style=center src="../assets/function_concatenate_1.png"  style="width:800px" class="border"></img> 

Results:
<p align="center">
<img src="../assets/function_concatenate_2.png"  style="width:400px" class="border"></img> 
</p>

### Concatenate with Spaces
Concatenate joins values together and returns the result as a string separated by spaces.

<img src="../assets/function_concatenatewithspaces_1.png"  style="width:800px" class="border"></img> 

Results:
<p align="center">
<img src="../assets/function_concatenatewithspaces_2.png"  style="width:400px" class="border"></img> 
</p>

### RemoveNumbers
RemoveNumbers will remove the first grouping of numbers and return the string.

<img src="../assets/function_removenumbers_1.png"  style="width:800px" class="border"></img> 

Results:
<p align="center">
<img src="../assets/function_removenumbers_2.png"  style="width:400px" class="border"></img> 
</p>

### DayOfWeek
DayOfWeek function takes a date and returns a number between 0-6 representing the day of week. 0 for Sunday and 6 for Saturday.

<img src="../assets/function_dayofweek_1.png"  style="width:800px" class="border"></img> 

Results:
<p align="center">
<img src="../assets/function_dayofweek_3.png"  style="width:400px" class="border"></img> 
</p>

### DayName
DayName function takes a date and returns value of the day of the week in a string value, either long or short (Monday vs Mon).

<img src="../assets/function_dayname_1.png"  style="width:800px" class="border"></img> 

Results:
<p align="center">
  <img src="../assets/function_dayname_2.png"  style="width:400px" class="border"></img> 
</p>

### WeekNumber
WeekNumber function takes a date and returns a week number (1-54) that corresponds to the week of year.

<img src="../assets/function_weeknumber_1.png"  style="width:800px" class="border"></img>

Results:
<p align="center">
<img src="../assets/function_weeknumber_2.png"  style="width:400px" class="border"></img>
</p>

### Left
Left function extracts a given number of characters from the left side of a string.

<img src="../assets/function_left_1.png"  style="width:800px" class="border"></img>

Results:
<p align="center">
<img src="../assets/function_left_2.png"  style="width:400px" class="border"></img>
</p>

### Right
Right function extracts a given number of characters from the right side of a string.

<img src="../assets/function_right_1.png"  style="width:800px" class="border"></img>

Results:
<p align="center">
<img src="../assets/function_right_2.png"  style="width:400px" class="border"></img>
</p>

### Split
Split function splits a string into multiple strings given the delimiter that separates them.

<img src="../assets/function_split_1.png"  style="width:800px" class="border"></img>

Results:
<p align="center">
<img src="../assets/function_split_2.png"  style="width:400px" class="border"></img>
</p>


### SumChildren
SumChildren function will sum the value of any child records.

In order to utilize the SumChildren function you will need a parent/child reference relationship between collections.

For more information on reference fields - [Reference Fields](https://docs.starlifter.io/#/how_to/reference_field?id=how-create-a-reference-field)

<img src="../assets/function_sumchildren_1.png"  style="width:800px" class="border"></img>

<figcaption>Child Collection</figcaption>
<p align="center">
<img src="../assets/function_sumchildren_2.png"  style="width:400px" class="border"></img>
</p>

<figcaption>Parent Collection</figcaption>
<p align="center">
<img src="../assets/function_sumchildren_3.png"  style="width:400px" class="border"></img>
</p>


### AvgChildren
SumChildren function will calculate an average value of any child records.

In order to utilize the AvgChildren function you will need a parent/child reference relationship between collections.

For more information on reference fields - [Reference Fields](https://docs.starlifter.io/#/how_to/reference_field?id=how-create-a-reference-field)

<img src="../assets/function_avgchildren_2.png"  style="width:800px" class="border"></img>

<figcaption>Child Collection</figcaption>
<p align="center">
<img src="../assets/function_sumchildren_2.png"  style="width:400px" class="border"></img>
</p>

<figcaption>Parent Collection</figcaption>
<p align="center">
<img src="../assets/function_avgchildren_1.png"  style="width:400px" class="border"></img>
</p>

### CountChildren
SumChildren function will count the number of any child records.

In order to utilize the CountChildren function you will need a parent/child reference relationship between collections.

For more information on reference fields - [Reference Fields](https://docs.starlifter.io/#/how_to/reference_field?id=how-create-a-reference-field)


<img src="../assets/function_countchildren_1.png"  style="width:800px" class="border"></img>


<figcaption>Child Collection</figcaption>
<p align="center">
<img src="../assets/function_sumchildren_2.png"  style="width:400px" class="border"></img>
</p>

<figcaption>Parent Collection</figcaption>
<p align="center">
<img src="../assets/function_countchildren_2.png"  style="width:400px" class="border"></img>
</p>



To learn more or ask additional questions, head over to the [StarLifter Community](https://community.starlifter.io).
