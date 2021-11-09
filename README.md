# External-IP-retriever

Python script that retrieves your external IP address from a source site
Script searches for the IP address based on the criteria of 4 sets of digits that are between 1-3 digits in one line of text and prints it.

This code has been developed for learning purposes using (re) regular expressions to find all matches and output them as string and (urllib.request) which accesses and retrieves data from the destination webpage.

The regular expression requests information back in a string form, the criteria for desired text (ipv4) is in the format of 4 blocks of between 1-3 numbers (78.19.215.10) - 4 octets
