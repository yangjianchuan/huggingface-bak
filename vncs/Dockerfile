FROM debian:sid
RUN apt update
RUN useradd -m -u 1000 user
RUN apt install xfce4-terminal lxde aqemu sudo curl wget aria2 qemu-system-x86 htop chromium screen tigervnc-standalone-server python3-pip python3-websockify python3 git -y
RUN git clone https://github.com/novnc/noVNC.git noVNC
RUN mkdir -p /home/user/.vnc
ARG VNC_PWD
ARG VNC_RESOLUTION
RUN --mount=type=secret,id=VNC_PWD,mode=0444,required=true \
    cat /run/secrets/VNC_PWD | vncpasswd -f > /home/user/.vnc/passwd
RUN chmod -R 777 /home/user/.vnc /tmp 
ENV HOME=/home/user \
    PATH=/home/user/.local/bin:$PATH
CMD vncserver -SecurityTypes VncAuth -rfbauth /home/user/.vnc/passwd -geometry $VNC_RESOLUTION && ./noVNC/utils/novnc_proxy --vnc localhost:5901 --listen 0.0.0.0:7860