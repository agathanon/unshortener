# Unshortener Extension Makefile
SRC_DIR := src
BUILD_DIR := build
EXTENSION_NAME := unshortener
VERSION := $(shell jq -r '.version' $(SRC_DIR)/manifest.json)
ZIP_FILE := $(EXTENSION_NAME)-$(VERSION).zip

all: zip
zip:
	@mkdir -p $(BUILD_DIR)
	zip -r $(BUILD_DIR)/$(ZIP_FILE) $(SRC_DIR) -x "*.DS_Store"
clean:
	rm -rf $(BUILD_DIR)

.PHONY: all zip clean