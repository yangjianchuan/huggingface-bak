FROM selenium/node-chrome

ENV SE_SCREEN_WIDTH 1850
ENV PYTHONUNBUFFERED 1
ENV G4F_DIR /app
ENV G4F_LOGIN_URL http://localhost:7900/?autoconnect=1&resize=scale&password=secret
ARG G4F_VERSION
ENV G4F_VERSION ${G4F_VERSION}
ARG G4F_USER
ENV G4F_USER ${G4F_USER:-g4f}
ARG G4F_USER_ID
ENV G4F_USER_ID ${G4F_USER_ID:-1000}
ARG G4F_NO_GUI
ENV G4F_NO_GUI $G4F_NO_GUI
ENV HOME /home/$G4F_USER
ENV SE_DOWNLOAD_DIR $HOME/Downloads
ENV SEL_USER $G4F_USER
ENV SEL_UID $G4F_USER_ID
ENV SEL_GID $G4F_USER_ID

USER root

# Python packages
RUN apt-get -qqy update \
  && apt-get -qqy install \
    python3 \
    python-is-python3 \
    pip \
    git \
    nginx
    
RUN git clone https://github.com/xtekky/gpt4free.git /tmp/gpt4free

# Cleanup
RUN rm -rf /var/lib/apt/lists/* /var/cache/apt/* \
  && apt-get -qyy autoremove \
  && apt-get -qyy clean

# Update entrypoint
COPY supervisor.conf /etc/supervisor/conf.d/selenium.conf
COPY supervisor-gui.conf /etc/supervisor/conf.d/gui.conf


# If no gui
RUN if [ "$G4F_NO_GUI" ] ; then \
  rm /etc/supervisor/conf.d/gui.conf \
  ; fi

# Change background image
RUN cp /tmp/gpt4free/docker/background.png /usr/share/images/fluxbox/ubuntu-light.png

# Add user
RUN groupadd -g $G4F_USER_ID $G4F_USER
RUN useradd -rm -G sudo -u $G4F_USER_ID -g $G4F_USER_ID $G4F_USER

# Fix permissions
RUN mkdir "${SE_DOWNLOAD_DIR}"
RUN chown "${G4F_USER_ID}:${G4F_USER_ID}" $SE_DOWNLOAD_DIR /var/run/supervisor /var/log/supervisor
RUN chown "${G4F_USER_ID}:${G4F_USER_ID}" -R /opt/bin/ /usr/bin/chromedriver /opt/selenium/
RUN touch /var/log/nginx/error.log
RUN mkdir /var/lib/nginx/body /var/lib/nginx/proxy /var/lib/nginx/fastcgi /var/lib/nginx/uwsgi /var/lib/nginx/scgi
RUN chmod -R 755 /var/log/nginx/error.log /var/lib/nginx/body /var/lib/nginx/proxy /var/lib/nginx/fastcgi /var/lib/nginx/uwsgi /var/lib/nginx/scgi
RUN chown -R "${G4F_USER_ID}:${G4F_USER_ID}" /var/log/nginx/

# Switch user
USER $G4F_USER_ID

# Set the working directory in the container.
# Set the working directory in the container.
WORKDIR $G4F_DIR

# Copy the project's requirements file into the container.
RUN cp /tmp/gpt4free/requirements.txt /app/

COPY nginx.conf /app/nginx.conf

# Upgrade pip for the latest features and install the project's Python dependencies.
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the entire package into the container.
RUN cp -r /tmp/gpt4free/g4f /app/g4f

# Expose ports
EXPOSE 8000