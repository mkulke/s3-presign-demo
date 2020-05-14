# s3 presign demo

You have to have AWS rights set up properly on your localhost for this to work.

## CORS

The S3 Bucket needs a CORS policy configured for this to work.

```
<CORSConfiguration>
 <CORSRule>
   <AllowedOrigin>http://localhost:5000</AllowedOrigin>
   <AllowedMethod>POST</AllowedMethod>
   <AllowedHeader>*</AllowedHeader>
 </CORSRule>
</CORSConfiguration>
```

## Environment

```
virtualenv -p python3 venv
. ./venv/bin/activate
pip install boto3 jinja2 flask
```

## Run Server

```
FLASK_APP=s3-presign-demo.py flask run
```

## Run Client

Open `http://localhost:5000/upload?path=some-path&bucket=some-bucket` in a browser.
