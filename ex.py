from pmpi import Communication

if __name__ == '__main__':

    class Some:

        def my_func(self, name):
            print(name)

    comm = Communication()
    comm.register("IDENTIFIER", Some().my_func)
    sendr = comm.sender()

    sendr.send("IDENTIFIER", "data")

    from time import sleep
    sleep(0.5)
    comm.end()
