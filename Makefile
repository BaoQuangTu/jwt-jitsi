install:
	pip3 install -r requirements.txt

run:
	-./tmp pkill -9 python3
	nohup python3 src/app.py > /log.out &