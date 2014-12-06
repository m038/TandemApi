# TODO: check for python
wget https://bootstrap.pypa.io/get-pip.py
python get-pip.py
pip install eve
pip install twilio
pip install -U flask-cors
pip install gunicorn
pip install greenlet
pip install eventlet

# install the tandem_api package
python setup.py install
