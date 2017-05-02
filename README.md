## Sonorus: speech-to-text service and filler detector
### Requirements
pip install -r requirements.txt  

### How to Run:
In the root folder  
```
export FLASK_APP=server
```
For debug mode:  
```
export FLASK_DEBUG=TRUE
```
To run  
```
flask run
```

### API calls
For speech recognition  
```
http://127.0.0.1/trans
```

For filler detection  
Reduce the time frame when sample the raw audio data.  



