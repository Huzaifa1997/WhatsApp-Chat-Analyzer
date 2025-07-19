import re
import pandas as pd
from pandas import DataFrame


def preprocess(data: object) -> DataFrame:
    #data = data.replace('\u202f', ' ').replace('\xa0', ' ')
    pattern = r'\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}[\s\u202f\xa0]?[APap][Mm]\s-\s'
    messages = re.split(pattern, data)[1:]
    dates = re.findall(pattern, data)
    print("Before fixing:")
    print("Messages:", len(messages))
    print("Dates:", len(dates))

    # Fix unequal length
    min_len = min(len(messages), len(dates))
    messages = messages[:min_len]
    dates = dates[:min_len]

    print("After fixing:")
    print("Messages:", len(messages))
    print("Dates:", len(dates))



    # After creating the DataFrame
    df = pd.DataFrame({'user_message': messages, 'message_date': dates})
    df['message_date'] = pd.to_datetime(df['message_date'], format='%m/%d/%y, %I:%M %p - ')
    df.rename(columns={'message_date': 'date'}, inplace=True)

    # Extract user and message from user_message
    users = []
    messages_cleaned = []

    for message in df['user_message']:
        entry = re.split(r'([\w\W]+?):\s', message)
        if len(entry) > 2:
            users.append(entry[1])
            messages_cleaned.append("".join(entry[2:]))
        else:
            users.append('group_notification')
            messages_cleaned.append(entry[0])

    df['user'] = users
    df['message'] = messages_cleaned

    # Now you can drop 'user_message'
    df.drop(columns=['user_message'], inplace=True)

    df['date'] = pd.to_datetime(df['date'])
    df['year'] = df['date'].dt.year
    df['only_date'] = df['date'].dt.date
    df['month'] = df['date'].dt.strftime('%B')
    df['month_num'] = df['date'].dt.month
    df['day'] = df['date'].dt.day
    df['hour'] = df['date'].dt.hour
    df['minute'] = df['date'].dt.minute
    df['period'] = df['hour'].apply(lambda x: f"{x:02d}-{(x + 1) % 24:02d}")
    df['message_length'] = df['message'].apply(len)
    df['day_name'] = df['date'].dt.day_name()

    return df
