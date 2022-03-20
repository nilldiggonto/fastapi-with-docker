FROM drupal:8.2

RUN apt-get update && apt-get install -y git \ 
    && rm -rf /var/lib/apt/lists/*

WORKDIR /var/www/html/themes/

RUN git clone  --single-branch --depth 1 https://github.com/drupal/drupal.git \
    && chown -R www-data:www-data bootstrap

WORKDIR /var/www/html