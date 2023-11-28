
class SetInterface:
    def read_interface(conf_file):
        try:
            with open(conf_file, "r") as file:
                lines = file.readlines()
                for line in lines:
                    if 'interface=' in line:
                        return line.split('=')[1]
        except NotImplementedError:
            print("Interface field is not implemented in conf file")
