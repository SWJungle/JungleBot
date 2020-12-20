import requests

def main() :
    ## webhook url
    url = "https://hooks.slack.com/services/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"
    
    text = "Jungle Bot First Messsage."
    
    payload = {
        "text": text
    }
    
    requests.post(url, json=payload)
    
#! this script using main function.
if __name__ == "__main__" :
    main()
