import json
import requests

class NotionClient:
    def __init__(self,token,database) -> None:
        self.database= database
        self.headers = {
            "Authorization": "Bearer" + token,
            "Content-Type": "application/json",
            "Notion-Version": "2021-08-16" 
        }

        def create_page(self,task, date, status):
            create_url = "https://api.notion.com/v1/pages"
            data = {
            "parent": { "database_id": "self.database" },
            "properties": {
                "Task": {
                    "title": [
                        {
                            "text": {
                                "content": task
                            }
                        }
                    ]
                },
                "Date": {
                    "date": [
                        {
                            "start":date,
                            "end":None
                        }
                    ]
                },
                "Status": {
                    "rich_text": [
                        {
                            "text": {
                                "content": status
                            }
                        }
                    ]
                }
            }}

            data = json.dumps(data)
            res = requests.post(create_url, headers = self.headers, data=data)
            print(res.status_code)
            return res
            
            

