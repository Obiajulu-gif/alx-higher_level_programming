#!/bin/bash
# send a get request to a given URL with a given URL with a header varaiable
curl -sH "X-School-User-Id: 98" "${1}"
