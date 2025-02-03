#!/usr/bin/env bash
source ~/.bashrc
DIRECTORY=.profile-fusion-api
deactivate 2> /dev/null
if [ -d "${DIRECTORY}" ]; then
    source ${DIRECTORY}/bin/activate
else
    virtualenv -p `which python3.11` ${DIRECTORY}
    source ${DIRECTORY}/bin/activate
fi

# export APP_NAME="profile-fusion-api"
# export APP_ENV="dev"