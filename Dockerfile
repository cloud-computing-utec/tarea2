FROM rancher/spark:1.5.2-1

USER root

WORKDIR /opt/app
COPY wordCount.py .
COPY requirements.txt .

ADD pyspark pyspark

COPY get-pip.py .
RUN python get-pip.py
RUN pip install -r requirements.txt
RUN rm -f get-pip.py
RUN rm -f requirements.txt