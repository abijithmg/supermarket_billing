FROM python:3.8

COPY app.py test_app.py README.md ./

# RUN pip install pytest

# CMD ["pytest", "./test_app.py"]

CMD [ "python", "./app.py" ]
