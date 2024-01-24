FROM nvidia/cuda:11.8.0-cudnn8-devel-ubuntu20.04

ARG DEBIAN_FRONTEND=noninteractive
ENV ROS_DISTRO=noetic

ENV SHELL=/bin/bash \
    NB_USER=argrobotx \
    NB_UID=1000

RUN echo 'Etc/UTC' > /etc/timezone && \
    ln -s /usr/share/zoneinfo/Etc/UTC /etc/localtime

###################################### user #####################################
RUN adduser --disabled-password \
    --gecos "Default user" \
    --uid ${NB_UID} \
    ${NB_USER} 

RUN echo "root:root" | chpasswd
RUN echo "${NB_USER}:111111" | chpasswd

ENV HOME=/home/${NB_USER}

RUN apt-get update && \
    apt-get install -q -y --no-install-recommends \
    tzdata \
    dirmngr \
    gnupg2 \
    git \
    vim \
    less \
    curl \
    wget \
    sudo \
    cmake \
    net-tools \
    lsb-release \
    build-essential \
    software-properties-common \
    && rm -rf /var/lib/apt/lists/*

###################################### ROS #####################################
RUN echo "deb http://packages.ros.org/ros/ubuntu focal main" > /etc/apt/sources.list.d/ros1-latest.list
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654

RUN apt-get update && apt-get install -y --no-install-recommends \
    ros-noetic-desktop-full=1.5.0-1* \
    && rm -rf /var/lib/apt/lists/*

RUN apt update && apt install -y --no-install-recommends \
    python3-pip \
    python3-setuptools \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

###################################### acme #####################################
RUN pip install git+https://github.com/deepmind/acme.git#egg=dm-acme[jax,tf,envs] \
    && pip install --upgrade "jax[cuda11_local]==0.4.3" -f https://storage.googleapis.com/jax-releases/jax_cuda_releases.html \
    && pip install --upgrade "jaxlib[cuda11_local]==0.4.3" -f https://storage.googleapis.com/jax-releases/jax_cuda_releases.html \
    && pip install \
        protobuf==3.20.3 \
        numpy==1.22.4

RUN apt update && apt install -y --no-install-recommends \
    python3-tk \
    && rm -rf /var/lib/apt/lists/* \
    && pip install \
        seaborn \
        dm-haiku==0.0.10

RUN pip install torch==2.1.1 torchvision==0.16.1 torchaudio==2.1.1 --index-url https://download.pytorch.org/whl/cu118 \
    && pip install gymnasium==0.29.1 \
    && pip install stable-baselines3==2.2.1 \
    && pip install \
        openai==1.5.0 \
        trajectopy-core==2.4.8 \
        huggingface-sb3==3.0 \
        huggingface_hub==0.20.2 \
        hf_transfer==0.1.4

RUN echo "root ALL=(ALL)  ALL" >> /etc/sudoers \
    && echo "source /opt/ros/${ROS_DISTRO}/setup.bash" >> ${HOME}/.bashrc 

ENV XLA_PYTHON_CLIENT_PREALLOCATE=false
ENV HF_HUB_ENABLE_HF_TRANSFER=1
