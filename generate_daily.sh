#!/bin/bash
KEYWORD="wireless earbuds"
DATE=$(date +%F)
curl "http://localhost:5000/generate?keyword=${KEYWORD}" -o "generated_posts/${KEYWORD// /_}_${DATE}.json"
