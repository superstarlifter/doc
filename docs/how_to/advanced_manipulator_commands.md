## Advanced manipulator commands

### Command toolbar
More complex commands can be accessed using the toolbar at the top of the screen

<img src="../assets/manipulator_command_toolbar_matt.png"  style="width:800px" class="border"></img>

**Dictionary:** Edit the collection dictionary (change data type, format, etc)

**Choose Fields** Edit the layout of a collection, including removing fields

**Merge Fields:** Concatenate the values of two fields in the same row

**Calculated Field:** Create a calcualted field within the collection

**Append Collection:** Combine data by appending data from another collection

**Project Rows:** Project rows from another collection into the collection

**Project Dates:** Project monthly, quarterly, or yearly dates into the collection

### Grouping and appending a collection
Grouping collections in StarLifter can be accomplished using two different methods.
1. Drag and drop:

Drag and drop a collection from the collection list on top of the collection tab in the collection preview. 

Continue adding more collections to the group by dragging and dropping. 

Pipeline commands will be applied to all collections in the group.
   
Saving will output a single collection including the cleaned data from each source collection in the group.

2. Appending a collection:

Select the collection from which you wish to append data

You have the options of applying a tag to the appended data. The tag will appear in an additional column. If you do not wish to apply a tag, StarLifter will automatically apply the collection name as a tag.

Select how to append fields to the collection, by choosing one of the following actions:
* Ignore field: Do not append this field to the collection
* Copy to field: Match this field to a field in the collection
* Create new field: Create a new field to the collection