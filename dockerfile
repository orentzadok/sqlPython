FROM python:3.12-alpine
WORKDIR /home
COPY script_py_with_sqli.py .
CMD ["python","script_py_with_sqli.py"]

