FROM node:10.17-slim as build-stage
WORKDIR /app
COPY package*.json ./
ENV VUE_APP_API_PATH='localhost' \
    VUE_APP_API_PORT='5000' \
    VUE_APP_API_PROTOCOL='http'
RUN npm install
COPY ./ .
RUN npm run build

FROM nginx as production-stage
RUN mkdir /app
COPY --from=build-stage /app/dist /app
COPY nginx.conf /etc/nginx/nginx.conf
