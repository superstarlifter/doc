## Using a view for data input

[**Video Tutorial**](https://youtu.be/IUkEAK2Cqyo?feature=shared)

Views can be used to control which users can view and edit data.

### Create a view:  
In this example, we will create a view where the budget owner can only edit the amount field for the line items they are responsible for.

<img src="../assets/inputingdata_matt01.png"  style="width:800px" class="border"></img>

1. Right-click in the collection and select **Create View**.

<img src="../assets/inputingdata_matt02.png"  style="width:300px" class="border"></img>

2.  Name the view. Select the fields you'd like included in the view, and choose which fields should not be editable by checking **Read only**.

<img src="../assets/inputingdata_matt03.png"  style="width:600px" class="border"></img>

3.  Select Filters to give access to the appropriate budget owner, determined by the owner field. Type "{{" and select how the budget owner will be identified: by the logged in user ID, user email, or user name, depending in the information contained in the owner field. This is most often the user name used to log into StarLifter.

<img src="../assets/inputingdata_matt04.png"  style="width:600px" class="border"></img>

4.  Select Users to set the specific edit permissions:
   * **Update:** Update editable fields
   * **Insert:** Insert new rows
   * **Delete:** Delete rows
   * **Config:** Change data types, formats, or add new fields.

<img src="../assets/inputingdata_matt05.png"  style="width:600px" class="border"></img>

5.  Share the view with the user by right-clicking in the collection and selecting **Share**.

<img src="../assets/inputingdata_matt06.png"  style="width:300px" class="border"></img>

6.  Set permissions to the appropriate level, and click Invite to send an invite email. By selecting Editor, you are giving the budget owner the permission to edit the fields they have access to. See
   [**Sharing data**](how_to/sharing_access.md) for more information.

<img src="../assets/inputingdata_matt07.png"  style="width:800px" class="border"></img>

### Impersonate a user to test the view:  
1. In the administration menu, select **Impersonate User**.

<img src="../assets/inputingdata_matt08.png"  style="width:300px" class="border"></img>

2. In the example below, only Bryan's budget items are displayed in the view, and Amount is the only editable field.

<img src="../assets/inputingdata_matt09.png"  style="width:800px" class="border"></img>





