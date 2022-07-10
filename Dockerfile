FROM ubuntu:focal
RUN echo SAST2022{Metaverse}

ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Asia/Shanghai

COPY files/sources.list /etc/apt/sources.list

RUN apt update\
    && apt install -y apt-utils openssh-server sudo zsh htop vim nano inetutils-ping python3 gcc g++ curl wget tmux unzip git mysql-server mysql-client nginx man \
    && echo "y\ny" | unminimize\
    && mkdir /run/sshd\
    && sh -c "$(wget https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O -)"

COPY files/hostname /etc/hostname
COPY files/mysqld.cnf /etc/mysql/mysql.conf.d/mysqld.cnf
COPY home /home

# Add user, config shell, set file permission
RUN useradd -m train\
    && useradd -m -G sudo nana\
    && useradd SAST2022{H0meLessOne}\
    && echo 'train:sast2022' | chpasswd\
    && echo 'nana:KawaiiNana_123' | chpasswd\
    && echo 'SAST2022{H0meLessOne}:a1b2c3d4f5' | chpasswd\
    && chsh train -s /usr/bin/zsh\
    && chsh nana -s /usr/bin/zsh\
    && chsh root -s /usr/bin/zsh\
    && chown nana:nana -R /home/nana\
    && chown train:train -R /home/train\
    && chmod -R 750 /home/nana\
    && chmod 440 /home/train/Puzzles/Storyteller/storyteller\
    && nginx -c /etc/nginx/nginx.conf\
    && nginx -s reload\
    && nginx -s stop\
    && service mysql start\
    && service mysql stop\
    && usermod -d /var/lib/mysql/ mysql\
    && chmod -R 777 /var/run/mysqld/
    


# Listen to sshd
CMD ["/usr/sbin/sshd", "-D", "-o", "ListenAddress=0.0.0.0"]

EXPOSE 22
EXPOSE 80
EXPOSE 443
EXPOSE 3306
EXPOSE 10001
EXPOSE 10002
