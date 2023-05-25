#!/bin/bash

rm -r $1
mkdir $1
chown $2 $1
echo done