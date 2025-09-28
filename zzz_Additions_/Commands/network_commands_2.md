# Ranked Linux Network Commands Cheat Sheet

| Rank | Command    | Description | Performance Notes | Effectiveness Notes | Best Use Case |
|------|-----------|-------------|------------------|-------------------|---------------|
| 1    | tcpdump   | Packet analyzer for capturing and analyzing network traffic | Lightweight, but CPU-intensive with heavy traffic | Captures raw packets, supports complex filters (e.g., `tcpdump -i eth0 port 80`) | Deep packet inspection, protocol debugging |
| 2    | ss        | Modern replacement for netstat, shows socket and connection details | Lower overhead than netstat, quick execution | Accurate socket stats, filters by state (e.g., `ss -tuln`) | Connection and socket analysis |
| 3    | iftop     | Real-time bandwidth monitoring with host-level granularity | Moderate resource usage, efficient for live monitoring | Shows per-connection bandwidth (e.g., `iftop -i eth0`) | Live traffic by source/destination |
| 4    | nethogs   | Monitors bandwidth usage per process, not just interfaces | Low CPU usage, focused on process-level data | Identifies apps consuming bandwidth (e.g., `nethogs eth0`) | Finding bandwidth-hogging processes |
| 5    | mtr       | Combines ping and traceroute for continuous network diagnostics | Lightweight, runs efficiently in real-time | Real-time hop-by-hop latency/loss (e.g., `mtr google.com`) | Persistent network path analysis |
| 6    | ip        | Modern tool for interface, routing, and link stats, replacing ifconfig | Very fast, minimal resource usage | Detailed network config (e.g., `ip addr`, `ip link`) | Interface and routing diagnostics |
| 7    | vnstat    | Tracks historical network traffic with daily/monthly summaries | Minimal overhead, runs in background | Tracks daily/monthly usage (e.g., `vnstat -i eth0`) | Long-term bandwidth monitoring |
| 8    | nload     | Displays real-time incoming/outgoing traffic with graphs | Moderate CPU usage due to graphical output | Visualizes traffic rates (e.g., `nload eth0`) | Quick bandwidth usage overview |
| 9    | ping      | Tests connectivity to a host using ICMP packets | Near-zero resource usage, instant execution | Measures packet loss/latency (e.g., `ping -c 4 google.com`) | Basic host reachability checks |
| 10   | traceroute | Tracks packet paths to a destination, showing hops and latency | Lightweight, but single-run, not continuous | Shows hop-by-hop routing (e.g., `traceroute google.com`) | Diagnosing routing issues |
| 11   | netstat   | Displays network connections, routing tables, and interface statistics | Higher overhead than ss, slower on busy systems | Lists connections/ports (e.g., `netstat -tulpn`) | Basic connection monitoring |
| 12   | ifconfig  | Displays network interface details (IP, MAC, status) | Moderate overhead, outdated compared to ip | Basic interface info (e.g., `ifconfig eth0`) | Simple interface checks |
