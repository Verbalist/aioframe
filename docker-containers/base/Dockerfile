FROM ubuntu:14.04
RUN sed -i 's/archive.ubuntu.com/ua.archive.ubuntu.com/' /etc/apt/sources.list
RUN apt-get update
RUN apt-get install -y vim openssh-server screen git
RUN update-rc.d ssh defaults
RUN echo 'root:password' | chpasswd
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/' /etc/ssh/sshd_config
