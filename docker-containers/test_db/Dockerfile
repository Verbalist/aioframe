FROM base

# ADD ssh/* /root/.ssh/
ADD ssh/core_test /root/.ssh/id_rsa
ADD ssh/core_test.pub /root/.ssh/id_rsa.pub
ADD ssh/config /root/.ssh/config

# install postgresql
RUN apt-get install -y postgresql

# configure postgresql
RUN sed 's/host    all             all             127\.0\.0\.1\/32            md5/host    all             all             127.0.0.1\/32            trust/' /etc/postgresql/*/main/pg_hba.conf -i &&\
 echo "" >> /etc/postgresql/9.3/main/pg_hba.conf && \
 echo "host    all             all             0.0.0.0/0            trust" >> /etc/postgresql/9.3/main/pg_hba.conf && \
 echo "" >> /etc/postgresql/9.3/main/postgresql.conf && \
 echo "listen_addresses = '*'" >> /etc/postgresql/9.3/main/postgresql.conf

# add sql scripts

ADD test-env.sql /opt/

# create databases
RUN service postgresql restart ; sleep 2 ; \
psql -U postgres -h 127.0.0.1 -c "CREATE ROLE test WITH PASSWORD 'test' LOGIN CREATEDB;"; \
psql -U test -h 127.0.0.1 -c "CREATE DATABASE test;" postgres ; \
psql -U test -h 127.0.0.1 -d test -f /opt/test-env.sql; \
service postgresql stop


RUN chmod 400 /root/.ssh/id_rsa &&\
    mkdir -p /var/log/gfrd &&\
    echo "import time" >> /opt/t.py &&\
    echo "while True:" >> /opt/t.py &&\
    echo " time.sleep(1)" >> /opt/t.py &&\
    echo " print(1)" >> /opt/t.py

CMD service postgresql restart && python3.4 /opt/t.py