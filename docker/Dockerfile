# 第一阶段 构建前端
FROM docker.qiudeng.cc/node:16.20

WORKDIR /root
RUN git clone https://github.com/qiudeng7/simple-knowledge-graph-generator.git

WORKDIR /root/simple-knowledge-graph-generator/vue
RUN npm --registry=https://registry.npm.taobao.org install && npm run build
RUN cp -r dist/* ../api/static/input

# 第二阶段 准备创建后端运行环境
FROM docker.qiudeng.cc/pytorch/pytorch:1.10.0-cuda11.3-cudnn8-runtime
RUN echo "deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic main restricted universe multiverse" > /etc/apt/sources.list \
&& echo "deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-updates main restricted universe multiverse" >> /etc/apt/sources.list \
&& echo "deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-backports main restricted universe multiverse" >> /etc/apt/sources.list \
&& apt update -y && apt upgrade -y  && apt install git -y

## 从第一阶段复制项目文件
COPY --from=0 /root/simple-knowledge-graph-generator /root/simple-knowledge-graph-generator

## 下载deepke
WORKDIR /root
RUN git clone https://github.com/zjunlp/DeepKE.git 

## 安装python依赖，deepke需要其中的setuptools才能安装。
RUN pip install -r /root/simple-knowledge-graph-generator/api/requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

## 编译安装deepke
WORKDIR /root/DeepKE
RUN python docker/setup_docker.py install && python docker/setup_docker.py develop

## 启动api
WORKDIR /root/simple-knowledge-graph-generator/api
CMD [ "python","api.py" ]