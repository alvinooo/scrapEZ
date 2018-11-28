#!/bin/bash

kill -9 `ps | grep hrome | awk '{print $1}'`