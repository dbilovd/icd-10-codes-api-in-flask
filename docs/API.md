
## API Documentation for OCD-10 Codes API

## Fetch a paginated list of available codes

```
GET /codes/?page=1
```

### Request

> 
> **Query**
> 
> |Key|Value|Description|
> |---|---|---|
> |page|Integer|1|
> 

### Example:

> 
> **Example: This's a right way to use.**
> 
> > 
> > ```
> > GET /codes/?page=1
> > ```
> > 
> > **Response**
> > 
> > > 
> > > **Body**
> > > 
> > > ```
> > > {
> > >   "responseCode": 200,
> > >   "responseMessage": "Success",
> > >   "data": [
> > >     {
> > >       "codeId": 1,
> > >       "parentCodeId": null,
> > >       "code": "A01",
> > >       "fullCode": "A01",
> > >       "title": "Code 1",
> > >       "fullTitle": "Code 1",
> > >       "createdAt": "2021-01-01 01:01:01",
> > >       "updatedAt": "2021-01-01 01:01:01",
> > >     },
> > >     {
> > >       "codeId": 2,
> > >       "parentCodeId": 1,
> > >       "code": "01",
> > >       "fullCode": "A0101",
> > >       "title": "Code 2",
> > >       "fullTitle": "Code 1, Code 2",
> > >       "createdAt": "2021-01-01 01:01:01",
> > >       "updatedAt": "2021-01-01 01:01:01",
> > >     }
> > >   ]
> > >   "meta": {
> > >     "totalPages": 1,
> > >     "totalItems": 1,
> > >     "itemsPerPage": 20,
> > >     "currentPage": 1,
> > >     "previousPage": null,
> > >     "nextPage": null,
> > >   }
> > > }
> > > ```
> > > 
> > 
> 
## Fetch a sincle code

```
GET /codes/<code-id>
```

### Request

> 
> **Query**
> 
> |Key|Value|Description|
> |---|---|---|
> |code-id|Integer|ID of code to update|
>

### Examples:

> 
> **Example: Successful Request**
> 
> > 
> > ```
> > GET /codes/2
> > ```
> > 
> > **Request**
> > 
> > 
> > **Response**
> > 
> > > 
> > > **Body**
> > > 
> > > ```
> > > {
> > >   "responseCode": 200,
> > >   "responseMessage": "Deleted",
> > >   "data": {
> > >     "codeId": 2,
> > >     "parentCodeId": 1,
> > >     "code": "A01",
> > >     "fullCode": "A01",
> > >     "title": "Colera",
> > >     "fullTitle": "Code 1",
> > >     "createdAt": "2021-01-01 01:01:01",
> > >     "updatedAt": "2021-01-01 01:01:01",
> > >   }
> > > }
> > > ```
> > > 
> > 
> 

## Create a new Code

```
POST /codes/
```

### Request

> 
> **Body**
> 
> |Key|Value|Type|Description|
> |---|---|---|---|
> |code|A01|text, integer|The Code for this particular OCD-10 code.|
> |title|Colera|text|The title or description for this particular OCD-10 code.|
> |parentCodeId|1|integer|The ID of the OCD-10 code this particular OCD-10 is a subcode of.|
> 

### Examples:

> 
> **Example: Successful Request**
> 
> > 
> > ```
> > POST /codes/
> > ```
> > 
> > **Request**
> > 
> > > 
> > > **Body**
> > > 
> > > |Key|Value|Type|Description|
> > > |---|---|---|---|
> > > |code|A01|text, integer|The Code for this particular OCD-10 code.|
> > > |title|Colera|text|The title or description for this particular OCD-10 code.|
> > > |parentCodeId|1|integer|The ID of the OCD-10 code this particular OCD-10 is a subcode of.|
> > > 
> > 
> > **Response**
> > 
> > > 
> > > **Body**
> > > 
> > > ```
> > > {
> > >   "responseCode": 200,
> > >   "responseMessage": "Success",
> > >   "data": {
> > >     "codeId": 1,
> > >     "parentCodeId": null,
> > >     "code": "A01",
> > >     "fullCode": "A01",
> > >     "title": "Code 1",
> > >     "fullTitle": "Code 1",
> > >     "createdAt": "2021-01-01 01:01:01",
> > >     "updatedAt": "2021-01-01 01:01:01",
> > >   }
> > > }
> > > ```
> > > 
> > 
> 

## Update an existing code

```
PATCH /codes/<code-id>
```

### Request

> 
> **Query**
> 
> |Key|Value|Description|
> |---|---|---|
> |code-id|Integer|ID of code to update|

> **Body**
> 
> |Key|Value|Type|Description|
> |---|---|---|---|
> |code|A01|text, integer|The Code for this particular OCD-10 code.|
> |title|Colera|text|The title or description for this particular OCD-10 code.|
> |parentCodeId|1|integer|The ID of the OCD-10 code this particular OCD-10 is a subcode of.|
> 

### Examples:

> 
> **Example: Successful Request**
> 
> > 
> > ```
> > PATCH /codes/2
> > ```
> > 
> > **Request**
> > 
> > > 
> > > **Body**
> > > 
> > > |Key|Value|Type|Description|
> > > |---|---|---|---|
> > > |code|A01|text, integer|The Code for this particular OCD-10 code.|
> > > |title|Colera|text|The title or description for this particular OCD-10 code.|
> > > |parentCodeId|1|integer|The ID of the OCD-10 code this particular OCD-10 is a subcode of.|
> > > 
> > 
> > **Response**
> > 
> > > 
> > > **Body**
> > > 
> > > ```
> > > {
> > >   "responseCode": 200,
> > >   "responseMessage": "Success",
> > >   "data": {
> > >     "codeId": 2,
> > >     "parentCodeId": 1,
> > >     "code": "A01",
> > >     "fullCode": "A01",
> > >     "title": "Colera",
> > >     "fullTitle": "Code 1",
> > >     "createdAt": "2021-01-01 01:01:01",
> > >     "updatedAt": "2021-01-01 01:01:01",
> > >   }
> > > }
> > > ```
> > > 
> > 
> 

## Delete an existing code

```
DELETE /codes/<code-id>
```

### Request

> 
> **Query**
> 
> |Key|Value|Description|
> |---|---|---|
> |code-id|Integer|ID of code to update|
>

### Examples:

> 
> **Example: Successful Request**
> 
> > 
> > ```
> > DELETE /codes/2
> > ```
> > 
> > **Request**
> > 
> > 
> > **Response**
> > 
> > > 
> > > **Body**
> > > 
> > > ```
> > > {
> > >   "responseCode": 200,
> > >   "responseMessage": "Deleted",
> > >   "data": {
> > >     "codeId": 2,
> > >     "parentCodeId": 1,
> > >     "code": "A01",
> > >     "fullCode": "A01",
> > >     "title": "Colera",
> > >     "fullTitle": "Code 1",
> > >     "createdAt": "2021-01-01 01:01:01",
> > >     "updatedAt": "2021-01-01 01:01:01",
> > >   }
> > > }
> > > ```
> > > 
> > 
> 
