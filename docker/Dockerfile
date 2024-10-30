FROM docker.qiudeng.cc/pytorch/pytorch:1.10.0-cuda11.3-cudnn8-runtime

RUN echo "deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic main restricted universe multiverse" > /etc/apt/sources.list \
&& echo "deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-updates main restricted universe multiverse" >> /etc/apt/sources.list \
&& echo "deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-backports main restricted universe multiverse" >> /etc/apt/sources.list \
&& apt update -y && apt upgrade -y  && apt install git -y

WORKDIR /root
RUN git clone https://github.com/zjunlp/DeepKE.git && git clone https://github.com/qiudeng7/simple-knowledge-graph-generator.git
RUN pip install -r /root/simple-knowledge-graph-generator/api/requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

WORKDIR /root/DeepKE
RUN python docker/setup_docker.py install && python docker/setup_docker.py develop

WORKDIR /root/simple-knowledge-graph-generator/api
CMD [ "python","api.py" ]