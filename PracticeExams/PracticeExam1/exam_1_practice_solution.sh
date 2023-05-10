#!/bin/bash

# Create a temporary file with the header line removed
tail -n +2 grades.txt > temp_file.txt

CLASS_SUM=0
NUM_STUDENTS=0

# Iterate over each line of the file, excluding the header
while read -r line
do

  # Increment the total number of students, which is needed to calculate
  # the class average.
  NUM_STUDENTS=$(( $NUM_STUDENTS + 1 ))

  # Grab the student's name in case we need to print a message
  STUDENT_NAME=$(echo $line | cut -f 1,2 -d ' ')

  # Grab the grade for each assignment using cut
  ASSIGNMENT_1=$(echo $line | cut -f 3 -d ' ')
  ASSIGNMENT_2=$(echo $line | cut -f 4 -d ' ')
  ASSIGNMENT_3=$(echo $line | cut -f 5 -d ' ')
  ASSIGNMENT_4=$(echo $line | cut -f 6 -d ' ')

  # Calculate the average
  STUDENT_AVERAGE=$(( $ASSIGNMENT_1 + $ASSIGNMENT_2 + $ASSIGNMENT_3 + $ASSIGNMENT_4 ))
  STUDENT_AVERAGE=$(( $STUDENT_AVERAGE / 4 ))

  # Add the student's average to the class sum
  CLASS_SUM=$(( $CLASS_SUM + $STUDENT_AVERAGE ))

  # Check to see if the student's grade falls within the two parameters and output
  # a message as needed
  if [ $STUDENT_AVERAGE -lt 75 ]
  then
    echo "Warning, student $STUDENT_NAME has an average of $STUDENT_AVERAGE%"
  elif [ $STUDENT_AVERAGE -gt 85 ]
  then
    echo "Congrats, student $STUDENT_NAME has an average of $STUDENT_AVERAGE%"
  fi

done < temp_file.txt # This redirection passes the temporary file to the read command

# Determine the class average
CLASS_AVERAGE=$(( $CLASS_SUM / $NUM_STUDENTS ))

echo "The class average is $CLASS_AVERAGE"

# Remove the temporary file
rm temp_file.txt
