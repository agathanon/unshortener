IMAGE_NAME=unshortener-api
CONTAINER_NAME=unshortener
CONTAINER_PORT=8000

build:
	docker build -t $(IMAGE_NAME) .
run:
	docker run --name $(CONTAINER_NAME) -d -p $(CONTAINER_PORT):8000 $(IMAGE_NAME)
stop:
	docker stop $(CONTAINER_NAME)
clean:
	docker rm $(CONTAINER_NAME)

clean-image:
	docker rmi $(IMAGE_NAME)