#!/usr/bin/bash

LOG_FILE="$HOME/Desktop/project.log"
DISK_THRESHOLD=80
HOSTNAME=$(hostname)

BACKUP_DIR="$HOME/Desktop/backups"
IMPORTANT_FILES="$HOME/Desktop/Flask_project"


log_message(){
    echo "$(date '+%Y-%m-%d %H:%M:%S') - $1" >> "$LOG_FILE"
}
space(){
    echo " " >> "$LOG_FILE"
}

# 1. Disk Usage Monitoring
disk_monitoring(){
    log_message "Starting Disk Usage Monitoring.."
    DISK_USAGE=$(df -P "$HOME" | awk 'NR==2 {gsub("%","",$5); print $5}')
    if [ -z "$DISK_USAGE" ]; then
       log_message "Error: could not retrieve disk usage"
       exit 1
    fi
    
    if [ "$DISK_USAGE" -gt "$DISK_THRESHOLD" ]; then
         ALERT_MSG="Alert: Disk usage on $HOSTNAME exceeds $DISK_THRESHOLD% (Current: $DISK_USAGE%)"
         log_message "$ALERT_MSG"
    else
         log_message "Disk usage is normal: $DISK_USAGE%"
    fi 
    log_message "Disk Usage Monitoring is Completed"
    space
}

# 2. CPU and Memory Monitoring
cpu_memory_monitoring(){
    log_message "Starting CPU and Memory Monitoring"
    CPU_USAGE=$(top -bn2 | grep "Cpu(s)" | tail -n1 | awk '{print $2 + $4}')
    MEM_USAGE=$(free -h | grep Mem | awk '{print $3 "/" $2 " (" int($3/$5*100) "%)"}')
    log_message "CPU Usage: $CPU_USAGE%"
    log_message "Memory Usage: $MEM_USAGE"
    space
}

# 3. Top Processes (Top 5 memory-consuming)
top_processes(){
   log_message "Top 5 Memory-Consuming Processes:"
   ps -eo pid,ppid,cmd,%mem,%cpu --sort=-%mem | head -n 6 >> "$LOG_FILE"
   space
}

# 4. system updates
system_updates(){
     log_message "Starting System Updates Checking..."
     if command -v apt &> /dev/null; then
        apt update > /dev/null 2>&1
        UPDATES=$(apt list --upgradable 2>/dev/null | wc -l)
        ((UPDATES--))  # Subtract header line
        log_message "Available updates: $UPDATES"
    else
        log_message "Error.. While Cheking System Updates."
    fi
    space
}

# 5. backup files
backup_files(){
    log_message "Starting Backup.."
    mkdir -p "$BACKUP_DIR"
    TIMESTAMP=$(date '+%Y%m%d_%H%M%S')
    BACKUP_FILE="$BACKUP_DIR/backup_$TIMESTAMP.tar.gz"
    tar -czf "$BACKUP_FILE" $IMPORTANT_FILES 2>> "$LOG_FILE"
    if [ $? -eq 0 ]; then
        log_message "Backup successful: $BACKUP_FILE"
        du -sh "$BACKUP_FILE" >> "$LOG_FILE"
    else
        log_message "Backup failed!"
    fi
    space
}

log_message "System Health Check Started on $HOSTNAME"
disk_monitoring
cpu_memory_monitoring
top_processes
system_updates
backup_files
log_message "System Health Check Completed."
