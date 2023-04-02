import subprocess
import tkinter as tk

# Define the IP address, username, password, and hex key
ip_address = "IPADDR"
username = "USERNAME"
password = "PASSWORD"
hex_key = "HEXKEY"

# Define the fan speed command prefix
ipmitool_cmd_prefix = f"ipmitool -I lanplus -H {ip_address} -U {username} -P {password} -y {hex_key} raw 0x30 0x30 0x02 0xff"

# Create a function to send the fan speed command
def set_fan_speed(speed):
    # Construct the full fan speed command
    fan_speed_cmd = f"{ipmitool_cmd_prefix} {speed}"
    # Print the command to the console
    print(fan_speed_cmd)
    # Uncomment the following line to execute the command
    subprocess.run(fan_speed_cmd, shell=True)

# Create a function to start the server
def start_server():
    # Construct the command to start the server
    server_start_cmd = f"ipmitool -I lanplus -H {ip_address} -U {username} -P {password} -y {hex_key} power on"
    # Print the command to the console
    print(server_start_cmd)
    # Uncomment the following line to execute the command
    subprocess.run(server_start_cmd, shell=True)

# Create a function to stop the server
def stop_server():
    # Construct the command to stop the server
    server_stop_cmd = f"ipmitool -I lanplus -H {ip_address} -U {username} -P {password} -y {hex_key} power off"
    # Print the command to the console
    print(server_stop_cmd)
    # Uncomment the following line to execute the command
    subprocess.run(server_stop_cmd, shell=True)

# Create the main window
root = tk.Tk()

# Change the background color of the window
root.configure(bg="white")

# Create the buttons for different fan speeds
for i in range(1, 11):
    # Calculate the fan speed value
    fan_speed = i * 10
    # Create a button for the fan speed
    button = tk.Button(root, text=f"{fan_speed}%", font=("Arial", 12), bg="gray", fg="white", padx=10, pady=5, width=10, command=lambda s=fan_speed: set_fan_speed(s))
    # Calculate the row and column index for the button
    row_index = (i - 1) // 5
    col_index = (i - 1) % 5
    # Add the button to the grid
    button.grid(row=row_index, column=col_index, padx=5, pady=5)

# Create a button to start the server
start_button = tk.Button(root, text="Start Server", font=("Arial", 12), bg="green", fg="white", padx=10, pady=5, width=10, command=start_server)
start_button.grid(row=2, column=0, padx=5, pady=5)

# Create a button to stop the server
stop_button = tk.Button(root, text="Stop Server", font=("Arial", 12), bg="red", fg="white", padx=10, pady=5, width=10, command=stop_server)
stop_button.grid(row=2, column=1, padx=5, pady=5)

root.mainloop()
