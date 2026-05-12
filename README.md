--------| Power consumption graph |--------

- Object of project: 
    Monitoring real-time power consumption.

- Solution: 
    Getting data from a ghost Shelly plug written in Phyton and displaying it in Grafana as a clear graph. MQTT is used as the transport layer, Telegraf as a translator between broker and database, InfluxDB as a database that is storring wattage data over time, Docker as a folder in which everything lives, this maintains environment consistency and provides a great structure for sharing the entire project.

- Tech that I used: 
    - Gemini, 
    - Docker, 
    - Mosquitto MQTT, 
    - Python, 
    - Telegraf, 
    - InfluxDB, 
    - Grafana.

- Configuration (Security)
    - Find the ".env.example" file,
    - Create a copy named ".env",
    - Generate an API Token in your InfluxDB instance and paste it into the ".env" file,
    - Create a "password.txt" for Mosquitto authentication (Refer to "mosquitto.conf")

- How to execute the project in Command Prompt:
    - docker copose up -d
    - pip install paho-mqtt
    - python sim_plug.py
    - Navigate to localhost:3000 to see the dashboard (Grafana)

- Security aspect:
    - Authentication: 
        The broken wasn't left open. I used a password file for Mosquitto.
    - Tokens:
        I used API Tokens for InfluxDB instead of hardcoding my admin password in the config file.
    - Separating areas:
        Each part of a project runs on its own container. That means when one crashes the others can continue running.    
