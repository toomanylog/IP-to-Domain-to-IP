
# IP-to-Domain-to-IP

Tools for resolving IP to domain names and vice versa. Two modules, IP to Domain and Domain to IP. Accepts HTTP/S proxies and thread management.

Choose your simple module by entering the given number then press enter.
- 1 for IP to Domain
- 2 for Domain to IP

The default value for threads is 50.
Proxies are optional, you can enter "n" to refuse to use them.

You can show the progress of the real-time check in the console.

At the end of the script you will get the total time your verification took and you can choose to return to the script home (during module selection) or exit the script.

The result files are created in the folder corresponding to the module and according to the following format:

```module_%Y-%m-%d_%H-%M-%S_valid_results.txt```

One IP/Domain/Proxy per line.

Example of formatting:
- For domains: domain.com
- For proxies: 0.0.0.0:0000
- For IP lists: 0.0.0.0

## Screenshots

![App Screenshot](https://i.ibb.co/GtJZn5c/001.png)
