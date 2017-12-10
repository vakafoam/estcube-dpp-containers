# Create image based on the official Node 6 image from dockerhub
FROM node:latest

# Create app directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Install app dependencies
COPY package.json /usr/src/app/
RUN npm install

# Bundle app source
COPY . /usr/src/app

# Expose the port the app runs in
EXPOSE 8200

# Serve the app
CMD [ "npm", "start" ]