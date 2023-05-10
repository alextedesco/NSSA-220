#!/bin/bash


num_rands=$1

min=$2

max=$3

i=1

avg=0

rm rands_$num_rands.txt

num_writer () {
  echo $1 >> rands_$num_rands.txt
}

random_numbers () {
  if [ -z $min ]
   then
     min=$((1))
  fi

  if [ -z $max ]
   then
     max=$((32767))
  fi
 
  while [ $i -le $num_rands ]
  do
  randomNumber=$(shuf -i $min-$max -n 1)
  num_writer $randomNumber
  avg=$((avg + $randomNumber))
    ((i++))
  done
  avg=$((avg / $num_rands))
  minNum=$(sort -n rands_$num_rands.txt | head -1)
  maxNum=$(sort -n rands_$num_rands.txt | tail -1)
  echo "You requested " $num_rands "numbers [between "$min "and" $max"]"
  echo "The smallest value generated was" $minNum
  echo "The largest value generated was" $maxNum
  echo "The average value generated was" $avg
}

random_numbers




