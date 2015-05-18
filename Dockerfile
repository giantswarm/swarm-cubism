FROM phusion/baseimage
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update -qq && \
	apt-get install -y -q --no-install-recommends \
	python2.7 python-pip build-essential python-dev

RUN pip install Flask Flask-Cache requests redis

ADD entrypoint.sh /app/entrypoint.sh
ADD server.py /app/server.py
ADD config.py /app/config.py
ADD giantswarm /app/giantswarm/
ADD templates /app/templates/
ADD static /app/static/

RUN chmod u+x /app/entrypoint.sh

EXPOSE 5000

ENTRYPOINT ["/app/entrypoint.sh"]
CMD ["python", "-u", "/app/server.py"]

