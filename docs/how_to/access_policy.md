## Access Policies
Access policies allow admins to grant users view and update access to specific data. This access is more than just sharing a collection, it can be filtered down to the row and field level. For example, an access policy can be created to limit updating of specific rows to the owner of that row.

### Creating an Access Policy Row
1. From the Toggle Menu on the far left, navigate to the System Definitions drop down and select SL Access Policies.


<img src="../assets/access_policy_1.png"  style="width:200px" class="border"></img>


2. Right click and select Insert Row to insert a blank row
3. Fill out the appropriate fields 
   * Resouce - The resource you are granting access to, in path format (/collection/example_domain.example_collection) 
   * Access - The type of access granted to the resource
      * Read -  view the data but not edit
      * Update -  edit the data 
      * Delete -  delete the data
      * Config - change the configuration of the collection. For example: Updating the field types
      * Edit - a grouping of the following access [‘config’, ‘read’, ‘create’, ‘update’, ‘delete’]
   * All Users - Does this rule apply to all users
   * User - The user this policy grants access
   * User Name - Username of from the User field. (Auto populated)
   * Condition - Set to 'true'
   * Filter - Filter access of data by rows
   * Fields - Filter access of data by fields
   * Parent - Used to link two policies together
      * Note:  Primarily used for sharing dashboards. When a dashboard is shared, an underlying access policy is created to share that data that supports the dashboard


<img src="../assets/access_policy_2.png"  style="width:800px" class="border"></img>


### Creating an Access Policy via sharing
* When a user shares a resource (collection, dashboard, etc) an access policy will automatically be created in the Access Policies table.
* Resources that require supporting resources will automatically create a policy for both resources.
    * For example when a user shares a dashboard with a user, 2 policies will be created 
      * 1 for the dasboard
      * 1+ for the read access to the data that supports the dashboard

* For more information on how to Share collections, dashboards and domains, visit: [Sharing Access](/docs/how_to/sharing_access.md)