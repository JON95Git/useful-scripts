#!/bin/bash

# You need to pass the parameters by command line
# ./sft_upload.sh p@$$word 22 username sftp_server /tmp

PASSWORD=$1
PORT=$2
USERNAME=$3
SFTP_SERVER=$4
REMOTE_PATH=$5
FILE=/tmp/file_path/file_name

sshpass -p "$PASSWORD" sftp -o Port=$PORT -o StrictHostKeyChecking=no $USERNAME@$SFTP_SERVER:$REMOTE_PATH <<< $'put '$FILE
