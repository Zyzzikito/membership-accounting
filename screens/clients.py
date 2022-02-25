from kivy.uix.screenmanager import Screen
from kivy.uix.screenmanager import SlideTransition
import gspread

class Clients(Screen):

    def logout(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'welcome'
        
    def id_abonement_list(self):
        id = '1i1XjLemtPa9Pj3nIYFXMVyINXoPZkq0qblnaMoVLZeY'
        gs = gspread.service_account(filename='fileapi.json')
        sh = gs.open_by_key(id)
        worksheet = sh.get_worksheet(1)
        Id_abonement = worksheet.col_values(1)
        Id_client = worksheet.col_values(2)
        Task_abonement = worksheet.col_values(6)
        Last_ab = worksheet.col_values(7)
        abonementy = worksheet.col_values(5)
        Abonement_list = {}
        for i in Id_abonement:
            if i == 'Идентификатор абонемента':
                continue
            i = int(i)
            Abonement_list[Last_ab[i]] = Id_abonement[i] + '-' + Id_client[i] + Task_abonement[i] + '/' + abonementy[i]
            return Abonement_list
