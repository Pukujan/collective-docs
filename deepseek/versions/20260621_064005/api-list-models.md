---
title: API — List Models
source: deepseek
url: https://api-docs.deepseek.com/api/list-models
fetched: 2026-06-21T06:39:54.668875
---

# API — List Models

* [](/)
* API Reference
* Models
* Lists Models

# Lists Models


```
GET ## /models


```


Lists the currently available models, and provides basic information about each one such as the owner and availability. Check [Models & Pricing](/quick_start/pricing) for our currently supported models.


## Responses[​](#responses)


* 200

OK, returns A list of models


* application/json


* Schema
* Example (from schema)
* Example

**Schema

**
**object** stringrequired**Possible values:** [`list`]

**data

**Model[]

required

* Array [


**id** stringrequiredThe model identifier, which can be referenced in the API endpoints.

**object** stringrequired**Possible values:** [`model`]

The object type, which is always "model".

**owned_by** stringrequiredThe organization that owns the model.

* ]


```
`{
  "object": "list",
  "data": [
    {
      "id": "string",
      "object": "model",
      "owned_by": "string"
    }
  ]
}
`
```

```
`{
  "object": "list",
  "data": [
    {
      "id": "deepseek-v4-flash",
      "object": "model",
      "owned_by": "deepseek"
    },
    {
      "id": "deepseek-v4-pro",
      "object": "model",
      "owned_by": "deepseek"
    }
  ]
}
`
```

Loading...[PreviousCreate FIM Completion (Beta)](/api/create-completion)[NextGet User Balance](/api/get-user-balance)