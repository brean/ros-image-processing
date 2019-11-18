include .env
export

up:
	docker-compose up -d
	if [ -f "/usr/bin/terminator" ] ; \
		then \
			make term; \
		fi ;

term:
	terminator -g terminator.conf -l ros-img-proc &

down:
	docker-compose down
