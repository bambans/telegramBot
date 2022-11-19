from requests import get, post
from json import loads

# Show some more information
debug = False

apiToken = '<your telegram bot api token>'
apiURL = f'https://api.telegram.org/bot{apiToken}'

# Get user data from your telegram bot updates, filtering by username
def getUserData(username):
        try:
            print('#### Get updates response ####')

            jsonResponse = loads(
                get(f'{apiURL}/getUpdates').text
            )

            for result in jsonResponse['result']:
                if result['message']['from']['username'] == username:
                    update = True
                    chatID = result['message']['from']['id']
                    firstName = result['message']['from']['first_name']
                    break
                else:
                    update = False
            
            if update:
                print('---- Updates received successfully ----')
                returnValue = {chatID, firstName}
            else:
                print('---- No updates received ----')
                returnValue = {None, None}

            if debug:
                print('')
                print('@@@@ getUpdates debug @@@@')
                print('----- jsonResponse -----')
                print(jsonResponse)
                print('----- returnValue -----')
                print(returnValue)
                print('')

            return returnValue
        except Exception as e:
            print(e)

# Send message to telegram user from your bot using chatID (returned by getUserData)
def sendToTelegram(chatID, message):
    try:
        print('#### Message response ####')

        jsonResponse = loads(
            post(
                f'{apiURL}/sendMessage',
                json = {
                    'chat_id': chatID,
                    'text': message
                }
            ).text
        )

        if jsonResponse['ok']:
            print('---- Message sent successfully ----')
            returnValue = True
        else:
            print('---- Message not sent ----')
            returnValue = False

        if debug:
            print('')
            print('@@@@ sendMessages debug @@@@')
            print('----- jsonResponse -----')
            print(jsonResponse)
            print('----- returnValue -----')
            print(returnValue)
            print('')
        
        return returnValue
    except Exception as e:
        print(e)
        return False

def main():
    try:
        chatID, name =  getUserData('<username>')
        sendToTelegram(chatID, f'Oi, {name}!')
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()
