#!/bin/bash

comm -23 <(sort $1) <(sort $2) > $3
