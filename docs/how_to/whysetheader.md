## Why to set a header row

If you have looked at a formula and asked yourself, 'What does this actually do?!' or, if you have copied a formula down a gigantic spreadsheet, you already know what a pain it is _not_ to have a header row.  What's a header row?  A header row defines the fields in your data table.  Meaning, it takes the top value in each column and assigns it as the name for all of the other rows. 

Look at the example below.  

<img src="../assets/whyheader.png"  style="width:600px" class="border"></img>

After the header row has been set, Account Number, Amount, Account Name, etc. are all set as the names of the columns in the data table.  

<img src="../assets/whyheader2.png"  style="width:1200px" class="border"></img>

Creating calculated fields is much easier since you reference field names (e.g. Amount) as opposed to field numbers (e.g. A5).  In addition to making it easier to reference fields in calculations, header rows apply discipline to your data.  We've all experienced the fragility of a spreadsheet.  Consider writing a formula in a spreadsheet and copying it down the lenghth of the column. What happens if one of cells' formulas is accidentally changed?  Your data could be corrupted!  

Once you have set a header row and defined the field, there's no chance that the first row of data is going to be treated differently than the last row of data.  In conclusion, set the header row so you may refer to data in language you understand. 

## How to set a header row

To set a header row:

1.	Select the header row

<img src="../assets/fib_06.png"  style="width:1200px" class="border"></img>

2.	Right click ➔ **Set header row**

<img src="../assets/fib_07.png"  style="width:1200px" class="border"></img>

3.  The header row is set

<img src="../assets/fib_09.png"  style="width:1200px" class="border"></img>
