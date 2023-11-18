def data_factoriser():
    with open("data/dataFactoriser.txt", "r") as file:
        line = file.readline().strip()
    if line == "1":
        with open("data/dataFactoriser.txt", "w") as file:
            file.write("0\n")
    else:
        with open("data/dataFactoriser.txt", "w") as file:
            file.write("1\n")
def data_light():
    with open("data/dataLight.txt", "r") as file:
        line = file.readline().strip()
    if line == "1":
        with open("data/dataLight.txt", "w") as file:
            file.write("0")
    else:
        with open("data/dataLight.txt", "w") as file:
            file.write("1")
def data_delta():
    with open("data/dataDelta.txt", "r") as file:
        line = file.readline().strip()
    if line == "1":
        with open("data/dataDelta.txt", "w") as file:
            file.write("0")
    else:
        with open("data/dataDelta.txt", "w") as file:
            file.write("1")
def data_options():
    with open("data/dataOptions.txt", "r") as file:
        line = file.readline().strip()
    if line == "1":
        with open("data/dataOptions.txt", "w") as file:
            file.write("0")
    else:
        with open("data/dataOptions.txt", "w") as file:
            file.write("1")
def data_menu():
    with open("data/dataMenu.txt", "r") as file:
        line = file.readline().strip()
    if line == "1":
        with open("data/dataMenu.txt", "w") as file:
            file.write("0")
    else:
        with open("data/dataMenu.txt", "w") as file:
            file.write("1")
def data_hist():
    with open("data/dataHistorique.txt", "r") as file:
        line = file.readline().strip()
    if line == "1":
        with open("data/dataHistorique.txt", "w") as file:
            file.write("0")
    else:
        with open("data/dataHistorique.txt", "w") as file:
            file.write("1")
