import os
import requests
from simple_term_menu import TerminalMenu
import webbrowser

def News():
     # Getting the news data
     data=[]
     try:
          resp  = requests.get(f"https://newsapi.org/v2/everything?q=Apple&from=2021-12-15&sortBy=popularity&apiKey={os.getenv('API_KEY')}") # Use your API KEY here
          d=resp.json()


          # Getting the news title and url in json and appending to the data list
          for i in d['articles']:
               json_data={i['title']:i['url']}
               data.append(json_data)


          # Adding Options
          options=['Quit']
          for i in d['articles']:
               options.append(i['title'])


          mainMenu=TerminalMenu(options)
          quitting=False


          # Functionality of the Options
          while quitting ==False:
               optionsIndex=mainMenu.show()
               optionsChoice=options[optionsIndex]
               if optionsChoice=='Quit':
                    quitting=True
               for option in data:
                    key, value = list(option.items())[0]
                    if key == optionsChoice:
                         print(value)
                         webbrowser.open(value, new=0, autoraise=True)
                         quitting =True
                    else:
                         pass

     except Exception as e:
          print(e)



# Executing the Function
if __name__=='__main__':
     News()