import requests
import base64


class beitraege_manager:

    def beitrag_aendern(self, watt_aktuell, kwh_tag, kwh_gestern, kwh_woche, kwh_letze_woche, kwh_monat,
                        kwh_leter_monat, kwh_jahr, kwh_letztes_jahr):
        credentials = "Python:4ak6 NJpX iZoy PMDD EvJT oM8Q"  # You can generate application password in WordPress > Users > Profile
        token = base64.b64encode(credentials.encode())
        post_url = "https://www.solar-community.org/wp-json/wp/v2/posts/"

        header = {"Authorization": "Basic " + token.decode('utf-8'), "Content-Type": "application/json"}

        postID = 209  # Steht in der URL des Posts
        post = {'title': 'Beitrag für Daten aus Python',
                'content': 'Aktuell erzeugte Watt: {} \n'
                           'KWh des aktuellen Tages: {} \n'
                           'KWh des vorigen Tages: {} \n'
                           'KWh der aktuellen Woche: {} \n'
                           'KWh der vorigen Woche: {} \n'
                           'KWh des aktuellen Monats: {} \n'
                           'KWh des vorigen Monats: {} \n'
                           'KWh des aktuellen Jahres: {} \n'
                           'KWh des vorigen Jahres: {}'.format(watt_aktuell, kwh_tag, kwh_gestern, kwh_woche,
                                                               kwh_letze_woche, kwh_monat, kwh_leter_monat, kwh_jahr,
                                                               kwh_letztes_jahr)
                }

        response = requests.post(post_url + str(postID), headers=header, json=post)
        print(response.status_code)
        print(response.content)

    def beitrag_erstellen(self):
        credentials = "Python:4ak6 NJpX iZoy PMDD EvJT oM8Q"  # You can generate application password in WordPress > Users > Profile
        token = base64.b64encode(credentials.encode())
        post_url = "https://www.solar-community.org/wp-json/wp/v2/posts"

        header = {"Authorization": "Basic " + token.decode('utf-8'), "Content-Type": "application/json"}

        post = {'date': '2022-07-10T20:00:35',
                'title': 'First REST API post',
                'slug': 'rest-api-1',
                'status': 'publish',
                'content': 'this is the content post',
                'author': '1',
                'excerpt': 'Exceptional post!',
                'format': 'standard'
                }

        response = requests.post(post_url, headers=header, json=post)
        print(response.status_code)
        print(response.content)

    def beitrag_löschen(self):
        next