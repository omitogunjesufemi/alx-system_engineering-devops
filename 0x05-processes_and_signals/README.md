# 0x05. Processes and signals

This project helped to understand:
- What is a PID
- What is a process
- How to find a process’ PID
- How to kill a process
- What is a signal
- What are the 2 signals that cannot be ignored

TASK | DESCRIPTION
--- | ---
`0-what-is-my-pid` | Bash script that displays its own PID.
`1-list_your_processes` | Bash script that displays a list of currently running processes.
`2-show_your_bash_pid` | Bash script that displays lines containing the bash word, thus allowing you to easily get the PID of your Bash process.
`3-show_your_bash_pid_made_easy` | Bash script that displays the PID, along with the process name, of processes whose name contain the word `bash`
`4-to_infinity_and_beyond` | Bash script that displays To infinity and beyond indefinitely
`5-dont_stop_me_now` | Bash script that stops `4-to_infinity_and_beyond` process
`6-stop_me_if_you_can` | Bash script that stops `4-to_infinity_and_beyond` process without `kill` or `killall`
`7-highlander` | Bash script that displays I am invinciblels! when receiving a SIGTERM signal
`8-beheaded_process` | Bash script that kills the process 7-highlander
`100-process_and_pid_file` | Determine process and save PID to file
