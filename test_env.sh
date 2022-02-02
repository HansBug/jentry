#!/bin/bash

if [ -e 'demo/oo_course_2019_17373331_homework_2' ]; then
  echo "Code from hdl has already exist."
else
  mkdir -p demo
  cd demo
  git clone https://github.com/HansBug/oo_course_2019_17373331_homework_2.git
  cd ..
fi

if [ -e 'demo/2018_spring_16061104_10' ]; then
  echo "Code from the fxxking hansbug has already exist."
else
  mkdir -p demo
  cd demo
  git clone https://github.com/HansBug/2018_spring_16061104_10.git
  cd ..
fi

export DEMO_PROJECT_PATH=demo/oo_course_2019_17373331_homework_2
export DEMO_COMPLEX_PROJECT_PATH=demo/2018_spring_16061104_10
export DEMO_ALL_PROJECT_PATH=demo
