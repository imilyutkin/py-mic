FROM node:carbon

WORKDIR /app

COPY package.json /app/

RUN npm install

COPY ./ /app/

ARG env=prod
RUN npm run build --prod --environment $env

FROM nginx
COPY --from=0 /app/dist/ /usr/share/nginx/html
COPY ./nginx-custom.conf /etc/nginx/conf.d/default.conf
