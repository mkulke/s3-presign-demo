from app import app
from flask import request, render_template
from service import get_presigned_tuple

@app.route('/upload')
def index():
    bucket = request.args.get('bucket')
    assert bucket
    path = request.args.get('path')
    assert path
    url, fields = get_presigned_tuple(bucket, path)
    return render_template('index.html',
                           key=fields['key'],
                           url=url,
                           signature=fields['signature'],
                           aws_access_key_id=fields['AWSAccessKeyId'],
                           x_amz_security_token=fields['x-amz-security-token'],
                           policy=fields['policy'])

