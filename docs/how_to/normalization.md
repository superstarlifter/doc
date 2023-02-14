## Normalization
Data entered or retrieved from external systems may be in different formats. Normalization converts these different values into a single standardized value.
For example, a state name may be 'CA' 'Ca.' or 'California'.

<img src="../assets/normalization_9.jpg"  style="width:400px" class="border"></img>



Normalization converts aliases to names ensuring that each state is represented by only one name


<img src="../assets/normalization_10.jpg"  style="width:400px" class="border"></img>

Normalizations are represented in a normalization collection using **Alias** and **Name** fields.
When a value is entered that matches an **Alias**, it is converted to the **Name** value.

<img src="../assets/normalization_12.png"  style="width:400px" class="border"></img>

'CA' is the Name, and the Aliases are 'California', 'SF, CA', and 'Ca.'

### How to create a new normalization
1. Right-click on the field you want to normalize and select **Normalize field**, **New**.

<img src="../assets/normalization_2.png"  style="width:600px" class="border"></img>

2. Name the new normalization collection

<img src="../assets/normalization_3.png"  style="width:600px" class="border"></img>

3. A new Normalization collection is created with a record for each unique value found in the normalized field.

<img src="../assets/normalization_4.png"  style="width:200px" class="border"></img>


4. For each **Alias** value, change the matching **Name** value to your desired normalized value.

<img src="../assets/normalization_5.png"  style="width:200px" class="border"></img>

5. In your original collection any **Alias** values from your normalized field will automatically be converted to the **Name** value.

<img src="../assets/normalization_6.png"  style="width:600px" class="border"></img>

### Adding data to a normalization collection

Any new data entered into your normalized field will be automatically added to the normalization collection.

<img src="../assets/normalization_18.jpg"  style="width:400px" class="border"></img>

Update the **Name** value to your desired normalized value

<img src="../assets/normalization_19.jpg"  style="width:400px" class="border"></img>

### Apply an existing normalization to a field 

You can apply a pre-existing normalization to another field. 

Right-click on the field your want to normalize and select **Normalize field** and select the pre-existing normalization.

<img src="../assets/normalization_20.png"  style="width:400px" class="border"></img>

