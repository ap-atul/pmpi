# pmpi
Python Message Passing Interface using Pipe communication

A simple message passing between different process. Useful in scenarios
where the main process (UI) required output from long running process
(mostly progress bar/ logs).

Construct a communication, add your functions to be called on data 
received. 

## Get it
1. Install 
```console
pip3 install git+https://github.com/AP-Atul/pmpi
```

2. Clone and install
```console
git clone https://github.com/AP-Atul/pmpi.git
python3 setup.py install
```

## Usage

```python
from pmpi import Communication

# create comm object
comm = Communication()

# add an id and function
comm.register("my_sick_function", func_name)

# get the sender
sender = comm.sender()

# use that sender to send message using id anywhere
sender.send("my_sick_function", "very_secret_data")

# finally close the comm
comm.end()
```
