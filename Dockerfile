FROM python:3.9-slim

WORKDIR /app

COPY GetData.py /app/

COPY playbook.yml /app/

RUN pip install ansible

VOLUME /app/csv_data

CMD ["ansible-playbook", "playbook.yml"]
