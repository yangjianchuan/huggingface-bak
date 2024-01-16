FROM python:3.11
RUN apt update 
RUN apt install git
RUN git clone https://github.com/renqabs/img_test.git
WORKDIR "img_test"
RUN pip install -r requirements.txt
EXPOSE 7860
CMD ["python", "main.py", "--host", "0.0.0.0:7860"]