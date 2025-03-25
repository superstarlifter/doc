## Creating a pipeline

[**Video Tutorial**](https://youtu.be/9gMl5IKxzNM?feature=shared)

As you clean and reformat your collection, a pipeline is automatically created to save your steps. Pipelines can be saved to be used again in the future.

<img src="../assets/pipeline_layout_matt.png"  style="width:800px" class="border"></img>

A pipeline is applied to a StarLifter collection. To begin, select the collection you wish to clean and reformat.

### Common transformer commands
The commands below can be accessed by right-clicking within the collection preview:

* **Delete rows like this:** Delete rows that contain the selected value
* **Set as header row:** Set the selected row to be the header row
* **Create field using value:** Create a field where every row contains the selected value
* **Change field name:** Change the name of the field
* **Merge two fields:** Concatenate the values of two fields in the same row
* **Split into multiple fields:** Split a single field into multiple fields
* **Filter:** Filter the collection
* **Fill empty values from prior rows:** Fill blank cells with the values from the prior row
* **Reference another collection:** Reference the field to a field in another collection, and pull in additional values from the referenced collection
* **Join fields from another collection:** Left-join on fields from another collection
* **Delete field:** Remove a field from the collection
* **Copy field:** Duplicate the field within the collection
* **Rotate fields to rows:** Unpivot or flatten data by putting selected rows into a single column
* **New field:** Add a new field to the collection

### Building and saving a pipeline
As you execute new plans to the collection, StarLifter saves your list of commands in the pipeline.

<img src="../assets/pipeline_commands_list_matt.png"  style="width:400px" class="border"></img>

To edit a command, click the pencil icon to the right of the command. To delete a command, click the ⨂ next to the command.

<img src="../assets/pipeline_commands_list_matt_2.png"  style="width:400px" class="border"></img>

To save your pipeline for future use, select **Save as** in the **Pipeline** dropdown.

<img src="../assets/pipeline_commands_list_matt_3.png"  style="width:400px" class="border"></img>

Once a pipeline is saved, it is available to use on other collections.

### Saving a collection
1. Select the domain you wish to output your collection to using the **Save to domain** dropdown. You can also create a new domain for the output collection by clicking **Save as**.

2. Click **Save as** from the **Save to collection** dropdown to create a new collection.

<img src="../assets/manipulator_collection_save1.png"  style="width:400px" class="border"></img>

3. Alternatively, select the collection you wish to overwrite.

<img src="../assets/manipulator_collection_save2.png"  style="width:400px" class="border"></img>

You can now see the cleaned and updated collection in your Collection Ribbon.