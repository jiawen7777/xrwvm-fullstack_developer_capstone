FROM node:18.12.1-bullseye-slim

RUN npm install -g npm@9.1.3

RUN apt update && apt upgrade -y && apt install curl -y


ADD package.json .
ADD app.js .
ADD review.js .
ADD dealership.js .
ADD data/dealerships.json .
ADD data/reviews.json .
COPY . .
RUN npm install

EXPOSE 3030

CMD [ "node", "app.js" ]
