# Python sample app using poetry package manager

## Building on 18.04

`pack build poetry-sample --buildpack paketo-buildpacks/python --builder paketobuildpacks/builder:buildpackless-base`

## Building on 18.04

`pack build poetry-sample --buildpack paketo-buildpacks/python --builder paketobuildpacks/builder-jammy-buildpackless-base`

## Running

`docker run --interactive --tty --env PORT=8080 --publish 8080:8080 poetry-sample`

## Viewing

`curl http://localhost:8080`
