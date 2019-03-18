FROM python:3.7.2

WORKDIR /home/yan/workspace/qa/qa_auto
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 80
CMD [ "python3", "loop_register.py" ]
