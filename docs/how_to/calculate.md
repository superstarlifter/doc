## Calculated Fields
Use calculated fields when you want to change data based on other values in the same row. These actions range from basic mathematical operations to if-then statements, to advanced Javascript calculations.   

## How to create a calculation
How-to video link - https://youtu.be/pC5Fmbb7r1A

Use a calculation to derive new values in a collection.

To create a calculation:

1.	Right click ➔ **Calculated fields**

<img src="../assets/calc.png"  style="width:200px" class="border"></img>

2.  Enter a **Name** and select a **Type** for field

<img src="../assets/calc_1.png"  style="width:600px" class="border"></img>

3.  Choose the format of the data type

<img src="../assets/calc_2.png"  style="width:600px" class="border"></img>

4. Select the select the timing of aggregation when rolled up

    For more information on aggregation timing visit [How to the aggregate](https://docs.starlifter.io/#/how_to/calculate?id=how-to-set-aggregate)


<img src="../assets/calc_3.png"  style="width:600px" class="border"></img>

5.  Select the elements to build your calculation. Input a **Field** **Number** or **Text**, or use an **IF** or **Function**

    For a list of available functions visit [Functions](https://docs.starlifter.io/#/how_to/functions)


<img src="../assets/calc_4.png"  style="width:600px" class="border"></img>

4.  Select **Save**

<img src="../assets/calc_5.png"  style="width:600px" class="border"></img>

6.  The calculation is now part of the collection.

<img src="../assets/calc_6.png"  style="width:600px" class="border"></img>



## How to set the aggregate
Setting the aggregate allows you to determine if you want to calculate your values prior to rolling up the data or after the roll up has occurred.

## Calculated Fields
Use calculated fields when you want to change data based on other values in the same row. These actions range from basic mathematical operations to if-then statements, to advanced Javascript calculations.   

## How to create a calculation
How-to video link - https://youtu.be/pC5Fmbb7r1A

Use a calculation to derive new values in a collection.

To create a calculation:

1.	Right click ➔ **Calculated fields**

<img src="../assets/calc.png"  style="width:200px" class="border"></img>

2.  Enter a **Name** and select a **Type** for field

<img src="../assets/calc_1.png"  style="width:600px" class="border"></img>

3.  Choose the format of the data type

<img src="../assets/calc_2.png"  style="width:600px" class="border"></img>

4. Select the select the timing of aggregation when rolled up

    For more information on aggregation timing visit [How to the aggregate](https://docs.starlifter.io/#/how_to/calculate?id=how-to-set-aggregate)


<img src="../assets/calc_3.png"  style="width:600px" class="border"></img>

5.  Select the elements to build your calculation. Input a **Field** **Number** or **Text**, or use an **IF** or **Function**

    For a list of available functions visit [Functions](https://docs.starlifter.io/#/how_to/functions)


<img src="../assets/calc_4.png"  style="width:600px" class="border"></img>

4.  Select **Save**

<img src="../assets/calc_5.png"  style="width:600px" class="border"></img>

6.  The calculation is now part of the collection.

<img src="../assets/calc_6.png"  style="width:600px" class="border"></img>



## How to order aggregations in calculated fields
Values differ based on whether data is aggregated before or after the calculation.

The following examples demonstrate each use case.

### Example - Calculate before roll up
 *How do we correctly calculate Bob's total pay over a rolled up period?*
 ___
- 2 Calculated fields have been created multiplying Hours by Rate, one before, one after
  
<img src="../assets/calc_14.png"  style="width:400px" class="border"></img><img src="../assets/calc_15.png"  style="width:400px" class="border"></img>

<br>
<br>

- Prior to rollup the both calculated fields correctly and we can see how much Bob made per day

<img src="../assets/calc_16.png"  style="width:600px" class="border"></img>

<br>
<br>

- When we roll up by week we can see the Calculate before field calculate correctly whereas the Calculate After field is attempting to calculate the hours by the merged rate field



<img src="../assets/calc_11.jpg"  style="width:600px" class="border"></img>

- ✅ Total - Calculated Before - Summed the result of each calucated field
- ❌ Total - Calculated After - Calculated the value of rolled up Rate by the of rolled up Hours

<br>
<br>
<br>


### Example 2 - Calcualting Profit after rolling up

 *How do we correctly calculate Sales Profit over a rolled up period?*
 ___
 
- 2 Calculated fields have been created calculating (Sale Price - Sale Cost)/Sale Price, one before, one after.
- Prior to rollup the data is calculated correctly.

<img src="../assets/calc_12.png"  style="width:600px" class="border"></img>

Once rolled up by week we can see the profit margin of the totals vs the total of each weeks profit margin.


<img src="../assets/calc_13.jpg"  style="width:600px" class="border"></img>

- ❌ Profit - Calculated Before - Summed the result of each calucated field
- ✅ Profit - Calculated After -  Calculated the value of rolled up Sales Price and Sales Cost
