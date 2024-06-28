FROM python:3.8

WORKDIR /super_market_billing

COPY app.py test_app.py README.md ./

# RUN pip install pytest

# CMD ["pytest"]

CMD [ "python", "./app.py" ]
