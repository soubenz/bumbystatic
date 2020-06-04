FROM node:12-alpine AS builder

# Install build tools
RUN apk update && apk upgrade
RUN apk --no-cache add --virtual native-deps git\
    g++ gcc libgcc libstdc++ linux-headers make python3-dev 

# Manually change npm's default directory
# to avoid permission errors
# https://docs.npmjs.com/resolving-eacces-permissions-errors-when-installing-packages-globally
ENV NPM_CONFIG_PREFIX=/home/node/.npm-global


# Install the application
COPY --chown=node:node ./ /home/node/app/
WORKDIR /home/node/app
RUN pip3 install -r requirements.txt
# Install Gridsome globally
USER node
RUN npm i -g netlify-cli
RUN npm i -g gridsome
USER node
RUN npm cache clean --force
RUN npm clean-install
# RUN cd .. && \
#     mv app/node_modules ./ && \
#     rm -rf app && \
#     mkdir app && \
#     mv node_modules app/

# Build
# WORKDIR /home/node/app
# CMD ~/.npm-global/bin/gridsome build && python
CMD uvicorn --host 0.0.0.0 build:app --reload 
# FROM node:12-alpine
# # Remove the project files
# # but keep the node modules
# WORKDIR /home/node
# USER node
# RUN mkdir build .npm-global
# COPY --from=builder /home/node/build/node_modules build/node_modules
# COPY --from=builder /home/node/.npm-global .npm-global
# ENV NETLIFY_AUTH_TOKEN=e5d08bdff52eac5fbf7c7abf3dab49edb69dd7b2abd79b22f042612663108c33
# # Get the source code without node_modules
# # Then build the site
# CMD cp -r app temp && \
#     rm -rf temp/node_modules && \
#     cp -r temp/* build/ && \
#     cd build && \
#     ~/.npm-global/bin/netlify build