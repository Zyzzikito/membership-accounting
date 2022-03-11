def id_abonement_list(self):
    id = '' #Тут ID таблицы
    gs = grspread.service_account(filename='fileapi.json')
    sh = gs.open_by_key(id)
    worksheet = sh.get_worksheet(1)
    abonement_list = worksheet.get_all_records()
    return abonement_list 
   
