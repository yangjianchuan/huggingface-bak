FROM debian:sid
RUN useradd -m -u 1000 user
RUN chown root:shadow /etc/shadow
RUN apt update
RUN apt install -y xfce4-terminal \
lxqt lightdm xfce4-goodies \
xfce4-appmenu-plugin \
xfce4-eyes-plugin \
xfce4-indicator-plugin \
xfce4-mpc-plugin  \
aqemu \
sudo \
curl \
wget \
aria2 \
qemu-system-x86 \
htop \
chromium \
screen \
tigervnc-standalone-server \
python3-pip \
python3-websockify \
python3 \
git \
fuse \
libfuse2 \
xdotool
RUN git clone https://github.com/novnc/noVNC.git noVNC
RUN mkdir -p /home/user/.vnc
ARG VNC_RESOLUTION
RUN --mount=type=secret,id=VNC_PASSWORD,mode=0444,required=true \
   echo 'user:$(cat /run/secrets/VNC_PASSWORD)' | chpasswd && \
   cat /run/secrets/VNC_PASSWORD | vncpasswd -f > /home/user/.vnc/passwd
RUN chmod -R 777 /home/user/.vnc /tmp
ENV HOME=/home/user \
    PATH=/home/user/.local/bin:$PATH
CMD vncserver -SecurityTypes VncAuth -rfbauth /home/user/.vnc/passwd -geometry $VNC_RESOLUTION && ./noVNC/utils/novnc_proxy --vnc localhost:5901 --listen 0.0.0.0:7860