# Using query parameters with the Microsoft Graph CLI

The Microsoft Graph CLI uses [JMESPath](http://jmespath.org/) query syntax to make queries against Microsoft Graph. The JMESPath queries result in the same [OData query parameters](https://docs.microsoft.com/en-us/graph/query-parameters?context=graph%2Fapi%2F1.0&view=graph-rest-1.0) used by Microsoft Graph.

## OData system query options
A Microsoft Graph API operation might support one or more of the following OData system query options in the CLI. These query options are compatible with the [OData V4 query language][odata-query].

>**Note:** OData 4.0 supports system query options in only GET operations.

| Name                     | Description | Example
|:-------------------------|:------------|:---------|
| **$count**        | Retrieves the total count of matching resources. | TBD
| **$expand**       | Retrieves related resources.| `mg users user show-user --user-id e8887f06-c72c-49a6-8788-d6a86300dea7 --expand "manager"`
| **$filter**       | Filters results (rows).|`mg applications application list --query "[?appId=='6881477a-a153-4bf1-973e-60abfad70ad5'].{appname: displayname, aud: signInAudience}" --output table`
| **$format**       | Returns the results in the specified media format.| TBD
| **$orderby**      | Orders results.| TBD
| **$search**       | Returns results based on search criteria. |
| **$select**       | Filters properties (columns).| `mg applications application list --select "DisplayName, Appid, SignInAudience"`
| **$skip**         | Indexes into a result set. Also used by some APIs to implement paging and can be used together with `$top` to manually page results. | TBD
| **$top**          | Sets the page size of results. | TBD


## Other query parameters

| Name                     | Description | Example
|:-------------------------|:------------|:---------|
| **$skipToken** | Retrieves the next page of results from result sets that span multiple pages. (Some APIs use `$skip` instead.) Not yet supported.  | TBD |

## Other OData URL capabilities

The following OData 4.0 capabilities are URL segments, not query parameters.

| Name                     | Description | Example 
|:-------------------------|:------------|:---------|
| **$ref** | Updates entities membership to a collection. Not yet supported. | TBD |
| **value** | Retrieves or updates the binary value of an item. Not yet supported. | TBD |
