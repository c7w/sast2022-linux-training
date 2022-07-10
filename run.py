PORT_MAPPING = {
    0: 22,
    1: 80,
    2: 3306,
    3: 10001,
    4: 10002
}

BASE_PORT = 40000

if __name__ == "__main__":
    for k in range(10):
        port_string = " ".join([f"-p {BASE_PORT + k * 5 + relative_port }:{container_port}" for relative_port, container_port in PORT_MAPPING.items()])
        command = f"docker run -d {port_string} -h SAST2022-Training --storage-opt size=10G cc7w/linux-training:v7" 
        print(command)
