#!/bin/bash

# APM Tool Overview:

# You’ll be writing an APM tool in Bash that will monitor a mix of processes in the form of executable programs written in C
# The script will start the processes, collect performance metrics, and perform a clean up at the end to kill these processes and any other processes that your script spawns

#-----------------------------------------------------

# Checklist:

# Tool collects process and system level metrics every 5 seconds 

# Tool collects %CPU and %memory utilization per process using ps

# Tool collects RX and TX data rates (in kB/qs) with a sampling interval of 1 second using ifstat

# Tool collects hard disk writes (in kB/s) to sda using iostat 

# Tool collects hard disk utilization on “/” in MB available using df 

# Tool outputs CPU and memory metrics to a CSV file specific to that process (<proc_name>_metrics.csv) with the format <seconds>, <%CPU>, <%memory>

# Tool writes all system level metrics to a file called system_metrics.csv with the format <seconds>, <RX data rate>, <TX data rate>, <disk writes>, <available disk capacity>

# Tool spawns all application processes

# Tool kills all application processes and any other processes it spawns in an exit trap function called cleanup

# Tool includes at least three functions that (1) spawn all applications and other processes, (2) collect system level metrics, (3) collect process level metrics

# Report showing results from a 15 minute run of the APM tool *In class Crittelli said 5 mins*

# Team submission not in a single zip file and/or missing any of the following items: the APM tool script, a report with the Excel plots included, and all output files create

# Provided Excel plot template and/or report template is not used

# Poor teamwork (assessed on an individual basis)

#-----------------------------------------------------

# Notes:
# Use ps or top for CPU%, Memory%
# Use iostat for Hard Disk Access Rates
# Use df for Hard Disk Utilization

# Time (in seconds)
timer=5
ip_address=127.0.0.1

rm system_metrics.csv 2> /dev/null || true 
rm APM1_metrics.csv 2> /dev/null || true 
rm APM2_metrics.csv 2> /dev/null || true 
rm APM3_metrics.csv 2> /dev/null || true 
rm APM4_metrics.csv 2> /dev/null || true 
rm APM5_metrics.csv 2> /dev/null || true 
rm APM6_metrics.csv 2> /dev/null || true 

touch system_metrics.csv
touch APM1_metrics.csv
touch APM2_metrics.csv
touch APM3_metrics.csv
touch APM4_metrics.csv
touch APM5_metrics.csv
touch APM6_metrics.csv

#Starts ifstat sampling 
ifstat -d 1 2> /dev/null

cleanup () {
  kill $PID1
  kill $PID2
  kill $PID3
  kill $PID4
  kill $PID5
  kill $PID6
}
trap cleanup exit

cpu_memory_percentage () {
  cpu=$( ps au | grep APM$1 | head -n 1 | xargs | sed 's/ /,/g' | cut -f 3 -d ',' )
  memory=$( ps au | grep APM$1 | head -n 1 | xargs | sed 's/ /,/g' | cut -f 4 -d ',' )
  echo $2, $cpu, $memory >> APM$1_metrics.csv
  #Output each to csv file [ >> APM#.csv ]
}

system_level () {
 RX_data_rate=$( ifstat ens160 | tail -n 2 | head -n 1 | xargs | cut -f 6 -d ' ' )
 TX_data_rate=$( ifstat ens160 | tail -n 2 | head -n 1 | xargs | cut -f 8 -d ' ' )
 disk_writes=$( iostat -x nvme0n1 | tail -n 2 | xargs | cut -f 4 -d ' ' )
 avalible_space=$( df / | tail -n 1 | xargs | cut -f 4 -d ' ' )
 echo $1, $RX_data_rate, $TX_data_rate, $disk_writes, $avalible_space >> system_metrics.csv
}

main () {
  ./executables/APM1 $ip_address &
   PID1=$( ps au | grep APM1 | head -n 1 | xargs | sed 's/ / /g' | cut -f 2 -d ' ' )
  ./executables/APM2 $ip_address &
   PID2=$( ps au | grep APM2 | head -n 1 | xargs | sed 's/ / /g' | cut -f 2 -d ' ' )
  ./executables/APM3 $ip_address &
   PID3=$( ps au | grep APM3 | head -n 1 | xargs | sed 's/ / /g' | cut -f 2 -d ' ' )
  ./executables/APM4 $ip_address &
   PID4=$( ps au | grep APM4 | head -n 1 | xargs | sed 's/  / /g' | cut -f 2 -d ' ' )
  ./executables/APM5 $ip_address &
   PID5=$( ps au | grep APM5 | head -n 1 | xargs | sed 's/  / /g' | cut -f 2 -d ' ' )
  ./executables/APM6 $ip_address &
   PID6=$( ps au | grep APM6 | head -n 1 | xargs | sed 's/ / /g' | cut -f 2 -d ' ' )
  while [ $timer -le 300 ]
  # Checks if it has been 5-minutes
  do
    # Collect performance metric
    count=1
    while [ $count -le 6 ]
      do
        cpu_memory_percentage $count $timer
	count=$(( $count + 1 ))
      done
	
    system_level $timer
    timer=$(( $timer + 5 ))
    sleep 5

  done
  exit 1
}

main 
