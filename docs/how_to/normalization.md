## Normalization
Data entered or retrieved from external systems may be in different formats. Normalization converts these different values into a single standardized value.
For example, a state name may be 'CA' 'Ca.' or 'California'.

<img src="../assets/normalization_9.jpg"  style="width:400px" class="border"></img>



Normalization converts aliases to names ensuring that each state is represented by only one name.


<img src="../assets/normalization_10.jpg"  style="width:400px" class="border"></img>

Normalizations are represented in a normalization collection using **Alias** and **Name** fields.
When a value is entered that matches an **Alias**, it is converted to the **Name** value.

<img src="../assets/normalization_12.png"  style="width:400px" class="border"></img>

'CA' is the Name, and the Aliases are 'California', 'SF, CA', and 'Ca.'

### How to create a new normalization
1. Right-click on the field you want to normalize and select **Normalize field**, **New**.

<img src="../assets/normalization_2.png"  style="width:600px" class="border"></img>

2. Name the new normalization collection.

<img src="../assets/normalization_3.png"  style="width:600px" class="border"></img>

3. A new Normalization collection is created with a record for each unique value found in the normalized field.

<img src="../assets/normalization_4.png"  style="width:200px" class="border"></img>


4. For each **Alias** value, change the matching **Name** value to your desired normalized value.

<img src="../assets/normalization_5.png"  style="width:200px" class="border"></img>

5. In your original collection, right-click in the grid that contains the **Alias** value you would like to change and select Fields. 

<img src="../assets/normalization_6.png"  style="width:600px" class="border"></img>

6. Click on the **Name** (State/Territory) field, and change the data type to [Reference](https://docs.starlifter.io/#/how_to/references?id=create-a-reference).
7. Set the following fields:
   * Reference Collection: Name of the Normalization Collection (State)
   * Reference Collection Field to Match: the Alias field (State/Territory)
   * Check "Use *Field Name* as a display value"
   * Additional Reference fields: Select the normalization collection. Name (State.Name) as an additional referenced field.
8. Click Save

   Your field should now be normalized. 

### Adding data to a normalization collection

Any new data entered into your normalized field will be automatically added to the normalization collection.

<img src="../assets/normalization_18.jpg"  style="width:400px" class="border"></img>

Update the **Name** value to your desired normalized value.

<img src="../assets/normalization_19.jpg"  style="width:400px" class="border"></img>

### Apply an existing normalization to a field 

You can apply a pre-existing normalization to another field. 

Right-click on the field your want to normalize and select **Normalize field** and select the pre-existing normalization.

<img src="../assets/normalization_20.png"  style="width:800px" class="border"></img>

The normalization will change the values of your field to the normalized values

<img src="../assets/normalization_21.png"  style="width:400px" class="border"></img>


<img src="../assets/normalization_22.png"  style="width:800px" class="border"></img>


To learn more or ask additional questions, head over to the [StarLifter Community](https://community.starlifter.io).
