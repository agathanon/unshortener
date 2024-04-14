IMAGE_NAME=unshortener-api
CONTAINER_NAME=unshortener

build:
	docker build -t $(IMAGE_NAME) .
run:
	docker run --name $(CONTAINER_NAME) -d $(IMAGE_NAME)
stop:
	docker stop $(CONTAINER_NAME)
clean:
	docker rm $(CONTAINER_NAME)

clean-image:
	docker rmi $(IMAGE_NAME)