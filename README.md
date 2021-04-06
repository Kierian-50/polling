Polling file 
=============

Originally polling is a powerful python utility used to wait for a function to return a certain expected condition.
Some possible uses cases include:

- Wait for API response to return with code 200
- Wait for a file to exist (or not exist)
- Wait for a thread lock on a resource to expire

Here, I rewrite the code to be use in the context of listening the ttys0's file and stop the polling when the user
want to stop. This is why I rewrite the code: it's wasn't possible to stop the polling with a command but only with a 
timeout or a number of try and this is what I did using python object.

### So, the version that I rewrite is useful to listen a file and stop the polling when you want and not with a timeout.

# Examples

### Example: As an example I will simply show the way that I use it

```python
from polling import Polling

class test:
    
    def __init__(self):
        self.file_handle = Polling()
        self.file_to_read = open('/dev/ttsy0', 'r', encoding="utf8", errors='ignore')

    def target(self):
        """The method that the polling will execute"""
        line = self.file_to_read.readline()
        print(line)
    
    def main(self):
        """Main method"""
        self.file_handle.poll(
            lambda: test.target(self),  # Method which says what to do,
            poll_forever=True)
    
    def kill(self):
        """Stop the polling"""
        if self.file_handle is not None:
            self.file_handle.stop = True # Stop the polling
        print("Ant this is the end !")
```

Hope that it can be useful for someone !
