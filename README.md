# LSB (Least Significant Bit) steganography by encrypting Vigenère cipher encryption using Flask Framework

### How to Install Package and Run the Application
Install Required Packages: 
```bash
pip install -r requirements.txt
```

Run the Application:
```bash
python app.py
```


# API Spec

## Embedding API

Endpoint :  POST /api/hide 

Request Form Body :

```bash
curl --location --request POST '127.0.0.1:3000/api/hide' \
--form 'image=@"images.png"' \
--form 'message="Lorem ipsum dolor sit amet, consectetur adipiscing elit."' \
--form 'key="secret"'
```

Response Body Success :

```bash
{
  "data" : {
    "image" : "http://127.0.0.1:3000/static/image_b200a319-31fd-4f86-a1e1-d380f3ba2708.png",
  }
}
```

## Extraction API

Endpoint : POST /api/reveal

Request Form Body :

```bash
curl --location --request POST '127.0.0.1:3000/api/reveal' \
--form 'image=@"image_b200a319-31fd-4f86-a1e1-d380f3ba2708.png"' \
--form 'key="secret"'
```

Response Body Success : 

```bash
{
  "data" : {
    "message" : "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
  }
}
```
