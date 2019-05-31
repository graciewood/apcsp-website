#!/bin/bash

echo -e "Content type: text/html\n\n"

echo "<h1>Status of Raspberry Pis</h1>"

echo "<h2>Which Raspberry Pis are active?</h2>"

echo "<pre>$(./rpistatus)</pre>"
