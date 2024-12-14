# API Spec

## Embedding API

Endpoint :  POST /api/hide 

Request Form Body :

```json
{
  "image" : "@images.jpg",
  "key" : "rahasia",
  "message" : "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris mollis arcu eu tincidunt tincidunt. Maecenas id enim laoreet, tincidunt augue vel, congue elit. Pellentesque justo nulla, finibus vitae ante vitae, malesuada fermentum tellus."
}
```

Response Body Success :

```json
{
  "data" : {
    "image" : "http://127.0.0.1:3000/static/image_b200a319-31fd-4f86-a1e1-d380f3ba2708.png",
  }
}
```

## Extraction API

Endpoint : POST /api/reveal

Request Form Body :

```json
{
  "image" : "@image_b200a319-31fd-4f86-a1e1-d380f3ba2708.png",
  "key" : "rahasia"
}
```

Response Body Success : 

```json
{
  "data" : {
    "message" : "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris mollis arcu eu tincidunt tincidunt. Maecenas id enim laoreet, tincidunt augue vel, congue elit. Pellentesque justo nulla, finibus vitae ante vitae, malesuada fermentum tellus."
  }
}
```
