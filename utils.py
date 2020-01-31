from database import db_session
from models import Handoff

# Update the DB from the Data.xlsx file
def updateDB():
    data_file = pd.read_excel('Book2.xlsx')
    for data in range(0, len(data_file)):
        db_session.add(Handoff(data_file['systemName'][data], data_file['nodeName']
                              [data], data_file['hostName'][data], data_file['instanceNumber'][data], ""))
        db_session.commit()

# Remove duplicates in a List
def Remove(list_with_duplicates):
    final_list = []
    for num in list_with_duplicates:
        if num not in final_list:
            final_list.append(num)
    return final_list


# def getNotesForDate(date):
     


