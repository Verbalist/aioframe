FROM ubuntu:14.04
RUN sed -i 's/archive.ubuntu.com/ua.archive.ubuntu.com/' /etc/apt/sources.list && \
apt-get update && \
apt-get install -y vim openssh-server screen git && \
update-rc.d ssh defaults && \
echo 'root:password' | chpasswd && \
sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/' /etc/ssh/sshd_config
