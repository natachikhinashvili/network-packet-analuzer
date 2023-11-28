class SetInterface:
    def read_interface(conf_file):
        interface=""
        try:
            with open(conf_file, "r") as file:
                lines = file.readlines()
                for line in lines:
                    if 'interface=' in line:
                        interface = line.split('=')[1]
                        interface = interface.strip()
        except NotImplementedError:
            print("Interface field is not implemented in conf file")
        return interface