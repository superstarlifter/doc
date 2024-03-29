## Create a Reference
[**Video Tutorial**](https://youtu.be/YemXi1X9r-I?feature=shared)

A reference field stores a reference to a field in another collection. For example, the AccountCode field in a General Ledger collection is a reference to the Chart of Accounts collection.

When you define a reference field, a relationship is created between the two collections. Adding a reference field to a collection makes the other fields in the referenced collection available as well.

### Set up reference field
1. Right click on the field you wish to reference to another collection ➔ **Fields**

2. Change **Data Type** to Reference.

<img src="../assets/references_matt1.png"  style="width:800px" class="border"></img>

3. Select the **Reference collection** and **Reference collection field to match**.

<img src="../assets/references_matt3.png"  style="width:800px" class="border"></img>

4. To use the field to match as the display value, check **Use as display value**. Alternatively, the display value in the referenced collection will be displayed in the reference field. In this example, the name of Account 1019 is Due from Parent.

   <img src="../assets/references_matt10.png"  style="width:800px" class="border"></img>


5. Click **Save**.


### Adding fields from a referenced collection
1. You also have the option of adding fields from the referenced collection. Select Add field from **Additional referenced fields**, and check the fields to add.

<img src="../assets/references_matt5.png"  style="width:800px" class="border"></img>

2. Click **Save**

<img src="../assets/references_matt4.png"  style="width:800px" class="border"></img>


4. The added fields are now available in the collection.

<img src="../assets/references_matt6.png"  style="width:800px" class="border"></img>

**Note:** The added fields are not editable in the collection. They update dynamically as changes are made to the referenced collection.
